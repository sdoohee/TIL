names = ["홍길동", "이몽룡", "성춘향", "변학도"]
result = False

input_name = input("이름 입력 : ")

for name in names:
    if name == input_name:
        result = True
        break

if result:
    print("명단에 있습니다")
else:
    print("명단에 없습니다")