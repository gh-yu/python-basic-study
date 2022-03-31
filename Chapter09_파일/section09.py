# Section09
# 파일 읽기, 쓰기
# 읽기 모드 : r, 쓰기 모드(기존 파일 삭제) : w, 추가 모드(파일 생성 또는 추가) : a (append)
# 쓰기 모드는 기존 파일에 덮어 씀 / 추가 모드는 기존에 파일 있으면 뒷부분에 내용 추가하고 없으면 생성
# 상대 경로('../', './'), 절대 경로 확인('C:\...')
# 기타 : https://docs.python.org/3.7/library/functions.html#open


# 파일 읽기
# read(), for문, readline(), readlines()

# 예제1
f = open('./resource/review.txt', 'r')
content = f.read()
print(content)
print(dir(f))
# 반드시 close로 리소스 반환 (외부 connection작업, close안하면 예외 발생)
f.close()
 
print("--------------------------")

# 예제2
# read() : 전체 내용 읽기, read(10) : 10글자 읽기
# with문을 사용하면 close를 해주지 않아도 됨 (파이썬에서 알아서 해줌)
with open('./resource/review.txt', 'r') as f:
    c = f.read()
    print(c)
    print(list(c))
    print(iter(c))


print("--------------------------")

# 예제3
with open('./resource/review.txt', 'r') as f:
    for c in f:
        # print(c) # 줄바꿈 문자로 인해 한 줄 씩 띄워서 출력됨
        print(c.strip()) # strip() : 양쪽 공백 제거
        
print("--------------------------")

# 예제4
with open('./resource/review.txt', 'r') as f:
    content = f.read()
    print(">", content)
    content = f.read() # 내용 없음
    print(">", content) # content 출력 안됨. 한 번 읽고 커서가 끝으로 가서 더 읽을 내용이 없어서 빈 내용 출력됨

print("--------------------------")

# 예제5
# readline() : 한 줄씩 읽기 - while 사용, readline(문자수) : 문자수 읽기
with open('./resource/review.txt', 'r') as f:
    line = f.readline()
    # print(line)
    while line: # 값이 없으면 0(False), 있으면 True
        print(line, end=' #### ')
        line = f.readline()

print("\n--------------------------")

# 예제6
# readlines() : 전체 읽은 후 라인 단위 리스트 저장 (한 줄씩 리스트 형태로 받기 )
with open('./resource/review.txt', 'r') as f:
    contents = f.readlines() # 파일의 내용을 한 줄, 한 줄 리스트 형태로 반환(줄바꿈이 구분자)
    print(contents) # ['The film, projected in the form of animation,\n', .... ]
    for c in contents:
        print(c, end=' ***** ')
        
print("\n--------------------------")

# 예제6
score = []
with open('./resource/score.txt', 'r') as f:
    score = []
    for line in f:
        score.append(int(line)) # txt파일에 저장되어 있는건 문자 형식
    print(score)

print('Average :  {:6.3}'.format(sum(score)/len(score)))


# 파일 쓰기 
# write()

# 예제1
with open('./resource/text1.txt', 'w') as f:
    f.write("Nice!\n")
    
# 예제2
with open('./resource/text1.txt', 'a') as f:
    f.write("Good!\n")
    
# 예제3
from random import randint
with open('./resource/text2.txt', 'w') as f:
    for cnt in range(6):
        f.write(str(randint(1, 50))) # randint(1, 50) : 1부터 50이하의 랜덤 정수
        f.write('\n')
        
# 예제4
# writelines : 리스트 -> 파일로 저장
with open('./resource/text3.txt', 'w') as f:
    list = ['Kim\n', 'Park\n', 'Cho\n']
    f.writelines(list)
    
# 예제5
# print함수로 파일에 내용 쓰기 (파일에 로그 기록할 때 가끔 쓰임)
with open('./resource/text4.txt', 'w') as f:
    print('test Contents1!', file=f) 
    print('test Contents2!', file=f)