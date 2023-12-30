import threading
import socket
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from cryptography.hazmat.primitives.ciphers import algorithms, Cipher, modes
from cryptography.hazmat.primitives import padding
import sys
class Ui_Window(QMainWindow):
    finished = pyqtSignal(bytes)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.pushButton_send.clicked.connect(self.Text)
        self.finished.connect(self.updateText)
        # 首先，代码导入了必要的依赖：`os`模块、`algorithms`、`Cipher`和`modes`类、`padding`模块。其中，`os`模块主要用于生成随机种子，`Cipher`和`modes`类用于创建加密和解密所需的实例，`padding`模块则用于填充。
        k = b'6\x1a\xf66\x10\xc7\xec\xc8\xeb\xde\xf7\xce\xf6\x83\xc7\xe0k:\xae\xa2#\xc9\xd0\xd5\x974\x8e:=6\xddX'
        v = b'Fuw\xec>f8\x97\x13\xf9\xb0\xcfp\xc6\xea\xd0'
        self.mima = Cipher(algorithms.AES(k), modes.CBC(v))  # 实例化
        # 然后，代码定义了一个16字节长的密钥`k`和一个16字节长的向量`v`
        self.s = socket.socket()  # 创建 socket 对象
        host = socket.gethostname()  # 获取本地主机名
        port = 12965  # 设置端口号
        self.s.connect((host, port))
        threading.Thread(target=self.recv).start()

    def Text(self):
        threading.Thread(target=self.send).start()

    def send(self):
        text = self.textEdit.toPlainText()
        enc = self.mima.encryptor()  # 加密
        pad = padding.PKCS7(256).padder()  # 填充
        aa = enc.update(pad.update(text.encode()) + pad.finalize()) + enc.finalize()  # 得到加密结果aa
        self.s.send(aa)

    def recv(self):
        while True:
            res = self.s.recv(1024)

            self.finished.emit(res)

    def updateText(self,ret:bytes):
        dec = self.mima.decryptor()  # 解密方法
        unpad = padding.PKCS7(256).unpadder()  # 拿掉填充
        jm = unpad.update(dec.update(ret) + dec.finalize()) + unpad.finalize()
        jm = jm.decode()
        print(jm)  # 输出解密内容
        self.textDisplay.setText(jm)
        self.nameDisplay.setText(str(ret))

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(844, 506)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")

        self.gridLayout_3.addLayout(self.verticalLayout, 0, 1, 1, 1)

        self.pushButton_send = QPushButton(self.widget)
        self.pushButton_send.setObjectName(u"pushButton_send")

        self.gridLayout_3.addWidget(self.pushButton_send, 4, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 4, 0, 1, 1)

        self.pushButton_end = QPushButton(self.widget)
        self.pushButton_end.setObjectName(u"pushButton_end")
        self.pushButton_end.setStyleSheet(u"")

        self.gridLayout_3.addWidget(self.pushButton_end, 4, 3, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_2, 1, 0, 1, 1)

        self.nameDisplay = QTextBrowser(self.widget)
        self.nameDisplay.setObjectName(u"nameDisplay")
        font = QFont()
        font.setPointSize(9)
        font.setItalic(False)
        self.nameDisplay.setFont(font)

        self.gridLayout_3.addWidget(self.nameDisplay, 0, 0, 1, 1)

        self.textEdit = QTextEdit(self.widget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(600, 100))
        self.textEdit.setMaximumSize(QSize(16777215, 300))
        font1 = QFont()
        font1.setItalic(False)
        font1.setUnderline(False)
        self.textEdit.setFont(font1)
        self.textEdit.setStyleSheet(u"background-color: rgb(161, 214, 255);")

        self.gridLayout_3.addWidget(self.textEdit, 3, 0, 1, 4)

        self.textDisplay = QTextBrowser(self.widget)
        self.textDisplay.setObjectName(u"textDisplay")
        self.textDisplay.setMinimumSize(QSize(200, 200))
        font2 = QFont()
        font2.setItalic(True)
        self.textDisplay.setFont(font2)

        self.gridLayout_3.addWidget(self.textDisplay, 2, 0, 1, 4)


        self.gridLayout_2.addLayout(self.gridLayout_3, 0, 4, 1, 1)


        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 844, 22))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_send.setText(QCoreApplication.translate("MainWindow", u"\u53d1\u9001", None))
        self.pushButton_end.setText(QCoreApplication.translate("MainWindow", u"\u5173\u95ed", None))
        self.nameDisplay.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p></body></html>", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u5b50\u9875\u9762", None))
    # retranslateUi

