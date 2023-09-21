question = input("문장을 입력하세요 : ")

alpha = 0
number = 0
space = 0
etc = 0

for i in question:
    if i.isalpha():
        alpha += 1
    elif i.isdigit():
        number += 1
    elif i.isspace():
        space += 1
    else:
        etc += 1


print("알파벳 {}개: ".format(alpha))
print("숫자 {}개: ".format(number))
print("스페이스 : {}개".format(space))
print("기타 : {}개".format(etc))