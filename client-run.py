import sys
from PyQt5.QtWidgets import *
import ui_client   #把需要运行的项目传进来
#运行的固定代码
app = QApplication(sys.argv)
# 创建一个子类
w = ui_client.Ui_Window()
# 展示传进来的项目
w.show()
app.exec()
