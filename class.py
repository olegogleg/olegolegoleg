class Person:
    age1 = 0
    name1 = ""
    def age (self, age=0):
        if age<100:
            self.__age1 = age
        else:
            print("возраст меньше 100 должен быть")
    def name (self, name=""):
        self.__name1 = str(name)
    def getCoords (self):
        return self.__age1, self.__name1
    def getinfo (self):
        print("Имя: " + str(self.__age1) + ", возраст: " + str(self.__name1))
prsn = Person()
prsn.age (99)
prsn.name ("Олег")
prsn.getinfo()
