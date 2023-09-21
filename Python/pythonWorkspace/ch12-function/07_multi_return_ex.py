def order() :
    price = int(input("상품가격 입력 : "))
    qty = int(input("주문수량 입력 : "))

    amount = price * qty # 주문액

    return price, qty, amount # 여러 개의 값 리터

price, qty, amount = order()

print("------------------------")
print(f"상품 가격 : {price}원")
print(f"주문 수량 : {qty}개")
print(f"주문액 : {amount}원")