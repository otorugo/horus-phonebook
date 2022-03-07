import json
from werkzeug.exceptions import HTTPException


class HandledException(HTTPException):
    def __init__(self, e) -> None:
        self.response = e.get_response()
        self.response.content_type = "application/json"
        self.response.data = json.dumps(
            {"name": e.name, "description": e.description}
        )


class AlreadyAddedPhone(HTTPException):
    code = 400
    description = "O numero já foi adicionado"

    def __init__(self, phone_number=None) -> None:
        if phone_number:
            self.description = f"O numero {phone_number} já existe na agenda!"
        super().__init__(description=self.description)


class AlreadyDeletedPhone(HTTPException):
    code = 400
    description = "O numero já foi deletado da agenda"

    def __init__(self, phone_number=None) -> None:
        if phone_number:
            self.description = (
                f"O numero {phone_number} já foi deletado da agenda!"
            )
        super().__init__(description=self.description)
