class Car:
    def set_car(self):
        # 인스턴스 변수 값 설정ㄹ
        self.car_num = '01가1234'
        self.car_type = '아반떼'
        self.company = '현대'
        self.year = 2023
        self.dis = 1600

    def show_car_info(self):
        print("차량번호 :",self.car_num)
        print("차종 :",self.car_type)
        print("제조사 :",self.company)
        print("연식 :",self.year)
        print("배기량 :",self.dis)

car1 = Car()
car1.set_car()
car1.show_car_info()