class Point():
    def __init__(self, input1, input2): # magic method, auto called every time you create a new "Point"
        self.x = input1
        self.y = input2

p = Point(2,8)
print(p.x)
print(p.y)