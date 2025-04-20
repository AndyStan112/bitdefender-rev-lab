import argparse
import sys
if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='scan.py')
    parser.add_argument('mode', choices=['-d', '-e', ''],default="",nargs='?')
    parser.add_argument('permission')
    print(parser.parse_args(["test"]))
    