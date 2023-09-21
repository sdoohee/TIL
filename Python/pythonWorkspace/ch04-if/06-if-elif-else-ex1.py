
# num1 = int(input("정수 1 입력: "))
# num2 = int(input("정수 2 입력: "))
# num3 = int(input("정수 3 입력: "))


# if num1 >= num2 and num1 >= num3:
#     max_num = num1
# elif num2 >= num3:
#     max_num = num2
# else:
#     max_num = num3

# print("가장 큰 수:", max_num)

num1 = int(input("정수1 입력 : "))
num2 = int(input("정수2 입력 : "))
num3 = int(input("정수3 입력 : "))

max = num1

if num2 > max:
    max = num2
elif num3 > max:
    max = num3
else:
    pass

print("제일 큰 수 :",max)
