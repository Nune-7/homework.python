class Hotel:
    def __init__(self, name_1, place):
        self.name_1 = name_1
        self.place = place
        self.rooms_mid = {"room1" : "free", "room2": "free", "room3": "free"}
        self.mid_room_price = 15000
        self.rooms_lux = {"room1" : "free", "room2": "free", "room3": "free"}
        self.lux_room_price = 25000
        self.new_rm = {}
        self.new_rl = {}
        self.book_rm = {}
        self.book_rl = {}

    def only_pres(self):
        a = f"The Hotel is {self.name_1}, which is situated in the {self.place}"
        return a
    def pres_mid(self):
        for i,m in self.rooms_mid.items():
            if m == "free":
                self.new_rm[i] = m
        o = f"Available mid rooms -  {self.book_rm}"
        return o
    def pres_lux(self):
        for n,l in self.rooms_lux.items():
            if l == "free":
                self.new_rl[n] = l
        o_1 = f"Available lux rooms -  {self.book_rm}"
        return o_1
    def booking_mid(self):
        for j,k in self.new_rm.items():
            if k == "free":
                self.book_rm[j] = "busy"
        g = f"Reserved mid rooms -  {self.book_rm}"
        return g

    def booking_lux(self):
        for b,c in self.new_rl.items():
            if c == "free":
                self.book_rl[b] = "busy"
        g_1 = f"Reserved lux rooms -  {self.book_rm}"
        return g_1

class Taxi:
    def __init__(self, name_2, car_type, price_for_tour):
        self.name_2 = name_2
        self.car_type = car_type
        self.price_for_tour = 5000
    def Taxi_pres(self):
        p = f"Taxi {self.name_2} has {self.car_type}, which price is {self.price_for_tour}"
        return p


class Tour(Hotel, Taxi):
    def __init__(self, name_1, place, car_type, price_for_tour):
        Hotel.__init__(self, name_1, place)
        Taxi.__init__(self, car_type, price_for_tour)
    def tour_pres(self):
        price_lux = lux_room_price + price_for_tour
        price_mid = mid_room_price + price_for_tour
        y = f"We represent you {self.name} hotel, which is in {self.place}. Our offer for mid room will coast {self.price_mid},\n Our offer for lux room will coast {self.price_lux}"
        return y

object1 = Hotel("Marianna", "Tsahkadzor")

print(object1.only_pres())
print(object1.pres_mid())
print(object1.pres_lux())
print(object1.booking_mid())
print(object1.booking_lux())

object2 = Taxi("Hello", "Meredes", 5000)
print(object2.Taxi_pres())

object3 = Tour("Marianna", "Tsahkadzor", "Meredes", 5000)
print(object3.tour_pres())