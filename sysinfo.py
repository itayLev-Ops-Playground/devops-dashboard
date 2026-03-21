
import socket
import getpass
import os

sysinfo = {
  "hostname": socket.gethostname(),
  "current_user": getpass.getuser(),
  "working_directory": os.getcwd()
}

def show_sysinfo():
  """
  Prints system info.
  This function prints each one of the system properties.
  """
  
  for prop, value in sysinfo:
    print(f"{prop}: {value}")
  
