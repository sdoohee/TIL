try:
    num = int(input("숫자 입력 : "))
except ValueError:
    pass  # 아무것도 수행하지 않고 다음 문장 수행
else:
    print(num)
finally:
    print("종료")