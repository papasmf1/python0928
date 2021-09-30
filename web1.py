# web1.py 
#from 패키지명 import 모듈명 
from bs4 import BeautifulSoup

#페이지 로딩
#연속적으로 메소드나 함수를 호출: 메서드 체인 
page = open("c:\\work\\test01.html", "rt", encoding="utf-8").read()
#검색이 용이한 객체 생성: 정해진 문자열(html문서, xml은 주로 데이터 저장과 교환)
soup = BeautifulSoup(page, "html.parser")
#전체 페이지를 보기
print( soup.prettify() )

