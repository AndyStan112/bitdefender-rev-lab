import subprocess
from io import BytesIO


class Adb:
    def __init__(self, mode: str = ""):
        self.mode = mode

    def get_package_path(self, package: str) -> str:
        command = f"pm path {package}"
        return self.shell(command).strip().split(":")[-1]

    def pull_package(self, package: str) -> BytesIO:
        path = self.get_package_path(package)
        return self.pull(path)

    def pull(self, path: str) -> BytesIO:
        command = f"exec-out cat {path}"
        return BytesIO(self._stream(command))

    def execute(self, command: str) -> str:
        _command = f'adb {self.mode} {command}'
        return self._execute(_command)

    def shell(self, command: str) -> str:
        _command = f'adb shell {self.mode} {command}'
        return self._execute(_command)

    def _stream(self, command: str) -> bytes:
        _command = f'adb {self.mode} {command}'
        return subprocess.check_output(_command, shell=True)

    def _execute(self, command: str) -> str:
        output = subprocess.check_output(command, shell=True).decode("utf-8")
        if ("* daemon not running; starting now at" in output):
            raise Exception("Demon just started, try again")
        return output


if __name__ == "__main__":
    adb = Adb("-e")
    print(adb.execute("devices"))
