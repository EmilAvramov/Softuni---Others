from project.rooms.room import Room

class AloneOld(Room):
    def __init__(self, family_name: str, pension: float) -> None:
        super().__init__(family_name, pension, 1)
        self.room_cost: int = 10