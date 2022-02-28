# The Album class should receive a name (string) upon initialization and might receive one or more songs.
# It also has instance attributes: published (False by default) and songs (an empty list). It has four methods:
# -	add_song(song: Song)
# o	Adds the song to the album and returns "Song {song_name} has been added to the album {name}."
# o	If the song is single, returns "Cannot add {song_name}. It's a single"
# o	If the album is published, returns "Cannot add songs. Album is published."
# o	If the song is already added, return "Song is already in the album."
# -	remove_song(song_name: str)
# o	Removes the song with the given name and returns "Removed song {song_name} from album {album_name}."
# o	If the song is not in the album, returns "Song is not in the album."
# o	If the album is published, returns "Cannot remove songs. Album is published."
#
# -	publish()
# o	Publishes the album (set to True) and returns "Album {name} has been published."
# o	If the album is published, returns "Album {name} is already published."
# -	details()
# o	Returns the information of the album, with the songs in it, in the format:
# "Album {name}
#  == {first_song_info}
#  == {second_song_info}
#  …
#  == {n_song_info}"

from .song import Song


class Album:

    def __init__(self, name: str, *songs) -> None:
        self.name = name
        self.published = False
        self.songs = list(songs)

    def add_song(self, song: Song) -> str:
        if song.name in [s.name for s in self.songs]:
            return 'Song is already in the album.'
        elif self.published:
            return 'Cannot add songs. Album is published.'
        elif song.single:
            return f"Cannot add {song.name}. It's a single"
        else:
            self.songs.append(song)
            return f'Song {song.name} has been added to the album {self.name}.'

    def remove_song(self, song_name: str) -> str:
        if self.published:
            return 'Cannot remove songs. Album is published.'
        elif song_name not in [s.name for s in self.songs]:
            return 'Song is not in the album.'
        else:
            return f'Removed song {song_name} from album {self.name}.'

    def publish(self) -> str:
        if self.published:
            return f'Album {self.name} is already published.'
        else:
            self.published = True
            return f'Album {self.name} has been published.'

    def details(self) -> str:
        retval = f'Album {self.name}'
        if self.songs:
            retval += '\n== ' + '\n== '.join([song.get_info() for song in self.songs])
        return retval
