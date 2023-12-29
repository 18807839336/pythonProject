import socket  # 导入 socket 模块
from cryptography.hazmat.primitives.ciphers import algorithms, Cipher, modes
from cryptography.hazmat.primitives import padding
#首先，代码导入了必要的依赖：`os`模块、`algorithms`、`Cipher`和`modes`类、`padding`模块。其中，`os`模块主要用于生成随机种子，`Cipher`和`modes`类用于创建加密和解密所需的实例，`padding`模块则用于填充。
k= b'6\x1a\xf66\x10\xc7\xec\xc8\xeb\xde\xf7\xce\xf6\x83\xc7\xe0k:\xae\xa2#\xc9\xd0\xd5\x974\x8e:=6\xddX'
v = b'Fuw\xec>f8\x97\x13\xf9\xb0\xcfp\xc6\xea\xd0'
mima = Cipher(algorithms.AES(k), modes.CBC(v))  #实例化
#然后，代码定义了一个16字节长的密钥`k`和一个16字节长的向量`v`
s = socket.socket()  # 创建 socket 对象
host = socket.gethostname()  # 获取本地主机名
port = 12345  # 设置端口号
s.connect((host, port ))
while True:
    text=input()


    s.send(text.encode())

    t_enc=s.recv(1024)
    dec = mima.decryptor()
    # 代码调用了加密器`Cipher.encryptor()`方法，并用该加密器对需要加密的文本进行加密。
    unpad = padding.PKCS7(256).unpadder()
    print(unpad.update(dec.update(t_enc) + dec.finalize()) + unpad.finalize())



