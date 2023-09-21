# split() 메소드
string = "Python Programming"
string_split = string.split()
print(string_split)

names = "홍길동, 이몽룡, 성춘향, 변학도"
names_split = names.split(',')   # 구분자 : 
print(names_split)

colors = "red:blue:yello:green"
colors_split = colors.split(':')
print(colors_split)

# 리스트의 각 요소 출력
for color in colors_split:
    print(color)

# 문자열인 경우 출력 확인
for color in colors:
    print(color)

# range() 사용 : 인덱스로 출력
for i in range(0, len(colors_split)):
    print(colors_split[i])