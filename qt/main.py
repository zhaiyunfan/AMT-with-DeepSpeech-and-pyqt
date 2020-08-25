import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from functools import partial

import HelloWorld

def changeLabel(ui):
    if ui.label.text() == "HELLO WORLD":
        ui.label.setText("HELLO PYQT")
    else:
        ui.label.setText("HELLO WORLD")

def clickExit(app):
    app.quit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = HelloWorld.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.pushButton.clicked.connect(partial(changeLabel, ui))
    ui.actionExit.triggered.connect(partial(clickExit, app))
    sys.exit(app.exec_())

