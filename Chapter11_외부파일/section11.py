# Section11
# 파이썬 외부 파일 처리
# 파이썬 Excel, CSV 파일 읽기 및 쓰기

# CSV : MIME - text/csv
# 대부분 콤마(,)로 구분, 탭(|)으로 구분되어 있는 파일도 있음

import csv

# 예제1
with open('./resource/sample1.csv', 'r') as f:
    reader = csv.reader(f)
    # next(reader) # Header 스킵 (한 줄 건너뜀)
    # 확인
    print(reader) # <_csv.reader object at 0x0000025E62C6B2B8>
    print(type(reader)) # <class '_csv.reader'>
    print(dir(reader)) # __iter__ 가지고 있음
    
    # iterator기 때문에 for문 돌릴 수 있음
    for c in reader:
        print(c)
        
    ''' 
    출력 결과 - 하나의 줄이 리스트로 나옴
    ['번호', '이름', '가입일시', '나이'] # 첫 번째가 열이름 -> next(reader)로 Header 스킵
    ['1', '김정수', '2017-01-19 11:30:00', '25']
    ...
    '''
    
# 예제2
with open('./resource/sample2.csv', 'r') as f:
    reader = csv.reader(f, delimiter='|') # delimiter 기본 값 ','
    # next(reader) # Header 스킵 (한 줄 건너뜀)
    # 확인
    print(reader) 
    print(type(reader)) 
    print(dir(reader)) 
    
    for c in reader:
        print(c)
        
# 예제3
with open('./resource/sample1.csv', 'r') as f:
    reader = csv.DictReader(f)
    
    # for c in reader:
    #     print(c)
    
    '''
    출력 결과
    OrderedDict([('번호', '1'), ('이름', '김정수'), ('가입일시', '2017-01-19 11:30:00'), ('나이', '25')])
    OrderedDict([('번호', '2'), ('이름', '박민구'), ('가입일시', '2017-02-07 10:22:00'), ('나이', '35')])
    '''
    
    for c in reader:
        for k, v in c.items():
            print(k, v)
        print('-------------')
        

# 예제4
w = [[1,2,3], [4,5,6], [7,8,9], [10,11,12], [13,14,15], [16,17,18]]

# open할 때 자동으로 newline 넣어주는 옵션이 있기 때문에 writerow하면 두번 줄바꿈됨 
# newline='' -> 새줄문자(줄바꿈 문자) 처리x
with open('./resource/sample3.csv', 'w', newline='') as f:
    wt = csv.writer(f)
    
    for v in w:
        wt.writerow(v)  # 리스트 각 요소를 파일에 씀

# 예제5
with open('./resource/sample4.csv', 'w', newline='') as f:
    wt = csv.writer(f)
    wt.writerows(w) # 리스트 한 번에 파일에 씀


# XSL, XLSX : MIME - applications/vnd.excel, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
# openpyxl, xlswriter, xlrd, xlwt, xlutils
# pandas를 주로 사용(pandas 내부에서 openpyxl, xlrd 사용)
# pandas 공식 문서 : https://pandas.pydata.org/docs/reference/api/pandas.read_excel.html
# pip install xlrd
# pip install openpyxl
# pip install pandas

import pandas as pd

# sheetname='시트명' 또는 숫자, header=숫자, skiprow=숫자
xlsx = pd.read_excel('./resource/sample.xlsx', engine='openpyxl')

# 상위 데이터 확인
print(xlsx.head()) # head(상단)부터 5개 행 리턴
print()

# 데이터 확인
print(xlsx.tail()) # tail(하단)부터 5개 행 리턴

print(xlsx.shape) # 행, 열 개수 반환 -> (20, 7)


# 엑셀 or CSV 다시 쓰기
# index=False -> 기본 값은 True (인덱스 컬럼 생성됨 -> 첫줄 제외 행마다 0, 1, 2, .. 번호 붙여줌)
xlsx.to_excel('./resource/result.xlsx', index=False)
xlsx.to_csv('./resource/result.csv', index=False)
xlsx.to_excel('./resource/result2.xlsx')
