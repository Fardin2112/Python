class New:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def prints(self):
        print(self.name)
        self.var2 = 3

    def print2(self, prints):
        print(self.var2)
cll = New("harshit", 23)

cll.print2()