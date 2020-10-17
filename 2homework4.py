class Country:
    def __init__(self, name_1, continent):
    	self.name_1 = name_1
    	self.continent = continent
    def Country_pres(self):
        a = f"The clothes are brought from The {self.name_1} country, which is situated in the {self.continent} continent"
        return a

class Brand:
    def __init__(self, name_2, start_date):
    	self.name_2 = name_2
    	self.start_date = start_date
    def Brand_pres(self):mmm
        b = f"{self.name_2} brand is founded in {self.start_date} in Germany"
        return b


class Season:
    def __init__(self, name_3, av_temperature):
        self.name_3 = name_3
        self.av_temperature = av_temperature
    def Season_pres(self):
        c = f"{self.name_3} season clothes are worn in {self.av_temperature} average temperature"
        return c

class Product(Country,Brand,Season):
    def __init__(self, type_1, name_1, continent, name_2, start_date, name_3, av_temperature, price, quantity):
        self.type_1 = type_1
        Country.__init__(self, name_1, continent)  
        Brand.__init__(self, name_2, start_date)
        Season.__init__(self, name_3, av_temperature) 
        self.price = price
        self.quantity = quantity
    def Product_pres(self):
        d = f"We present you {self.type_1} product, which belongs {self.name_2} brand4"
        return d
   
    def price_disc(self):
        persent = 10
        new_price = self.price * persent / 100
        return new_price

    def Quantity_inc(self):
        increase = input("Tekk me how much you would like to increase?\n")
        new_quantity = self.quantity + int(increase)
        return new_quantity

object1 = Product(1,2,3,4,5,6,7,8,9)
print(object1.price_disc())



