# 전역 변수
a = 1 # 함수 밖에서 정의된 전역 변수

def show():
    print(a) # 전역변수는 모든 곳에서 사용 가능
    b = 20 
    c = b + a  # 전역 변수 사용
    print(c)

def add():
    print(x)
    print(a) # 전역변수는 모든 곳에서 사용 가능

show()

x = 100  # 전역 변수는 함수 호출 전에는 정의되어 있어야 함
add()
print(a) # 전역변수는 모든 곳에서 사용 가능

