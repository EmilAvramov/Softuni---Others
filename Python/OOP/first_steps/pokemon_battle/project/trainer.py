from project.pokemon import Pokemon


class Trainer:
    def __init__(self, _name=None):
        self.name = _name
        self.pokemons = []

    def add_pokemon(self, _pokemon: Pokemon):
        if _pokemon.name not in [pokemon.name for pokemon in self.pokemons]:
            self.pokemons.append(_pokemon)
            return f"Caught {_pokemon.pokemon_details()}"
        return "This pokemon is already caught"

    def release_pokemon(self, _pokemon_name: str):
        for pos, name in enumerate(self.pokemons):
            if _pokemon_name == name.name:
                self.pokemons.remove(pos)
                return f"You have released {_pokemon_name}"
        return "Pokemon is not caught"

    def trainer_data(self):
        result = f"Pokemon Trainer {self.name}\n"
        result += f"Pokemon count {len(self.pokemons)}\n"
        for pokemon in self.pokemons:
            result += f"- {pokemon.pokemon_details()}\n"
        return result
