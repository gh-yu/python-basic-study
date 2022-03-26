# Section04-1
# 파이썬 데이터 타입(자료형)
# 데이터타입, 숫자형, 숫자형 연산

'''
int : 정수
float : 실수
complex : 복소수
bool : 불린
str : 문자열(시퀀스)
list : 리스트(시퀀스)
tuple : 튜플(시퀀스)
set : 집합
dict : 사전

bytearray
byte
frozenset
'''

v_str1 = "Niceman"
v_bool = True
v_str2 = "Coodboy"
v_float = 10.3
v_int = 7
v_dict = {
    "name" : "Kim",
    "age" : 25
}
v_list = [3, 5, 7]
v_tuple = 3, 5, 7
v_set = {7, 8, 9}

# 타입 출력
print(type(v_str1))
print(type(v_bool))
print(type(v_str2))
print(type(v_int))
print(type(v_float)) 
print(type(v_dict))
print(type(v_list))
print(type(v_tuple))
print(type(v_set))

"""
실행 결과
<class 'str'>
<class 'bool'>  
<class 'str'>  
<class 'int'>  
<class 'float'>
<class 'dict'>
<class 'list'>
<class 'tuple'>
<class 'set'>
"""


# Numeric Operation (숫자형 연산자)
# https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex
"""
+ 
- 
* 
/ 
// : 몫 
% : 나머지
abs(x) 
int(x) 
float(x) 
complex(x)
pow(x, y) 
x ** y : 제곱
....
"""

i1 = 39
i2 = 939
big_int1 = 99999999999999999999999999999999999999999
big_int2 = 77777777777777777777777777777777777777777
f1 = 1.234
f2 = 3.784
f3 = .5 # 0.5
f4 = 10. # 10.0

print(i1 * i2)
print(big_int1 * big_int2)
print(f1 ** f2) # f1에 f2 제곱
print(f3 + i2) # 0.5 + 939 = 939.5 -> 실수 자료형으로 자동 형변환

result = f3 + i2
print(result, type(result)) # 939.5 <class 'float'>

a = 5.
b = 4
c = 10

print(type(a), type(b)) 
result2 = a + b
print(result2) # 9.0

# 형변환
# int, float, complex(복소수), bool

print(int(result2)) # float -> int
print(float(c)) # int -> float, 10.0
print(complex(3)) # 정수 -> 복소수, (3+0j)
print(int(True)) # 1 Bool -> 정수
print(int(False)) # 0 Bool -> 정수
print(bool(0), bool(3), bool(-1)) # 정수 -> Bool, False True True
# 0이면 False, 0이 아니면 True
print(int('3')) # 문자 -> 정수
print(complex(False)) # Bool -> 복소수, 0j

# 단항 연산자
y = 100;
y += 100
print(y)
y *= 100
print(y)

# 수치 연산 함수
# https://docs.python.org/3/library/math.html # 수학 관련 함수

print(abs(-7)) # 절대값 구하기, 7
n, m = 10, 20 # 동시에 변수 2개 선언 및 할당 가능
n, m = divmod(100, 8) # 100을 8로 나눠서 몫을 n에, 나머지를 m에
print(n, m)

import math

print(math.ceil(5.1)) # x 이상의 수 중에서 가장 작은 정수 (올림)
print(math.floor(3.874)) # x 이하의 수 중에서 가장 큰 정수 (내림)