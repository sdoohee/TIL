# 튜플 (tuple)

# 빈 튜플 생성
t1 = ()
print(t1)

t2 = tuple()
print(t2)

t3 = (1, 2, 3)
print(t3)

t4 = 4, 5, 6  # 괄호 없어도 튜플로 생성
print(t4)

t5 = [1, 2], [3, 4] # 리스트로 튜플 생성
print(t5) # ([1, 2], [3, 4])

t3 = (1, 2, 3)
t6 = t3, (7, 8, 9)  # 다른 튜플 포함 가능
print(t6) # ((1, 2, 3), (7, 8, 9))

t7 = tuple([5, 6, 7, 8]) # tuple() 함수 사용
print(t7)

print(type(t7)) # <class 'tuple'> 

# 튜플 생성 시 주의
# 숫자 1만 포함된 튜플 생성
t = (1,)
print(t) # (1,)
print(type(t)) # <class 'tuple'>

# (1)만 적으면 튜플이 아니라 정수 1이 저장된 int 타입
t = (1)
print(t) # 1
print(type(t)) # <class 'int'>

# 다음과 동일
t = 1
print(t) # 1
print(type(t)) # <class 'int'>

# 튜플을 리스트로 변환
t3 = (1, 2, 3)
to_list1 = list(t3)
print(to_list1)  # [1, 2, 3]

t3 = (1, 2, 3)
t6 = t3, (7, 8, 9) # ((1, 2, 3), (7, 8, 9))
to_list2 = list(t6)
print(to_list2) # [(1, 2, 3), (7, 8, 9)]
# 리스트로 변환되었지만, 안의 원소는 그대로 튜플로 유지

# 튜플 변경 시 오류
# 추가/수정/삭제 다 안 됨
t = (1, 2, 3)
print(t[1])
# t[0] = 5 # not support item assignment

###############################################

# (1) 이름이 my_tuple인 빈 튜플 생성
my_tuple = ()
print(my_tuple)

# (2) ("삼성", "엘지", "현대") 튜플을 리스트로 변환
company = ('삼성','엘지','현대')
companys = list(company)
print(companys) # ['삼성', '엘지', '현대']