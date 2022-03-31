# Section07-2
# 파이썬 클래스 상세 이해
# 상속, 다중상속

# 예제1
# 상속 기본
# 슈퍼클래스(부모) 및 서브클래스(자식) -> 모든 속성, 메소드 사용 가능
# 상속 사용 이유 ❔ 
# 코드를 재사용, 중복되는 코드를 최소화 → 코드의 생산성, 가독성 ↑

# 라면 -> 속성 (종류, 회사, 맛, 면 종류, 이름) : 부모

class Car:
    """Parent Class""" # pep 8 원칙
    def __init__(self, tp, color):
        self.type = tp
        self.color = color
    
    def show(self):
        return 'Car Class "Show Method!"'

# 상속 -> class 클래스명(부모클래스명):
class BmwCar(Car): 
    """Sub Class"""
    def __init__(self, car_name, tp, color):
        super().__init__(tp, color) # 부모의 init메소드 호출
        self.car_name = car_name

    def show_model(self) -> None:
        return "Your Car Name : %s" % self.car_name

class BenzCar(Car): 
    """Sub Class"""
    def __init__(self, car_name, tp, color):
        super().__init__(tp, color) # 부모의 init메소드 호출
        self.car_name = car_name

    def show_model(self) -> None:
        return "Your Car Name : %s" % self.car_name

    def show(self):
        # print(super().show()) # super라는 키워드로 부모의 생성자, 속성에 접근 가능
        return super().show() + ' Car Info : %s %s %s' % (self.car_name, self.type, self.color)

# 일반 사용
model1 = BmwCar('520d', 'sedan', 'red')

print(model1.color) # Super
print(model1.type) # Super
print(model1.car_name) # Sub
print(model1.show()) # Super
print(model1.show_model()) # Super
print(model1.__dict__) # {'type': 'sedan', 'color': 'red', 'car_name': '520d'}
print(type(model1))

# Method Overriding(오버라이딩)
model2 = BenzCar('220d', 'suv', 'black')
print(model2.show()) # 부모에 있는 show()가 아닌 자식에 있는 show()메소드가 호출됨
# 내 목적에 맞게 부모의 메소드를 재구현(재작성하여 재활용)

# Parent Method Call
model3 = BenzCar('350d', 'sedan', 'silver')
print(model3.show())

# Inheritance Info(상속 정보)
print(BmwCar.mro()) 
print(BenzCar.mro()) 
# [<class '__main__.BmwCar'>, <class '__main__.Car'>, <class 'object'>]
# mro() : 상속 정보를 리스트 형태로 반환 (상속받은 클래스 리스트)
# 모든 클래스는 object클래스를 상속 받음 (object클래스는 모든 클래스의 부모 클래스)

# 예제2
# 다중 상속

# class X(object): # 모든 클래스는 object를 상속받음, 명시적 사용
    # pass # 통과해줘, 나중에 구현할 거야

class X():
    pass

class Y():
    pass

class Z():
    pass

class A(X, Y):
    pass

class B(Y, Z):
    pass

class M(B, A, Z):
    pass

print(M.mro())
# [<class '__main__.M'>, <class '__main__.B'>, <class '__main__.A'>, 
# <class '__main__.X'>, <class '__main__.Y'>, <class '__main__.Z'>, <class 'object'>]

# 복잡한 다중상속은 코드 해석 어려움(코드의 복잡도 ↑), 보통은 다중 상속할 때 2개 정도


