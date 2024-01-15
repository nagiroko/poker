class card:
    def __init__(self, name, value, type):
        self.name = name
        self.value = value
        self.type = type

    def read(self,user):
        print( str(user)+" drew the " +str(self.name) +" of " +str(self.type))