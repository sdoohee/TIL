money = int(input("교환할 돈은 얼마 입니까? "))

c500 = money //500
change = money % 500

c100 = change // 100
change = change % 100

c50 = change // 50
change = change % 50

c10 = change // 10
change = change % 10

print("\n오백원짜리 : {}개".format(c500))
print("/n백원짜리 : {}개".format(c100))
print("/n오십원짜리 : {}개".format(c50))
print("/n십원짜리 : {}개".format(c10))
print("바꾸지 못한 잔돈 : {}".format(change))
