from project.decoration.base_decoration import BaseDecoration


class DecorationRepository:

    def __init__(self) -> None:
        self.decorations = []

    def add(self, decoration: BaseDecoration) -> None:
        self.decorations.append(decoration)

    def remove(self, decoration: BaseDecoration) -> bool:
        if decoration in self.decorations:
            self.decorations.remove(decoration)
            return True
        return False

    def find_by_type(self, decoration_type: str):
        for decoration in self.decorations:
            if decoration.decoration_type == decoration_type:
                return decoration
        return 'None'
