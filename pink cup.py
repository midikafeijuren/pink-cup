
#aes加密
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import pad, unpad
from Cryptodome.Random import get_random_bytes
 
def encrypt(plaintext, key):
    '''加密函数'''
    
    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))
    return cipher.iv + ciphertext
 
def decrypt(ciphertext, key):
    '''解密函数'''
    iv = ciphertext[:AES.block_size]
    ciphertext = ciphertext[AES.block_size:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return plaintext
#this is meaningful
#|
#v
'''
#pyqt5
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
 
app = QApplication(sys.argv)
window = QMainWindow()
button = QPushButton('Hello, PyQt5!')
window.setCentralWidget(button)
window.show()
sys.exit(app.exec_())

'''