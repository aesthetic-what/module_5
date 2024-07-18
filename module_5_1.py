class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = int(number_of_floors)

    def go_to(self, new_floor):
        for i in range(1, self.number_of_floors):
            if new_floor > self.number_of_floors or new_floor < 1:
                print('Такого этажа не существует')
            elif i <= new_floor:
                print(i)


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(6)
h2.go_to(10)
