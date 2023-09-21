def get_interset(deposit, int_rate):
    interest = deposit * int_rate / 100
    return interest

deposit = int(input("예금액 입력 : "))
int_rate = float(input("이자율 입력(%) : "))

interest = int(get_interset(deposit,int_rate))
print("이자액 : {}원".format(format(interest,',')))