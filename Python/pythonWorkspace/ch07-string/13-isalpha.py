# isalpha() / isdihit() / isspace()
#  문자/숫자/공백 여부 확인 메소드

phone = input("전화번호 입력 (숫자만) : ")

if phone.isdigit():
    pass
else:
    print("숫자만 입력하세요")

print("입력한 값 : ", phone)

