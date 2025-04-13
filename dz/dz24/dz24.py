

class Automobile:

    def __init__(self, model, year, manufacturer, power, color, price):
        self.model = model
        self.year = year
        self.manufacturer = manufacturer
        self.power = power
        self.color = color
        self.price = price

    def print_info(self):
        print(" Данные автомобиля " .center(40, "*"))
        print(f"Название модели: {self.model}\nГод выпуска: {self.year}\n"
              f"Производитель: {self.manufacturer}"
              f"\nМощность двигателя: {self.power}\nЦвет машины: {self.color}\n"
              f"Цена: {self.price}")
        print("=" * 40)

    def set_model(self, model):
        self.model = model

    def get_model(self):
        return self.model

    def set_year(self, year):
        self.year = year

    def get_year(self):
        return self.year

    def set_manufacturer(self, manufacturer):
        self.manufacturer = manufacturer

    def get_manufacturer(self):
        return self.manufacturer

    def set_power(self,  power):
        self.power = power

    def get_power(self):
        return self.power

    def set_color(self,  color):
        self.color = color

    def get_color(self):
        return self.color

    def set_price(self,  price):
        self.price = price

    def get_price(self):
        return self.price


h1 = Automobile("X7 M50i", 2021, "BMW", "530 л.с.", "white", 10790000)
h1.print_info()
# Automobile.print_info(h1)
h1.set_model("X9 AB5o")
h1.set_year("2024")
h1.set_manufacturer("Audi")
h1.set_power("540.л.с.")
h1.set_color("red")
h1.set_power("10780000")
print(h1.get_model())
print(h1.get_year())
print(h1.get_manufacturer())
print(h1.get_power())
print(h1.get_color())
print(h1.get_price())
h1.print_info()