from werkzeug.exceptions import HTTPException


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
