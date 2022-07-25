#! Opening other programs in python
import subprocess

#   Popen() method. P stands for Process
subprocess.Popen("path_to_app.exe")
subprocess.Popen(['start', 'hello.txt'], shell=True)  # Double click
