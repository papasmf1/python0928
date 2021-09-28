# DemoLoop.py 

#수열 함수
print( list(range(10)) ) 
print( list(range(1,11)) ) 
print( list(range(10,0,-1)) ) 

#리스트 내장(컴프리헨션)
lst = list(range(1,11))
print( [i**2 for i in lst if i > 5] )

