from unittest import TestCase, main
from project.movie import Movie


class TestMovie(TestCase):
    def setUp(self) -> None:
        self.movie: Movie = Movie("Movie", 1999, 5.5)

    def test_constructor(self):
        self.assertEqual(self.movie.name, "Movie")
        self.assertEqual(self.movie.year, 1999)
        self.assertEqual(self.movie.rating, 5.5)
        self.assertEqual(self.movie.actors, [])

    def test_name_get(self):
        self.movie.__name = "New Name"
        self.assertEqual(self.movie.name, "Movie")

    def test_name_set(self):
        with self.assertRaises(ValueError) as ve:
            self.movie.name = ""

        self.assertEqual("Name cannot be an empty string!", str(ve.exception))

    def test_year_get(self):
        self.movie.__year = 2010
        self.assertEqual(self.movie.year, 1999)

    def test_year_set(self):
        with self.assertRaises(ValueError) as ve:
            self.movie.year = 1800

        self.assertEqual("Year is not valid!", str(ve.exception))

    def test_actor_success(self):
        self.movie.actors.append("Actor")
        self.assertEqual(len(self.movie.actors), 1)

    def test_actor_add_success(self):
        self.movie.add_actor("New")
        self.movie.add_actor("New Two")
        self.assertEqual(len(self.movie.actors), 2)
        self.assertEqual(self.movie.actors, ["New", "New Two"])

    def test_actor_failure(self):
        self.movie.actors = ["Actor"]
        self.assertEqual(
            self.movie.add_actor("Actor"),
            "Actor is already added in the list of actors!",
        )
        self.assertEqual(len(self.movie.actors), 1)

    def test_gt_higher(self):
        self.movie_2 = Movie("Second", 2000, 6)
        self.assertTrue(self.movie.rating < self.movie_2.rating)
        self.assertEqual(
            self.movie > self.movie_2,
            f'"{self.movie_2.name}" is better than "{self.movie.name}"',
        )

    def test_gt_lower(self):
        self.movie_2 = Movie("Second", 2000, 4)
        self.assertTrue(self.movie.rating > self.movie_2.rating)
        self.assertEqual(
            self.movie > self.movie_2,
            f'"{self.movie.name}" is better than "{self.movie_2.name}"',
        )

    def test_repr(self):
        self.assertEqual(
            str(self.movie),
            f"Name: {self.movie.name}\n"
            f"Year of Release: {self.movie.year}\n"
            f"Rating: {self.movie.rating:.2f}\n"
            f"Cast: {', '.join(self.movie.actors)}",
        )


if __name__ == "__main__":
    main()
