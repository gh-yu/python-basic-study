# Section07-1
# 파이썬 클래스 상세 이해
# Self, 클래스, 인스턴스 변수

# 클래스, 인스턴스 차이 중요
# 클래스 - 객체
# 클래스를 변수에 할당 - 인스턴스화시켜 사용 (객체를 메모리에 올려서, 페이로드해서 사용) 
# 네임스페이스 : 객체를 인스턴스화 할 때 저장된 공간 
#               각각의 객체가 가지고 있는 독립적인 공간 / 클래스도 네임스페이스를 가지고 있음 (각 인스턴스가 공동으로 공유)
# 클래스 변수 : 직접 사용 가능, 객체보다 먼저 생성 
#              클래스 내에 선언된 변수 -> class MyClass: 클래스변수 = 값 
#              클래스.클래스변수 이렇게 접근
# 인스턴스 변수 : 객체마다 별도로 존재, 인스턴스 생성 후 사용 
#                각각의 인스턴스 마다 독립된 변수, 
#                생성자 클래스 __init__()내부에서 생성 -> self.인스턴스변수 = 값
# UserInfo("yu") -> 인스턴스 생성(인스턴스화)
# user1 = UserInfo("yu") -> 생성된 인스턴스를 user1에 할당 

# 선언
# class 클래스명:
#     함수
#     함수
#     함수

# class라는 예약어로 클래스 선언,
# 클래스와 관련 있는 함수를 한 클래스에 모음


# 예제1
# 클래스명 : 첫글자, 다음 문자 첫글자도 대문자로 표기 -> 파스칼 표기법
class UserInfo:
    # pass 
    # 속성, 메소드 : 
    # 속성은 상태(사람의 이름, 성별, 키..) 
    # 메소드는 기능(걷다, 뛰다.. 등의 움직임)
    
    # def __init__(self) -> None:
    #     pass

    # __init__ : 객체가 생성될 때 자동으로 호출되는 함수 -> 생성자
    def __init__(self, name): # 객체가 메모리에 할당될 때, 초기화하는 함수 (생성자)
        self.name = name
        # print("초기화 : ", name)
    def user_info_p(self):
        print("Name : ", self.name)


# user1 = UserInfo() # 클래스를 user1에 할당할때 __init__(self) 자동으로 호출
# TypeError: __init__() missing 1 required positional argument: 'name'

# 인스턴스화 : 할당(변수에 할당) -> 인스턴스명 = 클래스()
# 클래스를 생성, 클래스를 이용해 인스턴스화해서 사용, 인스턴스화된 변수들은 서로 독립적인 네임스페이스라는 창고에 name 등의 속성들을 저장
# 클래스는 붕어빵 찍어내는 틀, 클래스라는 틀로 여러 개의 객체를 만들 수 있음(user1, user2.. 사람 여러명)
# 네임스페이스 : 각각의 인스턴스가 가지고 있는 자기 자신의 저장 공간 -> 객체마다 다른 값 가지고 있음 (user1과 user2는 같지 않다)
print(UserInfo("yu")) # <__main__.UserInfo object at 0x0000019D56D9EE10>
print(UserInfo("yu").user_info_p()) # Name :  yu 
user1 = UserInfo("Kim") # 객체 생성시 클래스의 __init__함수에서 필요로 하는 매개변수 넘겨줘야 함
user1.user_info_p()
user2 = UserInfo("Park")
user2.user_info_p() # user1과 user1은 가지고 있는 속성값이 다르다. 다른 객체
print(user1.name)
print(user2.name)

# 객체마다 다른 id값을 가짐
print(id(user1)) # 2143854849608 
print(id(user2)) # 2143854891192  
# 네임스페이스 출력 : .__dict__
print(user1.__dict__) # {'name': 'Kim'} 
print(user2.__dict__) # {'name': 'Park'}


# 예제3
# self의 이해
class SelfTest:
    def function1(): # function1은 self인자가 없기 때문에 클래스 메소드 (클래스에서 직접 호출할 수 있음, 여러 인스턴스들이 공유하는 공통 함수)
        print('function1 called!')
    def function2(self): # self인자가 있으면 인스턴스 메소드 (인스턴스를 생성해서 호출 or 인자에 인스턴스를 넣어 호출)
        print('function2 called!')
        print(id(self))
        

self_test = SelfTest()
# self_test.function1() # TypeError: function1() takes 0 positional arguments but 1 was given -> function1은 self 인자가 없어서 누구의 function1인지 모르는 것
SelfTest.function1() # 클래스에서 호출해야 함 (인스턴스에서 접근하면 에러) 
self_test.function2()

print(id(self_test)) 
# SelfTest.function2() # TypeError: function2() missing 1 required positional argument: 'self'
SelfTest.function2(self_test) # 인스턴스 메소드 클래스에 직접 접근해서 호출하려면 인자에 인스턴스를 넣어 호출


# 예제3
# 클래스 변수, 인스턴스 변수

class WareHouse:
    # 클래스 변수 : self가 없는, 여러 인스턴스에서 공동으로 공유하는 함수
    stock_num = 0
    def __init__(self, name):
        self.name = name
        WareHouse.stock_num += 1 # 클래스 변수는 클래스에 직접 접근

    def __del__(self): # 인스턴스가 종료될 때 호출되는 함수
        WareHouse.stock_num -= 1

user1 = WareHouse('Kim')
user2 = WareHouse('Park')
user3 = WareHouse('Lee')

print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__) # {'name': 'Lee'} -> 클래스 변수가 아닌 자신의 인스턴스 변수만 가지고 있음
print(WareHouse.__dict__) # 클래스 네임스페이스, 클래스 변수(공유)
print(dir(WareHouse))
# 클래스 변수인 stock_num을 가지고 있음 -> 'stock_num': 3, 
# {'__module__': '__main__', 'stock_num': 3, '__init__': <function WareHouse.__init__ at 0x00000285A94072F0>, '__del__': <function WareHouse.__del__ at 0x00000285A9407378>, '__dict__': <attribute '__dict__' of 'WareHouse' objects>, '__weakref__': <attribute '__weakref__' of 'WareHouse' objects>, '__doc__': None}

print(user1.name)
print(user2.name)
print(user3.name)

# 인스턴스에서 클래스 변수에 접근 가능
print(user1.stock_num) # 자기 네임스페이스에 없으면 클래스 네임스페이스에서 변수를 찾음 
print(user2.stock_num)
print(user3.stock_num) # 3

del user1 # del로 인스턴스를 지울 수 있음(메모리에서 삭제)

print(WareHouse.stock_num) # 직접 접근 가능

print(user2.stock_num) # 2 (삭제하고 나서 -1됨)
print(user3.stock_num) 


