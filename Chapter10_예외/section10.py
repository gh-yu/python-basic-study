# Section10
# 파이썬 예외처리의 이해

# 예외 종류
# 문법적으로는 에러가 없지만, 코드 실행(런타임) 프로세스에서 발생하는 에외 처리도 중요
# linter : 코드 스타일, 문법 체크

# SyntaxError : 잘못된 문법

# print('Test) # SyntaxError: EOL while scanning string literal
# if True   # SyntaxError: invalid syntax
#     pass
# x => y 

# NameError : 참조변수 없음

a = 10
b = 15

# print(c) # 예외 발생 NameError: name 'c' is not defined

# ZeroDivisionError : 0 나누기 에러
# print(10 / 0) # ZeroDivisionError: division by zero

# IndexError : 인덱스 범위 오버

x = [10, 20, 30]

print(x[0])
# print(x[3]) # IndexError: list index out of range

# KeyError

dic = {'name': 'Kim', 'Age': 33, 'city': 'seoul'}

# print(dic['hobby']) # KeyError: 'hobby'
print(dic.get('hobby')) # 딕셔너리 키 접근시 get() 사용하기 -> 없을시 None 반환

# AttributeError : 모듈, 클래스에 있는 잘못된 속성 사용시에 에러
# 없는 메소드, 속성에 접근시 에러

from multiprocessing.sharedctypes import Value
import time

print(time.time()) 
# print(time.month()) # AttributeError: module 'time' has no attribute 'month'

# ValueError : 참조 값이 없을 때 발생
x = [1, 5, 9]

# x.remove(10) # ValueError: list.remove(x): x not in list
# x.index(10) # ValueError: 10 is not in list

# FileNotFoundError 

# f = open('test.txt', 'r') # FileNotFoundError: [Errno 2] No such file or directory: 'test.txt'

# TypeError

x = [1,2]
y = (1,2)
z ='test'

# print(x + y) # FileNotFoundError: [Errno 2] No such file or directory: 'test.txt'
# print(x + z) # TypeError: can only concatenate list (not "str") to list

print(x + list(y)) # 형변환 필요

# 항상 예외가 발생하지 않을 것으로 가정하고 먼저 코딩
# 그 후 런타임 예외 발생시 에외 처리 코딩 권장(EAFP 코딩 스타일)

# 예외 처리 기본
# try : 에러가 발생할 가능성이 있는 코드 실행
# except : 에러명1  (에러 처리 - 여러 개 가능)
# except : 에러명2
# else : 에러가 발생하지 않았을 경우 실행
# finally : 항상 실행

# 예제1
name = ['Kim', 'Lee', 'Park']

try:
    z = 'Kim' # z = 'Cho' 예외 발생
    x = name.index(z)
    print('{} Found it! in name[{}]'.format(z, x))
except ValueError:
    print('Not found it! - Occurred ValueError!')
else:
    print("Ok! else!")

# 예제2
name = ['Kim', 'Lee', 'Park']

try:
    z = 'Jin'
    x = name.index(z)
    print('{} Found it! in name[{}]'.format(z, x))
except: # 어떤 에러가 올지 모를때 except: 로 처리해도 됨
    print('Not found it! - Occurred Error!')
else:
    print("Ok! else!")


# 예제3
name = ['Kim', 'Lee', 'Park']

try:
    z = 'Kim'
    x = name.index(z)
    print('{} Found it! in name[{}]'.format(z, x))
except: # 어떤 에러가 올지 모를때 except: 로 처리해도 됨
    print('Not found it! - Occurred Error!')
else:
    print("Ok! else!")
finally: # 예외 발생 여부에 상관없이 항상 수행
    print('finally ok!') 


# 예제4
# 예외 처리는 하지 않지만, 무조건 수행되는 코딩 패턴

try:
    print('try')
finally:
    print('Ok Finally!!!')


# 예제5
name = ['Kim', 'Lee', 'Park']

try:
    z = 'Kims'
    x = name.index(z)
    print('{} Found it! in name[{}]'.format(z, x))
except ValueError as e: # 여러 예외를 계층적으로 잡을 수 있음 (순서 중요)
    print(e)
except IndexError: 
    print('Not found it! - Occurred Error!')    
except Exception: # 어떤 에러가 올지 모를때 Exception 명시적으로 적어줌
    print('Not found it! - Occurred Error!')    
else:
    print("Ok! else!")
finally: # 예외 발생 여부에 상관없이 항상 수행
    print('finally ok!') 
    
# 예제6
# 에외 발생 : raise
# raise 키워드로 예외 직접 발생

try:
    a = 'Kimd'
    if a == 'Kim':
        print('ok 허가!')
    else:
        raise ValueError
except ValueError as e:
    print('문제 발생')
except Exception as e:
    print(e)
else:
    print('ok')