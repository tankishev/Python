# Create a class called Smartphone. Upon initialization it should receive a memory (number).
# It should also have 2 other instance attributes: apps (empty list by default) and is_on (False by default).
# Create 3 methods:
# -	power() - sets is_on on True if the phone is off, otherwise sets it to False
# -	install(app, app_memory)
# o	If there is enough memory on the phone and it is on, install the app (add it to apps and decrease
# the memory of the phone) and return "Installing {app}"
# o	If there is enough memory, but the phone is off, return "Turn on your phone to install {app}"
# o	Otherwise return "Not enough memory to install {app}"
# -	status() - returns "Total apps: {total_apps_count}. Memory left: {memory_left}"


class Smartphone:

    def __init__(self, memory: int) -> None:
        self.memory = memory
        self.apps = []
        self.is_on = False

    def power(self) -> None:
        self.is_on = not self.is_on

    def install(self, app: str, memory: int) -> str:
        if memory <= self.memory and self.is_on:
            self.memory -= memory
            self.apps.append(app)
            return f'Installing {app}'
        elif memory <= self.memory and not self.is_on:
            return f'Turn on your phone to install {app}'
        else:
            return f'Not enough memory to install {app}'

    def status(self) -> str:
        return f'Total apps: {len(self.apps)}. Memory left: {self.memory}'


smartphone = Smartphone(100)
print(smartphone.install("Facebook", 60))
smartphone.power()
print(smartphone.install("Facebook", 60))
print(smartphone.install("Messenger", 20))
print(smartphone.install("Instagram", 40))
print(smartphone.status())
