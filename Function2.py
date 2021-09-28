# Function2.py 

#디버깅 연습
def intersect(prelist, postlist):
    #지역변수 리스트로 초기화
    retList = []
    # H(0) | A(1) | M(2)
    for x in prelist:
        if x in postlist and x not in retList:
            retList.append(x)
    return retList

#호출 
#중단점, 중지점(Break Point)
print( intersect("HAM","SPAM") )


#합집합 함수(가변인자)
def union(*ar):
    result = []
    for item in ar:
        for x in item:
            if x not in result:
                result.append(x)
    return result 

#호출 
print( union("HAM","EGG") )
print( union("HAM","EGG","SPAM") )


#불변형식 (정수, 실수, 튜플, 문자열...)
a = 1.2 
print( id(a) )
a = 2.3 
print( id(a) )

#가변형식 99%
print("---가변형식---")
lst = [1,2,3]
print( id(lst) )
lst.append(4)
print( id(lst) )

#람다 함수(이름이 없는 간단한 함수 정의)
g = lambda x,y:x*y 
print( g(3,4) )
print( (lambda x:x*x)(3) )

print( globals() )

