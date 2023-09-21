def get_area():
    rect_width = float(input("가로길이 입력 : "))
    rect_height = float(input("세로길이 입력 : "))
    return (rect_width * rect_height)

print("사각형의 면적 : %d" %get_area())