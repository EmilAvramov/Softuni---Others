import psycopg2

connection = psycopg2.connect(
    host="localhost",
    database="pet_hotel",
    user="postgres",
    password="1123QwER",
)

cursor = connection.cursor()
cursor.execute("SELECT * FROM cat")


class Cat:
    def __init__(self, cat_id, owner_id, name, age) -> None:
        self.id = cat_id
        self.owner = owner_id
        self.name = name
        self.age = age

    def __repr__(self) -> str:
        return f"My id is {self.id}, my owner id is {self.owner}. My name is {self.name} and I'm {self.age} years old."


cats = [Cat(*row) for row in cursor.fetchall()]
print(*cats, sep="\n")

connection.close()
