class Animals:
    def spaeks(self):
        print("Animals speaks")

class Cat(Animals):
    def meowas(self):
        print("Cat meows")
paka = Cat()
paka.meowas()
paka.spaeks()