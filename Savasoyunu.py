import random
import os

class Dusman():
    def __init__(self):
        self.sagmi = True
        self.saglik = random.randint(30, 70)
        self.guc = random.randint(20, 50)
        self.kalkan = random.randint(0, 10)

    def vur(self, player):
        damage = self.guc - player.kalkan
        player.saglik -= damage
        if player.saglik <= 0:
            player.sagmi = False


class Player():
    def __init__(self):
        self.sagmi = True
        self.saglik = random.randint(300, 400)
        self.guc = random.randint(40, 70)
        self.kalkan = random.randint(5, 15)

    def vur(self, dusman):
        damage = self.guc - dusman.kalkan
        dusman.saglik -= damage
        if dusman.saglik <= 0:
            dusman.sagmi = False
            dusmanlar.remove(dusman)


dusmanlar = list()
for i in range(10):
    dusmanlar.append(Dusman())

player = Player()

while True:
    print("""               |Savaş Oyununa Hoş Geldiniz|
Başlamak İçin Adınızı Yazıp 'Enter'e Ya Da Çıkmak İçin [Q] Tuşuna Basın: """)
    giris = input("")
    if giris == "q" or giris == "Q":
        exit()

    while True:
        os.system("cls")
        print()
        print("{} Karakterinin Durumu  --->>>  Sağlık: {}  ---  Güç: {}  ---  Kalkan: {}".format(giris, player.saglik, player.guc,
                                                                                        player.kalkan))
        if player.sagmi == False:
            print("Game Over.. :(")
            quit()

        if not dusmanlar:
            print("Oyunu Kazandınız! Tebrikler!")
            quit()

        for i in dusmanlar:
            print("{}. Düşman  --->>>  Sağlık: {}  ---  Güç: {}  ---  Kalkan: {}".format(dusmanlar.index(i), i.saglik,
                                                                                         i.guc, i.kalkan))
        secim = input("Düşman Seçin: ")
        if secim == "q" or giris == "Q":
            exit()
        try:
            dusman = dusmanlar[int(secim)]
            player.vur(dusman)
            if dusmanlar:
                saldiran = dusmanlar[random.randint(0, len(dusmanlar) - 1)]
                saldiran.vur(player)
            else:
                print("Düşman Kalmadı!")
        except:
            print("Hatalı Girdiniz! Oyuna devam etmek için 'Enter'e, oyundan çıkmak için [Q] tuşuna basın!")
            input()