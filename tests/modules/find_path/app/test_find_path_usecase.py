import pytest

from src.modules.find_path.app.find_path_usecase import FindPathUsecase
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.infra.repositories.blocos_repository_mock import BlocosRepositoryMock


class Test_FindPathUsecase:

    def test_find_path(self):
        repo = BlocosRepositoryMock()
        usecase = FindPathUsecase(repo)

        response = usecase("R17", "R2")
        assert response == []


