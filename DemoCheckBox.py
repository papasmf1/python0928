# DemoCheckBox.py
import sys
from PyQt5.QtWidgets import *

#100% 코딩하는 스타일로 작업(유지보수하기 편하다) 
class DemoWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        #setGeometry(x, y, width, height)
        self.setGeometry(200, 200, 400, 400)

        self.myBox1 = QCheckBox("아이폰", self)
        #(x축, y축)
        self.myBox1 .move(10, 20)
        #(width, height)
        self.myBox1.resize(150, 30)
        #체크박스 위젯의 시그널에 슬롯 메서드 연결
        self.myBox1.stateChanged.connect(self.checkBoxState)

        self.checkBox2 = QCheckBox("안드로이드폰", self)
        self.checkBox2.move(10, 50)
        self.checkBox2.resize(150, 30)
        self.checkBox2.stateChanged.connect(self.checkBoxState)

        self.checkBox3 = QCheckBox("윈도우폰", self)
        self.checkBox3.move(10, 80)
        self.checkBox3.resize(150, 30)
        self.checkBox3.stateChanged.connect(self.checkBoxState)

        self.statusBar = QStatusBar(self)
        self.setStatusBar(self.statusBar)

    def checkBoxState(self):
        msg = ""
        if self.myBox1.isChecked() == True:
            msg += "아이폰 "
        if self.checkBox2.isChecked() == True:
            msg += "안드로이드폰 "
        if self.checkBox3.isChecked() == True:
            msg += "윈도우폰 "
        self.statusBar.showMessage(msg)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoWindow = DemoWindow()
    demoWindow.show()
    app.exec_()