# pylint: disable-all


import requests


API_CALL = "https://api.qrserver.com/v1/create-qr-code/?size=300x300&data="


def create_qr_code(website):
    response = requests.get(API_CALL+website)
    with open("./data/QR_code.png", "wb") as file:
        file.write(response.content)
        
        
create_qr_code("www.roostgame.com")