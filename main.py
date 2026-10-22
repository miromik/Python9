import random


class Auto:
    def __init__(self, rek, huippu):
        self.rekisteritunnus = rek
        self.huippunopeus = huippu
        self.nopeus = 0
        self.kuljettu_matka = 0

    def kiihdyta(self, muutos):
        self.nopeus += muutos
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        if self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, tunnit):
        self.kuljettu_matka += self.nopeus * tunnit


if __name__ == "__main__":
    # eka auto ja testit
    a = Auto("ABC-123", 142)
    print("Auto luotu:", a.rekisteritunnus, a.huippunopeus)
    print("Nopeus:", a.nopeus, "Matka:", a.kuljettu_matka)

    # vähän kiihdyttelyä
    a.kiihdyta(30)
    a.kiihdyta(70)
    a.kiihdyta(50)
    print("Uusi nopeus:", a.nopeus)

    a.kiihdyta(-200)
    print("Hätäjarrutus nopeus:", a.nopeus)

    # testataan kuljetaan matkaa
    a.nopeus = 60
    a.kuljettu_matka = 2000
    a.kulje(1.5)
    print("Matka 1.5h jälkeen:", a.kuljettu_matka)

    # autokilpailu
    print("\nKisa alkaa!")
    autot = []
    for i in range(1, 11):
        autot.append(Auto(f"ABC-{i}", random.randint(100, 200)))

    kisa_paalla = True
    tunnit = 0

    while kisa_paalla:
        tunnit += 1
        for auto in autot:
            auto.kiihdyta(random.randint(-10, 15))
            auto.kulje(1)
            if auto.kuljettu_matka >= 10000:
                kisa_paalla = False

    print(f"Kisa ohi, tunteja meni: {tunnit}")
    print("Rekisteri\tHuippu\t\tNopeus\t\tMatka")
    for auto in autot:
        print(f"{auto.rekisteritunnus}\t\t{auto.huippunopeus} km/h\t{auto.nopeus} km/h\t{auto.kuljettu_matka} km")