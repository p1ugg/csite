from flask import Flask, render_template, request, redirect, jsonify
import logging
import hashlib
from urllib.parse import urlencode
import requests

import os

logging.basicConfig(level=logging.DEBUG)


application = Flask(__name__)

courses = {
    1: {
        'desc': 'Оплата курса "SMM Менеджер"',
    },
    2: {
        'desc': 'Оплата курса "Менеджер по продажам"',
    },
    3: {
        'desc': 'Оплата курса "Бариста"',
    },
    4: {
        'desc': 'Оплата курса "Бармен"',
    },
    5: {
        'desc': 'Оплата курса "Хостес"',
    },
    6: {
        'desc': 'Оплата курса "Оператор колл-центра"',
    },
    7: {
        'desc': 'Оплата курса "Секретарь-референт"',
    },
    8: {
        'desc': 'Оплата курса "Таролог"',
    },
    9: {
        'desc': 'Оплата курса "Владелец продукта"',
    },
    10: {
        'desc': 'Оплата курса "PR Менеджер"',
    },
    11: {
        'desc': 'Оплата курса "Шаурмист"',
    },
}

ORDER_FILE = 'order_number.txt'

def get_next_order_number():
    if not os.path.exists(ORDER_FILE):
        with open(ORDER_FILE, 'w') as f:
            f.write('1')  

    with open(ORDER_FILE, 'r') as f:
        current_order_number = int(f.read())

    next_order_number = current_order_number + 1

    with open(ORDER_FILE, 'w') as f:
        f.write(str(next_order_number))

    return current_order_number



@application.route('/')
def home():
    merchant_order_id = request.args.get('MERCHANT_ORDER_ID')
    intid = request.args.get('intid')

    logging.debug(f'MERCHANT_ORDER_ID: {merchant_order_id}, intid: {intid}')
    print(merchant_order_id, intid)

    return render_template('index.html', merchant_order_id=merchant_order_id, intid=intid)

@application.route('/contact_us')
def contact_us():
    return render_template('contact_info.html')


@application.route('/success')
def success():
    return render_template('success.html')


@application.route('/notification', methods=['GET', 'POST'])
def notification():
    secret_word = "Спартак"
    sign = request.form.get('SIGN')
    order_id = request.form.get('MERCHANT_ORDER_ID')
    amount = request.form.get('AMOUNT')
    currency = request.form.get('CUR_ID')
    received_sign = hashlib.md5(f"{order_id}:{amount}:{secret_word}:{currency}".encode()).hexdigest()
    if sign == received_sign:
        print(f"Payment: {order_id}")
        print(f"Payment Amount: {amount}")

        email = order_id 

        return "OK", 200
    else:
        return "FAIL", 400

# @application.route('/buy_course', methods=['POST'])
# def buy_course():
#     email = request.form.get('email')
#     username = request.form.get('username')
#     print(email, username)

#     payment_url = "https://pay.freekassa.com/?m=53528&oa=1000&o=2&s=146bc3db76fa06bd969b0dc2c7c6b7de&currency=RUB"
#     return redirect(payment_url)


@application.route('/process_payment', methods=['POST'])
def process_payment():

    data = request.json
    course_id = data.get('course_id')  

    course = courses.get(course_id)
    if not course:
        return jsonify({'error': 'Курс не найден'}), 404
    

    desc = course['desc']

    merchant_id = 'a08bb2f7-f4d2-499d-8a4e-41c4150cb98d'  # ID вашего магазина
    amount = 500  # Сумма к оплате
    currency = 'RUB'  # Валюта
    secret = '4b7195e8f4338f5c9450e18c6485b94a'  # Секретный ключ
    order_id = f'order_{get_next_order_number()}'  # Номер заказа
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

    buy_link = "https://aaio.so/merchant/pay?" + urlencode(params)
    
    
    return jsonify({'redirect_url': buy_link})




if __name__ == '__main__':
    application.run(debug=True)
