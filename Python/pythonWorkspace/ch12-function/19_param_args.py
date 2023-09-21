# 가변길이 매개변수 : *args

# def show_players(*args):
#     for arg in args:
#         print(arg, end=" ")

#     print()   


def show_players(*players):
    for player in players:
        print(player, end=" ")

    print() 

show_players("홍길동")
show_players("홍길동", "이몽룡")
show_players("치치파스", "죠코비치", "알카라스")