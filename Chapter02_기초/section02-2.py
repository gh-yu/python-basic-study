# Section02-2
# 파이썬 기초 코딩
# 몸풀기 코딩 실습

# import this # 파이썬 언어 철학 출력힘
# # 붙이면 인터프리터가 해석 안함, 주석 할때 한 칸 띄우는 것이 기본 인덴트 원칙
import sys

# 파이썬 기본 인코딩 : UTF-8
print(sys.stdin.encoding) # 입력 인코딩 : utf-8
print(sys.stdout.encoding) # 출력 인코딩 : utf-8

# 출력문
print('My name is Goodboy')

# 변수 선언
myName = 'Goodboy'
# 변수 : 값을 저장하는 공간
# 오른쪽에 있는 값을 왼쪽에 할당
# myName : 변수, 'Goodboy' : 값

# 조건문 : 조건에 맞으면 실행
if myName == "Goodboy":
    print('ok')
else:
    print('no')

# == : 같다 (파이썬에서는 문자열 ==로 비교)
# 변수 myName에 담긴 값이 'Goodboy'와 같으면 'ok' 출력

# 반복문
# 구구단 출력
for i in range(1, 10):
    for j in range(1, 10):
        print('%d * %d = ' % (i,j), i*j)


# 들여쓰기 (indent) 안하면 에러가 남 -> indent도 문법
# for i in range(1, 10):
# print('%d * %d = ' % (i,j), i*j) 
# IndentationError: expected an indented block

# 변수 선언(한글) <- 권장되지 않음
이름 = "좋은사람"
print(이름)

# 함수 선언(한글)
def 인사():
    print("안녕하세요. 반갑습니다.")

인사() # 함수 실행

# 함수 선언
def greeting():
    print('hello!')

# 함수 실행
greeting()

# 클래스
class Cookie:
    pass # pass문 : 함수나 클래스의 구현을 미룰때 사용

# 객체 생성
cookie = Cookie()

print(id(cookie)) # id() : Return the identity of an object.
# 2242348404920
print(dir(cookie)) # dir() : 매개변수로 전달된 객체의 구성 목록 리스트(클래스의 함수들) 반환
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']