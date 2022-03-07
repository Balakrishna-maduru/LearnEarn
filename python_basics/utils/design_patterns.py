
class Subject:
    def __init__(self) -> None:
        self.observers = []

    def attach(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)
    
    def detach(self, observer):
        try:
            self.observers.remove(observer)
        except ValueError:
            pass

    def notify(self, modifier=None):
        for observer in self.observers:
            if observer != modifier:
                observer.update(self)

class Core(Subject):
    def __init__(self, name) -> None:
        super().__init__()
        self.name = name
        self._temp = None
    
    @property
    def temp(self):
        return self._temp

    @temp.setter
    def temp(self, temp):
        self._temp = temp
        self.notify()

class TempViewer:
    def update(self, subject):
        print(f'{subject.name} --> {subject.temp}')


c1 =Core("c1")
c2 =Core("c2")

t1 = TempViewer()
t2 = TempViewer()
t3 = TempViewer()
t4 = TempViewer()

c1.attach(t1)
c1.attach(t2)
c1.attach(t3)
c2.attach(t1)
c2.attach(t2)

c1.temp = 20
c2.temp = 30
c1.temp = 40