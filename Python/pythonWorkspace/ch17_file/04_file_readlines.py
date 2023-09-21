
# 파일 읽기 : readlines()로 전체 파일 읽기

# 1개 행이 리스트의 요소
# 행 끝에 \n 포함되어 있음
f1 = open('test.txt', 'r', encoding='utf-8')
lines = f1.readlines() # 리스트로 생성
print(lines)
f1.close()

# 전체 라인 읽어서 1행씩 출력
f2 = open('test.txt', 'r', encoding='UTF-8')
lines = f2.readlines()
for line in lines:
    print(line, end='')
f2.close()



