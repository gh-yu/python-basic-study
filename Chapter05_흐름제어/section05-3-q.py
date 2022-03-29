# Section05-3
# 파이썬 흐름제어(제어문)
# 제어문 관련 퀴즈(정답은 영상)

# 1 ~ 5 문제 if 구문 사용
# 1. 아래 딕셔너리에서 '가을'에 해당하는 과일을 출력하세요.
q1 =  {"봄": "딸기", "여름": "토마토", "가을": "사과"}

print(q1.get("가을"))

for k in q1.keys():
    if k == '가을':
        print(q1[k])

for k,v in q1.items():
    if k == '가을':
        print(v)

if '가을' in q1.keys():
    print(q1['가을'])


# 2. 아래 딕셔너리에서 '사과'가 포함되었는지 확인하세요.
q2 =  {"봄": "딸기", "여름": "토마토", "가을": "사과"}

# print("포함" if list(q2.values()).index("사과") else "사과 없음")
print("포함" if "사과" in list(q2.values()) else "사과 없음")

for v in q2.values():
    if v == "사과":
        print(v, "포함")

for k,v in q2.items():
    if v == "사과":
        print(k, v, "포함")
        break
else:
    print("사과 없음")    


# 3. 다음 점수 구간에 맞게 학점을 출력하세요.
# 81 ~ 100 : A학점
# 61 ~ 80 :  B학점
# 41 ~ 60 :  C학점
# 21 ~ 40 :  D학점
#  0 ~ 20 :  E학점

score = 77

# if score > 80 and score <= 100:  
#     print("A학점")
# elif score > 60 and score <= 80: elif하는 의미 없음 -> and 이후 필요 xxx
#     print("B학점")
# elif score > 40 and score <= 80:
#     print("B학점")
# elif score > 20 and score <= 40:
#     print("C학점")
# else:
#     print("E학점")        

if score >= 81:
    print("A학점")
elif score >= 61:
    print("B학점")
elif score >= 41:
    print("B학점")
elif score >= 21:
    print("C학점")
else:
    print("E학점")   

# 4. 다음 세 개의 숫자 중 가장 큰수를 출력하세요.(if문 사용) : 12, 6, 18
a, b, c = 55, 6, 18

print(max(a, b, c))    

nums = [12, 6, 18]
max = 0
for num in nums:
    if max < num:
        max = num

print(max)


for num in [a, b, c]:
    if max < num:
        max = num

print(max)

max = a
if b > max:
    best = b
if c > max:
    max = c

print(max)


# 5. 다음 주민등록 번호에서 7자리 숫자를 사용해서 남자, 여자를 판별하세요. (1,3 : 남자, 2,4 : 여자)
rrn = "960911-2162711"
# gender_num = int(rrn.split('-')[1][0])
gender_num = int(rrn[7])

gender = ""
if gender_num in [2, 4]:
    gender = "여자"
elif gender_num in [1, 3]:
    gender = "남자"

print(gender)

gender = "여자" if gender_num in [2, 4] else "남자"

print(gender)

if int(rrn[7]) % 2 == 0:
    print("여자")
else:
    print("남자")



# 6 ~ 10 반복문 사용(while 또는 for)

# 6. 다음 리스트 중에서 '정' 글자를 제외하고 출력하세요.
q3 = ["갑", "을", "병", "정"]

# q3.remove("정")
# print(q3)
print(list(q for q in q3 if q != '정'))
print([q for q in q3 if q != '정'])

for q in q3:
    if q != '정':
        print(q, end=" ")

print()

i = 0
while i < len(q3):
    if q3[i] != '정':
        print(q3[i], end=" ")  
    i += 1

print()

# 7. 1부터 100까지 자연수 중 '홀수'만 한 라인으로 출력 하세요.
for n in range(1, 101):
    if n % 2 != 0:
        print(n, end=' ')

print()

# 8. 아래 리스트 항목 중에서 5글자 이상의 단어만 출력하세요.
q4 = ["nice", "study", "python", "anaconda", "!"]

for q in q4:
    if len(q) >= 5:
        print(q)

print(list(q for q in q4 if len(q) >= 5))

# 9. 아래 리스트 항목 중에서 소문자만 출력하세요.
q5 = ["A", "b", "c", "D", "e", "F", "G", "h"]

for q in q5:
    if q.islower():
        print(q)

for q in q5:
    if q.isupper():
        continue
    else:
        print(q, end=' ')

print()
print([s for s in q5 if s.islower()])

# 10. 아래 리스트 항목 중에서 소문자는 대문자로 대문자는 소문자로 출력하세요.
q6 = ["A", "b", "c", "D", "e", "F", "G", "h"]

for q in q6:
    if q.islower():
        print(q.upper())
    elif q.isupper():
        print(q.lower())

print([s.upper() if s.islower() else s.lower() for s in q6])


# 리스트 컴프리헨션
numbers = []
for n in range(1, 101):
    numbers.append(n)
print(numbers)

# 리스트 컴프리헨션 사용시 직관적이고 더 빠름
numbers2 = [x for x in range(1, 101)]
print(numbers2)

numbers3 = {x for x in range(1, 101)}
print(numbers3) # {1, 2, .., 100}
print(type(numbers3)) # <class 'set'>

# numbers3 = tuple(x for x in range(1, 101))