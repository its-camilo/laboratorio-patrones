class OrderState:
    def pay(self, order): print("Acción no permitida en este estado")
    def ship(self, order): print("Acción no permitida en este estado")
    def deliver(self, order): print("Acción no permitida en este estado")


class Pending(OrderState):
    def pay(self, order):
        print("Pago recibido")
        order.state = Paid()


class Paid(OrderState):
    def ship(self, order):
        print("Pedido enviado")
        order.state = Shipped()


class Shipped(OrderState):
    def deliver(self, order):
        print("Pedido entregado")
        order.state = Delivered()


class Delivered(OrderState):
    pass  # estado final


class Order:
    def __init__(self):
        self.state: OrderState = Pending()

    def pay(self): self.state.pay(self)
    def ship(self): self.state.ship(self)
    def deliver(self): self.state.deliver(self)


order = Order()
order.ship()  # Acción no permitida en este estado (aún está Pending)
order.pay()  # Pago recibido
order.ship()  # Pedido enviado
order.deliver()  # Pedido entregado
