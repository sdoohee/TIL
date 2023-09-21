name = "홍길동"
age = 20

print(name, age)
print(name + "의 나이 : " + str(age))   # 문자열 연결 연산자 + 사용 시
# str() 형변환

# 숫자 입력 : input() 함수 사용
# input() 입력 결과 : 문자열
num = input("숫자 입력 : ")
print(num + str(5))  # 문자열과 숫자 연결 시 오류 발생 -> 형변환 필요 ; str()

# 결과가 10 + 5는 15가 출력되도록
num = float(input("숫자 입력 : "))
print(num + int(5))

resulat = eval(input("수식 입력 : "))
print(resulat)
