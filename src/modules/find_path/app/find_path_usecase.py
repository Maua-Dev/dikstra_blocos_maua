from typing import List
from src.shared.domain.repositories.blocos_repository_interface import IBlocosRepository
from src.shared.helpers.functions import path_finder


class FindPathUsecase:
    def __init__(self, repo: IBlocosRepository):
        self.repo = repo

    def __call__(self, start: str, end: str) -> List[str]:
        response = path_finder.path_finder(self.repo.get_matrix(), start, end)
        return response
