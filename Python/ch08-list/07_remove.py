# 리스트 삭제

#  remove(값) : 리스트에서 값에 해당되는 요소 제거
n = [1, 2, 3, 3, 4, 5, 4, 3]
n.remove(4) # 첫 번째 4만 제거
print(n) # [1, 2, 3, 3, 5, 4, 3]

# 동일한 원소를 한번에 제거
# 몇 개 있는지 확인하고, 그 수만큼 반복
# 모든 3 제거
n = [1, 2, 3, 3, 4, 5, 4, 3]

cnt = n.count(3)
for i in range(cnt):
    n.remove(3)
    print("3 삭제 : ", n)

print(n)

# pop() : 리스트의 마지막 요소 반환하고 삭제
x = ['a', 'b', 'c', 'd']
y = x.pop() 
print(y) # d
print(x) # ['a', 'b', 'c']

# 계속 pop()해서 더 이상 요소가 없으면 빈 리스트 출력
x.pop()
x.pop()
x.pop()
print(x) # []

# 리스트가 비어있는데 pop() 하면 오류
x.pop() # pop from empty list


# pop(index) : 인덱스 위치에 있는 요소 반환하고 삭제
heroes = ['슈퍼맨', '스파이더맨', '헐크',' 아이언맨', '배트맨']
# 헐크 삭제
heroes.pop(2)
print(heroes)

# clear() : 리스트 비우기 (모든 요소 삭제)
n = [1, 2, 3, 3, 4, 5, 4, 3]
n.clear()
print(n) # []

# del 리스트[인덱스]
n = [1, 2, 3, 4, 5, 6, 7, 8]
del n[2] # 3삭제
print(n)

n = [1, 2, 3, 4, 5, 6, 7, 8]
del n[2:5] # 3, 4, 5 삭제 (start에서 end-1까지)
print(n)

# 3, 4, 5, 6, 7, 8 삭제
n = [1, 2, 3, 4, 5, 6, 7, 8]
del n[2:]
print(n)


# 3, 4, 5, 6 범위에서 3, 5 삭제
n = [1, 2, 3, 4, 5, 6, 7, 8]
del n[2:6:2] # 인덱스2~5까지 범위. 간격 2 
print(n)

# n 완전 삭제
n = [1, 2, 3, 4, 5, 6, 7, 8]
del n
print(n) # name 'n' is not defined