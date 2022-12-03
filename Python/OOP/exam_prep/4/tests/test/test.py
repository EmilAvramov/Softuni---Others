from unittest import TestCase, main
from project.team import Team


class TestTeam(TestCase):
    def setUp(self) -> None:
        self.rocket = Team("Rocket")

    def test_constructor(self):
        self.assertEqual("Rocket", self.rocket.name)
        self.assertEqual({}, self.rocket.members)

    def test_name_get_proper(self):
        name = self.rocket.name
        self.assertEqual(name, "Rocket")

    def test_name_get_error(self):
        with self.assertRaises(AttributeError) as ae:
            name = self.rocket.__name
        self.assertEqual(ae.exception.__class__.__name__, "AttributeError")

    def test_name_set_proper(self):
        self.rocket.name = "NewName"
        self.assertEqual("NewName", self.rocket.name)

    def test_name_set_error(self):
        with self.assertRaises(ValueError) as ve:
            self.rocket.name = "123"
        self.assertEqual(
            "Team Name can contain only letters!", str(ve.exception)
        )

        with self.assertRaises(AttributeError) as ae:
            self.rocket.name = 111
        self.assertEqual(
            "'int' object has no attribute 'isalpha'", str(ae.exception)
        )

    def test_add_member_assignment(self):
        self.rocket.add_member(Name=21, Name2=25)
        self.assertEqual(len(self.rocket.members), 2)
        self.rocket.add_member()
        self.assertEqual(len(self.rocket.members), 2)
        self.rocket.add_member(Name=30)
        self.assertEqual(len(self.rocket.members), 2)

    def test_add_member_message(self):
        self.assertEqual(
            "Successfully added: Name", self.rocket.add_member(Name=21)
        )
        self.assertEqual(
            "Successfully added: Name2, Name3",
            self.rocket.add_member(Name2=21, Name3=30),
        )

    def test_remove_member_unassignment(self):
        self.rocket.add_member(Name=21, Name2=25)
        self.rocket.remove_member("Name")
        self.rocket.remove_member("Name2")
        self.assertEqual(len(self.rocket.members), 0)

    def test_remove_member_messages(self):
        self.rocket.add_member(Name=21, Name2=25)
        self.assertEqual(
            "Member Name removed", self.rocket.remove_member("Name")
        )
        self.assertEqual(
            "Member with name NOT does not exist",
            self.rocket.remove_member("NOT"),
        )

    def test_gt(self):
        self.another = Team("Another")
        self.rocket.add_member(Name=21, Name2=25)
        self.assertTrue(self.rocket > self.another)
        self.another.add_member(Name=21, Name2=25, Name3=30)
        self.assertFalse(self.rocket > self.another)

    def test_len(self):
        self.rocket.add_member(Name=21, Name2=25)
        self.assertEqual(len(self.rocket), 2)

    def test_add(self):
        self.another = Team("Another")
        self.rocket.add_member(Name=21, Name2=25)
        self.another.add_member(Name3=30)
        new_team = self.rocket + self.another
        self.assertEqual(new_team.__class__.__name__, "Team")
        self.assertEqual(new_team.name, "RocketAnother")
        self.assertEqual(len(new_team.members), 3)

    def test_str(self):
        self.rocket.add_member(Name3=30)
        self.assertEqual(
            "Team name: Rocket\nMember: Name3 - 30-years old", str(self.rocket)
        )
        self.rocket.add_member(Name=21, Name2=25)
        self.assertEqual(
            "Team name: Rocket\nMember: Name3 - 30-years old\nMember: Name2 - 25-years old\nMember: Name - 21-years old",
            str(self.rocket),
        )


if __name__ == "__main__":
    main()
