from .base_dto import BaseDTO


class ContactDTO(BaseDTO):
    name: str
    phone_number: str

    def outputDTO(self):
        removable_keys = []
        return self._outputDTO(removable_keys)
