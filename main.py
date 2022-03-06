from flask import Flask, request
from src.controllers.contact_controller import ContactController

app = Flask(__name__)


@app.post("/contact")
def add_contact():
    try:
        contact_input = request.get_json()
        with ContactController() as contact_controller:
            new_contact = contact_controller.add(contact_input)
        return {"new_contact": new_contact}

    except Exception as e:
        raise e


@app.get("/contact/all")
def get_all_contacts():
    try:
        with ContactController() as contact_controller:
            all_contacts = contact_controller.get_all()
            return all_contacts
    except Exception as e:
        raise e


@app.patch("/contact/update")
def update_phone_number():
    try:
        body = request.get_json()
        old_phone_number = body.get("old_phone_number", None)
        new_phone_number = body.get("old_phone_number", None)

        with ContactController() as contract_controller:
            result = contract_controller.update_phone_number(
                old_phone_number, new_phone_number
            )

        return result
    except Exception as e:
        raise e


@app.delete("/contact/<phone_number>")
def delete_contact(phone_number: str):
    try:
        with ContactController() as contact_controller:
            deleted_contact = contact_controller.delete_contact(
                phone_number=phone_number
            )
        return {"deleted_contact": deleted_contact}
    except Exception as e:
        raise e


config_dict = {"host": "0.0.0.0", "port": "4000", "debug": True}

if __name__ == "__main__":
    app.run(**config_dict)
