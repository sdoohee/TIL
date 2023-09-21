# if : hong이 이기는 모든 경우
# elif : 비기는 경우
# else 

hong = input('홍길동 입력 : ')
lee = input('이몽룡 입력 : ')

if  hong == "가위" and lee == "보" or \
    hong == "바위" and lee == "가위" or \
    hong == "보" and lee == "바위" :
    print("홍길동이 이겼습니다")
elif hong == lee:
    print("비겼습니다")
else:
    print("이몽룡이 이겼습니다")