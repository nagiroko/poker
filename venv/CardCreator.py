class card:
    def __init__(self, name, value, type):
        self.name = name
        self.value = value
        self.type = type

    def read(self):
        print("You drew the " +str(self.name) +" of " +str(self.type))