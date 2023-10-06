from Controller import Controller

class Main:
    def __init__(self):
        self.c = Controller()

    def start(self):
        print()

    while True:
        num = input("\n1. 전체도서조회 2.도서등록 3.도서수정 4.도서삭제 5.검색 6.종료 : ")
        if num == '1':
            self.c.select()
        elif num == '2':
            self.c.select()
        elif num == '3':
            self.c.select()
        elif num == '4':
            self.c.select()
        elif num == '5':
            self.c.select()
        elif num == '6':
            print("종료합니다")
            break
        else:
            print("잘못 입력하였습니다")

if __name__ == "__main__":
    print("메인입니다")

    main = Main()
    main.start()
