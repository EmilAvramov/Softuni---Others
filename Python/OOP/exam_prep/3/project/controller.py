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
                if player.need_sustenance is False:
                    return f"{player.name} have enough stamina."
                if sustenance_type == "Food":
                    for supply in self.supplies:
                        if supply.__class__.__name__ == "Food":
                            if player.stamina + supply.energy >= 100:
                                player.stamina = 100
                            else:
                                player.stamina += supply.energy
                            self.supplies.remove(supply)
                            player_index = self.players.index(player)
                            self.players[player_index] = player
                            return f"{player_name} sustained successfully with {supply.name}."
                    return Exception("There are no food supplies left!")
                elif sustenance_type == "Drink":
                    for supply in self.supplies:
                        if supply.__class__.__name__ == "Drink":
                            if player.stamina + supply.energy >= 100:
                                player.stamina = 100
                            else:
                                player.stamina += supply.energy
                            self.supplies.remove(supply)
                            player_index = self.players.index(player)
                            self.players[player_index] = player
                            return f"{player_name} sustained successfully with {supply.name}."
                    return Exception("There are no drink supplies left!")

    def duel(self, first_player_name: str, second_player_name: str):
        pass

    def next_day(self):
        pass

    def __str__(self) -> str:
        pass
