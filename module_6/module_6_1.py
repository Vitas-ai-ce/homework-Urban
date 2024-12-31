# Задача "Съедобное, несъедобное":

class Animal:
    alive = True
    fed = False
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        if food.edible:
            print(f'{self.name} съел {food.name}')
        else:
            print(f'{self.name} не стал есть {food.name}')

class Plant:
    edible = False
    def __init__(self, name):
        self.name = name


class Mammal(Animal):
    fed = True
    pass


class Predator(Animal):
    alive = False
    pass


class Flower(Plant):
    pass

class Fruit(Plant):
    edible = True



if __name__ == "__main__":
    a1 = Predator('Волк с Уолл-Стрит')
    a2 = Mammal('Хатико')
    p1 = Flower('Цветик семицветик')
    p2 = Fruit('Заводной апельсин')
    print(a1.name)
    print(p1.name)
    print(a1.alive)
    print(a2.fed)
    a1.eat(p1)
    a2.eat(p2)
    print(a1.alive)
    print(a2.fed)



