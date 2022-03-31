# Section08
# 파이썬 모듈과 패키지

# 패키지 에제
# 상대 경로
# .. : 부모 디렉토리
# . : 현재 디렉토리

# 사용1(클래스)
# from 패키지명.파일명 import 클래스명
from pkg.fibonacci import Fibonacci

Fibonacci.fib(300)

print("ex1 : ", Fibonacci.fib2(400))
print("ex1 : ", Fibonacci().title)

# 사용2(클래스)

from pkg.fibonacci import * # 다 가져오는거 권장하지 않음

Fibonacci.fib(500)

print("ex2 : ", Fibonacci.fib2(400))
print("ex2 : ", Fibonacci().title)

# 사용3(클래스) 
# as : Alias -> 권장하는 방식
from pkg.fibonacci import Fibonacci as fb 


fb.fib(1000)

print("ex2 : ", fb.fib2(400))
print("ex2 : ", fb().title)

# 사용4(함수)
# calculations 파일에 있는 모든 함수 가져옴
import pkg.calculations as c

print("ex4 : ", c.add(10, 100))
print("ex4 : ", c.mul(10, 100))

# 사용5(함수)
# 모든 함수 아닌 내가 필요한 함수만 가져옴 -> 권장
# 필요한 것만 리소스에 올림, 리소스 낭비 X
from pkg.calculations import div as d

print("ex5 : ", int(d(10, 100)))

# 사용6
import pkg.prints as p
import builtins # builtins모듈은 기본으로 import하기 때문에 import문 작성 필요 X
p.print1()
p.print2()
print(dir(builtins))


# 모듈 import 및 모듈 내 클래스 사용
import pkg.fibonacci as f

f.Fibonacci.fib(4)

