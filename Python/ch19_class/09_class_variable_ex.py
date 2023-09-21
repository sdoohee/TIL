class Donation:
    total_donation = 0

    def __init__(self, name, donation):
        self.name = name
        self.donation_amount = donation
        self.add_donation()

    def add_donation(self):
        Donation.total_donation += self.donation_amount

    def show_donation_info(self):
        print("성명 : ", self.name)
        print("기부금 : ", self.donation_amount)
        self.show_total_donation()

    def show_total_donation(self):
        print("총 기부금 : ", Donation.total_donation)

d1 = Donation("홍길동",10000)
d1.show_donation_info()
# d1.show_total_donation()

print("----------------------------")

d2 = Donation("이몽룡",20000)
d2.show_donation_info()
# d2.show_total_donation()

print("----------------------------")

d3 = Donation("성춘향",30000)
d3.show_donation_info()
# d3.show_total_donation()
