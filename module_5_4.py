class House:
    house_history = []

    def __new__(cls, *args):
        cls.house_history.append(args[0])
        return cls.house_history

    def __init__(self, name, number):
        self.name = name
        self.number_of_floors = number

    #def __del__(self):                                                # совместно c __new__ не работает
        #print(f'{self.name}, дом снесен, но он останется в истории')  # почему так не понятно


Korp1 = House('Волга', 15)
Korp2 = House('Долг', 7)
Korp3 = House('Династия', 14)
#del Korp1
#input()
#del Korp2
#input()

print(House.house_history)
