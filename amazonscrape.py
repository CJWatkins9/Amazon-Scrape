import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.de/Sony-Digitalkamera-Anti-Distortion-Verschluss-Vario-Sonnar/dp/B07G4RNJ1R/ref=sr_1_2_sspa?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=sony+a7&qid=1571448960&sr=8-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyTTA3QTYyWjE2WTFLJmVuY3J5cHRlZElkPUEwNDQwNDAwWU42Qko0NUI2UTdaJmVuY3J5cHRlZEFkSWQ9QTAwOTIzODYyV1I2WE9POVROTTlKJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=='

headers = {"User-agent":'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'}

def check_price():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[0:3])


    if (converted_price < 199.99):
        send_mail()

    print(converted_price)
    print(title.strip())
    send_mail()


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('cjwatkins9@gmail.com','*******')
    subject= 'HEY check out this price!'
    body= 'The price fell down https://www.amazon.de/Sony-Digitalkamera-Anti-Distortion-Verschluss-Vario-Sonnar/dp/B07G4RNJ1R/ref=sr_1_2_sspa?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&keywords=sony+a7&qid=1571448960&sr=8-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyTTA3QTYyWjE2WTFLJmVuY3J5cHRlZElkPUEwNDQwNDAwWU42Qko0NUI2UTdaJmVuY3J5cHRlZEFkSWQ9QTAwOTIzODYyV1I2WE9POVROTTlKJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=='
    msg = f"Subject:{subject}\n\n{body}"

    server.sendmail('cjwatkins9@gmail.com','cjwatkins9@gmail.com',msg)
    print('Email has been sent')

    server.quit()

check_price()





