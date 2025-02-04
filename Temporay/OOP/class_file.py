class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def bark(self):
        print(f"{self.name} Barks")

dog1 = Dog("Tommy", 5)
dog1.bark()

#Inheritance 
class Doberman(Dog):
    def __init__(self, name, age, color,isAggressive):
        # super().__init__(name, age)
        Dog.__init__(self,name, age)
        
        self.color = color
        self.isAggressive = isAggressive
        
    def is_aggressive(self):
        print(f"{self.name} aggressive: {self.isAggressive} age: {self.age} color: {self.color}")
        
        
dog2 = Doberman("Tommy", 5, "Black", True)

dog2.is_aggressive()