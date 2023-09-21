
payment_method = int(input("번호 입력 (1. 현금, 2. 카드): "))

if payment_method == 1 or payment_method == 2:
    amount = int(input("지불액: "))
    
    if payment_method == 1:
        discount_rate = 10
    else:
        discount_rate = 5
    
    discount = int(amount * (discount_rate / 100))
    
    print(f"할인율 {discount_rate}%")
    print(f"할인액: {discount}원")

else:
    print("잘못 입력하셨습니다")
