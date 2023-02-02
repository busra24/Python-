# BÜŞRA KARACA
# NO : 20120101019

import time
print("Mailin geçerliliğini kontrol eden programa hoşgeldiniz.")
a= input("Mailinizi giriniz:")

b = a.find("@")
c = a[0:b].count(" ")
d = 'gmail' in a[b:]
e = 'medeniyet' in a[b:]
f = 'com' in a[b:] 
g = 'edu' in a[b:]
h = a[b:].count(".tr")


if b == -1:                             #@ bulunmadığı durum için
    print("Mailinizi yanlış girdiniz.")
    time.sleep(2)

elif c != 0:                            #@ dan önce boşluk var mı kontrolü
    print("Mailinizi yanlış girdiniz.")
    time.sleep(2)

elif '.' not in a[b:]:                  #@ dan sonraki yerlerde nokta var mı kontrolü
    print("Mailinizi yanlış girdiniz.")
    time.sleep(2)
    
elif d == False and e == False:         #alan adları var mı kontrolü
    print("Mailinizi yanlış girdiniz.")
    time.sleep(2)

elif f == False and g == False :        #com veya edu var mı kontrolü
    print("Mailinizi yanlış girdiniz.")
    time.sleep(2)
    
elif e == True and g == False:          #medeniyet alan adıyla edu kullanılmış mı kontrolü
    print("Mailinizi yanlış girdiniz.")
    time.sleep(2)

elif g == True and h == 0:              #edu varsa .tr var mı kontrolü
    print("Mailinizi yanlış girdiniz.")
    time.sleep(2)

else:                                   #yazılanlar doğruysa
    print("Mailinizi doğru girdiniz.")
    time.sleep(2)

