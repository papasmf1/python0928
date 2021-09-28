# class2.py 
#클래스를 정의(새로운 형식을 만들기)
#원본은 1개 
class Person:
    #클래스에서 공유하는 변수값
    num_person = 0 
    #생성자(초기화)메서드
    def __init__(self):
        self.name = "default name"
        Person.num_person += 1 
    #인스턴스 메서드 
    def print(self):
        print("My name is {0}".format(self.name))

#인스턴스 생성(복사본은 여러개)
p1 = Person()
p2 = Person()
p3 = Person() 
print("인스턴스의 갯수:{0}".format(Person.num_person) )


