# 리스트 메소드

# len() / count()
a = [1, 2, 3, 3, 4]
print("원소의 개수 : ", len(a))
print("3의 개수 : ", a.count(3))

# append() : 리스트의 맨 뒤에 새로운 요소 추가
a = [1, 2, 3, 3, 4]
a.append(5)
print(a)

# 2개 이상인 경우 리스트로 추가 : 하위 리스트로 추가
a.append([6, 7]) 
print(a) # [1, 2, 3, 3, 4, 5, [6, 7]]

# a.append(8, 9) # 원소를 여러 개 추가하면 오류 
# takes exactly one argument

# 빈 리스트 생성하고 요소 나중에 추가
values = []
values.append(10)
values.append(20)
values.append(30)
print(values)

# for 문 사용하여 요소 추가
x = []
for i in range(5):
    x.append(i)

# 리스트 전체 요소 출력
for i in x:
    print(i)
