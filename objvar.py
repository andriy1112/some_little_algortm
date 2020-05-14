class Robot:
    population = 0

    def __init__(self, name):
        '''Инициализация данних'''
        self.name = name
        print('(Инициализация {0})'.format(self.name))
        Robot.population += 1
    def __del__(self):
        '''я умираю'''
        print('{0} уничтожаетса'.format(self.name))
        Robot.population -= 1
        if Robot.population == 0:
            print('{0} бил последним'.format(self.name))
        else:
            print('сталось {0:d} роботов'.format(self.population))
    def sayHi(self):
        print('hello. My name is {0}'.format(self.name))
    def howMany():
        print('We have {0:d} robots'.format(Robot.population))

    howMany = staticmethod(howMany)
droid = Robot('R2-D2')
droid.sayHi()
Robot.howMany()

droid2 = Robot('C-3PO')
droid2.sayHi()
Robot.howMany()

print('\nhare robot can to do something\n')

print('robots ends work lets kill robots')
del droid
del droid2

Robot.howMany()