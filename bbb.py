import sys
from PyQt5.QtWidgets import *

from PyQt5.QtCore import *
import socket

from cryptography.fernet import Fernet

aa = b'v8vokhBDdz6WtM5nBkIg4lvsjJEm_lOjroSyzdNaa88='
bb = Fernet(aa)
from UI import Ui_MainWindow
import threading

import os

from cryptography.hazmat.primitives.ciphers import algorithms, Cipher, modes
# from cryptography.hazmat.primitives.ciphers import *
from cryptography.hazmat.primitives import padding

k = b'6\x9a\xf66\x10\xc7\xec\xc8\xeb\xde\xf7\xce\xf6\x83\xc7\xe0k:\xae\xa2#\xc9\xd0\xd5\x974\x8e:=6\xddX'
v = b'Fuw\xec>f8\x97\x13\xf9\xb0\xcfp\xc6\xea\xd0'
# print(os.urandom(16))

c = Cipher(algorithms.AES(k), modes.CBC(v))


class MyWindow(QMainWindow):
    finished = pyqtSignal(str)

    def __init__(self):

        # 切记一定要调用父类的__init__方法，因为它里面有很多对UI空间的初始化操作
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.finished.connect(self.updateText)
        self.ui.listWidget.itemClicked.connect(self.renmin)
        self.ui.pushButton_2.clicked.connect(self.zx)

        # 创建客户端套接字
        self.sk = socket.socket()
        # 尝试连接服务器
        # b.start()
        self.sk.connect(('127.0.0.1', 8890))
        self.sk.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, True)
        self.sk.ioctl(socket.SIO_KEEPALIVE_VALS, (1, 60 * 1000, 30 * 1000))


    def jiami(self):

        pad = padding.PKCS7(128).padder()
        enc = c.encryptor()
        text = b'hello world1234565465'
        aa = enc.update(pad.update(text) + pad.finalize()) + enc.finalize()
        print(aa)

    def jiemi(self):
        v = b'Fuw\xec>f8\x97\x13\xf9\xb0\xcfp\xc6\xea\xd0'
        c = Cipher(algorithms.AES(os.urandom(32)), modes.CBC(v))
        dec = c.decryptor()
        unpad = padding.PKCS7(128).unpadder()
        print(unpad.update(dec.update(aa) + dec.finalize()) + unpad.finalize())

    def renmin(self, item):
        item_text = item.text()
        self.ui.ch_text.append(item_text + "")

    def zx(self):
        threading.Thread(target=self.send()).start()

    def send(self):
        try:
            wenben = self.ui.textEdit.toPlainText()
            pad = padding.PKCS7(256).padder()
            enc = c.encryptor()
            print(wenben)
            # text = b'hello world1234565465'
            aa = enc.update(pad.update(wenben.encode()) + pad.finalize()) + enc.finalize()
            print(aa)
            self.sk.send(bytes(aa, encoding='utf-8'))
            ret = self.sk.recv(1024)
            self.finished.emit(ret.decode('utf-8') + '\n')

        except Exception as e:
            print(type(e).__name__)
            print('error')

    def updateText(self, ret: str):
        print(type(ret).__name__, 9)
        # a = bb.decrypt(ret.encode()).decode()
        # print(a)
        dec = c.decryptor()
        # 代码调用了加密器`Cipher.encryptor()`方法，并用该加密器对需要加密的文本进行加密。
        unpad = padding.PKCS7(256).unpadder()
        # print()
        temp=unpad.update(dec.update(ret.encode()) + dec.finalize()) + unpad.finalize()
        print(temp)
        self.ui.textBrowser.append(temp)
        # self.ui.textBrowser.append(ret)


if __name__ == '__main__':
    # 第一步！！！！只要是Qt制作APP，必须有且只有1个QApplication对象
    # sys.argv当做参数的目的是将运行时的命令参数传递给QApplication对象
    print(type(bb).__name__)
    app = QApplication(sys.argv)
    # 创建一个子类
    w = MyWindow()

    # 展示窗口
    w.show()

    # 第二步！！！！程序进行循环等待状态，运行程序，直到关闭了窗口
    app.exec()
