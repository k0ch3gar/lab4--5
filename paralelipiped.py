class Paralelipiped:
    def __init__(self,length,width,height):
        self.length = length
        self.height = height
        self.width = width

    def area(self):
        s = 2 *(self.width * self.length + self.width * self.height + self.length * self.height)
        return s

    def volume(self):
        return self.height * self.length * self.width


paralelipiped = Paralelipiped(3,2,4)
print(paralelipiped.area(),paralelipiped.volume())
print("hello world")
