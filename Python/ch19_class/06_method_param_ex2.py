class Television:
    def __init__(self, channel, volume, on):
        self.channel = channel
        self.volume = volume
        self.on = on

    def set_channel(self, channel):
        self.channel = channel
    
    def set_volume(self, volume):
        self.volume = volume

    def show_tv_info(self):
        print('채널 : ', self.channel)
        print('볼륨 : ', self.volume)
        print('전원 ON : ', self.on)
    
myTv = Television(9, 10, True)
myTv.show_tv_info()

print()

myTv.set_channel(11)
myTv.set_volume(15)
myTv.show_tv_info()

print()

# 인스턴스를 통해 인스턴스 변수 직접 접근 가능
myTv.channel = 100 
myTv.show_tv_info()