import psutil
import platform
import socket
from datetime import datetime

print("="*40,"Name PC: ",socket.gethostname(),"="*40)

print("="*40,"OS: ",platform.system(),"="*40)

print("="*40,"Virtual memory: ",psutil.virtual_memory(),"="*40)

print("="*40, "Procesor: ",platform.processor(),"="*40)