class Person:
    pass

class Bird:
    pass

#Person클래스를 상속받아서 Student를 정의
class Student(Person):
    pass

p, s = Person(), Student()

#함수의 경우는 isinstance() 
#메서드의 경우는 ~.methodA() 
print("p is instance of Person: ", isinstance(p, Person))
print("s is instance of Person: ", isinstance(s, Person))
print("p is instance of Object: ", isinstance(p, object))
print("p is instance of Bird: ", isinstance(p, Bird))
print("int is instance of Object: ", isinstance(int, object))