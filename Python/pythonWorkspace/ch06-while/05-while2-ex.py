n = 0
money = 10000
song = 2000

# while True:
while money != 0:
    n = n + 1
    money = money - song
    print('노래를 %s곡 불렀습니다.' % n )

    if money == 0:
        print('잔액이 없습니다. 종료합니다.')
        break
    else:
        print('현재 %s원 남았습니다.' % money)