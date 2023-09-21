# 3명의 회원을 입력받아서 리스트에 추가하고 리스트 내용 출력
members = []

for i in range(3):
    members.append(input("회원 입력 : "))

print("회원 명단 : ", end=" ")
for member in members:
    print(member, end=" ")
