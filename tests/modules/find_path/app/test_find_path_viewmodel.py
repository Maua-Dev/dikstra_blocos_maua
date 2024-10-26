import pytest

from src.modules.find_path.app.find_path_viewmodel import FindPathViewmodel
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.infra.repositories.blocos_repository_mock import BlocosRepositoryMock


class Test_FindPathViewmodel:

    def test_find_path(self):
        viewmodel = FindPathViewmodel(path=['R17', 'R18', 'R19', 'Portaria', 'R1', 'R2'])

        response = viewmodel.to_dict()
        assert response =={'path': ['R17', 'R18', 'R19', 'Portaria', 'R1', 'R2'], 'message': 'Path found successfully'}


