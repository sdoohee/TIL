# (1) calculator.py 모듈의 add() / multiplyy() 호출해서
# 3, 4 전달하고 연산 결과 출력
# import pack.pack2.calculator

# print(pack.pack2.calculator.add(3,4))
# print(pack.pack2.calculator.multipy(3,4))

# import pack.pack2.calculator as cal

# print(cal.add(3,4))
# print(cal.multipy(3,4))

from pack.pack2.calculator import add, multipy

print(add(3, 4))
print(multipy(3, 4))

# (2) show.py 모듈의 함수 3개 호출하여 결과 출력
# 매개변수 필요한 경우 임의값 전달
from pack.pack1.show import *

show_name()
print(get_age())
print(get_total(3, 4))