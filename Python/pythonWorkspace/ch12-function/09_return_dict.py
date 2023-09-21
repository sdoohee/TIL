def get_info():
    member = {}
    name = input('이름 입력 : ')
    age = input('나이 입력 : ')
    member['이름'] = name
    member['나이'] = age
    return member

print(get_info()) # {'이름': 'kim', '나이': '23'}
print(type(get_info))

# 또는 

def get_info():
    name = input("이름 입력 : ")
    age = int(input("나이 입력 : "))
    return {'이름':name,'나이':age}

dictionary = get_info()
print(dictionary)
print(type(dictionary))