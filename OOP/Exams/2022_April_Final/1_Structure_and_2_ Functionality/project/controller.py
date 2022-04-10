from project.supply.supply import Supply
from project.player import Player


class Controller:

    def __init__(self) -> None:
        self.players = []
        self.supplies = []

    def add_player(self, *players):
        added_players = []
        for p in players:
            if p not in self.players:
                self.players.append(p)
                added_players.append(p)
        retval = ', '.join([el.name for el in added_players])
        return f"Successfully added: {retval}"

    def add_supply(self, *supplies):
        for s in supplies:
            self.supplies.append(s)

    def sustain(self, player_name: str, sustenance_type: str):
        found_player = self.__find_player_by_name(player_name)
        if found_player and sustenance_type in ("Food", "Drink"):
            if found_player.need_sustenance:
                found_supply = self.__find_supply_by_type(sustenance_type)
                if found_supply:
                    energy = found_supply.energy
                    found_player.stamina = min(100, found_player.stamina + energy)
                    return f"{player_name} sustained successfully with {found_supply.name}."
                raise Exception(f"There are no {sustenance_type.lower()} supplies left!")
            return f"{player_name} have enough stamina."

    def duel(self, first_player_name: str, second_player_name: str):
        # Check if duel possible
        p1 = self.__find_player_by_name(first_player_name)
        p2 = self.__find_player_by_name(second_player_name)
        no_stamina = ''
        if p1 and p1.stamina == 0:
            no_stamina += f"Player {first_player_name} does not have enough stamina."
        if p2 and p2.stamina == 0:
            if no_stamina != '':
                no_stamina += '\n'
            no_stamina += f"Player {second_player_name} does not have enough stamina."
        if no_stamina != '':
            return no_stamina

        # Duel begins
        players = sorted([p1, p2], key=lambda p: p.stamina)
        p1 = players[0]
        p2 = players[1]
        p2_stamina_left = p1.attack(p2)
        if p2_stamina_left == 0:
            return self.__declare_winner(p1, p2)
        p2.attack(p1)
        return self.__declare_winner(p1, p2)

    def next_day(self):
        for player in self.players:
            stamina_reduction = min(player.stamina, player.age * 2)
            player.stamina -= stamina_reduction
            self.sustain(player.name, "Food")
            self.sustain(player.name, "Drink")

    def __str__(self):
        retval = ''
        if self.players:
            retval += '\n'.join([str(player) for player in self.players]) + '\n'
        if self.supplies:
            retval += '\n'.join([supply.details() for supply in self.supplies]) + '\n'
        return retval.rstrip()

    def __find_supply_by_type(self, supply_type: str) -> Supply:
        for i in range(len(self.supplies) - 1, -1, -1):
            if self.supplies[i].supply_type == supply_type:
                return self.supplies.pop(i)

    def __find_player_by_name(self, player_name: str) -> Player:
        for player in self.players:
            if player.name == player_name:
                return player

    @staticmethod
    def __declare_winner(player_one: Player, player_two: Player):
        if player_one.stamina > player_two.stamina:
            return f"Winner: {player_one.name}"
        return f"Winner: {player_two.name}"
