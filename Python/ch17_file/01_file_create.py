
# 파일 생성 : 파일명만 적으면 현재 디렉터리에 생성

# 먼저 파일 경로 확인
import os
print(os.getcwd())

# 현재 C:\pythonWorkspace 폴더에서 하위 ch17_file 폴더로 이동
# cd ch17_file 
# 다시 상위 폴더로 이동하는 경우 : cd ..

# 파일 생성 : 현재 ch17_file 디렉터리에 생성
# 상대 경로로 찾아감
f = open("file1.txt", "w") # 내용 없는 빈 파일 생성됨
f.close()

# 주의! : 존재하지 않는 디렉터리에 생성하면 에러
# 절대 경로 사용
f = open("C:/myFolder/file1.txt", 'w') # FileNotFoundError
f.close()

# 주의! : 경로명에 슬래시(/) 사용
f = open("C:/pythonWorkspace/ch17_file/file2.txt", 'w') 
f.close()

# 주의! : 경로명에 역슬래시(\) 사용하면 오류
#  OSError: [Errno 22] Invalid argument: 
f = open("C:\pythonWorkspace\ch17_file\file2.txt", 'w') 
f.close()

# 경로명에 역슬래시(\) 2번(\\) 사용하면 오류 없음
f = open("C:\\pythonWorkspace\\ch17_file\\file3.txt", 'w') 
f.close()

