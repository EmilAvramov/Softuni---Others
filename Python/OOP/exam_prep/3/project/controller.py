from typing import Union
from project.player import Player
from project.supply.supply import Supply


class Controller:
    def __init__(self) -> None:
        self.players: list = []
        self.supplies: list = []

    def find_player(self, name: str):
        for player in self.players:
            if player.name == name:
                return player
        return False

    def find_supply(self, supply_type: str):
        for supply in self.supplies[::-1]:
            if supply.__class__.__name__ == supply_type:
                index = [
                    i
                    for i, v in enumerate(self.supplies)
                    if v.__class__.__name__ == supply_type
                ][-1]
                return supply, index
        return False

    def add_player(self, *players: Player):
        names: list = []
        for player in players:
            if self.find_player(player.name) is False:
                self.players.append(player)
                names.append(player.name)
        return f"Successfully added: {', '.join(names)}"

    def add_supply(self, *supplies: Supply):
        for supply in supplies:
            self.supplies.append(supply)

    def sustain(self, player_name: str, sustenance_type: str):
        player: Union[Player, bool] = self.find_player(player_name)
        if player:
            if sustenance_type == "Food" or sustenance_type == "Drink":
                if player.stamina == 100:
                    return f"{player.name} have enough stamina."
                if sustenance_type == "Food":
                    if self.find_supply("Food"):
                        supply, index = self.find_supply("Food")
                        player.increase_stamina(supply.energy)
                        self.supplies.pop(index)
                        return f"{player.name} sustained successfully with {supply.name}."
                    return Exception("There are no food supplies left!")
                elif sustenance_type == "Drink":
                    if self.find_supply("Drink"):
                        supply, index = self.find_supply("Drink")
                        player.increase_stamina(supply.energy)
                        self.supplies.pop(index)
                        return f"{player.name} sustained successfully with {supply.name}."
                    return Exception("There are no drink supplies left!")

    def duel(self, first_player_name: str, second_player_name: str):
        player_1: Player = self.find_player(first_player_name)
        player_2: Player = self.find_player(second_player_name)
        winner = None

        if player_1.stamina == 0 and player_2.stamina == 0:
            return f"Player {player_1.name} does not have enough stamina.\nPlayer {player_2.name} does not have enough stamina."
        elif player_1.stamina == 0:
            return f"Player {player_1.name} does not have enough stamina."
        elif player_2.stamina == 0:
            return f"Player {player_2.name} does not have enough stamina."
        else:
            if player_1.stamina > player_2.stamina:
                if player_1.stamina - player_2.stamina / 2 <= 0:
                    player_1.stamina = 0
                    winner = player_2
                    return f"Winner: {winner.name}"
                else:
                    player_1.stamina -= player_2.stamina / 2
                    if player_2.stamina - player_1.stamina / 2 <= 0:
                        player_2.stamina = 0
                        winner = player_1
                        return f"Winner: {winner.name}"
                    else:
                        player_2.stamina -= player_1.stamina / 2
            else:
                if player_2.stamina - player_1.stamina / 2 <= 0:
                    player_2.stamina = 0
                    winner = player_1
                    return f"Winner: {winner.name}"
                else:
                    player_2.stamina -= player_1.stamina / 2
                    if player_1.stamina - player_2.stamina / 2 <= 0:
                        player_1.stamina = 0
                        winner = player_2
                        return f"Winner: {winner.name}"
                    else:
                        player_1.stamina -= player_2.stamina / 2
        if player_1.stamina > player_2.stamina:
            return f"Winner: {player_1.name}"
        else:
            return f"Winner: {player_2.name}"

    def next_day(self):
        for player in self.players:
            if player.stamina - player.age * 2 <= 0:
                player.stamina = 0
            else:
                player.stamina -= player.age * 2
            self.sustain(player.name, "Food")
            self.sustain(player.name, "Drink")

    def __str__(self) -> str:
        result: list = []
        new_line = "\n"
        for player in self.players:
            result.append(str(player))
        for supply in self.supplies:
            result.append(supply.details())
        return new_line.join(result)
