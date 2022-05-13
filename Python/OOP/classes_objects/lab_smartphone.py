class Smartphone:
    def __init__(self, _memory: int) -> None:
        self.memory = _memory
        self.apps = []
        self.is_on = False

    def power(self):
        if self.is_on:
            self.is_on = False
        else:
            self.is_on = True

    def install(self, _app: str, _app_memory: int):
        if self.memory >= _app_memory and self.is_on:
            self.apps.append(_app)
            self.memory -= _app_memory
            return f"Installing {_app}"
        elif self.memory >= _app_memory and self.is_on is False:
            return f"Turn on your phone to install {_app}"
        else:
            return f"Not enough memory to install {_app}"

    def status(self):
        return f"Total apps: {len(self.apps)}. Memory left: {self.memory}"


smartphone = Smartphone(100)
print(smartphone.install("Facebook", 60))
smartphone.power()
print(smartphone.install("Facebook", 60))
print(smartphone.install("Messenger", 20))
print(smartphone.install("Instagram", 40))
print(smartphone.status())
