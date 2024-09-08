from flask import Flask, render_template, request, redirect
import logging
logging.basicConfig(level=logging.DEBUG)


application = Flask(__name__)

# @application.route('/')
# def home():
#     return render_template('index.html')

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

@application.route('/buy_course', methods=['POST'])
def buy_course():
    email = request.form.get('email')
    username = request.form.get('username')
    print(email, username)

    payment_url = "https://pay.freekassa.com/?m=53528&oa=1000&o=2&s=146bc3db76fa06bd969b0dc2c7c6b7de&currency=RUB"
    return redirect(payment_url)

if __name__ == '__main__':
    application.run(debug=True)