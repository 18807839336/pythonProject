import datetime
import threading
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import socket
import time

from cryptography.hazmat.primitives.ciphers import algorithms, Cipher, modes
from cryptography.hazmat.primitives import padding


class Ui_MainWindow(QMainWindow):  # 传输一个具体的QMainWindow
    # 信号：提醒界面更新,传输bytes字节流，因为加密解密都是字节流传输进行操作的
    finished = pyqtSignal(bytes)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        k = b'6\x1a\xf66\x10\xc7\xec\xc8\xeb\xde\xf7\xce\xf6\x83\xc7\xe0k:\xae\xa2#\xc9\xd0\xd5\x974\x8e:=6\xddX'
        v = b'Fuw\xec>f8\x97\x13\xf9\xb0\xcfp\xc6\xea\xd0'
        self.mima = Cipher(algorithms.AES(k), modes.CBC(v))
        self.pushButton_send.clicked.connect(self.thread_send)
        self.finished.connect(self.updateText)
        threading.Thread(target=self.ser_socket).start()

    def ser_socket(self):
        #服务器端开放端口，等待客户端连接
        s = socket.socket()  # 创建 socket 对象
        host = socket.gethostname()  # 获取本地主机名
        port = 12963  # 设置端口
        s.bind((host, port))  # 绑定端口
        s.listen()  # 监听
        self.c, self.addr = s.accept()    #实例化对象之后要用self，表明是对象自己的属性
        while True:
            # 建立客户端连接
            res = self.c.recv(1024)   #res定义为客户端给服务端传来的消息
            self.finished.emit(res)   #把发送的信息传给信号量，提示更新数据
            print(res)  # 接受sever端发来的信息，打印出来

    def thread_send(self):
        ##启动一个线程，函数为ser_send,防止信息堵塞
        threading.Thread(target=self.ser_send).start()

    def ser_send(self):
        text = self.textEdit.toPlainText()+datetime.now()    #定义text变量为手动输入在文本显示框的内容
        length = len(text)
        self.time_send.setText(length)#
        enc = self.mima.encryptor()  # 加密
        pad = padding.PKCS7(256).padder()  # 填充
        aa = enc.update(pad.update(text.encode()) + pad.finalize()) + enc.finalize()  # 将text加密得到结果aa
        self.c.send(aa)# 发送加密信息aa


    def updateText(self, ret: bytes):
        dec = self.mima.decryptor()  # 解密方法
        unpad = padding.PKCS7(256).unpadder()  # 拿掉填充
        jm = unpad.update(dec.update(ret) + dec.finalize()) + unpad.finalize()
        jm = jm.decode()
        print(jm)  # 输出解密内容
        self.textDisplay.setText(str(jm))+datetime.now()   #在主页面textDisplay中显示解密内容
        self.textBrowser.setText(str(ret))+datetime.now()   #在主页面中textBrowser显示加密内容

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(933, 506)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.nameDisplay = QTextBrowser(self.widget)
        self.nameDisplay.setObjectName(u"nameDisplay")

        self.gridLayout_2.addWidget(self.nameDisplay, 0, 0, 1, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.textDisplay = QTextBrowser(self.widget)
        self.textDisplay.setObjectName(u"textDisplay")
        self.textDisplay.setMinimumSize(QSize(200, 200))
        font = QFont()
        font.setItalic(True)
        self.textDisplay.setFont(font)

        self.gridLayout_3.addWidget(self.textDisplay, 2, 0, 1, 5)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_2, 1, 0, 1, 1)

        self.pushButton_send = QPushButton(self.widget)
        self.pushButton_send.setObjectName(u"pushButton_send")

        self.gridLayout_3.addWidget(self.pushButton_send, 5, 3, 1, 1)

        self.pushButton_end = QPushButton(self.widget)
        self.pushButton_end.setObjectName(u"pushButton_end")
        self.pushButton_end.setStyleSheet(u"")

        self.gridLayout_3.addWidget(self.pushButton_end, 5, 4, 1, 1)

        self.textEdit = QTextEdit(self.widget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(600, 100))
        self.textEdit.setMaximumSize(QSize(16777215, 300))
        font1 = QFont()
        font1.setItalic(False)
        font1.setUnderline(False)
        self.textEdit.setFont(font1)
        self.textEdit.setStyleSheet(u"background-color: rgb(161, 214, 255);")

        self.gridLayout_3.addWidget(self.textEdit, 3, 0, 1, 5)

        self.time_send = QTextBrowser(self.widget)
        self.time_send.setObjectName(u"time_send")

        self.gridLayout_3.addWidget(self.time_send, 5, 0, 1, 1)

        self.time_return = QTextBrowser(self.widget)
        self.time_return.setObjectName(u"time_return")

        self.gridLayout_3.addWidget(self.time_return, 5, 1, 1, 1)

        self.textBrowser = QTextBrowser(self.widget)
        self.textBrowser.setObjectName(u"textBrowser")
        font2 = QFont()
        font2.setPointSize(9)
        self.textBrowser.setFont(font2)

        self.gridLayout_3.addWidget(self.textBrowser, 0, 0, 1, 2)


        self.gridLayout_2.addLayout(self.gridLayout_3, 0, 1, 1, 1)


        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 933, 22))
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
        self.nameDisplay.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">\u7231\u7761\u89c9\u7684\u661f\u661f</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">\u53ef\u4e50\u52a0\u51b0</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">\u7eff\u8c46\u997c\u7ec5\u58eb                             </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px;"
                        " margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">\u4e9a\u5386\u5c71\u5927</span></p></body></html>", None))
        self.pushButton_send.setText(QCoreApplication.translate("MainWindow", u"\u53d1\u9001", None))
        self.pushButton_end.setText(QCoreApplication.translate("MainWindow", u"\u5173\u95ed", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u52a0\u5bc6\u89e3\u5bc6\u804a\u5929\u4fe1\u606f\u8f6f\u4ef6", None))
    # retranslateUi




