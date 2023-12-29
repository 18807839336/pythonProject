import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit

if __name__=='__main__':
    #第一步！！！！只要是Qt制作APP，必须有且只有1个QApplication对象
    #sys.argv当做参数的目的是将运行时的命令参数传递给QApplication对象
    app = QApplication(sys.argv)

    w = QWidget()

    #设置窗口标题
    w.setWindowTitle("第一个PYQT程序")

    #纯文本
    label = QLabel("账号",w)
    label.setGeometry(25,20,30,30)

    #文本框
    edit = QLineEdit(w)
    edit.setPlaceholderText("请输入账号")
    edit.setGeometry(65,20,200,20)
    
    #往窗口里面加控件
    btn1 = QPushButton("zhangsan",w)
    btn1.setGeometry(50,80,70,30)

   
    #展示窗口
    w.show()


    #第二步！！！！程序进行循环等待状态，运行程序，直到关闭了窗口
    app.exec()