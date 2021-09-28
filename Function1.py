# 주석을 추가할 경우 사용 
# Function1.py 

#함수를 정의
def times(a,b):
    return a*b 

#함수를 호출
result = times(5,6)
print( result )

#리턴을 하지 않는 함수
def setValue(newValue):
    #지역변수(a)
    a = newValue
    print("함수내부: ", a)

#호출
setValue(5)

#다중의 값을 리턴(Tuple로 받기)
def swap(x,y):
    return y, x 

#호출
result = swap(3,4)
print( result )
print( result[0] )
print( result[1] )


