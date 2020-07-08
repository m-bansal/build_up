class a:
    def __init__(self,radius):
        self.radius=radius
        self.area=3.14*self.radius*self.radius
    def display(self):
        print('radius = %f'%self.radius)
        print('area = %f'%self.area)
ob=a(2)
ob.display()
