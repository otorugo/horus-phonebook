from flask import Flask, request
from src.controllers.contact_controller import ContactController
from utils.dtos.contact_dto import ContactDTO

app = Flask(__name__)


@app.post("/contact")
def add_contact():
    try:
        contact_input = request.get_json()
        with ContactController() as contact_controller:
            new_contact = contact_controller.add(contact_input)
    except Exception as e:
        raise e
    else:
        return {"new_contact": ContactDTO(**new_contact).outputDTO()}


@app.get("/contact/all")
def get_all_contacts():
    try:
        with ContactController() as contact_controller:
            all_contacts = contact_controller.get_all()
    except Exception as e:
        raise e
    else:
        return {
            "contacts": [
                ContactDTO(**contact).outputDTO() for contact in all_contacts
            ]
        }


@app.patch("/contact/update")
def update_phone_number():
    try:
        body = request.get_json()
        old_phone_number = body.get("old_phone_number", None)
        new_phone_number = body.get("new_phone_number", None)

        with ContactController() as contract_controller:
            result = contract_controller.update_phone_number(
                old_phone_number, new_phone_number
            )

    except Exception as e:
        raise e
    else:
        return ContactDTO(**result).outputDTO()


@app.delete("/contact/<phone_number>")
def delete_contact(phone_number: str):
    try:
        with ContactController() as contact_controller:
            deleted_contact = contact_controller.delete_contact(
                phone_number=phone_number
            )
    except Exception as e:
        raise e
    else:
        return {"deleted_contact": ContactDTO(**deleted_contact).outputDTO()}


config_dict = {"host": "0.0.0.0", "port": "4000", "debug": True}

if __name__ == "__main__":
    app.run(**config_dict)
