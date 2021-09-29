# DemoFilter.py 

#함수를 정의
def getBiggerThan20(i):
    return i > 20 

#필터링하는 조건으로 함수를 넘기기 
lst = [10, 25, 30]
item = filter(getBiggerThan20, lst)
for item in lst:
    print(item)


