crypto_currencies = {
    "bitcoin": 0,
    "dogecoin": 0,
}

def set_amount(*, crypto, value):
    if(crypto in crypto_currencies):
        crypto_currencies[crypto] = value 
    else:
        raise KeyError("Key is not found for crypto currency: "+crypto)
  
set_amount(crypto="bitcoin", value=1000)
set_amount(crypto="doge", value=3000)

print(crypto_currencies)