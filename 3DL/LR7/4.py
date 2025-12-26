from abc import ABC, abstractmethod

class PaymentSystem(ABC):
    @abstractmethod
    def pay(self, amount):
        pass
    @abstractmethod
    def refund(self, amount):
        pass
class CreditCardPayment(PaymentSystem):
    def pay(self, amount):
        print(f"Оплата картой: {amount} руб.")
    def refund(self, amount):
        print(f"Возврат на карту: {amount} руб.")
class PayPalPayment(PaymentSystem):
    def pay(self, amount):
        print(f"Оплата через PayPal: {amount} руб.")
    def refund(self, amount):
        print(f"Возврат через PayPal: {amount} руб.")
# Попытка создать экземпляр абстрактного класса (раскомментируй, чтобы увидеть ошибку)
# payment = PaymentSystem()  # Ошибка! Нельзя создать экземпляр абстрактного класса
# Пример работы с реальными реализациями
card = CreditCardPayment()
card.pay(1000)
card.refund(200)
paypal = PayPalPayment()
paypal.pay(500)
paypal.refund(100)