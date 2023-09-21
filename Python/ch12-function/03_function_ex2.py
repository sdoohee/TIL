# def show_main(): # 앞에 적어도 됨
#     print('메인화면: "방문을 환영합니다"')

def login():
    id=input('id입력하시오')
    pw=input('비밀번호 입력하시오')
    if id=='abcd' and pw=='1234':
        print('로그인 성공')
        show_main()
    else:
        print('로그인 실패')

def show_main():
    print('메인화면: "방문을 환영합니다"')

login()