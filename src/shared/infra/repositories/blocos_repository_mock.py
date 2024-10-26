from typing import Dict

from src.shared.domain.repositories.blocos_repository_interface import IBlocosRepo


class BlocosRepositoryMock(IBlocosRepo):
    __matrix: Dict[str, Dict[str, int]]

    def __init__(self):
        self.__matrix = {
            "Portaria": {"R1": 9.296, "R19": 4.783},
            "R1":   {"Portaria": 9.296, "R2": 2.664},
            "R2":   {"R1": 2.664, "R21": 9.978},
            "R21":  {"R2": 9.978, "R3": 1.087},
            "R3":   {"R21": 1.087, "R4": 1.553},
            "R4":   {"R3": 1.553, "R5": 1.645},
            "R5":   {"R4": 1.645, "R6": 1.400},
            "R6":   {"R5": 1.400, "R7": 2.300},
            "R7":   {"R6": 2.300, "R8": 5.699, "R9": 1.660},
            "R8":   {"R7": 5.699},
            "R9":   {"R7": 1.660, "R10": 1.812},
            "R10":  {"R9": 1.812,  "R11": 2.031},
            "R11":  {"R10": 2.031, "R12": 1.570},
            "R12":  {"R11": 1.570, "R13": 3.064},
            "R13":  {"R12": 3.064, "R14": 3.026, "R20": 5.024},
            "R14":  {"R13": 3.026, "R15": 1.674},
            "R15":  {"R14": 1.674, "R16": 1.700},
            "R16":  {"R15": 1.700, "R17": 2.460},
            "R17":  {"R16": 2.460, "R18": 4.378},
            "R18":  {"R17": 4.378, "R19": 3.280},
            "R19":  {"R18": 3.280, "R20": 8.330, "Portaria": 4.783},
            "R20":  {"R19": 8.330, "R13": 5.024}
        }

    def get_matrix(self) -> Dict[str, Dict[str, int]]:
        return self.__matrix
