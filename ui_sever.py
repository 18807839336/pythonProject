import threading

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import socket

from cryptography.hazmat.primitives.ciphers import algorithms, Cipher, modes
from cryptography.hazmat.primitives import padding


class Ui_MainWindow(QMainWindow):  # 传输一个具体的QMainWindow
    # 信号：提醒界面更新
    finished = pyqtSignal(str)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        k = b'6\x1a\xf66\x10\xc7\xec\xc8\xeb\xde\xf7\xce\xf6\x83\xc7\xe0k:\xae\xa2#\xc9\xd0\xd5\x974\x8e:=6\xddX'
        v = b'Fuw\xec>f8\x97\x13\xf9\xb0\xcfp\xc6\xea\xd0'
        self.mima = Cipher(algorithms.AES(k), modes.CBC(v))
        self.pushButton_send.clicked.connect(self.thread_send)
        self.finished.connect(self.updateText)
        threading.Thread(target=self.ser_socket).start()

    def thread_send(self):
        threading.Thread(target=self.ser_send).start()

    def updateText(self, ret: str):
        self.textDisplay.setText(str(ret))

    def ser_send(self):
        text = self.textEdit.toPlainText()
        enc = self.mima.encryptor()  # 加密
        pad = padding.PKCS7(256).padder()  # 填充
        aa = enc.update(pad.update(text.encode()) + pad.finalize()) + enc.finalize()  # 得到加密结果aa
        self.c.send(aa)  # 发送加密信息给sever

    def ser_socket(self):
        # 然后，代码定义了一个16字节长的密钥`k`和一个16字节长的向量`v`
        s = socket.socket()  # 创建 socket 对象
        host = socket.gethostname()  # 获取本地主机名
        port = 12965  # 设置端口
        s.bind((host, port))  # 绑定端口
        s.listen(5)  # 等待客户端连接
        self.c, self.addr = s.accept()
        print('连接地址：', self.addr)
        while True:
            # 建立客户端连接
            # print('连接地址：', addr)
            print('wait...')
            res = self.c.recv(1024)
            dec = self.mima.decryptor()  # 解密方法
            unpad = padding.PKCS7(256).unpadder()  # 拿掉填充
            jm = unpad.update(dec.update(res) + dec.finalize()) + unpad.finalize()
            jm = jm.decode()
            print(jm)  # 输出解密内容
            self.finished.emit(str(jm))
            print(res)  # 接受sever端发来的信息，打印出来


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
        self.nameList = QListWidget(self.widget)
        icon = QIcon()
        iconThemeName = u"window-new"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        __qlistwidgetitem = QListWidgetItem(self.nameList)
        __qlistwidgetitem.setIcon(icon);
        QListWidgetItem(self.nameList)
        QListWidgetItem(self.nameList)
        QListWidgetItem(self.nameList)
        QListWidgetItem(self.nameList)
        self.nameList.setObjectName(u"nameList")
        self.nameList.setMinimumSize(QSize(200, 0))
        self.nameList.setMaximumSize(QSize(300, 16777215))
        self.nameList.setStyleSheet(u"background-color: rgb(226, 255, 254);")

        self.gridLayout_2.addWidget(self.nameList, 0, 0, 1, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.textDisplay = QTextBrowser(self.widget)
        self.textDisplay.setObjectName(u"textDisplay")
        self.textDisplay.setMinimumSize(QSize(200, 200))
        font = QFont()
        font.setItalic(True)
        self.textDisplay.setFont(font)

        self.gridLayout_3.addWidget(self.textDisplay, 2, 0, 1, 12)

        self.nameDisplay = QTextBrowser(self.widget)
        self.nameDisplay.setObjectName(u"nameDisplay")
        font1 = QFont()
        font1.setPointSize(24)
        font1.setItalic(False)
        self.nameDisplay.setFont(font1)

        self.gridLayout_3.addWidget(self.nameDisplay, 0, 0, 1, 1)

        self.pushButton_end = QPushButton(self.widget)
        self.pushButton_end.setObjectName(u"pushButton_end")
        self.pushButton_end.setStyleSheet(u"")

        self.gridLayout_3.addWidget(self.pushButton_end, 4, 11, 1, 1)

        self.textEdit = QTextEdit(self.widget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(600, 100))
        self.textEdit.setMaximumSize(QSize(16777215, 300))
        font2 = QFont()
        font2.setItalic(False)
        font2.setUnderline(False)
        self.textEdit.setFont(font2)
        self.textEdit.setStyleSheet(u"background-color: rgb(161, 214, 255);")

        self.gridLayout_3.addWidget(self.textEdit, 3, 0, 1, 12)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_3, 0, 6, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_7, 0, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_2, 1, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_2, 0, 7, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_4, 0, 5, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_5, 0, 4, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")

        self.gridLayout_3.addLayout(self.verticalLayout, 0, 9, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer, 0, 8, 1, 1)

        self.pushButton_send = QPushButton(self.widget)
        self.pushButton_send.setObjectName(u"pushButton_send")

        self.gridLayout_3.addWidget(self.pushButton_send, 4, 10, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 4, 0, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_6, 0, 3, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_8, 0, 1, 1, 1)

        self.gridLayout_2.addLayout(self.gridLayout_3, 0, 6, 1, 1)
        self.nameDisplay.setMaximumSize(QSize(80, 80))
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

        __sortingEnabled = self.nameList.isSortingEnabled()
        self.nameList.setSortingEnabled(False)
        ___qlistwidgetitem = self.nameList.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u53ef\u4e50\u52a0\u51b0", None));
        ___qlistwidgetitem1 = self.nameList.item(1)
        ___qlistwidgetitem1.setText(
            QCoreApplication.translate("MainWindow", u"\u5389\u5bb3\u7684\u9648\u5bfc", None));
        ___qlistwidgetitem2 = self.nameList.item(2)
        ___qlistwidgetitem2.setText(
            QCoreApplication.translate("MainWindow", u"\u7231\u7761\u89c9\u7684\u661f\u661f", None));
        ___qlistwidgetitem3 = self.nameList.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u4e94\u597d\u9752\u5e74", None));
        ___qlistwidgetitem4 = self.nameList.item(4)
        ___qlistwidgetitem4.setText(
            QCoreApplication.translate("MainWindow", u"\u7eff\u8c46\u997c\u7231\u597d\u8005", None));
        self.nameList.setSortingEnabled(__sortingEnabled)

        self.nameDisplay.setHtml(QCoreApplication.translate("MainWindow",
                                                            u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                            "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                            "p, li { white-space: pre-wrap; }\n"
                                                            "</style></head><body style=\" font-family:'SimSun'; font-size:24pt; font-weight:400; font-style:normal;\">\n"
                                                            "<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p></body></html>",
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
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u4e3b\u9875\u9762", None))
    # retranslateUi
