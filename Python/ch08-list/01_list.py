# 리스트

# 빈 리스트 생성
list1 = list()
list2 = []

print(list1)
print(list2)

# 생성과 동시에 초기화
ints = [32, 56, 64, 72, 12]
floats = [1.1, 2.2, 3.3]
strings = ["홍길동", "이몽룡", "성춘향"]

# 리스트 안에 리스트 포함 가능
numbers = [100, 200, 300, [10, 20, 30]]

print(numbers)


# 리스트의 각 원소의 값을 변수에 저장
nums = [1, 2, 3]
a, b, c = nums
print(a)
print(b)
print(c)

# 리스트의 각 원소 출력
names = ["홍길동", "이몽룡", "성춘향"]

for name in names:
    print(name)

# 리스트의 각 원소 출력 : range() 함수 사용
# index 사용
for i in range(0, len(names)):
    print(names[i])


# 리스트 원소의 합 구하기
nums = [1, 2, 3]

total = 0
for n in nums:
    total += n

print(total)

# sum() 내장함수 사용해서 리스트의 원소의 합 구하기
nums = [1, 2, 3]
print(sum(nums))

# 주의 : 하위 리스트 포함할 경우 sum() 사용 불가
nums = [1, 2, 3, [10, 20]] 
# print(sum(nums)) # 오류
print(sum(nums[3])) # 30