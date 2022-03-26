# Section04-4
# 파이썬 데이터 타입(자료형)
# 딕셔너리, 집합 자료형

# 딕셔너리(Dictionary) : 순서x, 중복x, 수정o, 삭제o

# Key, Value (Json) -> MongoDB
# key를 통해 값을 찾음, key는 중복x
# Key에는 숫자, 문자열 들어갈 수 있음
# 선언
a = {'name': 'kim', 'Phone': '010-7777-7777', 'birth': 871024}
b = {0: 'Hello Python', 1: 'Hello Coding'}
c = {'arr': [1, 2, 3, 4, 5]} # 모든 데이터값(리스트, 튜플..)을 value에 담을 수 있음

# 출력
print(type(a)) # <class 'dict'>
print(a['name']) # 이렇게 직접 접근하여 조회하면 해당하는 key값 없을시 KeyError나기 때문에 안전하지 않음
# print(a['name1']) # KeyError: 'name1' (존재X -> 에러 발생)
print(a.get('name')) # get함수로 키의 value 가져옴
print(a.get('address')) # 해당하는 key값 없다면 None 반환 (존재X -> None 처리)
print(c['arr'][1:3])

# 딕셔너리 추가
a['address'] = 'Seoul'
print(a)
a['rank'] = [1, 3, 4]
a['rank2'] = (1, 2) 
print(a)

a['rank2'] = (1, 2, 3) # 재할당
print(a)

# keys, values, items 
# dict_keys, dict_values, dict_items : 반복문(iterate) 사용 가능
print(a.keys()) # Key만 리스트 형태로 가져옴 -> dict_keys(['name', 'Phone', 'birth', 'address', 'rank', 'rank2'])
print(list(a.keys())) # 사용하려면 리스트로 형변환 필요 -> ['name', 'Phone', 'birth', 'address', 'rank', 'rank2']

temp = list(a.keys())
print(temp[1:3])

print(a.values()) # dict_values(['kim', '010-7777-7777', 871024, 'Seoul', [1, 3, 4], (1, 2, 3)])
print(list(a.values())) 

print(a.items()) # dict_items([('name', 'kim'), ('Phone', '010-7777-7777'), ('birth', 871024), ('address', 'Seoul'), ('rank', [1, 3, 4]), ('rank2', (1, 2, 3))])
print(list(a.items()))
for item in a.items():
    print('key={0}, value={1}'.format(item[0], item[1]))

for key in a.keys():
    print('key={0}, value={1}'.format(key, a.get(key)))

print(2 in b) # False
print('name2' not in a) # True



# 집합(Sets) (순서x, 중복x)
a = set()
b = set([1, 2, 3, 4])
c = set([1, 4, 5, 6, 6])
d = set("abcdefg") # 문자열을 집합으로 만들 수 있음

print(type(a))
print(c) # 중복 허용x : 중복 자동으로 지워짐 -> {1, 4, 5, 6} 
print(d) # {'b', 'c', 'f', 'g', 'd', 'e', 'a'}

# set은 주로 형변환해서 사용
t = tuple(b)
print(t)
l = list(b)
print(l)

s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])

# 교집합 : 두 집합 중 중복된 요소만 출력됨 -> {4, 5, 6}
print(s1.intersection(s2)) 
print(s1 & s2)

# 합집합 : 두 집합을 합하고 중복된 요소 제거됨 -> {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(s1 | s2)
print(s1.union(s2))

# 차집합 -> s1에서 s2를 뺌 {1, 2, 3}
print(s1 - s2)
print(s1.difference(s2))


# 추가 & 제거
s3 = set([7, 8, 10, 15])

s3.add(18)
s3.add(7) # 7은 이미 있어서 중복 저장 안됨

print(s3)

s3.remove(7) # 7 데이터 가진 요소 지우기, 없는 데이터는 에러
print(s3)

s3.clear() # 전체 요소 지우기
print(type(s3)) # <class 'set'>