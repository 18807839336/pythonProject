# -*- coding: utf-8 -*-
import socket
import threading

from PyQt5 import QtWidgets
from cryptography.hazmat.primitives.ciphers import algorithms, Cipher, modes
from cryptography.hazmat.primitives import padding
k= b'6\x1a\xf66\x10\xc7\xec\xc8\xeb\xde\xf7\xce\xf6\x83\xc7\xe0k:\xae\xa2#\xc9\xd0\xd5\x974\x8e:=6\xddX'
v = b'Fuw\xec>f8\x97\x13\xf9\xb0\xcfp\xc6\xea\xd0'
#然后，代码定义了一个16字节长的密钥`k`和一个16字节长的向量`v`
#使用`padding.PKCS7`实例化了填充器`pad`。
c = Cipher(algorithms.AES(k), modes.CBC(v))

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class aa(QThread):
    def __init__(self):
        super().__init__()
        self.base=None
        self.sk = socket.socket()
        self.sk.bind(('127.0.0.1', 8890))
        self.sk.listen()
        self.conn, self.addr = self.sk.accept()

    def run(self):

        # 监听链接
        print(111211)

        while True:
            print(11111111)
            # 接收客户端信息
            try:
                self.ret = self.conn.recv(1024)

                dec = c.decryptor()
                # 代码调用了加密器`Cipher.encryptor()`方法，并用该加密器对需要加密的文本进行加密。
                unpad = padding.PKCS7(256).unpadder()

                self.base.textBrowser.append((unpad.update(dec.update(self.ret) + dec.finalize()) + unpad.finalize()).decode()+'\n')
                # 打印客户端信息
                print(self.ret.decode('utf-8')+'8')
                # 结束处理
                if self.ret == b'bye':
                    self.conn.send(b'bye')
                    break

            except:
                print('error')
        # 关闭客户端链接

        self.conn.close()
        # 关闭服务器套接字
        self.sk.close()


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(844, 498)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.listWidget = QtWidgets.QListWidget(self.widget)
        self.listWidget.setMinimumSize(QSize(200, 0))
        self.listWidget.setMaximumSize(QSize(300, 16777215))
        self.listWidget.setStyleSheet("background-color: rgb(226, 255, 254);")
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        icon = QIcon.fromTheme("window-new")
        item.setIcon(icon)
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.gridLayout_2.addWidget(self.listWidget, 0, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setStyleSheet("")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_3.addWidget(self.pushButton, 3, 3, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_3.addWidget(self.pushButton_2, 3, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 3, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_3.addLayout(self.verticalLayout, 0, 1, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(self.widget)
        self.textEdit.setMinimumSize(QSize(600, 100))
        self.textEdit.setMaximumSize(QSize(16777215, 300))
        self.textEdit.setStyleSheet("background-color: rgb(161, 214, 255);")
        self.textEdit.setObjectName("textEdit")
        self.gridLayout_3.addWidget(self.textEdit, 2, 0, 1, 4)
        self.textBrowser = QtWidgets.QTextBrowser(self.widget)
        self.textBrowser.setMinimumSize(QSize(200, 200))
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout_3.addWidget(self.textBrowser, 1, 0, 1, 4)
        self.ch_text = QtWidgets.QTextBrowser(self.widget)
        font = QFont()
        font.setPointSize(24)
        self.ch_text.setFont(font)
        self.ch_text.setObjectName("ch_text")
        self.gridLayout_3.addWidget(self.ch_text, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_3, 0, 6, 1, 1)
        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QRect(0, 0, 844, 22))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("MainWindow", "可乐加冰"))
        item = self.listWidget.item(1)
        item.setText(_translate("MainWindow", "厉害的陈导"))
        item = self.listWidget.item(2)
        item.setText(_translate("MainWindow", "爱睡觉的星星"))
        item = self.listWidget.item(3)
        item.setText(_translate("MainWindow", "五好青年"))
        item = self.listWidget.item(4)
        item.setText(_translate("MainWindow", "绿豆饼爱好者"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton.setText(_translate("MainWindow", "发送"))
        self.pushButton_2.setText(_translate("MainWindow", "关闭"))
        self.textEdit.setHtml(_translate("MainWindow",
                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">你好</p></body></html>"))
        self.ch_text.setHtml(_translate("MainWindow",
                                        "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                        "p, li { white-space: pre-wrap; }\n"
                                        "</style></head><body style=\" font-family:\'SimSun\'; font-size:24pt; font-weight:400; font-style:normal;\">\n"
                                        "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p></body></html>"))
        self.menu.setTitle(_translate("MainWindow", ""))


class Ui_MainWindow2(QMainWindow):
    def __init__(self, *args, **kwargs):
        self.item_num = -1
        super().__init__(*args, **kwargs)
        self.setupUi(self)

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(937, 570)
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
        self.textBrowser = QTextBrowser(self.widget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setMinimumSize(QSize(200, 200))


        self.gridLayout_3.addWidget(self.textBrowser, 1, 1, 1, 3)

        self.textEdit = QTextEdit(self.widget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(600, 100))
        self.textEdit.setMaximumSize(QSize(16777215, 300))
        self.textEdit.setStyleSheet(u"background-color: rgb(161, 214, 255);")

        self.gridLayout_3.addWidget(self.textEdit, 2, 1, 1, 3)

        self.graphicsView = QGraphicsView(self.widget)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setMinimumSize(QSize(50, 50))
        self.graphicsView.setMaximumSize(QSize(80, 80))

        self.gridLayout_3.addWidget(self.graphicsView, 0, 1, 1, 1)

        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"")

        self.gridLayout_3.addWidget(self.pushButton, 3, 3, 1, 1)

        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout_3.addWidget(self.pushButton_2, 3, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 3, 1, 1, 1)

        self.gridLayout_2.addLayout(self.gridLayout_3, 0, 6, 2, 2)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.pushButton_4 = QPushButton(self.widget)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.gridLayout_4.addWidget(self.pushButton_4, 1, 1, 1, 1)

        self.pushButton_3 = QPushButton(self.widget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout_4.addWidget(self.pushButton_3, 1, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_2, 1, 0, 1, 1)

        self.listWidget = QListWidget(self.widget)
        icon = QIcon(QIcon.fromTheme(u"window-new"))

        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setMinimumSize(QSize(120, 0))
        self.listWidget.setMaximumSize(QSize(600, 16777215))
        self.listWidget.setStyleSheet(u"background-color: rgb(226, 255, 254);")

        self.gridLayout_4.addWidget(self.listWidget, 0, 0, 1, 3)

        self.gridLayout_2.addLayout(self.gridLayout_4, 0, 0, 1, 1)

        self.gridLayout.addWidget(self.widget, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 937, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow",
                                                         u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
                                                         "p, li { white-space: pre-wrap; }\n"
                                                         "hr { height: 1px; border-width: 0; }\n"
                                                         "li.unchecked::marker { content: \"\\2610\"; }\n"
                                                         "li.checked::marker { content: \"\\2612\"; }\n"
                                                         "</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">input</p></body></html>",
                                                         None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"发送", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"关闭", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"删除", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"添加", None))


        # __sortingEnabled = self.listWidget.isSortingEnabled()
        # self.listWidget.setSortingEnabled(False)
        # self.listWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton_4.clicked.connect(lambda: self.remove_item())
        self.pushButton_3.clicked.connect(lambda: self.add_item())
        # self.pushButton_2.clicked.connect(lambda: self.show_text())

    # retranslateUi
    def remove_item(self):
        print(self.listWidget.currentRow())
        # print(self.listWidget.currentItem())
        a = self.listWidget.currentRow()
        if a >= 0:
            self.listWidget.takeItem(a)
            self.item_num -= 1

    def add_item(self):
        print(self.item_num)
        QListWidgetItem(self.listWidget)
        a = self.listWidget.item(self.item_num + 1)
        self.item_num += 1
        a.setText(f'聊天对象{self.item_num}')

    def show_text(self, a):
        print()
        # info = input('>>>')
        c = bytes(self.textEdit.toPlainText(), encoding='utf-8')
        print(c)
        a.conn.send(c)
        # self.textBrowser.append()


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
        self.sk.connect(('127.0.0.1', 8898))
        self.sk.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, True)
        self.sk.ioctl(socket.SIO_KEEPALIVE_VALS, (1, 60 * 1000, 30 * 1000))

    def renmin(self, item):
        item_text = item.text()
        self.ui.ch_text.setText(item_text)

    def zx(self):
        threading.Thread(target=self.send()).start()

    def send(self):
        try:
            print('this')
            wenben = self.ui.textEdit.toPlainText()

            self.sk.send(bytes(wenben, encoding='utf-8'))
            ret = self.sk.recv(1024)
            self.finished.emit(ret.decode('utf-8'))

        except:
            print('error')

    def updateText(self, ret):

        self.ui.textBrowser.setText(ret)
