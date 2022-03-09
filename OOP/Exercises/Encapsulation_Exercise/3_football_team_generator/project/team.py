from .player import Player


class Team:

    def __init__(self, name: str, rating: int) -> None:
        self.__name = name
        self.__rating = rating
        self.__players = []

    def add_player(self, player: Player) -> str:
        if any(p.name == player.name for p in self.__players):
            return f'Player {player.name} has already joined'
        self.__players.append(player)
        return f'Player {player.name} joined team {self.__name}'
    
    def remove_player(self, player_name: str) -> Player or str:
        try:
            player = self.__players.pop(next(i for i, p in enumerate(self.__players) if p.name == player_name))
            return player
        except StopIteration:
            return f'Player {player_name} not found'
