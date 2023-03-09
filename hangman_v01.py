"""
Hangman - Adam asmaca oyunu 
1-Oyun için bir kelime listesi hazirlayin. +
2-Rastgele bir kelime seçin. +
2.1-Seçilen rastgele kelimeyi listeden çikartalim ki oyunun devaminda tekrar secilmesin. +
3-Seçilen kelimenin harf sayisini bulun ve _ işaretleri ile ekrana yazdirin. +
4-Kullanicidan harf tahmini isteyin. +
5-Kullanicinin girdiği harf, seçilen kelime içerisinde var mi diye kontrol edin. 
6-Eğer girilen harf seçilen kelime içerisinde varsa, _ işaretleri yerine girilen harfi yazdirin.
7-Eğer girilen harf seçilen kelime içerisinde yoksa, kullanicinin canini azaltin.
8-Kullanicinin cani tükendiğinde, oyunu sonlandirin ve kaybettiğini belirtin.
9-Eğer kullanici kelimeyi tamamlarsa, oyunu sonlandirin ve kazandiğini belirtin.

"""
import time
import random
import os

kelime_listesi = ["matematik","programlama","python","muhasebe","algoritma"]
kelime = random.choice(kelime_listesi)
kelime_uzunlugu = len(kelime)


kalan_can = 10

tahminler = ""
print("-----------------------------")
print("\nAdam asmaca oyununa hosgeldiniz...\n")
print("-----------------------------\n")
oyuncu_adi = input("Isminizi Giriniz: ")
os.system('cls')

print("\nMerhaba " + oyuncu_adi + " hazirsan oyun başliyor!!!\n")

for i in range(3,0,-1):
    print(i)
    time.sleep(1)


os.system('cls')

while kalan_can >0:

    kalan_harf = 0

    print(f"\nKelime uzunlugu: {kelime_uzunlugu}\n")

    for harf in kelime:
        if harf in tahminler:
            print(harf,end=" ")
        else:
            print("_ ",end=" ")
            kalan_harf += 1
        
    if kalan_harf == 0:
        print("\n\n-----------------------------")
        print("Tebrikler Oyunu kazandiniz...")
        print("-----------------------------\n")
        break

    tahmin = input("\n\nHarf Tahmininiz: ")
    tahminler += tahmin

    if tahmin not in kelime:
        kalan_can -= 1
        os.system('cls')
        print("-----------------------------")
        print("Yanlis Tahmin!!!")
        print(f"Kalan can: {kalan_can}")
        print("-----------------------------\n")

        if kalan_can == 0:
            print("\nKaybettiniiiiz.... :)")


    

