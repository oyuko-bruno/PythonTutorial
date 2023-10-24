class cars:
    # constructors
    def __init__(self,type , color,model):
        self.type = type
        self.color = color
        self.model = model

        #method
    def onyesha(self):
            print(f"I love{self.model} cars which is a {self.type} being {self.color}")

myobj=cars("Saloon","white","toyota")
myobj.onyesha()