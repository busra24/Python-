# Bilgisayarın rastgele seçtiği sayıyı tahmin etme

import random

def TahminEt():
    try:
        kullanıcı_seçim = int(input("0 ve 20 arasında bir sayı giriniz: "))
        bilgisayar_seçim = random.randint(0,20)
        if kullanıcı_seçim == bilgisayar_seçim:
            print("Doğru tahmin ettiniz.")
        else:
            print("Yanlış tahmin.\nBilgisayarın seçimi: ",bilgisayar_seçim)
    
    except ValueError:
        print("Lütfen sayı giriniz!!")

TahminEt()

