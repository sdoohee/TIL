def get_names():
    names = []
    for i in range(3):
        name = input("이름 입력 : ")
        names.append(name)
    return names

names = get_names()
print(names)
print(type(names))