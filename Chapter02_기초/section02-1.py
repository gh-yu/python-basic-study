# Section02-1
# 파이썬 기초 코딩
# Print 구문의 이해

# 참조 : https://www.python-course.eu/python3_formatted_output.php

# 기본 출력
# 문자열 표현 방식 : 파이썬에서 문자열을 만드는 방법은 총 4가지
print('hello Python!') # 작은 따옴표
print("hello Python!") # 큰 따옴표
print("""hello Python!""") # 큰 따옴표 세개
print('''hello Python!''') # 작은 따옴표 세개
print("""you, 
you,
you
""") # '''나 """를 이용하여 여러 줄의 문자열 출력 가능

print() # 줄바꿈 출력

# Separator 옵션 사용 : sep로 값 사이에 문자 넣기
# print(값1, 값2, sep='문자 또는 문자열') : '' 안에 있는 값으로 붙여줌
print('T', 'E', 'S', 'T') # T E S T
print('T', 'E', 'S', 'T', sep='') # TEST
print('2019', '02', '19', sep='-') # 2019-02-19 
print('niceman', 'google.com', sep='@') # niceman@google.com

# end 옵션 사용 : print는 기본적으로 줄바꿈 출력, end='' 지정하면 줄바꿈X
print('Welcome To', end=' ')
print('the black parade', end=' ')
print('piano notes')
# Welcome To the black parade piano notes

print()

# format 사용 [], {}, ()
# {} 안에 들어갈 문자를 format함수의 인수로 전달. 순서(인덱스값), 변수를 지정하여 문자 매칭 가능
print('{} and {}'.format('You', 'Me')) # You and Me
print("{0} and {1} and {0}".format('You', 'Me')) # You and Me and You
print("{a} are {b}".format(a='You', b='Me')) # You are Me

# %s : 문자, %d : 정수, %f : 실수
print("%s's favorite number is %d" % ('geoni', 7)) # geoni's favorite number is 7
# format함수 대신 % 사용

print("Test1: %5d, Price: %4.2f" % (776, 6534.123)) # Test1:   776, Price: 6534.12
# %5d : 정수 다섯자리 정렬
# %4.2f : 정수 네자리 정렬, 소수점 지정 자리 두자리까지 표시 
print("Test1: {0: 5d}, Price:{1: 4.2f}".format(776, 6534.123)) # Test1:   776, Price: 6534.12
print("Test1: {a: 5d}, Price:{b: 4.2f}".format(a=776, b=6534.123)) # Test1:   776, Price: 6534.12
# 딕셔너리 활용하여 포맷팅

"""
참고 : Escape 코드

\n : 개행
\t : 탭
\\ : 문자
\' : 문자
\" : 문자
\r : 캐리지 리턴
\f : 폼 피드
\a : 벨 소리
\b : 백 스페이스
\000 : 널 문자
...

"""

print("'you'") # 'you'
print('\'you\'') # 'you'
print('"you"') # "you"
print("""'you'""") # 'you'
print('\\you\\\n\n\n\n') # \you\
print('\t\t\ttest') #                         test

# file 옵션 사용
import sys

f = open('console.log', 'a')  # 로그를 저장할 파일 open 
sys.stdout = f
print('GeeksForGeeks', file=sys.stdout)

sys.stdout = sys.__stdout__   # 원래의 stdout으로 복구
f.close() # 로그 파일 닫기