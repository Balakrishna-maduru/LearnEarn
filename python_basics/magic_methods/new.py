class Employee:
    def __new__(cls):
        print("__new__ magic method is called")
        inst = object.__new__(cls)
        cls.a = 10
        print(dir(cls))
        return inst

    def __init__(self):
        print("__init__ magic method is called")
        print(f"a : {self.a}")
        print(dir(self))
        self.name = 'Satya'

#e = Employee()


class Employee:
    def __init__(self):
        self.name = 'Swati'
        self.salary = 10000

    def __str__(self):
        return 'name='+self.name+' salary=$'+str(self.salary)

# e = Employee()
# print(e)


class Distance:
    def __init__(self, x=None, y=None):
        self.ft = x
        self.inch = y

    def __add__(self, x):
        temp = Distance()
        temp.ft = self.ft+x.ft
        temp.inch = self.inch+x.inch
        if temp.inch >= 12:
            temp.ft += 1
            temp.inch -= 12
        return temp

    def __str__(self):
        return 'ft:'+str(self.ft)+' in: '+str(self.inch)

# d1=Distance(3,10)
# d2=Distance(4,4)
# print("d1= {} d2={}".format(d1, d2))
# d3=d1+d2
# print(d3)


class Distance:
    def __init__(self, x=None, y=None):
        self.ft = x
        self.inch = y

    def __ge__(self, x):
        val1 = self.ft*12+self.inch
        val2 = x.ft*12+x.inch
        if val1 >= val2:
            return True
        else:
            return False


d1 = Distance(2, 1)
d2 = Distance(4, 10)
print(d1 >= d2)
