import pytest

from src.modules.find_path.app.find_path_usecase import FindPathUsecase
from src.modules.find_path.app.find_path_controller import FindPathController
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.blocos_repository_mock import BlocosRepositoryMock


class Test_FindPathController:

    def test_find_path(self):
        repo = BlocosRepositoryMock()
        usecase = FindPathUsecase(repo)
        controller = FindPathController(usecase)

        response = controller(request=HttpRequest(body={
            'start': 'R17',
            'end': 'R2'
        }))
        assert response.status_code == 200
        assert response.body.get('message') == 'Path found successfully'
        assert response.body.get('path') == ['R17', 'R18', 'R19', 'Portaria', 'R1', 'R2']

    def test_find_path_without_start(self):
        repo = BlocosRepositoryMock()
        usecase = FindPathUsecase(repo)
        controller = FindPathController(usecase)

        response = controller(request=HttpRequest(body={
            'end': 'R2'
        }))
        assert response.status_code == 400
        assert response.body == 'Field start is missing'
    
    def test_find_path_without_end(self):
        repo = BlocosRepositoryMock()
        usecase = FindPathUsecase(repo)
        controller = FindPathController(usecase)

        response = controller(request=HttpRequest(body={
            'start': 'R17',
        }))
        assert response.status_code == 400
        assert response.body == 'Field end is missing'


