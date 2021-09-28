#부모 클래스 정의 
class Person:
    #초기화 메서드 
    def __init__(self, name, phoneNumber):
        self.name = name
        self.phoneNumber = phoneNumber
    #인스턴스 메서드 
    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(
            self.name, self.phoneNumber))

#자식 클래스 정의
class Student(Person):
    #상속받은 메서드를 재정의(덮어쓰기, override)
    def __init__(self, name, phoneNumber, subject, studentID):
        #명시적으로 부모 클래스 생성자 호출
        #Java, C#(super, base키워드)
        Person.__init__(self, name, phoneNumber)
        self.subject = subject
        self.studentID = studentID
    #정의되지 않은 인자 처리

    #상속받은 메서드를 덮어쓰기(재정의) 
    def printInfo(self):
        print("Info(Name:{0}, Phone Number: {1})".format(  
            self.name, self.phoneNumber))
        print("Info(Subject:{0}, StudentID: {1})".format(  
            self.subject, self.studentID))

    def methodA(self, server, **user):
        strURL = "http://" + server + "/?"
        for key in user.keys():
            strURL += key + "=" + user[key] + "&"
        return strURL 

#인스턴스 생성 
p = Person("전우치", "010-222-1234")
s = Student("이순신", "010-111-1234","컴공", "991122")

p.printInfo()
s.printInfo()

print( s.methodA("credu.com", id="kim", name="전우치") ) 



