# Section12-1
# 파이썬 데이터베이스 연동(SQLite)
# 테이블 생성 및 삽입

# sqlite3 기본적으로 가지고 있음
import sqlite3
import datetime
# from datetime import datetime

# 삽입 날짜 생성
now = datetime.datetime.now() 
print('now : ', now) # 2022-03-31 12:17:35.999750

nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')
print("nowDatetime : ", nowDatetime)
# print(datetime.datetime.strftime(now, '%Y-%m-%d %H:%M:%S'))


# sqlite3
print('sqlite3.version', sqlite3.version) # 2.6.0
print('sqlite3.sqlite_version', sqlite3.sqlite_version) # 3.21.0
# 최신으로 설치하고 싶으면 pip install로

# DB 생성 & Auto Commit
# Commit : DB 반영, Rollback : 수정사항 되돌림
conn = sqlite3.connect('D:/study/lecture/python_web_dev_all_in_one/python_basic/resource/database.db', isolation_level=None)

# conn.commit() # isolation_level=None으로 auto commit 설정했기 때문에 commit()할 필요 없음

# DB생성(메모리)
# conn = sqlite3.connect(":memory:")

# Cursor 연결
c = conn.cursor()
print('Cursor Type : ', type(c)) # <class 'sqlite3.Cursor'>

# 테이블 생성(Data Type : TEXT, NUMERIC, INTEGER, REAL, BLOB)
c.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username text, email text, \
          phone text, website text, regdate text)")

# 데이터 삽입
# insert문 안에 플레이스 홀더(?)의 역할 -> 두 번째 인자에 튜플을 넘기면 순서대로 값이 매칭됨
c.execute("INSERT INTO users VALUES(1, 'Yu', 'Yu@gmail.com', \
          '010-1221-3213', 'Yu.com', ?)", (nowDatetime, ))
c.execute("INSERT INTO users(id, username, email, phone, website, regdate) VALUES (?,?,?,?,?,?)",
          (2, 'Park', 'Park@daum.net', '010-1111-1111', 'Park.com', nowDatetime))

# 위 코드 2번 실행하면 -> IntegrityError: UNIQUE constraint failed: users.id

# Many 삽입(튜플, 리스트)
# dataset을 만들어서 한번에 insert할 수 있음 : executemany()
# 파일을 읽어 오거나, web에서 json형식 딕셔너리로 다뤄서 튜플, 리스트로 변환해서 한 번에 insert하는게 빠름
userList = (
    (3, 'Lee', 'Lee@naver.com', '010-2222-2222', 'Lee.com', nowDatetime),
    (4, 'Cho', 'Cho@naver.com', '010-2222-2222', 'Cho.com', nowDatetime),
    (5, 'Yoo', 'Yoo@naver.com', '010-2222-2222', 'Yoo.com', nowDatetime)   
)

c.executemany("INSERT INTO users(id, username, email, phone, website, regdate) \
    VALUES (?,?,?,?,?,?)", userList)
# 리스트의 개수와 짝이 맞기 때문에 내부적으로 반복문을 통해서 insert해줌

# 테이블 데이터 삭제
# print("users db deleted : ", conn.execute("delete from users").rowcount, "rows")

# 롤백
# conn.rollback()

# 접속 해제
conn.close()