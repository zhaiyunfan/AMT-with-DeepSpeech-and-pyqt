import os,sys,socket,qdarkstyle,webbrowser,datetime
from PyQt5.Qt import QThread
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog,QInputDialog,QMessageBox
from functools import partial

import GUI

# 下面是一些自定义函数
def getIP(ui)->str: # 启动IP地址的输入框
    text, ok=QInputDialog.getText(MainWindow, 'Text Input Dialog', '输入服务器ip地址')
    if ok and text:
        return str(text)

def timePrint(ui):  # 打印当前时间
    now_time = datetime.datetime.now()
    now_time = datetime.datetime.strftime(now_time,'%H:%M:%S')
    ui.textBrowser.append(now_time)

# 下面是一些触发函数
def clickExit(app):
    app.quit()

def clickVHV(ui):
    webbrowser.open("https://verovio.humdrum.org/",new=0,autoraise=True)
    timePrint(ui)
    ui.textBrowser.append("已启动VHV编辑器")
    # 如果VHV在win上运行的问题解决了，可以用os.system启动本地VHV，详见README

def openFile(ui,MainWindow):
    ui.uploadProgressBar.setValue(0)
    get_filename_path, ok = QFileDialog.getOpenFileName(MainWindow,
                                        "选取要上传的文件",
                                    "/",
                                        "All Files (*);;Text Files (*.wav)")
    if ok:
        timePrint(ui)
        ui.textBrowser.append("已选择上传音频文件路径为" + str(get_filename_path)+"\n")
        ui.uploadLabel.setText("已选择文件")
        ui.filename_path = get_filename_path

def openDirectory(ui,MainWindow):
    ui.downloadProgressBar.setValue(0)
    get_directory_path = QFileDialog.getExistingDirectory(MainWindow,
                                    "选取下载路径文件夹",
                                    "/")
    if get_directory_path!="":                                
        timePrint(ui)
        ui.textBrowser.append("已选择下载音频文件路径为" + str(get_directory_path)+"\n")
        ui.downloadLabel.setText("已选择文件夹")
        ui.directory_path = get_directory_path
        # print(ui.directory_path)

def uploadPush(ui,c):
    timePrint(ui)
    ui.textBrowser.append("开始上传音频，请稍候")
    ui.uploadProgressBar.setValue(30)
    cmd = "upload"
    c.send(bytes(cmd,encoding='gbk'))         # 发送用户输入的命令
    ui.uploadProgressBar.setValue(60)
    data = c.recv(1024)                       # 设定接受数据大小
    filepath = ui.filename_path               # 输入要从上传的文件
    with open(filepath,"rb") as f:            # 以只读方式打开指定的文件
        file = f.read()                       # 以byte 的方式读取文件内容
        datas = c.sendall(file)               # 发送文件内容
    data = c.recv(20480)
    ui.uploadProgressBar.setValue(100)
    timePrint(ui)
    ui.textBrowser.append("上传音频成功，正在识谱，请稍候")

def downloadPush(ui,c):
    timePrint(ui)
    ui.textBrowser.append("开始下载音频，请稍候")
    ui.downloadProgressBar.setValue(30)
    cmd = "down"                                  # 获取用户输入的命令
    c.send(bytes(cmd,encoding='gbk'))             # 发送用户输入的命令
    filepath = "/home/zhaiyunfan/文档/data.txt"   # 输入要从服务器下载的文件
    c.send(bytes(filepath,encoding='gbk'))        # 向服务器发送我们要下载的信息
    ui.downloadProgressBar.setValue(60)
    data = c.recv(20480)                          # 指定接受数据大小
    with open("data.krn","wb") as f:              # 打开本地文件，将接受到的数据写入本地指定的目录
        f.write(data)    
    data = c.recv(20480)
    ui.downloadProgressBar.setValue(100)
    timePrint(ui)
    ui.textBrowser.append("下载曲谱成功，您可以在菜单栏启动VHV编辑器以预览、修改曲谱或输出其他格式曲谱")

# 上面是一些触发函数

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())   #界面风格
    MainWindow = QMainWindow()
    ui = GUI.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    # 连接服务器
    # HOST = "10.18.148.102"          # 定义服务器ip
    HOST = getIP(MainWindow)
    PORT = 5555                      # 定义端口号
    addr = (HOST,PORT)               # 由于使用socket进行连接，需要把ip和端口先转换为元组
    c = socket.socket(socket.AF_INET,socket.SOCK_STREAM)     # 设定了网络连接方式，以及传输使用的协议
    QMessageBox.about(MainWindow, "提示", "正在连接服务器，请勿操作窗口，等待程序自动处理")
    c.connect(addr)                  #连接服务器  
    QMessageBox.about(MainWindow, "提示", "服务器连接成功")

    # 在下面绑定信号和槽
    ui.upSelectButton.clicked.connect(partial(openFile, ui,MainWindow))
    ui.downSelectButton.clicked.connect(partial(openDirectory,ui,MainWindow))

    ui.upPushButton.clicked.connect(partial(uploadPush,ui,c))
    ui.downPushButton.clicked.connect(partial(downloadPush,ui,c))

    ui.actionExit.triggered.connect(partial(clickExit, app))
    ui.action_VHV.triggered.connect(partial(clickVHV,ui))
    # 在上面绑定信号和槽

    sys.exit(app.exec_())
