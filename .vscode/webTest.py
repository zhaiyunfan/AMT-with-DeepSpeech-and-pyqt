import socket                    # 调用socket库

HOST = "192.168.43.198"          # 定义服务器ip
PORT = 5555                      # 定义端口号
addr = (HOST,PORT)               # 由于使用socket进行连接，需要把ip和端口先转换为元组
c = socket.socket(socket.AF_INET,socket.SOCK_STREAM)     # 设定了网络连接方式，以及传输使用的协议
c.connect(addr) #连接服务器  

def send_file():
    data = c.recv(1024)                       # 设定接受数据大小
    print(str(data,encoding='gbk'))           # 打印出来，看起来直观，测试用，可以去除
    filepath = input("请输入文件名和路径:")      # 输入要从上传的文件
    with open(filepath,"rb") as f:            # 以只读方式打开指定的文件
        file = f.read()                  # 以byte 的方式读取文件内容
        datas = c.sendall(file)                      # 发送文件内容

def get_file():
    filepath = input("请输入服务器文件路径：")   # 输入要从服务器下载的文件
    c.send(bytes(filepath,encoding='gbk'))   # 向服务器发送我们要下载的信息
    data = c.recv(20480)                     # 指定接受数据大小
    with open("shadow.txt","wb") as f:       # 打开本地文件，将接受到的数据写入本地指定的目录
        f.write(data)


def main():
    while True:
        cmd = input("请输入命令:")                 # 获取用户输入的命令
        c.send(bytes(cmd,encoding='gbk'))        # 发送用户输入的命令
        if cmd == "bye":                         # 如果用户输入bye结束程序
            break
        if cmd == "upload":                      # 如果用户输入upload,调用send_file()函数，进行文件上传
            send_file()
        if cmd == "down":                        # 如果用户输入down,调用get_file()函数，进行文件下载
            get_file()
        data = c.recv(20480)                     # 设置接受数据大小
        print(str(data,encoding='gbk'))          # 将接受的数据打印出来，没多大用
    # ~ c.send(b'word')  #发送字符串前面加b转换bytes比特格式     
    c.close()


if __name__  == "__main__":                      # 调用main()函数
    main()