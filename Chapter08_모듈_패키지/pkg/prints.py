def print1():
    print("Hi")

def print2():
    print("Hello")

# 단위 실행 (독립적으로 파일 실행)
# 해당 모듈에서 테스트 할 때만 실행되는 테스트 코드
# 다른 파일에서 호출할 때는 실행 안 됨 (자기 자신 main이 아니기 때문)
if __name__ == "__main__":
    print1()
    print2()



