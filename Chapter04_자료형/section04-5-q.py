# Section04-5
# 파이썬 데이터 타입(자료형)
# 딕셔너리, 집합 자료형
# 데이터 타입 관련 퀴즈(정답은 영상)

# 1. 아래 문자열의 길이를 구해보세요.
from operator import indexOf


q1 = "dk2jd923i1jdk2jd93jfd92jd918943jfd8923"

print(len(q1))

# 2. print 함수를 사용해서 아래와 같이 출력해보세요.
#    apple;orange;banana;lemon
print("apple", "orange", "banana", "lemon", sep=';')
print("apple;orange;banana;lemon")

# 3. 화면에 * 기호 100개를 표시하세요.
print("*" * 100)

# 4. 문자열 "30" 을 각각 정수형, 실수형, 복소수형, 문자형으로 변환해보세요.
str1 = "30"
strToInt = int(str1)
strToFloat = float(str1)
strToComplex = complex(str1)
strToStr = str(str1)

print(type(str), type(strToInt), type(strToFloat), type(strToComplex), type(strToStr))

# 5. 다음 문자열 "Niceman" 에서 "man" 문자열만 추출해보세요.
q5 = "Niceman"
print(q5[4:])
mIdx = q5.index("m")
print(q5[mIdx:mIdx+3])

# 6. 다음 문자열을 거꾸로 출력해보세요. : "Strawberry"
q6 = "Strawberry"

print(list(reversed(q6))) # ['y', 'r', 'r', 'e', 'b', 'w', 'a', 'r', 't', 'S'] -> for문으로 출력 필요
print(q6[::-1]) # 뒤에서 부터 1개씩 skip하며 출력

# 7. 다음 문자열에서 '-'를 제거 후 출력하세요. : "010-7777-9999"
q7 = "010-7777-9999"
print(q7[0:3]+q7[4:8]+q7[9:13])
print(q7.replace('-', ''))

# 정규표현식
import re
print(re.sub('[^0-9]', '', q7)) # [^0-9] : 숫자가 아니다

# 8. 다음 문자열(URL)에서 "http://" 부분을 제거 후 출력하세요. : "http://daum.net"
q8 = "http://daum.net"
idx = q8.index('/d')
print(q8[idx+1:len(q8)])
print(q8[7:len(q8)])

# 9. 다음 문자열을 모두 대문자, 소문자로 각각 출력해보세요. : "NiceMan"
print("NiceMan".upper())
print("NiceMan".lower())

# 10. 다음 문자열을 슬라이싱을 이용해서 "cde"만 출력하세요. : "abcdefghijklmn"
print("abcdefghijklmn"[2:5])

# 11. 다음 리스트에서 "Apple" 항목만 삭제하세요. : ["Banana", "Apple", "Orange"]
q11 = ["Banana", "Apple", "Orange"]
q11.remove("Apple")
# del q11[1]
print(q11)

# 12. 다음 튜플을 리스트로 변환하세요. : (1,2,3,4)
q12 = (1,2,3,4)
print(list(q12))
print([s for s in q12]) # list로 변환됨
print({s for s in q12}) # dict으로 변환됨
print(([s for s in q12])) # set으로 변환됨

# 13. 다음 항목을 딕셔너리(dict)으로 선언해보세요. : <성인 - 100000 , 청소년 - 70000 , 아동 - 30000>
q13 = {"성인":100000, "청소년":70000, "아동":30000}
print(q13)

# q13_dict = {}
# q13_dict["성인"] = 100000

# 14. 13번 에서 선언한 dict 항목에 <소아 - 0> 항목을 추가해보세요.
q13["소아"] = 0

print(q13)

# 15. 13번에서 선언한 딕셔너리(dict)에서 Key 항목만 출력해보세요.
print(list(q13.keys()))

# 16. 13번에서 선언한 딕셔너리(dict)에서 value 항목만 출력해보세요.
print(tuple(q13.values()))

# *** 결과 값만 정확하게 출력되면 됩니다. ^^* 고생하셨습니다. ***
