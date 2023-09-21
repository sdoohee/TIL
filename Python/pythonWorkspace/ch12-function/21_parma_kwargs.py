# 가변길이 매개변수 : **kwargs 
# key =  value 값을 받음

def show_keyward(**kwargs):
    print("--------------------------")
    for key in kwargs.keys():
        print(key, end=' ')

    print('\n')

    for value in kwargs.values():
        print(value, end=' ')

    print('\n')

    for item in kwargs.items():
        print(item)

show_keyward(id='abcd',
             name="kim",
             phone="010-1234-1234")

show_keyward(id='sky',
             name="lee",
             phone="010-1111-1111",
             address="제주도")