import argparse
import re
from datetime import timedelta, datetime


def parse_interval(interval: str) -> timedelta:
    pattern = r"(\d+)\s*(microseconds?|milliseconds?|seconds?|minutes?|hours?|days?|weeks?)"
    matches = re.findall(pattern, interval, re.IGNORECASE)

    if not matches:
        raise argparse.ArgumentTypeError("Invalid format")
    kwargs = {}
    for value, unit in matches:
        unit = unit.lower().rstrip('s') + 's'
        kwargs[unit] = kwargs.get(unit, 0) + int(value)

    return timedelta(**kwargs)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(prog='scan.py')
    parser.add_argument(
        'mode', choices=['-d', '-e', ''], default="", nargs='?')
    parser.add_argument(
        '--search_time',
        type=lambda s: datetime.strptime(s, "%Y-%m-%d %H:%M"),
        default=datetime.now(),
        help='Datetime to search in format YYYY-MM-DD HH:MM'
    )

    parser.add_argument("--interval", type=parse_interval,
                        default=timedelta(hours=1),
                        help="""Interval to search composed of multiple pairs of the form '<value> <unit>'.
                        Possible units: {microseconds, milliseconds, seconds, minutes, hours, days, week}.
                        Must include at least one valid param. Extra text and pluralism is ignored.
                        Example :'1 day, 3 hours and 2 minutes' is equivalent to '1 day 3 hour 2 minute'
                        """)

    parser.add_argument('permission', type=str)
    return parser.parse_args()
