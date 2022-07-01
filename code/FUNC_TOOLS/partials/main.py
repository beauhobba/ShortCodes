from functools import partial

crypto_currencies = {
    "bitcoin": 0,
    "dogecoin": 0,
}

def set_amount(*, crypto, value):
    if(crypto in crypto_currencies):
        crypto_currencies[crypto] = value 
    else:
        raise KeyError("Key is not found for crypto currency: "+crypto)
    
# partial functions
set_bitcoin = partial(set_amount, crypto = "bitcoin")
set_dogecoin = partial(set_amount, crypto = "dogecoin")



set_bitcoin(value=1000)
set_dogecoin(value=2000)

print(crypto_currencies)