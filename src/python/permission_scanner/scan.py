#!/usr/bin/env python
# PYTHON_ARGCOMPLETE_OK
from lib.adb import Adb
from permission_scanner.argument_parser import parse_args
from datetime import datetime, timedelta
from functools import partial
import argparse

from loguru import logger
logger.remove()

from androguard.core.apk import APK  # noqa


def get_range(search_time: datetime, interval: timedelta) -> (timedelta, timedelta):
    return (search_time - interval, search_time + interval)


def is_in_range(time_range: (timedelta, timedelta), install_time: datetime) -> bool:
    range_start, range_end = time_range
    return range_start <= install_time and install_time <= range_end


class Scanner:

    def __init__(self, mode: str):
        self.adb = Adb(mode)

    def get_install_time(self, package: str):
        command = f"pm dump {package} | grep  firstInstallTime"
        date_string = self.adb.shell(command).split("=")[1].strip("\n")
        return datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")

    def get_package_names(self) -> list[str]:
        lines = self.adb.shell("pm list packages -f -3").splitlines()
        return [line.split("=")[-1] for line in lines]

    def get_permissions(self, package: str) -> list[str]:
        apk_data = self.adb.pull_package(package)
        apk = APK(apk_data.read(), raw=True)
        return [permission.split(".")[-1] for permission in apk.get_permissions()]

    def has_permission(self, package: str, permission: str) -> bool:
        return permission in self.get_permissions(package)

    def scan(self, search_time: datetime, interval: timedelta, permission: str) -> list[(str, datetime)]:
        packages = self.get_package_names()
        time_range = get_range(search_time, interval)
        return [
            (package, install_time)
            for package in packages
            if (install_time := self.get_install_time(package))
            if is_in_range(time_range, install_time)
            if self.has_permission(package, permission)
        ]


def main():
    args = parse_args()
    scanner = Scanner(args.mode)
    apps = scanner.scan(args.search_time, args.interval, args.permission)

    if not apps:
        print("No apps found with the specified permission in the given time range.")
        return

    print(
        f"\nFound {len(apps)} app(s) with permission '{args.permission}' installed near {args.search_time}:\n")
    print(f"{'PACKAGE':<50} {'INSTALL TIME'}")
    print("-" * 70)
    for package, install_time in apps:
        print(f"{package:<50} {install_time}")


if __name__ == "__main__":
    main()
