# strip() / lstrip() / rstrip()
s1 = " hello "
print(s1)
print(s1.strip())
print(s1.lstrip())
print(s1.rstrip())

id = "sun"
input_id = " sun"
if id == input_id.strip():
    print("로그인 성공")
else:
    print("로그인 실패")