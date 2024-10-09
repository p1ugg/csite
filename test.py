import hashlib
from urllib.parse import urlencode

merchant_id = 'a08bb2f7-f4d2-499d-8a4e-41c4150cb98d'  # ID вашего магазина
amount = 500  # Сумма к оплате
currency = 'RUB'  # Валюта
secret = '4b7195e8f4338f5c9450e18c6485b94a'  # Секретный ключ
order_id = '3'  # Номер заказа
desc = 'Оплата курса "СММ Менеджер"'  # Описание заказа
lang = 'ru'  # Язык формы

sign = f':'.join([
    str(merchant_id),
    str(amount),
    str(currency),
    str(secret),
    str(order_id)
])

params = {
    'merchant_id': merchant_id,
    'amount': amount,
    'currency': currency,
    'order_id': order_id,
    'sign': hashlib.sha256(sign.encode('utf-8')).hexdigest(),
    'desc': desc,
    'lang': lang
}

print("https://aaio.so/merchant/pay?" + urlencode(params))