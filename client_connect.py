import socket  # 导入 socket 模块

s = socket.socket()  # 创建 socket 对象
host = socket.gethostname()  # 获取本地主机名
port = 12345  # 设置端口
s.bind((host, port))  # 绑定端口

s.listen(5)  # 等待客户端连接
c, addr = s.accept()
print('连接地址：', addr)
while True:
      # 建立客户端连接
    #print('连接地址：', addr)

    print(c.recv(1024).decode())
    text = input()
    c.send(text.encode())
