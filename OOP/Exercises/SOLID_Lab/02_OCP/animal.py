def add_other_animal_sounds(func):
    new_sounds = {
        'chicken': 'cluck'
    }

    def wrapper(animals: list):
        for animal in animals:
            if animal.species in ['cat', 'dog']:
                func([animal])
            else:
                print(new_sounds.get(animal.species, 'no sound'))
    return wrapper


class Animal:
    def __init__(self, species):
        self.species = species

    def get_species(self):
        return self.species


@add_other_animal_sounds
def animal_sound(animals: list):
    for animal in animals:
        if animal.species == 'cat':
            print('meow')
        elif animal.species == 'dog':
            print('woof-woof')


animals = [Animal('cat'), Animal('dog')]
animal_sound(animals)

## добавете ново животно и рефакторирайте кода да работи без да се налага да се правят промени по него
## при добавяне на нови животни
animals = [Animal('cat'), Animal('dog'), Animal('chicken')]
animal_sound(animals)
