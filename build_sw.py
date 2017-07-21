#!/usr/bin/python

from subprocess import call
import os

def main():
    output_directory = "sandbox"
    make_path(output_directory)
    os.chdir(output_directory)
    call(["qmake","../src"])
    call("make")

def make_path(path):
    try: 
        os.makedirs(path)
    except OSError:
        if not os.path.isdir(path):
            raise

if __name__ == "__main__":
    main()
