num = input("도형 입력(1: 사각형, 2: 삼각형, 3 원) : ")

if num == "1":
    width = int(input("가로 입력 : "))
    height = int(input("세로 입력 : "))
    
    area = width * height
    shape = "사각형"    

elif num == "2":
    base = int(input("밑변 입력 : "))
    height = int(input("높이 입력 : "))

    area = (base * height) / 2   
    shape = "삼각형" 

else :
    radius = int(input("반지름 입력 : "))

    area = radius * radius * 3.141592 
    shape = "원"    



print("%s의 면적 = %.2f" % (shape, area))

