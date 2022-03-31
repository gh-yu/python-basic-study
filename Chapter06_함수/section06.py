# Section06
# 파이썬 함수식 및 람다(lambda)

# 함수 정의 방법
# def 함수명(parameter):
#   code

# 함수 호출
# 함수명(parameter)

# 함수 선언 위치 중요
# 함수 호출은 함수 선언문 위에 있으면 안됨(파이썬은 한 줄씩 해석하는 인터프리터 언어기 때문)

# 예제1
def print_hello(world):
    print("Hello,", world)

print_hello("Python!")
print_hello(77)

# 예제2
def hello_return(world):
    val = "Hello " + str(world)
    return val

str = hello_return("Python!!!")
print(str)

# 예제3 - 다중 리턴
def func_mul(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return y1, y2, y3

val1, val2, val3 = func_mul(100)
print(type(val1), val2, val3)
# 파이썬은 함수에서 여러 개의 값 반환할 수 있음


# 예제4 - 데이터 타입 반환 (리스트, 튜플, 딕셔너리..)
def func_mul(x):
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return [y1, y2, y3] # 리스트로 반환

lt = func_mul(100)
print(lt, type(lt)) # <class 'list'>

# *args, **kwargs 이해

# *args : 가변 인자
# 매개변수에 * 한 개를 붙이면 인수를 몇개를 넣어 호출하든 튜플 형태로 받아줌
def args_func(*args): # 매개변수명 자유롭게 변경 가능
    print(args) 
    print(type(args)) # <class 'tuple'>
    
    # for t in args: # 튜플 -> 이터레이터 가능
    #     print(t)

    # enumerate(iterable) -> index와 value 반환
    # enumerate()로 튜플에 인덱스 생성 (i는 인덱스, v는 값)
    for i,v in enumerate(args): 
        print(i, v)

args_func('kim') # ('kim',)
args_func('kim', 'Park')
args_func('kim', [1, 2])
args_func() # ()

# 인덱스가 없는 range도 enumerate로 인덱스 생성하여 값에 접근 가능 
for i,v in enumerate(range(10)):
    print(f"{i}:{v}", end=' ')

print()

# **kwargs : 키워드 가변 인자
# 매개변수에 ** 2개를 붙이면 딕셔너리로 받음
def kwargs_func(**kwargs):
    print(kwargs)
    for k, v in kwargs.items():
        print(k, v)

kwargs_func(name1="Kim") # {'name1': 'Kim'}
kwargs_func(name1="Kim", name2="Park", name="Lee")
kwargs_func() # {}

# *args, **kwargs가 함수의 매개변수면 인수 넘겨주지 않아도 에러 x

# 전체 혼합
# arg1, arg2는 필수적으로 받아야 함
# *args, **kwargs를 통해 여러 개의 인자를 받아 효율적으로 함수의 기능 구현할 수 있음
def example_mul(arg1, arg2, *args, **kwargs):
    print(arg1, arg2, args, kwargs)

example_mul(10, 20) # 10 20 () {}
example_mul(10, 20, 'park', 'kim', age1=24, age2=35) # 10 20 ('park', 'kim') {'age1': 24, 'age2': 35}

# 예제5
# 중첩함수(클로저)
# 변수 선언 줄일 수 있고, 메모리 관리를 효율적으로 할 수 있음
# 파이썬 데코레이터 - https://dojang.io/mod/page/view.php?id=2427

def nested_func(num):
    def func_in_func(num):
        print('>>>', num)
    print("in func")
    func_in_func(num + 10000) # 함수 안에서 함수 호출

nested_func(10000) 

# 예제6
# 매개변수 자료형 int, 반환형 list임을 명시 (다른 자료형을 넣어도 예외 발생 x, 명시적 사용)
def func_mul3(x : int) -> list:
    y1 = x * 100
    y2 = x * 200
    y3 = x * 300
    return [y1, y2, y3] 

print(func_mul3(5))

def tot_length2(word: str, num: int) -> None:
    print('hint exam2 : ', len(word) * num)

tot_length2("nice", 10)



# 람다식 예제
# 람다식 : 메모리 절약, 가독성 향상, 코드 간결
# 함수는 객체 생성 -> 리소스(메모리) 할당
# 람다는 즉시 실행(Heap 초기화) -> 메모리 초기화
# 람다식 남발하면 가독성이 떨어짐

# 일반적 함수 -> 변수 할당
def mul_10(num : int) -> int:
    return num * 10

var_func = mul_10 # 함수 객체 생성, 리소스에 할당됨
print(var_func) # 함수 사용하지 않았어도 메모리에 올라감 -> <function mul_10 at 0x0000021068777488> 
print(type(var_func)) # <class 'function'>

print(var_func(10))

# x -> 매개변수, x * 10 -> 리턴값
lambda_mul_10 = lambda x: x * 10
print(lambda num: num * 10) # <function <lambda> at 0x000002922A847620>
print('>>>', lambda_mul_10(10))

# 데이터 전처리 등, 대량의 데이터 처리 등에 람다 사용하면 좋음

# 매개변수로 함수를 받음
def func_final(x, y, func):
    print(x * y * func(10))

func_final(10, 10, lambda_mul_10)

# 함수 호출할때 lambda로 즉시 함수 만들어서 인자에 넘길 수 있음
# 함수를 매개변수로 넘길때 함수를 람다식으로 작성해서 넘기면 메모리 절약
func_final(10, 10, lambda x : x * 5000) 


 # 추가 학습
 
def ex(n, kwargs=3):
    print(n, kwargs)
    
ex(1)   