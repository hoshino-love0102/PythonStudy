class TV:
    def __init__(self, volume, Channel,on):
        self.volume = volume
        self.Channel = Channel
        self.on = on

    def show(self):
        print(f"{self.Channel}, {self.volume}, {self.on}")
    def setChannel(self, Channel):
        self.Channel = Channel

t=TV(9,10,True)
t.setChannel(11)
t.show()