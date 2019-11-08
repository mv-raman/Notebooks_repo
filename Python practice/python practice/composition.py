class Rocket:
    def __init__(self,name,distance):
        self.name=name
        self.distance=distance
    def lauch(self):
        print('rocket %s launched %s distance'%(self.name,self.distance))

class MarsRover():
    def __init__(self,name,distance,maker):
        self.rocket=Rocket(name,distance)
        self.maker=maker
    def get_maker(self):
        print('%s launched by %s'%(self.rocket.name,self.maker))


z=MarsRover('mars_rover','to mars','isro')
z.get_maker()
z.rocket.lauch()