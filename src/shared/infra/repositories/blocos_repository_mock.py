from typing import Dict

from src.shared.domain.repositories.blocos_repository_interface import IBlocosRepo


class BlocosRepositoryMock(IBlocosRepo):
    __matrix: Dict[str, Dict[str, int]]

    def __init__(self):
        self.__matrix = {
            "A": {"B": 2, "C": 4},
            "B": {"A": 2, "C": 1, "D": 5},
            "C": {"A": 4, "B": 1, "D": 3},
            "D": {"B": 5, "C": 3}
        }

    def get_matrix(self) -> Dict[str, Dict[str, int]]:
        return self.__matrix
