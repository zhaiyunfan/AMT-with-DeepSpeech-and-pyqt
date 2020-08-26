import sys,qdarkstyle
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from functools import partial

import GUI

# 下面是一些触发函数

def clickExit(app):
    app.quit()

def openFile(ui,MainWindow):
    get_filename_path, ok = QFileDialog.getOpenFileName(MainWindow,
                                        "选取要上传的文件",
                                    "/",
                                        "All Files (*);;Text Files (*.mp3)")
    if ok:
        ui.textBrowser.setText(str(get_filename_path))
        ui.uploadLabel.setText("已选择文件")

def openDirectory(ui,MainWindow):
    get_directory_path = QFileDialog.getExistingDirectory(MainWindow,
                                    "选取下载路径文件夹",
                                    "/")
    ui.textBrowser.setText(str(get_directory_path))
    ui.downloadLabel.setText("已选择文件夹")

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

    # ui.pushButton.clicked.connect(partial(changeLabel, ui))
    ui.actionExit.triggered.connect(partial(clickExit, app))
    
    # 在上面绑定信号和槽

    sys.exit(app.exec_())

