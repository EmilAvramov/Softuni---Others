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
                    for supply in reversed(self.supplies):
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
                    for supply in reversed(self.supplies):
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
        player_1: Player = self.find_player(first_player_name)
        player_2: Player = self.find_player(second_player_name)
        winner = None

        if player_1.stamina == 0 and player_2.stamina == 0:
            return f"Player {first_player_name} does not have enough stamina.\nPlayer {second_player_name} does not have enough stamina."
        elif player_1.stamina == 0:
            return f"Player {first_player_name} does not have enough stamina."
        elif player_2.stamina == 0:
            return f"Player {second_player_name} does not have enough stamina."
        else:
            if player_1.stamina > player_2.stamina:
                if player_1.stamina - player_2.stamina / 2 <= 0:
                    player_1.stamina = 0
                    winner = player_2
                    return f"Winner: {winner.name}"
                else:
                    player_1.stamina -= player_2.stamina / 2
                    if player_2.stamina - int(player_1.stamina / 2) <= 0:
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
            for supply in self.supplies:
                if supply.__class__.__name__ == "Food":
                    player.increase_stamina(supply.energy)
                    self.supplies.remove(supply)
                    break
            for supply in self.supplies:
                if supply.__class__.__name__ == "Drink":
                    player.increase_stamina(supply.energy)
                    self.supplies.remove(supply)
                    break

    def __str__(self) -> str:
        result: list = []
        new_line = "\n"
        for player in self.players:
            result.append(
                f"Player: {player.name}, {player.age}, {player.stamina}, {player.need_sustenance}"
            )
        for supply in self.supplies:
            result.append(
                f"{supply.__class__.__name__}: {supply.name}, {supply.energy}"
            )
        return new_line.join(result)
