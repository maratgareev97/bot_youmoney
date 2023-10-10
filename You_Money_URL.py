import yookassa

import Token

def creat_Oplata():
    yookassa.Configuration.account_id = Token.api_id
    yookassa.Configuration.secret_key = Token.Api_key

    payment = yookassa.Payment.create({
        "amout" : {
            "value": 100,
            "currency" : "RUB"
        },
        "confirmation": {
            "type": "redirect",
            "return_URL": "https://t.me/ShamilgareevBot"
        },
        "description": "Покупка чего-либо",
        "capture": True
    })

    url = payment.configuration.configuration_url

    return  url, payment.id

def oplata_chek(id):
    payment = yookassa.Payment.find_one(id)
    if payment.status == "succeeded":
        return True
    else:
        return  False
