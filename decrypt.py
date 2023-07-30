import os
import subprocess
import pkg_resources
import multiprocessing
from cryptography.fernet import Fernet
import tkinter as tk
from tkinter import simpledialog

REQUIRED_PACKAGES = [
    'cryptography'
]

for package in REQUIRED_PACKAGES:
    try:
        dist = pkg_resources.get_distribution(package)
        print('{} ({}) está instalado'.format(dist.key, dist.version))
    except pkg_resources.DistributionNotFound:
        print('{} NO está instalado'.format(package))
        subprocess.call(['pip', 'install', package])

def cargar_key():
    return open('key.key', 'rb').read()

def decrypt(item, key):
    f = Fernet(key)
    with open(item, 'rb') as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open(item, 'wb') as file:
        file.write(decrypted_data)

def get_all_files_in_directory(dir_path):
    files_list = []
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            files_list.append(os.path.join(root, file))
    return files_list

if __name__ == '__main__':
    path_to_encrypt = 'C:\\Users\\[nombre de usuario]\\Desktop'  # Reemplaza [nombre de usuario] con tu nombre de usuario
    all_files = get_all_files_in_directory(path_to_encrypt)

    # Solicitar la contraseña al usuario
    root = tk.Tk()
    root.withdraw()
    password = simpledialog.askstring("Contraseña", "Introduce la contraseña para desencriptar los archivos:", show='*')
    if password == "contraseña_correcta":
        key = cargar_key()
        with multiprocessing.Pool() as pool:
            pool.starmap(decrypt, [(file, key) for file in all_files])
    else:
        print("Contraseña incorrecta.")
