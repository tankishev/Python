# The Guild class receives a name (string). The Guild should also have one instance attribute players
# (an empty list which will contain the players of the guild). The class also has 3 additional methods:
# -	assign_player(player: Player)
# o	Adds the player to the guild and returns "Welcome player {player_name} to the guild {guild_name}".
# Remember to change the player's guild in the player class.
# o	If he is already in the guild, returns "Player {player_name} is already in the guild."
# o	If the player is in another guild, returns "Player {player_name} is in another guild."

# -	kick_player(player_name: str)
# o	Removes the player from the guild and returns "Player {player_name} has been removed from the guild.".
# Remember to change the player's guild in the player class to "Unaffiliated".
# o	If there is no such player in the guild, returns "Player {player_name} is not in the guild."

# -	guild_info()
# o	Returns the guild's information, including the players in the guild, in the format:
# "Guild: {guild_name}
# {first_player's info}
# …
# {Nplayer's info}"

from .player import Player


class Guild:

    def __init__(self, name: str) -> None:
        self.name = name
        self.players = []

    def assign_player(self, player: Player) -> str:
        if player.guild == player.default_guild:
            self.players.append(player)
            player.guild = self.name
            return f'Welcome player {player.name} to the guild {self.name}'

        elif player in self.players:
            return f'Player {player.name} is already in the guild.'

        else:
            return f'Player {player.name} is in another guild.'

    def kick_player(self, player_name: str) -> str:
        try:
            player = None
            for p in self.players:
                if p.name == player_name:
                    player = p
                    break

            self.players.remove(player)
            player.guild = player.default_guild
            return f'Player {player_name} has been removed from the guild.'

        except ValueError:
            return f'Player {player_name} is not in the guild.'

    def guild_info(self) -> str:
        retval = f'Guild: {self.name}'
        if self.players:
            retval += '\n' + '\n'.join([player.player_info() for player in self.players])
        return retval
