class Rocket:
    def __init__(self,name,distance):
        self.name=name
        self.distance=distance
    def lauch(self):
        print('rocket %s launched %s distance'%(self.name,self.distance))


class MarsRover(Rocket):
    def __init__(self,name,distance,maker):
        self.maker=maker
        Rocket.__init__(self,name,distance)

    def get_maker(self):
        print('rocket by made by %s organisation'%(self.maker))


r1=Rocket("baserocket","till earth strathosphere")
r2=MarsRover("mars rover","till mars","isro")
r1.lauch()
r2.lauch()
r2.get_maker()