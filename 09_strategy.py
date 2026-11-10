class DiscountStrategy:
    def apply(self, total: float) -> float:
        raise NotImplementedError


class NoDiscount(DiscountStrategy):
    def apply(self, total): return total


class StudentDiscount(DiscountStrategy):
    def apply(self, total): return total * 0.90


class EmployeeDiscount(DiscountStrategy):
    def apply(self, total): return total * 0.80


class VIPDiscount(DiscountStrategy):
    def apply(self, total): return total * 0.70


class Cart:
    def __init__(self, strategy: DiscountStrategy):
        self.items = []
        self.strategy = strategy

    def add(self, price: float):
        self.items.append(price)

    def total(self) -> float:
        return self.strategy.apply(sum(self.items))


cart = Cart(StudentDiscount())
cart.add(100); cart.add(50)
print(cart.total())  # 135.0
cart.strategy = VIPDiscount()
print(cart.total())  # 105.0
