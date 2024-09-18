class PaymentMethod:
    def pay(self, amounth):
        pass

class CrediteCart(PaymentMethod):
    def pay(self, amounth):
        return f"Summa {amounth}, oplachivaetsya po creditnoy carte"


class PayPal(PaymentMethod):
    def pay(self, amounth):
        return f"Summa {amounth}, oplachivaetsya po PayPal"
    

class BankTransfer(PaymentMethod):
    def pay(self, amounth):
        return f"Summa {amounth}, oplachivaetsya po bankovskomu perevou "

payments = [CrediteCart(), PayPal(), BankTransfer()]

for payment in payments:
    print(payment.pay(input("Vvedite summu: ")))



    