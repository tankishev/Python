# Create a class called Hero. Upon initialization it should receive a name (string) and health (number).
# Create two methods:
# •	defend(damage) - reduce the given damage from the hero's health:
# o	if the health become 0 or less, set it to 0 and return "{name} was defeated"
# •	heal(amount) - increase the health of the hero with the given amount


class Hero:

    def __init__(self, name: str, health: int) -> None:
        self.name = name
        self.health = health
        self.alive = True

    def defend(self, damage: int) -> str:
        if self.alive:
            self.health -= damage
            if self.health <= 0:
                self.health = 0
                self.alive = False
                return f"{self.name} was defeated"

    def heal(self, amount: int) -> None:
        if self.alive:
            self.health += amount
