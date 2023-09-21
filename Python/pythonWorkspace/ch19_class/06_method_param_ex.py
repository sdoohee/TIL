
class Television:

    def __init__(self, channel, volume, on) :
        self.channel = channel
        self.volume = volume
        self.on = on

    def set_channel(self, channel):
        self.channel = channel

    def set_volume(self, volume):
        self.volume = volume

    def on(self, on):
        self.on = on

    def get_channel(self):
        return self.channel
    
    def get_volume(self):
        return self.volume
    
    def get_on(self):
        return self.on


t1 = Television(9 , 10, True)

print('채널 : ', t1.get_channel())
print('볼륨 : ', t1.get_volume())
print('전원 on : ', t1.get_on())

print('--------------------------------------')
t1.set_channel(11)
t1.set_volume(15)

print('채널 : ', t1.get_channel())
print('볼륨 : ', t1.get_volume())
print('전원 on : ', t1.get_on())