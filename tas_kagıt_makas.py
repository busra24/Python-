#Klasik taş kağıt makas oyunu. Kullanıcı seçtikten sonra bilgisayar da seçim yapıyor ve karşılaştırılıyor. 
#Oyun, kullanıcı seçim ekranında 1, 2, ya da 3 dışında bir veri girene kadar devam ediyor.

import random

print(("Taş Kağıt Makas").center(30,"*"))
kullanıcı_skor = 0
bilgisayar_skor = 0
seçim_liste = ["1","2","3"]

while True:
    print("1-Taş\n2-Kağıt\n3-Makas\n")
    kullanıcı_seçim = input("Seçiminiz: ")
    bilgisayar_seçim = random.choice(seçim_liste)

    if kullanıcı_seçim == "1":
        if bilgisayar_seçim == "1":
            print("Bilgisayar seçimi : 1")
            print("Berabere")
        elif bilgisayar_seçim == "2":
            print("Bilgisayar seçimi : 2")
            print("Kaybettiniz")
            bilgisayar_skor += 100
        else:
            print("Bilgisayar seçimi : 3")
            print("Kazandınız")
            kullanıcı_skor += 100
    
    elif kullanıcı_seçim == "2":
        if bilgisayar_seçim == "1":
            print("Bilgisayar seçimi : 1")
            print("Kazandınız")
            kullanıcı_skor += 100
        elif bilgisayar_seçim == "2":
            print("Bilgisayar seçimi : 2")
            print("Berabere") 
        else:
            print("Bilgisayar seçimi : 3")
            print("Kaybettiniz")
            bilgisayar_skor += 100
    
    elif kullanıcı_seçim == "3":
        if bilgisayar_seçim == "1":
            print("Bilgisayar seçimi : 1")
            print("Kaybettiniz")
            bilgisayar_skor += 100
        elif bilgisayar_seçim == "2":
            print("Bilgisayar seçimi : 2")
            print("Kazandınız")
            kullanıcı_skor += 100
        else:
            print("Bilgisayar seçimi : 3")
            print("Berabere")
            
    else:
        print("Oyun sonlandı")
        break

if kullanıcı_skor > bilgisayar_skor:
    print("Oyunu kazandınız.")
    print(f"Skorunuz: {kullanıcı_skor}\nBilgisayar skor: {bilgisayar_skor}")
else:
    print("Oyunu kaybettiniz.")
    print(f"Skorunuz: {kullanıcı_skor}\nBilgisayar skor: {bilgisayar_skor}")
