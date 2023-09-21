# (1) 형변환 : int() 사용
# kor = int(input("국어 점수를 입력해주세요. : "))
# en = int(input("영어 점수를 입력해주세요. : "))
# math = int(input("수학 점수를 입력해주세요. : "))

# sum = kor + en + math

# avr = sum / 3

# print("총점 : ", sum)
# print("평균 : %.2f" %avr)

# (2) 형변환 : eval() 사용
kor = eval(input('국어 점수 입력: ')) 
en = eval(input('영어 점수 입력: ')) 
math = eval(input('수학 점수 입력: '))
sum = (kor + en + math)
print('총점: '+ str(sum))

# avr = float(sum/3)
avr = sum/3
print('평균: %.2f' % avr) 