class MyClass:
    #생성자 메서드 
    def __init__(self, value):
        self.Value = value 
        print("Instance is created! Value = ", value)
    #소멸자 메서드     
    def __del__(self):
        print("Instance is deleted!")
        

c = MyClass(10)
#참조 카운트: 1-->0 
#del c 

print("전체 코드 실행 종료")
