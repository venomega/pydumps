#!/usr/bin/env python3
import subprocess
import sys
import os
os.chdir(sys.path[0])
os.popen("curl www.cubadebate.cu > file.txt.new","r")

