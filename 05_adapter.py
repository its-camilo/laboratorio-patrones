# Interfaz que espera nuestra aplicación nueva
class PaymentProcessor:
    def pay(self, amount: float) -> str:
        raise NotImplementedError


# Sistema legacy (no lo podemos cambiar)
class LegacyPaymentGateway:
    def make_payment(self, value_in_cents: int) -> str:
        return f"Pago legacy procesado por {value_in_cents} centavos"


class LegacyPaymentAdapter(PaymentProcessor):
    def __init__(self, legacy_gateway: LegacyPaymentGateway):
        self.legacy = legacy_gateway

    def pay(self, amount: float) -> str:
        # Adapta la unidad (dólares -> centavos) y el nombre del método
        cents = int(amount * 100)
        return self.legacy.make_payment(cents)


gateway = LegacyPaymentGateway()
processor = LegacyPaymentAdapter(gateway)
print(processor.pay(25.50))  # Pago legacy procesado por 2550 centavos
