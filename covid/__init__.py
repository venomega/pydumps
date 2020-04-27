import subprocess
import sys
import os

def error(string):
    print (string, file=sys.stderr)
    exit(1)
os.chdir(sys.path[0])
r=subprocess.run(["python3", f"get_page.py"])

fd = open("file.txt.new", "r")
print ("\n\n")
string= fd.read()
if len(string) < 100000:
    error("Error downloading a file. please check you have internet connection, or are not behind a captive portal")

df = open("file.txt", "w")
df.write(string)
df.close()


r=subprocess.run(["python3", f"get_data.py"])
