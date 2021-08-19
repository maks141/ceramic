import decimal
from cart.cart import Cart
from yookassa import Configuration, Payment, payment
from django.core.mail import send_mail
from main.forms import CartForm

class Pay():

    obj = ''

    def __init__(self):
        pass

    def create_pay(self, request):
        Configuration.account_id = "827165"
        Configuration.secret_key = "test_dwxIiqOGKRKOweO7fffyTllqWOEKqnBdPUN-V6NoAcs"
        cart = Cart(request)
        summ = cart.get_total_price()
        payment = Payment.create({
            "amount": {
                "value": str(summ),
                "currency": "RUB"
            },
            "confirmation": {
                "type": "redirect",
                "return_url": "http://127.0.0.1:8000/pay-redirect"
            },
            "capture": True,
            "description": "Заказ №1"
        })
        return payment

class SaveForm():
    email = ''
    number = ''
    gift_sertificate = ''
    city = ''
    name_of_user = ''
    street = ''
    house = ''
    room = ''

    def __init__(self):
        pass
    
    def Email(self):
        return self.email
    def Number(self):
        return self.number
    def Gift_sertificate(self):
        return self.gift_sertificate
    def City(self):
        return self.city
    def Name_of_user(self):
        return self.name_of_user
    def Street(self):
        return self.street
    def House(self):
        return self.house
    def Room(self):
        return self.room

class GetCart():
    def get_cart(request):
        cart = Cart(request)
        return cart

class GetOrder():
    names = ''

    

