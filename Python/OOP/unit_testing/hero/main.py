from project.hero import Hero
from unittest import TestCase, main


class TestHero(TestCase):
    def setUp(self) -> None:
        self.hero = Hero("username", 5, 20, 5)
        self.hero2 = Hero("next", 5, 20, 5)

    def test_constructor(self):
        self.assertEqual("username", self.hero.username)
        self.assertEqual(5, self.hero.level)
        self.assertEqual(20, self.hero.health)
        self.assertEqual(5, self.hero.damage)

    def test_str(self):
        self.assertEqual(
            "Hero username: 5 lvl\nHealth: 20\nDamage: 5\n", str(self.hero),
        )

    def test_enemy_same(self):
        copy = Hero("username", 5, 20, 3)
        with self.assertRaises(Exception) as e:
            self.hero.battle(copy)

        self.assertEqual(str(e.exception), "You cannot fight yourself")

    def test_self_no_health(self):
        self.hero.health = 0
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.hero2)

        self.assertEqual(
            str(ve.exception),
            "Your health is lower than or equal to 0. You need to rest",
        )

    def test_enemy_no_health(self):
        self.hero2.health = 0
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.hero2)

        self.assertEqual(
            str(ve.exception), "You cannot fight next. He needs to rest",
        )

    def test_draw(self):
        self.assertEqual("Draw", self.hero.battle(self.hero2))

    def test_win(self):
        self.hero2.health = 1
        self.hero2.damage = 0
        self.assertEqual("You win", self.hero.battle(self.hero2))
        self.assertEqual(6, self.hero.level)
        self.assertEqual(25, self.hero.health)
        self.assertEqual(10, self.hero.damage)

    def test_lose(self):
        self.hero.health = 1
        self.hero.damage = 0
        self.assertEqual("You lose", self.hero.battle(self.hero2))
        self.assertEqual(6, self.hero2.level)
        self.assertEqual(25, self.hero2.health)
        self.assertEqual(10, self.hero2.damage)


if __name__ == "__main__":
    main()
