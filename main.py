# 5-m
class Mashina:
    def start(self):
        print("Mashina ishga tushdi")

    def drive(self):
        self.start()
        print("Mashina harakatlandi")

    def stop(self):
        self.drive()
        print("Mashina to‘xtadi")

h1 = Mashina()
h1.start()
print("---------")
h1.drive()
print("---------")
h1.stop()

# 6-m
class Telefon:
    def yoq(self):
        print("Telefon yoqildi")

    def qongiroq(self):
        self.yoq()
        print("Qo‘ng‘iroq qilinyapti")

    def ochir(self):
        self.qongiroq()
        print("Telefon o‘chirildi")

h1 = Telefon()
h1.yoq()
print("---------")
h1.qongiroq()
print("---------")
h1.ochir()
