import os,sys,qdarkstyle,webbrowser,datetime
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from functools import partial

import GUI

# 下面是一些触发函数

def timePrint(ui):
    now_time = datetime.datetime.now()
    now_time = datetime.datetime.strftime(now_time,'%H:%M:%S')
    ui.textBrowser.append(now_time)

def clickExit(app):
    app.quit()

def clickVHV(ui):
    webbrowser.open("https://verovio.humdrum.org/",new=0,autoraise=True)
    timePrint(ui)
    ui.textBrowser.append("已启动VHV编辑器")
    # 如果VHV在win上运行的问题解决了，可以用os.system启动本地VHV，详见README

def openFile(ui,MainWindow):
    get_filename_path, ok = QFileDialog.getOpenFileName(MainWindow,
                                        "选取要上传的文件",
                                    "/",
                                        "All Files (*);;Text Files (*.mp3)")
    if ok:
        timePrint(ui)
        ui.textBrowser.append("已选择上传音频文件路径为" + str(get_filename_path)+"\n")
        ui.uploadLabel.setText("已选择文件")
        ui.filename_path = get_filename_path

def openDirectory(ui,MainWindow):
    get_directory_path = QFileDialog.getExistingDirectory(MainWindow,
                                    "选取下载路径文件夹",
                                    "/")
    if get_directory_path!="":                                
        timePrint(ui)
        ui.textBrowser.append("已选择下载音频文件路径为" + str(get_directory_path)+"\n")
        ui.downloadLabel.setText("已选择文件夹")
        ui.directory_path = get_directory_path
        # print(ui.directory_path)

# 上面是一些触发函数

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())   #界面风格
    MainWindow = QMainWindow()
    ui = GUI.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    # 在下面绑定信号和槽

    ui.upSelectButton.clicked.connect(partial(openFile, ui,MainWindow))
    ui.downSelectButton.clicked.connect(partial(openDirectory,ui,MainWindow))

    ui.actionExit.triggered.connect(partial(clickExit, app))
    ui.action_VHV.triggered.connect(partial(clickVHV,ui))
    # 在上面绑定信号和槽

    sys.exit(app.exec_())

