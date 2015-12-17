"""programa que crea el resumen de una contrasenya"""

from Crypto.Hash import SHA256

CLAU = input("ingrese una contraseña: ")
CLAU = CLAU.encode("UTF-8")

OBJH = SHA256.new(CLAU)
RESUM = OBJH.digest()
IV = b"1234567887654321"

print(OBJH.hexdigest())



