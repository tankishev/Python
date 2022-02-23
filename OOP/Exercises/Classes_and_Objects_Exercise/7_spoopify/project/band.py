# The Band class should receive a name (string) upon initialization. It also has an attribute albums (an empty list).
# The class has three methods:
# -	add_album(album: Album)
# o	Adds an album to the collection and returns "Band {band_name} has added their newest album {album_name}."
# o	If the album is already added, returns "Band {band_name} already has {album_name} in their library."
# -	remove_album(album_name: str)
# o	Removes the album from the collection and returns "Album {name} has been removed."
# o	If the album is published, returns "Album has been published. It cannot be removed."
# o	If the album is not in the collection, returns "Album {name} is not found."
# -	details()
# o	Returns the information of the band, with their albums, in this format:
# "Band {name}
#  {album details}
#  ...
#  {album details}"


from .album import Album


class Band:

    def __init__(self, name: str) -> None:
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        if album in self. albums:
            return f'Band {self.name} already has {album.name} in their library.'
        else:
            self.albums.append(album)
            return f'Band {self.name} has added their newest album {album.name}.'

    def remove_album(self, album_name: str):
        matches = [a for a in self.albums if a.name == album_name]
        if not matches:
            return f'Album {album_name} is not found.'
        else:
            album = matches[0]
            if album.published:
                return 'Album has been published. It cannot be removed.'
            else:
                self.albums.remove(matches[0])
                return f'Album {matches[0].name} has been removed.'

    def details(self) -> str:
        retval = f'Band {self.name}'
        if self.albums:
            retval += '\n' + '\n'.join([album.details() for album in self.albums])
        return retval
