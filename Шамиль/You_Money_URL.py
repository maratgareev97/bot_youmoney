import yookassa
import uuid

import Token


def creat_Oplata(money):
    yookassa.Configuration.account_id = Token.Api_id
    yookassa.Configuration.secret_key = Token.Api_key

    payment = yookassa.Payment.create({
        "amount": {
            "value": money,
            "currency": "RUB"
        },
        "confirmation": {
            "type": "redirect",
            "return_url": "https://www.example.com/return_url"
        },
        "capture": True,
        "description": "Заказ №1"
    },  uuid.uuid4())


    url = payment.confirmation.confirmation_url

    return url, payment.id


def oplata_chek(id):
    payment = yookassa.Payment.find_one(id)
    if payment.status == "succeeded":
        return True
    else:
        return False
