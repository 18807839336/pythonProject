import sys
from PyQt5.QtWidgets import *
import ui_sever   #把需要运行的项目传进来
#运行的固定代码
app = QApplication(sys.argv)
# 创建一个子类
w = ui_sever.Ui_MainWindow()
# 展示传进来的项目
w.show()
app.exec()