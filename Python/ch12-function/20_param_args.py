def order_coffee(coffee, *options):
    print(coffee,', 옵션 :', end='')
    for option in options:
        print(option, end=' ')
    print()

order_coffee('아메리카노', 'Tall', 'HOT', '시럽추가', 'stay')
order_coffee('카페라떼', 'Grande', 'ICE', 'go')

#####################################################

def order_coffee(coffee, *options):
    option_str = ", ".join(options) if options else "없음"
    print(f"{coffee}, 옵션: {option_str}")

order_coffee("아메리카노", "Tall", "HOT", "시럽", "stay")
order_coffee("까페라떼", "Grande", "ICE", "go")
order_coffee("오렌지 주스")