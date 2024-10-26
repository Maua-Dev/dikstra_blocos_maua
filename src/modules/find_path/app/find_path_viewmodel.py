from typing import List
from src.shared.domain.entities.user import User
from src.shared.domain.enums.state_enum import STATE


class FindPathViewmodel:
    message: str
    path: List[str]

    def __init__(self, path: List[str]):
        self.path = path
        self.message = "Path found successfully"

    def to_dict(self):
        return {
            'path': self.path,
            'message': self.message
        }
