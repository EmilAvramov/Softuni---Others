class Programmer:
    def __init__(self, _name: str, _lang: str, _skills: int) -> None:
        self.name = _name
        self.language = _lang
        self.skills = _skills

    def watch_course(self, _course: str, _lang: str, _skills_earned: int):
        if _lang == self.language:
            self.skills += _skills_earned
            return f"{self.name} watched {_course}"
        else:
            return f"{self.name} does not know {_lang}"

    def change_language(self, _new_lang: str, _skills_needed: int):
        if self.language != _new_lang and self.skills >= _skills_needed:
            old = self.language
            self.language = _new_lang
            return f"{self.name} switched from {old} to {self.language}"
        elif self.language == _new_lang:
            return f"{self.name} already knows {self.language}"
        elif self.language != _new_lang and self.skills < _skills_needed:
            return (
                f"{self.name} needs {_skills_needed - self.skills} more skills"
            )


programmer = Programmer("John", "Java", 50)
print(programmer.watch_course("Python Masterclass", "Python", 84))
print(programmer.change_language("Java", 30))
print(programmer.change_language("Python", 100))
print(programmer.watch_course("Java: zero to hero", "Java", 50))
print(programmer.change_language("Python", 100))
print(programmer.watch_course("Python Masterclass", "Python", 84))
