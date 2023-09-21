# join() : 각 문자 사이에 특정 문자(열) 삽입
a = "aa"
print(a.join("bbb"))

delim = "-"
print(delim.join("대한민국"))

ch = ', '
print(ch.join("12345"))

sep = "-"
names = ["홍길동", "이몽룡", "성춘향"]
print(sep.join(names))

sep = "-"
numbers = ["10", "20", "30"]
print(sep.join(numbers))

# sep = "-"
# numbers = [10, 20, 30] # 숫자 값에는 적용 안 됨 : 오류
# print(sep.join(numbers))

