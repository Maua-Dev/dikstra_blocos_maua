from abc import ABC, abstractmethod
from typing import Dict

from src.shared.domain.entities.user import User


class IBlocosRepo(ABC):

    @abstractmethod
    def get_matrix(self) -> Dict[str, Dict[str, int]]:
        """
        Get the matrix of distances between the vertices.
        """
        pass

