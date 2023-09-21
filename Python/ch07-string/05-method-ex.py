email = input("이메일 입력 : ")

if email.find('@') == -1 or \
    email.find('.') == -1 or \
    email.find('.') - email.find('@') <= 1 or \
    email.find('@') == 0 or \
    email.find('.') == (len(email) - 1) or \
    email.count("@") > 1 or \
    email.count(".") > 1 :
    print("이메일 형식이 아닙니다")


print("입력한 이메일 : ", email)

# @와 .의 위치가 바뀐 경우
# email.index("@") > email.index(".") 