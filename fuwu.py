import socket

from PyQt5.QtWidgets import QApplication

# 创建服务器端套接字

# 设置给定套接字选项的值。
# sk.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# 把地址绑定到套接字

import UI

app = QApplication([])
c = UI.Ui_MainWindow2()

c.show()
a = UI.aa()
a.base = c
a.start()
c.pushButton_2.clicked.connect(lambda: UI.Ui_MainWindow2.show_text(c, a))
app.exec()
print(1)
# 接受客户端链接
