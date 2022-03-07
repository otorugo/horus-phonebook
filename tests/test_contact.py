from main import app
from src.controllers.contact_controller import ContactController
from json import dumps, loads
from random import randint

client = app.test_client()


def test_get_all_contacts_return_200():
    response = client.get("/contact/all")
    assert response.status_code == 200


def test_add_new_contact():
    phone_number = str(randint(10000, 80000))
    body = {"name": "Victor Teste", "phone_number": phone_number}
    response = client.post(
        "/contact", content_type="application/json", data=dumps(body)
    )
    response_data = response.data.decode("utf-8")
    response_data = loads(response_data)

    assert response.status_code == 200
    assert response_data["new_contact"]["phone_number"] == phone_number


def test_delete_contact():
    phone_number = str(randint(10000, 80000))
    body = {"name": "Victor Teste", "phone_number": phone_number}
    with ContactController() as contact_controller:
        contact_controller.add(body)

    response = client.delete(f"/contact/{phone_number}")
    response_data = response.data.decode("utf-8")
    response_data = loads(response_data)

    assert response.status_code == 200
    assert response_data["deleted_contact"]["phone_number"] == phone_number
