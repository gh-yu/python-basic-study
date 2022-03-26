# Section04-2
# 파이썬 데이터 타입(자료형)
# 문자열, 문자열 연산, 슬라이싱
# 문자열 중요성(가장 많은 분야에서 사용)

str1 = "I am person."
str2 = "NiceMan"
str3 = ' '
str4 = str('Nice')
str5 = str()

print(len(str1), len(str2), len(str3), len(str4), len(str5)) # 12 7  4 (공백도 한 글자로 침)

escape_str1 = "Do you have a \"big collection\""
print(escape_str1)
escape_str2 = "Tab\tTab\tTab"
print(escape_str2)

# Raw String
raw_s1 = r'C:\Programs\Test\Bin'
print(raw_s1)
raw_s2 = r'C:\\a\\a'
print(raw_s2)

# 멀티라인
# 변수 선언 후 \ 기호가 나오면 다음 줄에 이어진다는 뜻
multi = \
""" 
문자열 

멀티라인 

테스트 """
print(multi)

multi_str2 = \
    '''
    문자열 멀티라인 
    역슬래시(\) \
    테스트
    '''
# 멀티라인(역슬래시) 출력
print(multi_str2)

# 문자열 연산
str_o1 = '*'
str_o2 = 'abc '
str_o3 = 'def'
str_o4 = "Nicaman"

print(str_o1 * 100) # str_o1 100번 반복
print(str_o2 + str_o3) # 문자열 합치기
print(str_o1 * 3)
# print(str_o1 + 3) # TypeError: must be str, not int 

# 문자열은 immutable(불변), 한 번 할당 후 수정 불가능한 순회 가능한 시퀀스
print('a' in str_o4) # 문자열 in 문자열 : 'a'라는 문자열이 str_o4에 포함되어 있는지 -> True반환
print('f' in str_o4) # False
print('z' not in str_o4) # True

# str 속성 및 기능 살펴보기
print(dir(str_o1))
# ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', 
# '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', 
# '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', 
# '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', 
# '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 
# 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 
# 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 
# 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 
# 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 
# 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']


# 문자열 형 변환
print(str(77) + 'a')
print(str(10.4))


# 문자열 함수
# 참고 : https://www.w3schools.com/python/python_ref_string.asp

# a = 'niceman'
# b = 'orange'
# c = '  '

# print(a.islower())
# print(a.endswith('e')) # 'e'로 끝나니?
# print(a.capitalize())
# print(a.replace('nice', 'good'))
# print(c.isspace()) # 공백 포함?

# print(list(reversed(b))) # reverse() : 문자열 거꾸로
# print(list(b))
# print(tuple(b))
# print(set(b))
# print(set(a))
'''
출력 결과
['e', 'g', 'n', 'a', 'r', 'o']
['o', 'r', 'a', 'n', 'g', 'e']
('o', 'r', 'a', 'n', 'g', 'e')
{'n', 'a', 'o', 'r', 'e', 'g'} 
{'n', 'e', 'c', 'm', 'a', 'i'
set은 순서 유지 x, 중복 제거됨
'''


# 문자열 슬라이싱(인덱싱)
# 문자열 한 번 할당되면 변환 불가한 이유
# -> 인덱싱 때문(인덱스마다 주소를 가지고 있음 -> 그래서 수정 불가)
# 일부분 추출(정말 중요)

a = 'niceman' # 인덱스 0~6 : 7개 
b = 'orange' 

print(a[0:3]) # 인덱스 0~2까지 (마지막 인덱스 전까지 출력)
print(a[0:4])
print(a[0:len(a)]) # 인덱스0~6(끝까지) len(a) = 7
print(a[0:len(a)-1]) 
print(a[:4]) # 인덱스 0~4까지
print(a[:]) # 전체
print(b[0:4:2]) # 인덱스 0~4까지, 2개 점핑(2개씩 건너뜀) -> oa 
print(b[1:-2]) # 인덱스 1~4까지, -2 : 역순(7-2) -> ran
print(b[::-1]) # 처음부터 끝까지 출력, skip단위는 역순으로 = reverse() -> egnaro


# 추가 학습
str_o11 = "Niceman"
str_o12 = "Orange"
str_o13 = "this is string example....wow!!! this is really string"
str_o14 = "Kim Lee Park Joo"

print("Capitalize: ", str_o11.capitalize()) # 단어 첫글자 대문자화
print("endswith?: ", str_o12.endswith("s")) # 문자열이 's'로 끝나니?
print("join str: ", str_o11.join(["I'm ", "!"])) # 두 문자열 중간에 str_o11
print("replace1: ", str_o11.replace('Nice', 'Good')) # 전체 replace
print("replace2: ", str_o13.replace("is", "was", 3)) # 3개만 replace
print("split: ", str_o14.split(' ')) 
print("split: ", type(str_o14.split(' '))) # list 반환 -> split:  <class 'list'>
print("sorted: ", sorted(str_o11)) # revers=False 기본값
print("sorted: ", sorted(str_o11, reverse=True)) # reverse=True값 주면 거꾸로
print("reversed1: ", reversed(str_o12)) 
print("reversed2: ", list(reversed(str_o12))) #list 형 변환
'''
출력 결과
Capitalize:  Niceman
endswith?:  False
join str:  I'm Niceman!
replace1:  Goodman
replace2:  thwas was string example....wow!!! thwas is really string
split:  ['Kim', 'Lee', 'Park', 'Joo']
sorted:  ['N', 'a', 'c', 'e', 'i', 'm', 'n']
reversed1:  <reversed object at 0x0000018D07DDE2B0>
reversed2:  ['e', 'g', 'n', 'a', 'r', 'O']
'''

# immutable 설명
im_str = "Good Boy!"

print(dir(im_str))  # __iter__ 확인
# 출력
for i in im_str:
    print(i)

str_sl = 'Niceboy'

# immutable 삭제
del str_sl

# 아스키코드
a = 't'

print(ord(a)) # 문자의 유니코드 값(숫자)
print(chr(116)) # 유니코드 값 -> 문자


for one in im_str:
    print(one)

for one in im_str: print(one)
