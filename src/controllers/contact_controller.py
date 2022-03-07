from utils.error_handling_classes import (
    AlreadyAddedPhone,
    AlreadyDeletedPhone,
    HandledException,
)
from .base_controller import BaseController
from src.models.contact_model import ContactModel
from werkzeug.exceptions import HTTPException


class ContactController(BaseController):
    def __init__(self) -> None:
        super().__init__()

    def add(self, data: dict):
        try:
            phone_number = data.get("phone_number", None)
            obj = (
                self.session.query(ContactModel)
                .filter(ContactModel.phone_number == phone_number)
                .first()
            )
            if obj:
                raise AlreadyAddedPhone(phone_number)
            new_contact = ContactModel(**data)
            self.session.add(new_contact)
        except HTTPException as hp:
            raise HandledException(hp)
        except Exception as e:
            self.session.rollback()
            raise HandledException(e)
        else:
            self.session.commit()
        return self.to_dict(new_contact)

    def update_phone_number(self, old_phone_number, new_phone_number):
        try:
            flag_new_phone_number = (
                self.session.query(ContactModel)
                .filter(ContactModel.phone_number == new_phone_number)
                .first()
            )
            if flag_new_phone_number:
                raise AlreadyAddedPhone(new_phone_number)
            row: ContactModel = (
                self.session.query(ContactModel)
                .filter(ContactModel.phone_number == old_phone_number)
                .first()
            )
            row.phone_number = new_phone_number
        except HTTPException as hpe:
            raise HandledException(hpe)
        except Exception as e:
            self.session.rollback()
            raise HandledException(e)
        else:
            self.session.commit()
        return self.to_dict(row)

    def delete_contact(self, phone_number):
        try:
            row = (
                self.session.query(ContactModel)
                .filter(ContactModel.phone_number == phone_number)
                .first()
            )

            if row.deleted:
                raise AlreadyDeletedPhone(phone_number)
            row.deleted = True
        except HTTPException as hpe:
            raise HandledException(hpe)
        except Exception as e:
            self.session.rollback()
            raise HandledException(e)
        else:
            self.session.commit()
        return self.to_dict(row)

    def get_all(self):
        try:
            row = (
                self.session.query(ContactModel)
                .filter(ContactModel.deleted == 0)
                .all()
            )
        except Exception as e:
            raise HandledException(e)

        return self.to_dict_list(row)

    def __enter__(self):
        super().__enter__()
        return self

    def __exit__(self, *exc):
        super().__exit__(*exc)
