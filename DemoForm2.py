#DemoForm2.py 
# DemoForm2.ui(화면단) + DemoForm2.py(로직단)
import sys 
from PyQt5.QtWidgets import * 
from PyQt5 import uic 

#로딩하는 파일
form_class = uic.loadUiType("DemoForm2.ui")[0]

#폼클래스 정의(다중상속):QMainWindow 상속
class DemoForm(QMainWindow, form_class):
    #생성자 메서드
    def __init__(self):
        super().__init__() 
        self.setupUi(self)
    #시그널을 처리하는 슬롯 메서드
    def firstClick(self):
        self.label.setText("버튼1번 클릭")
    def secondClick(self):
        self.label.setText("버튼2번 클릭~~")
    def thirdClick(self):
        self.label.setText("버튼3번 클릭!!")

#진입점 체크(직접 모듈을 실행한 경우 수행)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoWindow = DemoForm()
    demoWindow.show()
    app.exec_() 
