import json, urlparse, sys, os
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from subprocess import call, Popen
import shlex

def main():
    Popen('C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\powershell.exe Stop-WebAppPool -Name "admin.softdreams.vn"')
if __name__ == '__main__':
     main()
