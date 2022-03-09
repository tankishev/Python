from .helper_class import AIBC


class ExercisePlan(AIBC):

    def __init__(self, trainer_id: int, equipment_id: int, duration: int) -> None:
        super().__init__()
        self.trainer_id = trainer_id
        self.equipment_id = equipment_id
        self.duration = duration

    @classmethod
    def from_hours(cls, trainer_id: int, equipment_id: int, hours: int):
        return cls(trainer_id, equipment_id, hours * 60)

    def __repr__(self) -> str:
        return f"Plan <{self.id}> with duration {self.duration} minutes"
