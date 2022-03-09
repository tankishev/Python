class PhotoAlbum:

    __PAGE_CAPACITY = 4

    def __init__(self, pages: int) -> None:
        self.photos = [[] for _ in range(pages)]
        self.pages = pages

    @classmethod
    def from_photos_count(cls, photos_count: int) -> int:
        pages = photos_count // PhotoAlbum.__PAGE_CAPACITY
        pages += min(1, photos_count % PhotoAlbum.__PAGE_CAPACITY)
        return cls(pages)

    def add_photo(self, label: str) -> str:
        try:
            free_page = self.__find_free_page()
            self.photos[free_page].append(label)
            used_slots = len(self.photos[free_page])
            return f"{label} photo added successfully on page {free_page + 1} slot {used_slots}"
        except TypeError:
            return "No more free slots"

    def display(self) -> str:
        retval = '-' * 11
        for page in self.photos:
            retval += '\n' + str('[] ' * len(page)).rstrip() + '\n' + '-' * 11
        return retval

    def __find_free_page(self):
        try:
            return next(i for i, page in enumerate(self.photos) if len(page) < PhotoAlbum.__PAGE_CAPACITY)
        except StopIteration:
            return


if __name__ == '__main__':
    album = PhotoAlbum(2)

    print(album.add_photo("baby"))
    print(album.add_photo("first grade"))
    print(album.add_photo("eight grade"))
    print(album.add_photo("party with friends"))
    print(album.photos)
    print(album.add_photo("prom"))
    print(album.add_photo("wedding"))

    print(album.display())
