# class1.py 

#클래스를 정의(새로운 형식을 만들기)
#원본은 1개 
class Person:
    #생성자(초기화)메서드
    def __init__(self):
        self.name = "default name"
    #인스턴스 메서드 
    def print(self):
        print("My name is {0}".format(self.name))

#인스턴스 생성(복사본은 여러개)
p1 = Person()
p2 = Person()
p2.name = "전우치"
p1.print()
p2.print()
#동적 형식을 언어여서 변수 추가가 자유롭다~~ 
Person.title = "new title"
print(p1.title)
print(p2.title)
print(Person.title)
