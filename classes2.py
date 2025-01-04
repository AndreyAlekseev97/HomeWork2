class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

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

    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        return House(self.name, self.number_of_floors + value)

    def __radd__(self, value):
        return House(self.name, value + self.number_of_floors)

    def __iadd__(self, value):
        self.number_of_floors += value
        return House(self.name, self.number_of_floors)



h1 = House('ЖК Перспектива', 10)
h2 = House('ЖК Квартал', 16)

print(h1)
print(h2)

print(h1==h2)

h1 = h1 + 6
print(h1)
print(h1==h2)

h1+=15
print(h1)

h2 = h2 +14
print(h2)

print(h1>h2)
print(h1>=h2)
print(h1<h2)
print(h1<=h2)
print(h1!=h2)