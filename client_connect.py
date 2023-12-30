import socket  # 导入 socket 模块
from cryptography.hazmat.primitives.ciphers import algorithms, Cipher, modes
from cryptography.hazmat.primitives import padding
#首先，代码导入了必要的依赖：`os`模块、`algorithms`、`Cipher`和`modes`类、`padding`模块。其中，`os`模块主要用于生成随机种子，`Cipher`和`modes`类用于创建加密和解密所需的实例，`padding`模块则用于填充。
k= b'6\x1a\xf66\x10\xc7\xec\xc8\xeb\xde\xf7\xce\xf6\x83\xc7\xe0k:\xae\xa2#\xc9\xd0\xd5\x974\x8e:=6\xddX'
v = b'Fuw\xec>f8\x97\x13\xf9\xb0\xcfp\xc6\xea\xd0'
mima = Cipher(algorithms.AES(k), modes.CBC(v))  #实例化
#代码定义了一个16字节长的密钥`k`和一个16字节长的向量`v`
s = socket.socket()  # 创建 socket 对象
host = socket.gethostname()  # 获取本地主机名
port = 12965  # 设置端口号
s.connect((host, port))
while True:
    text=input()#获取键盘输入
    enc = mima.encryptor()  # 加密
    pad = padding.PKCS7(256).padder()  # 填充
    aa = enc.update(pad.update(text.encode()) + pad.finalize()) + enc.finalize()  # 得到加密结果aa
    s.send(aa)  #发送加密内容给client端

    jiami2=s.recv(1024)
    print(jiami2)  # 接受sever端发来的加密信息，打印出来

    t_enc = jiami2  # 接受client传过来的加密内容aa,一次接受1024

    dec = mima.decryptor()   #解密方法
    unpad = padding.PKCS7(256).unpadder()    #拿掉填充
    print(unpad.update(dec.update(t_enc) + dec.finalize()) + unpad.finalize())#输出解密内容
