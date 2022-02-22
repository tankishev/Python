# The Trainer class should receive a name (string). The Trainer should also have an attribute pokemons
# (list, empty by default). The Trainer has three methods:
# -	add_pokemon(pokemon: Pokemon)
# o	Add the pokemon to the collection and return "Caught {pokemon_name} with health {pokemon_health}".
# Note: use the pokemon's details method.
# o	If the pokemon is already in the collection, it should return "This pokemon is already caught"
# o	Hint: to import the Pokemon class you should add "from project.pokemon import Pokemon"
# -	release_pokemon(pokemon_name: String)
# o	Check if you have a pokemon with that name and remove it from the collection. It should return "You have released {pokemon_name}"
# o	If there is no pokemon with that name in the collection, return "Pokemon is not caught"
# -	trainer_data()
# o	The method returns the information about the trainer and his pokemon collection in this format:
# "Pokemon Trainer {trainer_name}
#  Pokemon count {the amount of pokemon caught}
#  - {pokemon_details}
#  ...
#  - {pokemon_details}"


from .pokemon import Pokemon


class Trainer:

    def __init__(self, name: str) -> None:
        self.name = name
        self.pokemons = []

    def add_pokemon(self, pokemon: Pokemon) -> str:
        if pokemon not in self.pokemons:
            self.pokemons.append(pokemon)
            return f"Caught {pokemon.name} with health {pokemon.health}"
        else:
            return f"This pokemon is already caught"

    def release_pokemon(self, pokemon_name: str) -> str:
        if pokemon_name in [p.name for p in self.pokemons]:
            for pokemon in self.pokemons:
                if pokemon.name == pokemon_name:
                    self.pokemons.remove(pokemon)
                    return f"You have released {pokemon_name}"
        else:
            return "Pokemon is not caught"

    def trainer_data(self) -> str:
        retval = f"Pokemon Trainer {self.name}\n"
        retval += f'Pokemon count {len(self.pokemons)}'
        for pokemon in self.pokemons:
            retval += '\n- ' + pokemon.pokemon_details()
        return retval
