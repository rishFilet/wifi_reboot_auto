import os
import pyAesCrypt

buffer_size = 64 * 1024  # 64K
filename = os.getenv('SECURE_STORE_FILE')
password = os.getenv('SECURE_STORE_PASSWORD')
pyAesCrypt.encryptFile((os.getcwd(),"login.yaml"), filename, password, buffer_size)
