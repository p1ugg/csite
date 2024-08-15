from flask import Flask, render_template, request, redirect
import logging
logging.basicConfig(level=logging.DEBUG)


application = Flask(__name__)

@application.route('/')
def home():
    return render_template('index.html')

@application.route('/contact_us')
def contact_us():
    return render_template('contact_info.html')

# @application.route('/notification')
# def notification():
#     return '<html><body><h1>YES</h1></body></html>'

# @application.route('/notification', methods=['POST'])
# def notification():
#     MERCHANT_ORDER_ID = request.form.get('MERCHANT_ORDER_ID') 
#     AMOUNT = request.form.get('AMOUNT')  

#     print(f"Payment: {MERCHANT_ORDER_ID}")
#     print(f"Payment Amount: {AMOUNT}")

#     return "Notification received", 200


@application.route('/notification', methods=['GET', 'POST'])
def notification():
    secret_word = "Спартак"
    sign = request.form.get('SIGN')
    order_id = request.form.get('MERCHANT_ORDER_ID')
    amount = request.form.get('AMOUNT')
    currency = request.form.get('CUR_ID')
    received_sign = hashlib.md5(f"{order_id}:{amount}:{secret_word}:{currency}".encode()).hexdigest()
    print("111")
    if sign == received_sign:
        print(f"Payment: {order_id}")
        print(f"Payment Amount: {amount}")

        email = order_id 

        return "Notification received", 200
    else:
        return "Invalid signature", 400

@application.route('/buy_course', methods=['POST'])
def buy_course():
    email = request.form.get('email')
    username = request.form.get('username')
    print(email, username)

    payment_url = "https://pay.freekassa.com/?oa=499&o=%D0%9A%D1%83%D1%80%D1%81%20%D0%A1%D0%9C%D0%9C%20%D0%9C%D0%B5%D0%BD%D0%B5%D0%B4%D0%B6%D0%B5%D1%80&s=9307cbf9e5c4537c608fe920422f6391&currency=RUB&m=53528"
    return redirect(payment_url)

if __name__ == '__main__':
    application.run(debug=True)