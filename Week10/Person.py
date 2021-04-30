class Person:
    def __init__(self, name, id, gender, height, weight):
        self.name = name
        self.id = id
        self.gender = gender
        self.height = height
        self.weight = weight

    def setName(self, newName):
        self.name = newName

    def getName(self):
        return self.name

    def setID(self, newID):
        self.id = newID
        
    def getID(self):
        return self.id