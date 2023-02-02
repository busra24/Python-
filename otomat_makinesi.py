import random as r     
import time
bis = {'isim':'Bisküvi','adet':r.randint(0,4),'fiyat':6}
mas = {'isim':'Maske','adet':r.randint(0,4),'fiyat':1}
su = {'isim':'Su','adet':r.randint(0,4),'fiyat':1.5}
sak = {'isim':'Sakız','adet':r.randint(0,4),'fiyat':0.5}

dict = {'bisküvi':bis,'maske':mas,'su':su,'sakız':sak}
urunler = [bis,mas,su,sak]      
id_list = ['1','2','3','4']
gecerli_list =[20,10,5,1,0.5]               #Makineye atılabilecek geçerli miktarlar listeye atandı.
       
def fonk(urunler):                          #Seçim 2 için ürünlerden bulunan ve bulunmayan yazdıran fonksiyon
    for istek in urunler:
        if istek.get("adet")>0:             #Eğer ürün bulunuyorsa ürünün ismini ve adetini yazdırır.
             print(istek.get("isim"),istek.get("adet"),end=' adet\n')
        else:                               #Bulunmuyorsa olmayan ürünün bulunmadığını yazdırır.
            print("Makinede",istek.get("isim"),"yoktur.")
            
def func(urunler):                          #Seçim 1 için bulunan elemanlardan istenilenin tuşuna basılmasını isteyen fonksiyon
    for istek in urunler:
        if istek.get("adet")>0:             #Bulunan ürünlerin isim,id,fiyatını yazdırır. 
            print(istek.get("isim"),"için",istek.get("id"),"tuşlayınız.","(",istek.get("fiyat"),"TL )")

def hesap():                                #Seçilen tuşlamada yapılacak işlemleri içeren fonksiyon
    d = urunler[int(a)-1]                   #Seçilen işlemin 1 eksiği urunler listesindeki indeksine eşitler.
    guncel_bakiye = 0.0                     #Bakiyenin başlangıçtaki değeri
    print("Seçtiğiniz ürün:",d["isim"],"\nÜcreti:",d["fiyat"],"TL","\nLütfen ödemeyi yapınız.")
    while True:                             
        tutar = float(input("Girilen tutar (yalnızca 20-10-5-1-0.5 TL kabul edilir.):"))
        if tutar in gecerli_list:           #Girilen tutar geçerli listedeki elemanlardan birine eşitse bu bloğa girer.
            guncel_bakiye += tutar          #Girilen tutar bakiyeye eklenir.
            print("Güncel bakiye:",guncel_bakiye,"TL")
            if guncel_bakiye < d["fiyat"]:      #Eğer bakiye ürünün fiyatından azsa uyarı verir ve tekrardan tutar sorar.
                print("Yetersiz ödeme")
            elif guncel_bakiye >= d["fiyat"]:   #Eğer bakiye ürünün fiyatına eşit veya fazlaysa bu bloğa girer.
                print("Ürününüz hazırlanıyor.")
                print("-%20", end="", flush=True)
                time.sleep(1)
                print("\r", end="") 
                print("--%40",end="", flush=True) 
                time.sleep(1)
                print("\r", end="") 
                print("---%60",end="", flush=True)
                time.sleep(1)
                print("\r", end="") 
                print("----%80", end="", flush=True)
                time.sleep(1)
                print("\r", end="") 
                print("-----%100\n")
                time.sleep(1)
                print("\nÜrününüz hazır.Alabilirsiniz.")
                if guncel_bakiye - d["fiyat"]>0:        #Bakiye ürünün fiyatından fazlaysa para üstünü hesaplar.
                    para_ustu = guncel_bakiye - d["fiyat"]
                    print("\nPara üstünüzü unutmayın.Para üstü:",para_ustu,"TL") 
                break
        else:                                   #Geçerli listedeki elemanlar dışında tutar girilirse bu bloğa girer.
            print("Geçerli olmayan ödeme.Lütfen geçerli para atınız.")
            pass
        
print("Hoşgeldiniz.")
secim = int(input("Ürün için seçim yapmak için 1’i, makinede anlık olarak ne kadar ürün olduğunu görmek için 2’yi tuşlayınız:"))

while secim != 1 and secim != 2:        #Secim parametresi 1 ve 2'ye eşit değilse döngüye girer.
    print("Yanlış tuşladınız.")
    secim = int(input("Ürün için seçim yapmak için 1’i, makinede anlık olarak ne kadar ürün olduğunu görmek için 2’yi tuşlayınız:"))
    
while secim == 1 or secim == 2:
    if secim == 2:
        fonk(urunler)           #Fonksiyon çağırır.
        time.sleep(1)           #1 saniye bekleyerek seçim 1'e geçer.
        secim = 1               #Seçim 1'e geçmesi için komut

    if secim == 1:
        urunler[0].update({'id':'1'})         #Ürünler listesinin indeksine göre id numaraları eklendi.
        urunler[1].update({'id':'2'})
        urunler[2].update({'id':'3'})
        urunler[3].update({'id':'4'})
        
        print("\n")
        func(urunler)                       #Fonksiyonu çağırır.
        a = input("Giriniz:")
        
        while a not in id_list:             #Girilen tuşlama id_listte değilse döngüye girer.
             print("Yanlış tuşa bastınız.Tekrar deneyiniz.Ya da işlemi bitirmek için E'ye basınız.")
             a = input("Tekrar giriniz:")   #Tekrardan input alır.
             if a == 'E':                   #Kullanıcı E harfine basarsa program sonlanır.
                 print("İşlem sonlandırıldı.")
                 break

        d = urunler[int(a)-1]               #d isimli bir liste tanımlandı.
        if d["adet"]!=0:                #Eğer d listesinin adet bölümü sıfırdan farklıysa belirtilen tuşlamanın işlemlerini yapar.
            print("Seçim yapıldı.")
            hesap()
            break 
        else:                           #Olmayan bir ürün tuşlandığında hata vererek baştan devam eder.
            print("Yanlış tuşladınız.")
            continue

        
        

       
            
        
