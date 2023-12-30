from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Ui_Window(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
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
        font.setPointSize(24)
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
"</style></head><body style=\" font-family:'SimSun'; font-size:24pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9pt;\"><br /></p></body></html>", None))
        self.textEdit.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u5b50\u9875\u9762", None))
    # retranslateUi

