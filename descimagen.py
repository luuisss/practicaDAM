"""programa que desencripta una imatge"""

from Crypto.Cipher import AES

CLAU = b"1234567898765432"
IV = b"1234567887654321"

FILE_IMG = open("1.enc", 'rb')
FILE_DEC = open("2.jpg", 'wb')

BLOCS = 8192
OBJ = AES.new(CLAU, AES.MODE_CBC, IV)
BLOC = 0

while True:
    BLOC = FILE_IMG.read(BLOC)
    if not BLOC:
        break
    NUM = len(BLOC)
    MOD = NUM % 16
    if MOD > 0:
        PADDING = 16 - MOD
        BLOC += b"0"*PADDING

    DEC = OBJ.decrypt(BLOC)
    FILE_DEC.write(DEC)

FILE_DEC.close()
FILE_IMG.close()

