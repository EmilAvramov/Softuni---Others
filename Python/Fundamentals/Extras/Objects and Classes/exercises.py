class Exercise:

    def __init__(self, _topic: str, _course: str, _link: str,
                 _problems: list):
        self._topic = _topic
        self._course = _course
        self._link = link
        self._problems = problems

    def unpack_values(self):
        return self._topic, self._course, self._link, self._problems


data = input()
exercises = []

while data != "go go go":
    topic = data.split(" -> ")[0]
    course = data.split(" -> ")[1]
    link = data.split(" -> ")[2]
    problems = [i for i in data.split(" -> ")[3].split(', ')]
    exercises.append(
        Exercise(topic, course, link, problems).unpack_values())
    data = input()

item_index = 1

for exercise in exercises:
    print(f"Exercises: {exercise[0]}")
    print(f"Problems for exercises and homework "
          f"for the \"{exercise[1]}\" course @ SoftUni.")
    print(f"Check your solutions here: {exercise[2]}")
    for item in exercise[3]:
        print(f"{item_index}. {item}")
        item_index += 1
    item_index = 1
