# 리스트 안에 for문 포함
nums = [1, 2, 3, 4, 5]
x = [n for n in nums]
print(x)    # [1, 2, 3, 4, 5]

nums = [1, 2, 3, 4, 5]
x = [n*n for n in nums]
print(x)    # [1, 4, 9, 16, 25]

# if문 포함
nums = [1, 2, 3, 4, 5]
x = [n for n in nums if n % 2 == 0]
print(x)    # [2, 4]

# 주의 : if문이 for문 앞에 오면 오류
# x = [n if n % 2 == 0 for n in nums]

# if ~ else 포함
# 홀수이면 곱하기 100, 짝수이면 곱하기 10
nums = [1, 2, 3, 4, 5]
x = [n*10 if n % 2 == 0 else n*100 for n in nums]   # 짝수만 선택
print(x)    # [100, 20, 300, 40, 500]

# 주의 : if ~ else 가 for 뒤에 오면 오류
# x = [n*10 if n % 2 == 0 else n*100 for n in nums]