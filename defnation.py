class Vehicle:
        name = ""
        kind = "car"
        color = ""
        value = 100.00
        def description(self):
                desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
                return desc_str


fer = Vehicle()
fer.name = 'ferrari'
fer.color = 'red'
fer.value = 100000
print(fer.description())


jump = Vehicle()
jump.name = 'jump'
jump.color = 'green'
jump.value = 10000
print(jump.description())