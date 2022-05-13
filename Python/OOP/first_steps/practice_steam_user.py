class SteamUser:
    played_hours = 0

    def __init__(self, _name: str, _games: list) -> None:
        self.username = _name
        self.games = _games

    def play(self, _game: str, _hours: int):
        if _game in self.games:
            SteamUser.played_hours += int(_hours)
            return f"{self.username} is playing {_game}"
        else:
            return f"{_game} is not in library"

    def buy_game(self, _game: str):
        if _game not in self.games:
            self.games.append(_game)
            return f"{self.username} bought {_game}"
        else:
            return f"{_game} is already in your library"

    def status(self):
        return (
            f"{self.username} has {len(self.games)} games. Total play time: "
            f"{SteamUser.played_hours}"
        )


import unittest


class Tests(unittest.TestCase):
    def test_init(self):
        user = SteamUser("Me", ["CSGO", "Like A Dragon"])
        self.assertEqual(user.username, "Me")
        self.assertEqual(user.games, ["CSGO", "Like A Dragon"])
        self.assertEqual(user.played_hours, 0)

    def test_play_successful(self):
        user = SteamUser("Me", ["CSGO", "Like A Dragon"])
        res = user.play("CSGO", 3)
        self.assertEqual(res, "Me is playing CSGO")
        self.assertEqual(user.played_hours, 3)

    def test_play_unsuccessful(self):
        user = SteamUser("Me", ["CSGO", "Like A Dragon"])
        res = user.play("Overwatch", 2)
        self.assertEqual(res, "Overwatch is not in library")
        self.assertEqual(user.played_hours, 0)

    def test_add_game_successful(self):
        user = SteamUser("Me", ["CSGO", "Like A Dragon"])
        res = user.buy_game("Risk of Rain 2")
        self.assertEqual(res, "Me bought Risk of Rain 2")
        self.assertEqual(
            user.games, ["CSGO", "Like A Dragon", "Risk of Rain 2"]
        )

    def test_add_game_unsuccessful(self):
        user = SteamUser("Me", ["CSGO", "Like A Dragon"])
        res = user.buy_game("CSGO")
        self.assertEqual(res, "CSGO is already in your library")
        self.assertEqual(user.games, ["CSGO", "Like A Dragon"])

    def test_stats(self):
        user = SteamUser("Me", ["CSGO", "Like A Dragon"])
        res = user.status()
        self.assertEqual(res, "Me has 2 games. Total play time: 0")


if __name__ == "__main__":
    unittest.main()
