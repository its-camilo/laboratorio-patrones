class Chocolate:
    def prepare(self):
        raise NotImplementedError


class ChocolateBar(Chocolate):
    def prepare(self):
        return "Preparando una barra de chocolate Wonka"


class FizzyLiftingDrink(Chocolate):
    def prepare(self):
        return "Preparando un Fizzy Lifting Drink (bebida burbujeante)"


class EverlastingGobstopper(Chocolate):
    def prepare(self):
        return "Preparando un Everlasting Gobstopper (caramelo eterno)"


class WonkaFactory:
    def create_candy(self, candy_type: str) -> Chocolate:
        candy_type = candy_type.lower()
        if candy_type == "bar":
            return ChocolateBar()
        elif candy_type == "fizzy":
            return FizzyLiftingDrink()
        elif candy_type == "gobstopper":
            return EverlastingGobstopper()
        else:
            raise ValueError("Ese dulce no existe en la fábrica de Willy Wonka.")


factory = WonkaFactory()
print(factory.create_candy("bar").prepare())
print(factory.create_candy("fizzy").prepare())
print(factory.create_candy("gobstopper").prepare())
