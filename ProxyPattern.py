from abc import ABC, abstractmethod

class Coffee(ABC):
    @abstractmethod
    def make_coffee(self):
        pass

class Barista(Coffee):
    def make_coffee(self):
        print("Бариста готує каву")

class Ofitsiant(Coffee):
    def __init__(self):
        self.barista = Barista()
        self.paid = False

    def pay(self):
        print("Клієнт оплатив замовлення")
        self.paid = True

    def make_coffee(self):
        print("Офіціант прийняв замовлення")

        if not self.paid:
            print("Замовлення потрібно сплатити")
            return

        print("Офіціант передає замовлення баристі")
        self.barista.make_coffee()
        print("Офіціант приносить каву")

ofitsiant = Ofitsiant()
ofitsiant.make_coffee()

ofitsiant.pay()
ofitsiant.make_coffee()