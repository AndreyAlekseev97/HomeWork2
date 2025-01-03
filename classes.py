class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
        # self.info()

    # def info(self):
    #     print(f'Наименование: {self.name}. Этаж: {self.number_of_floors}')

    def go_to(self, new_floor):
        self.new_floor = new_floor
        for i in range(new_floor):
            if self.new_floor <= self.number_of_floors:
                print(i+1)
            else:
                if self. new_floor != self.number_of_floors:
                    print('Такого этажа не существует')
                break
        return self.new_floor

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название : {self.name}, количество этажей: {self.number_of_floors}'


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(16)
h2.go_to(5)

print(h1)
print(h2)

print(len(h1))
print(len(h2))