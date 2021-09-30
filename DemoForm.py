#DemoForm.py 
# DemoForm.ui(화면단) + DemoForm.py(로직단)
import sys 
from PyQt5.QtWidgets import * 
from PyQt5 import uic 

form_class = uic.loadUiType("DemoForm.ui")[0]

#폼클래스 정의(다중상속)
class DemoForm(QDialog, form_class):
    #생성자 메서드
    def __init__(self):
        super().__init__() 
        self.setupUi(self)
        self.label.setText("첫번째 Qt데모")

#진입점 체크(직접 모듈을 실행한 경우 수행)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoWindow = DemoForm()
    demoWindow.show()
    app.exec_() 
