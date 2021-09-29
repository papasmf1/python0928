# DemoFile.py 

for x in range(1,6):
    print(x, "*", x, "=", x*x)


for x in range(1,6):
    print(x, "*", x, "=", str(x*x).rjust(3) )


print("---서식문자---")
print("{0:x}".format(10))
print("{0:b}".format(10))
print("{0:,}".format(15000000))

#URL주소를 결합연산
url = "http://www.credu.com/?page=" + str(1) 
print( url ) 

#텍스트 파일을 읽기, 쓰기
f = open("c:\\work\\demo.txt", "wt")
f.write("첫번째\n두번째\n세번째\n")
f.close()

f = open("c:\\work\\demo.txt", "rt")
result = f.read()
print( result )

print("어디쯤:", f.tell() )
#처음로 돌아가~~ 
f.seek(0)
print( f.readline() )
print( f.readline() )
f.seek(0)
#리스트에 리턴
lst = f.readlines() 
print( lst )
f.close() 
