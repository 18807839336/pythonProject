import threading
import socket
import datetime

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from cryptography.hazmat.primitives.ciphers import algorithms, Cipher, modes
from cryptography.hazmat.primitives import padding
import sys
class Ui_Window(QMainWindow):
    # 信号：提醒界面更新,传输bytes字节流，因为加密解密都是字节流传输进行操作的
    finished = pyqtSignal(bytes)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        #给send按钮绑定Text函数逻辑
        self.pushButton_send.clicked.connect(self.Text)
        #给信号finished绑定updateText函数逻辑
        self.finished.connect(self.updateText)
        k = b'6\x1a\xf66\x10\xc7\xec\xc8\xeb\xde\xf7\xce\xf6\x83\xc7\xe0k:\xae\xa2#\xc9\xd0\xd5\x974\x8e:=6\xddX'
        v = b'Fuw\xec>f8\x97\x13\xf9\xb0\xcfp\xc6\xea\xd0'
        self.mima = Cipher(algorithms.AES(k), modes.CBC(v))  # 实例化
        # 代码定义了一个16字节长的密钥`k`和一个16字节长的向量`v`
        #和服务器端sever进行连接
        self.s = socket.socket()  # 创建 socket 对象
        host = socket.gethostname()  # 获取本地主机名
        port = 12963  # 设置端口号
        self.s.connect((host, port))
        #启动一个线程，函数为recv
        threading.Thread(target=self.recv).start()

    def recv(self):
        while True:
            res = self.s.recv(1024) #定义res变量为服务器端发送过来的内容
            self.finished.emit(res)  #将内容发送给信息，要跟新内容

    def Text(self):
        ##启动一个线程，函数为send,防止信息堵塞
        threading.Thread(target=self.send).start()

    def send(self):
        text = self.textEdit.toPlainText()#定义text变量为手动输入在文本显示框的内容
        length = len(text)
        self.time_send.setText(length)  ##
        enc = self.mima.encryptor()  # 加密
        pad = padding.PKCS7(256).padder()  # 填充
        aa = enc.update(pad.update(text.encode()) + pad.finalize()) + enc.finalize()  # 将text加密得到结果aa
        self.s.send(aa)+datetime.now() #发送加密信息aa


    def updateText(self,ret:bytes):
        #ret(形参，随便命名，不要和上面的res起冲突):服务器端发送过来的内容，以字节流形式传入函数，bytes表示传入该函数为字节流形式
        dec = self.mima.decryptor()  # 解密方法
        unpad = padding.PKCS7(256).unpadder()  # 拿掉填充
        jm = unpad.update(dec.update(ret) + dec.finalize()) + unpad.finalize()
        #定义变量jm为服务器端传入的ret解密内容
        jm = jm.decode()
        print(jm)  # 输出解密内容
        self.textDisplay.setText(jm)+datetime.now()   #在客户端textDisplay上显示内容
        self.nameDisplay.setText(str(ret))+datetime.now()     #在客户端nameDisplay上显示ret内容，str强制转换成字符型

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
        self.textDisplay = QTextBrowser(self.widget)
        self.textDisplay.setObjectName(u"textDisplay")
        self.textDisplay.setMinimumSize(QSize(200, 200))
        font = QFont()
        font.setItalic(True)
        self.textDisplay.setFont(font)

        self.gridLayout_3.addWidget(self.textDisplay, 2, 0, 1, 4)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")

        self.gridLayout_3.addLayout(self.verticalLayout, 0, 1, 1, 1)

        self.nameDisplay = QTextBrowser(self.widget)
        self.nameDisplay.setObjectName(u"nameDisplay")
        font1 = QFont()
        font1.setPointSize(9)
        font1.setItalic(False)
        self.nameDisplay.setFont(font1)

        self.gridLayout_3.addWidget(self.nameDisplay, 0, 0, 1, 1)

        self.pushButton_end = QPushButton(self.widget)
        self.pushButton_end.setObjectName(u"pushButton_end")
        self.pushButton_end.setStyleSheet(u"")

        self.gridLayout_3.addWidget(self.pushButton_end, 5, 3, 1, 1)

        self.textBrowser = QTextBrowser(self.widget)
        self.textBrowser.setObjectName(u"textBrowser")

        self.gridLayout_3.addWidget(self.textBrowser, 5, 1, 1, 1)

        self.textBrowser_2 = QTextBrowser(self.widget)
        self.textBrowser_2.setObjectName(u"textBrowser_2")

        self.gridLayout_3.addWidget(self.textBrowser_2, 5, 0, 1, 1)

        self.textEdit = QTextEdit(self.widget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(600, 100))
        self.textEdit.setMaximumSize(QSize(16777215, 300))
        font2 = QFont()
        font2.setItalic(False)
        font2.setUnderline(False)
        self.textEdit.setFont(font2)
        self.textEdit.setStyleSheet(u"background-color: rgb(161, 214, 255);")

        self.gridLayout_3.addWidget(self.textEdit, 3, 0, 1, 4)

        self.pushButton_send = QPushButton(self.widget)
        self.pushButton_send.setObjectName(u"pushButton_send")

        self.gridLayout_3.addWidget(self.pushButton_send, 5, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_2, 1, 0, 1, 1)

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
        self.nameDisplay.setHtml(QCoreApplication.translate("MainWindow",
                                                            u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                            "p, li { white-space: pre-wrap; }\n"
                                                            "</style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                                            "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>",
                                                            None))
        self.pushButton_end.setText(QCoreApplication.translate("MainWindow", u"\u5173\u95ed", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow",
                                                         u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                         "p, li { white-space: pre-wrap; }\n"
                                                         "</style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                                         "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>",
                                                         None))
        self.pushButton_send.setText(QCoreApplication.translate("MainWindow", u"\u53d1\u9001", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u5b50\u9875\u9762", None))
    # retranslateUi


