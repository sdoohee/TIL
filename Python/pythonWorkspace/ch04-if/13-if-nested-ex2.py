
print("☆☆☆☆☆☆☆☆☆☆상품 정보☆☆☆☆☆☆☆☆☆☆")
print("1 노트북 : 1,200,000 원")
print("2 디지털카메라 : 400,000 원")
print("☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆")

num = input("상품번호 입력 : ")

if num == "1" or num == "2":   
    cnt = int(input("주문 수량 입력 : "))

    if num == "1":
        product = "노트북"
        price = 1200000
        
    else: 
        product = "디지털카메라"
        price = 400000
    
    # 주문액 계산
    amount = cnt * price

    # 할인액 계산
    if amount >= 1000000:
        discount = int(amount * 0.1)
    elif amount >= 500000:
        discount = int(amount * 0.05)
    else:
        discount = 0
    

    # 총지불액 계산
    total = amount - discount

    # 결과 출력
    # print("상품명 : %s" % product ) 
    # print("가격 : {}원".format(format(price, ',' )))
    # print("주문 수량 : %d" % cnt ) 
    # print("주문액 : {}원".format(format(amount, ',' )))
    # print("할인액 : {}원".format(format(int(discount), ',' )))
    # print("총지불액 : {}원".format(format(int(total), ',' )))

    # print("상품명 : \t", product ) 
    # print("가격 :   \t", format(price, ',' ), "원")
    # print("주문 수량 : \t", cnt) 
    # print("주문액 : \t", format(amount, ',') , "원")
    # print("할인액 : \t", format(discount, ',' ), "원")
    # print("총지불액 : \t", format(total, ',' ),"원")

    # 오른쪽 정렬해서 출력
    print("상품명 : \t", product.rjust(12) ) 
    print("가격 :   \t", format(price, ',' ).rjust(12), "원")
    print("주문 수량 : \t", format(cnt, ',' ).rjust(12), "개")
    print("주문액 : \t", format(amount, ',').rjust(12) , "원")
    print("할인액 : \t", format(discount, ',' ).rjust(12), "원")
    print("총지불액 : \t", format(total, ',' ).rjust(12), "원")

else:
    print("잘못 입력하였습니다. 종료합니다.")
