# Section04-3
# 파이썬 데이터 타입(자료형)
# 리스트, 튜플

name1= 'Lee'
name2= 'Park'

# 변수를 여러개 선언하는 건 코드 길어지고 비효율적
# -> 자료구조 활용
name = ['Lee', 'Park']
print(name)  # ['Lee', 'Park']

# 리스트(순서ㅇ, 중복ㅇ, 수정ㅇ, 삭제ㅇ)
# like 그릇, 배열, ex. 숫자의 모음, 학생의 모음.. 

# 선언
a = [] # [] 대괄호로 선언
b = list() # list() 명시적 선언
print(type(a), type(b))

# 선언과 동시에 데이터 담아서 바로 초기화
c = [1, 2, 3, 4] # int 정수의 모음
d = [10, 100, 'Pen', 'Banana', 'Orange'] # 요소마다 데이터 타입 달라도 됨
e = [10, 100, ['Pen', 'Bnana', 'Orange']] # 리스트 요소에 리스트 할당 가능


# 인덱싱
# 정방향 : 0, 1, 2, .. / 역방향 : -1, -2, -3, ..
print(d[3])
print(d[-2])
print(d[0]+d[1]) # 110
print(e[2][1])
print(e[-1][-2])

# 슬라이싱 : 인덱스의 범위 지정 (ex. a[1:2])
print(d[0:3]) # list로 반환됨 -> [10, 100, 'Pen']
print(d[0:1]) # [10]
print(type(d[0:1])) # <class 'list'>
print(type(d[0])) # <class 'int'>
print(e[2][1:3]) # ['Bnana', 'Orange']


# 연산
print(c + d) # 두 리스트를 합쳐서 하나의 리스트로 반환 -> [1, 2, 3, 4, 10, 100, 'Pen', 'Banana', 'Orange']
print(c * 3) # 리스트 길이 3배로 늘어남(3번 반복) ->  [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
print(str(c[0]) + 'hi')


# 리스트 수정, 삭제
c[0] = 77 # 0번째 인덱스 값 변경
print(c) # [77, 2, 3, 4]

c[1:2] = [100, 1000, 10000] # 슬라이싱 처리해서 이 구간에 있는 요소 변경
print(c) # [77, 100, 1000, 10000, 3, 4] 1~2구간 중간에 삽입됨
# 슬라이싱 처리했을때 하나의 리스트에 원소 들어감
c[1] = ['a', 'b', 'c']
print(c) #  [77, ['a', 'b', 'c'], 1000, 10000, 3, 4]
# 하나의 인덱스에 리스트 자체 넣으면 리스트 안에 리스트가 삽입됨(중첩 : nested)

# del 키워드로 삭제
del c[1]
print(c) # [77, 1000, 10000, 3, 4]
del c[-1]
print(c) # [77, 1000, 10000, 3]
print("\n\n")

# 리스트 함수
y = [5, 2, 3, 1, 4]
print(y)
y.append(6) # 리스트 끝에 요소 추가
print(y)
y.sort() # 오름차순 정렬
print(y)
y.reverse() # 반대로
print(y)
y.insert(2, 7) # 인덱스 2~3사이에 요소 추가, 원하는 인덱스 자리에 추가할 때 사용
print(y)
y.remove(2) # 2라는 데이터 찾아서 지움
print(y)
y.remove(7)
print(y) 
y.pop() # 마지막 요소를 꺼내서 없앰 (Stack(LIFO 구조) -> pop, push)
print(y)
ex = [88, 77]
y.extend(ex) # 끝 부분에 리스트 연장(기존 리스트의 원소로 들어감 -> 하나의 리스트로 합쳐짐)
print(y)
y.append(ex) # 리스트 끝에 리스트 자체를 요소로 추가 
print(y)
print(y.count(88)) # count(x) : 리스트에 포함된 요소 x의 개수 세기 (없으면 0 반환)

# 삭제 : del, remove, pop

# list 속성 및 기능 확인하기
i = 1
for iter in dir(a):
    print(iter, end=', ')
    if (i % 5 == 0):
        print()
    i += 1
'''
__add__, __class__, __contains__, __delattr__, __delitem__,
__dir__, __doc__, __eq__, __format__, __ge__,
__getattribute__, __getitem__, __gt__, __hash__, __iadd__,
__imul__, __init__, __init_subclass__, __iter__, __le__,
__len__, __lt__, __mul__, __ne__, __new__,
__reduce__, __reduce_ex__, __repr__, __reversed__, __rmul__,
__setattr__, __setitem__, __sizeof__, __str__, __subclasshook__,
append, clear, copy, count, extend,
index, insert, pop, remove, reverse, sort
'''
print('\n\n')


# 튜플 (순서ㅇ, 중복ㅇ, 수정x, 삭제x)

# 프로그램에 영향을 끼치는 중요한 key값, 계좌 번호와 같은 데이터 
# -> 변경되면 프로그램 실행이 오작동되는 경우, 튜플에 저장하는 것이 좋음

a = () # 소괄호로 선언
a2 = tuple()
b = (1, ) # type : tuple
b2 = (1) # type : int
c = (1, 2, 3, 4)
c2 = 1, 2, 3, 4 # 소괄호 없이 선언 가능
d = (10, 100, ('a', 'b', 'c'))
e = (1, 2, 3, 4), (5, 6, 7, 8) # 이차원 배열 선언

# del c(2) # TypeError: 'tuple' object doesn't support item deletion 튜플은 요소 삭제 불가
# SyntaxError: can't delete function call 

print(type(a2))
print(type(b))
print(type(b2))
print(c2)
print(type(c2))
print(c[2])
print(c[3])
print(d[2][1])
print(e[1][1])
print(d[2:]) # 인덱스 2부터 다 출력 -> (('a', 'b', 'c'),) 마지막 콤마는 규칙
print(d[2][0:2])

print(c + d) # 튜플과 튜플 합치기
print(c * 3) # 튜플 곱하기(배열 요소 반복)  
# 확장해서 새로 만들기 가능, 기존 튜플은 변경 불가

# 튜플 함수

z = (5, 2, 1, 3, 4, 1)
print(z)
print(3 in z) # 3이라는 데이터를 가진 요소 튜플z에 있는지 -> True
print(z.index(5)) # 5라는 데이터를 가진 요소의 인덱스 반환 -> 0 
# 없는 데이터 넣을시 ValueError: tuple.index(x): x not in tuple
print(z.count(1)) # 튜플z에 1이 몇개 -> 2
print(len(z))
