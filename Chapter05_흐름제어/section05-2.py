# Section05-2
# 파이썬 흐름제어(반복문)
# 반복문 실습

# 코딩의 핵심 -> 조건 해결 중요

# 기본 반복문 : for, while

v1 = 1
while v1 < 11:
    print("v1 is :", v1) # 1~10
    v1 += 1

for v2 in range(10):
    print("v2 is :", v2) # 0~9

for v3 in range(1, 10):
    print("v3 is :", v3) # 1~9

# 1 ~ 100 합
sum1 = 0
cnt1 = 1
while cnt1 <= 100:
    sum1 += cnt1
    cnt1 +=1

print('1 ~ 100 합 : ', sum1)
print('1 ~ 100 합 : ', sum(range(1, 101)))
print('1 ~ 100 합: ', sum(range(1, 101, 2))) # 시작값, 끝값, 증감단위
print('0 ~ 9 합 : ', sum(range(10)))
print('0 ~ 19 : ', list(range(1, 20, 2))) # 1~19의 홀수 리스트 만들기

# 시퀀스(순서가 있는) 자료형 반복
# 문자열, 리스트, 튜플, 집합, 사전
# iterable 리턴 함수 : range, reversed, enumerate, filter, map, zip

names = ["Kim", "Park", "Cho", "Yoo"]

for name in names:
    print("You are : ", name)

word = "dreams"

for s in word:
    print("Word : ", s)

my_info = {
    "name": "Kim",
    "age": 23,
    "city": "Seoul"
}

# 기본 값은 키
for key in my_info:
    print("my_info", key)

# 값
for val in my_info.values():
    print("my_info", val)

print(val) # for문 돌고 나서도 val 변수 살아있음

# 키
for key in my_info.keys():
    print("my_info", key)

# 키 and 값
for k, v in my_info.items():
    print("my_info", k, v)

name ="KennRY"

for n in name:
    if n.isupper():
        print(n.lower())
    else:
        print(n.upper())


# break
numbers = [14, 2, 4, 5, 7, 9, 10, 37, 25, 24, 20]

for num in numbers:
    if  num == 33:
        print("found : ", num)
        break
    else:
        print("not found : 33")

# for - else 구문(반복문이 정상적으로 수행 된 경우 else 블럭 수행)
for num in numbers:
    if  num == 33:
        print("found : ", num)
        break # 반복문을 빠져 나감
    else:
        print("not found : 33")
else: # break가 실행된 경우에는 else 블럭 수행 안됨
    print("Not found 33........")


# continue

lt = ["1", 1, 5, True, 4.3, complex(4)]

for v in lt:
    if type(v) is float: # is, is not => ==, !=
        # print("float 찾았다!")
        continue # continue 실행시 아래 문장 실행 안되고, 반복문의 조건부로 바로 넘어감
    print("타입 : ", type(v))


nice_name = "Niceman"

print(reversed(nice_name))
print(list(reversed(nice_name)))
print(tuple(reversed(nice_name)))



# 추가 학습
i = 1
while i <= 10:
    print('i : ', i)
    if i == 6:
        break
    i += 1
else:
    print('else block run!')

for i in range(1, 11):
    for j in range(1, 11):
        print('{:4d}'.format(i * j), end='')
        # print('%4d' % (i * j), end='')
    print()