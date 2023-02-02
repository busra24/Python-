
class Insan():
    def __init__(self,isim,yas,sehir):
        self.isim = isim
        self.yas = yas
        self.sehir = sehir
        self.hobi = []
    def hobi_ekle(self,h):
        self.hobi.append(h)
    def bilgi(self):
        if self.hobi == []:
            pass
        else:
            print("Hobileri:")
            for i,j in enumerate(self.hobi):
                print(i+1,"-",j)
        print("{} {} yaşındadır ve {}'lidir.".format(self.isim,self.yas,self.sehir))

class Ogrenci(Insan):
    isim_listesi = []
    def __init__(self,isim,yas,sehir,egitim_seviyesi):
        super().__init__(isim,yas,sehir)
        self.egitim_seviyesi = egitim_seviyesi
        self.katilimci_ekle()
    
    def bilgi(self):
        super().bilgi()
        print("Eğitim seviyesi:",self.egitim_seviyesi)
    
    def hobi_ekle(self, h):
        return super().hobi_ekle(h)

    def katilimci_ekle(self):
        self.isim_listesi.append(self.isim)
          
    @classmethod
    def liste_goster(cls):
        if cls.isim_listesi == []:
            print("Kimse eklenmemiş")
        else:
            for i,j in enumerate(cls.isim_listesi):
                print(i+1,"-",j)
    
    @staticmethod
    def ort_hesap(a,b):
        yıl_sonu_ort = (a+b)/2
        print("Yıl sonu ortalaması:",yıl_sonu_ort)

a = Ogrenci("Büşra",19,"İstanbul","üniversite")
b = Ogrenci("Mert",16,"İstanbul","lise")
Ogrenci.ort_hesap(92,80)       
a.ort_hesap(85,95)
a.hobi_ekle("Kitap okumak")
b.hobi_ekle("yürümek")
a.bilgi()       
b.bilgi()
a.liste_goster()           
Ogrenci.liste_goster()

