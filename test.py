import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Параметры отправителя и получателя
from_email = "yarik.aimov2@gmail.com"
to_email = "pl1ya@yandex.ru"
password = "2006Yarik"

# Создание объекта сообщения
msg = MIMEMultipart()
msg['From'] = from_email
msg['To'] = to_email
msg['Subject'] = "Тема письма"

# Текст письма
body = "Это тело письма"
msg.attach(MIMEText(body, 'plain'))

# Настройка SMTP-сервера
smtp_server = "smtp.gmail.com"
smtp_port = 587  # Используется для TLS, для SSL может быть 465


server = None  # Инициализация переменной server

# Отправка сообщения
try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Запуск TLS (шифрование)
    server.login(from_email, password)  # Аутентификация
    text = msg.as_string()
    server.sendmail(from_email, to_email, text)
    print("Письмо успешно отправлено!")
except Exception as e:
    print(f"Ошибка: {e}")
finally:
    if server:
        server.quit() 