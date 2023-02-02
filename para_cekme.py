# Büşra Karaca 20120101019
gecerli_kupur = [50,20,10,5]
istenen_tutar = int(input("Çekmek istediğiniz tutarı giriniz:"))
while istenen_tutar % 5 != 0:
    print("Sadece 5'in katı tutarda istenen_tutar çekilebilir.")
    istenen_tutar = int(input("Çekmek istediğiniz tutarı giriniz:"))
else:
    print("Ödemeniz yapılıyor.\nParanızı alınız:")
    for i in gecerli_kupur:                     #kalan miktar sıfıra eşit olana kadar döner.
        if istenen_tutar >= i:
            adet = int(istenen_tutar / i)
            istenen_tutar = int(istenen_tutar % i) 
            print(f"{adet} adet {i} TL")
        
       
            
            
            
        
