# EncryptIt

## Descripción

EncryptIt es una herramienta de encriptación y desencriptación de archivos desarrollada en Python. Utiliza la biblioteca `cryptography.fernet` para generar una clave segura y encriptar archivos, y luego desencriptarlos con la misma clave. EncryptIt puede encriptar y desencriptar todos los archivos en un directorio específico.

## Instalación

Para instalar y ejecutar EncryptIt, necesitarás Python 3.6 o superior. También necesitarás instalar la biblioteca `cryptography`. Puedes instalarla con pip:

```
pip install cryptography
```

## Uso

Para usar EncryptIt, ejecuta el script `encrypt.py` para encriptar tus archivos y `decrypt.py` para desencriptarlos. Se te pedirá que introduzcas una contraseña. Asegúrate de recordarla, ya que la necesitarás para desencriptar tus archivos.

```
python encrypt.py
python decrypt.py
```

## Advertencia

EncryptIt es una herramienta poderosa. Encripta tus archivos de manera segura, pero si olvidas tu contraseña, no podrás recuperar tus archivos. Úsala con precaución.


## Licencia

[MIT](https://choosealicense.com/licenses/mit/)

---

