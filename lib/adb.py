import subprocess
class Adb:
    def __init__(self,mode:str = ""):
        self.mode = mode
    
    def execute(self,command:str):
        _command = f'adb {self.mode} {command}'
        output = subprocess.check_output(_command,shell=True).decode("utf-8")
        if("* daemon not running; starting now at" in output):
            raise Exception("Demon just started, try again")
        return subprocess.check_output(_command,shell=True).decode("utf-8")
    
if __name__ == "__main__":
    adb = Adb("-e")
    print(adb.execute("devices"))
        