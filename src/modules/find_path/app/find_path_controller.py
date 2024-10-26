from src.shared.helpers.external_interfaces.external_interface import IResponse, IRequest
from .find_path_usecase import FindPathUsecase
from .find_path_viewmodel import FindPathViewmodel
from src.shared.helpers.errors.controller_errors import MissingParameters, WrongTypeParameter
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import NoItemsFound
from src.shared.helpers.external_interfaces.http_codes import OK, NotFound, BadRequest, InternalServerError, Created


class FindPathController:

    def __init__(self, usecase: FindPathUsecase):
        self.FindPathUsecase = usecase

    def __call__(self, request: IRequest) -> IResponse:
        try:
            if request.data.get('start') is None:
                raise MissingParameters('start')
            if request.data.get('end') is None:
                raise MissingParameters('end')

            path = self.FindPathUsecase(
                start=request.data.get('start'),
                end=request.data.get('end')
            )

            viewmodel = FindPathViewmodel(path)

            return OK(viewmodel.to_dict())

        except NoItemsFound as err:

            return NotFound(body=err.message)

        except MissingParameters as err:

            return BadRequest(body=err.message)

        except WrongTypeParameter as err:

            return BadRequest(body=err.message)

        except EntityError as err:

            return BadRequest(body=err.message)

        except Exception as err:

            return InternalServerError(body=err.args[0])
