# 기존 파일 내용 덮어쓰지 않고
# 파일 끝에 새로 추가 
# 파일 열기 모드 : a 
# append

# 1개의 파일 객체 사용
f = open('test2.txt', 'a', encoding='utf-8')
append_data = "\n\nPython Programming"
f.write(append_data)

# 파일 읽어서 추가된 내용 확인
f = open('test2.txt', 'r', encoding='utf-8')
print(f.read())

f.close()

# 쓰기/읽기 다른 파일 객체 사용
f1 = open('test2.txt', 'a', encoding='utf-8')
append_data = "\n\nPython Programming2"
f1.write(append_data)
f1.close()

# 파일 읽어서 추가된 내용 확인
f2 = open('test2.txt', 'r', encoding='utf-8')
print(f2.read())
f2.close()