from models.models import Sheep
from typing import Dict

class FakeDB:
    def __init__(self):
        self.data: Dict[int, Sheep] = {}

    def get_sheep(self, id: int) -> Sheep:
        return self.data.get(id)

    def add_sheep(self, id:int, sheep: Sheep) -> None:

        if sheep.id in self.data:
            raise ValueError(f"Sheep with id {id} already exists.")

        self.data[id] = sheep
        return sheep

    def del_sheep(self, id: int) -> None:
        if id not in self.data:
            raise ValueError(f"Sheep with id {id} does not exist.")

        del self.data[id]


db = FakeDB()
db.data = {
    1: Sheep(id=1, name="Spice", breed="Gotland", sex="ewe"),
    2: Sheep(id=2, name="Pepper", breed="Suffolk", sex="ram"),
    3: Sheep(id=3, name="Cinnamon", breed="Merino", sex="ewe")
}