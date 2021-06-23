#!/usr/bin/python3

import subprocess as sp
import cgi

print("content-type: text/html")
print()

data=cgi.FieldStorage()

cmd=data.getvalue("command")

out = sp.getoutput("sudo " +cmd)
print(out)
