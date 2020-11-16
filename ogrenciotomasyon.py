#YENİ KAYITLARIN ALINDIGI FONKSİYON
def ekle():
    dosya=open("ogrenciler.txt","a")
    ad_soyad=input("isim soyisim giriniz: ")
    bolum=input("bolum giriniz")
    vize1=int(input("vize1 giriniz"))
    vize2=int(input("vize2 giriniz"))
    final=int(input("final giriniz"))
    dosya.write("\n")
    dosya.write(ad_soyad+":"+bolum+":"+str(vize1)+":"+str(vize2)+":"+str(final))
    dosya.close()
    print("\n\t EKLEME İŞLEMİ YAPILDI!!!\n")
#DOSYADAN VERİ SİLME FONKSİYONU
def sil():
    #KULLANICIYA İLK ÖNCE VAR OLAN VERİLERİ GÖSTERİYORUM YANLIŞ YAZMAMASI İÇİN
    listele()
    dizi = []
    ad=[]
    dosya=open("ogrenciler.txt","r")
    #DOSYADAKİ VERİLERİ BİR LİSTEYE ATIYORUM
    lines = dosya.readlines()
    dosya.close()
    sayac=len(lines)
    for x in range(sayac):
        #LİSTEYİ ÖZEL KARAKTERE GÖRE PARÇALAYIP BİR BAŞKA LİSTEYE AKTARIYORUM
       dizi.append( lines[x].split(":"))
        #DİZİ LİSTESİNİN İLK ELAMANI ADINI TEMİSL EDİYOR
       ad.append(dizi[x][0])
    delete=input("silmek istediginiz adı giriniz")
    kontrol=0
    #SİLİNMEK İSTENİLEN ADIN VAR OLUP OLMADIGI KONTROL EDİLİYOR
    for x in range(len(ad)):
         if delete==ad[x]:
             kontrol=1
             break
    #YOK İSE MESAJ VERİLİYOR
    if kontrol == 0:
        print("\n\t GİRİLEN İSİMDE ÖGRENCİ BULUNAMADI!!!\n")
    #VAR İSE SİLME İŞLEMİ YAPLIYOR
    else:
        print("\n\t İSİM MEVCUT!!! SİLME İŞLEMİ YAPILIYOR...\n")
        dosya=open("ogrenciler.txt","w")
        #SİLİNMEK İSTENİLEN ÖGRENCİ HARİÇ DİGERLERİ DOSYAYA YENİDEN YAZDIRILIYOR BÖYLECE SİLİNECEK VERİ KAYBOLMUŞ OLUYOR
        for y in range(sayac) :
            if dizi[y][0] == delete:
                continue
            else:
                dosya.write(dizi[y][0] +":"+ dizi[y][1] +":"+ dizi[y][2] +":"+ dizi[y][3] +":"+ dizi[y][4])
        dosya.close()
        print("\n\t"+delete+" İSİMLİ ÖGRENCİNİN VERİLERİ BAŞARILI ŞEKİLDE SİLİNDİ!!!\n")
#GÜNCELLEME FONKSİYONU
def guncelle():
    dizi = []
    ad = []
    dosya = open("ogrenciler.txt", "r")
    lines = dosya.readlines()
    dosya.close()
    sayac = len(lines)
    listele()
    for x in range(sayac):
        dizi.append(lines[x].split(":"))
        ad.append(dizi[x][0])
    update = input("güncelemek istediginiz adı giriniz")
    kontrol = 0
    for x in range(len(ad)):
        if update == ad[x]:
            kontrol = 1
            break
    #GÜNCELLENMEK İSTENİLEN VERİNİN VARLIGI KONTROL EDİLİYOR
    if kontrol == 0:
        print("\n\t GİRİLEN İSİMDE ÖGRENCİ BULUNAMADI!!!\n")
    else:
        dosya = open("ogrenciler.txt", "w")
        #VAR İSE GÜNCELLENECEK VERİYE KDAR NORMAL YAZDIRILIYOR GÜNCELLENECK VERİDE KULLANICIDAN GÜNCEL BİLGİLER ALINIYOR
        for y in range(sayac):
            if dizi[y][0] == update:
                ad_soyad = input("isim soyisim giriniz: ")
                bolum = input("bolum giriniz")
                vize1 = int(input("vize1 giriniz"))
                vize2 = int(input("vize2 giriniz"))
                final = int(input("final giriniz"))
                dosya.write(ad_soyad + ":" + bolum + str(vize1) + ":" + str(vize2) + ":" + str(final) +"\n")
            else:
                dosya.write(dizi[y][0] +":"+ dizi[y][1] +":"+ dizi[y][2] +":"+ dizi[y][3] +":"+ dizi[y][4])
        dosya.close()
        print("\n\t"+update+" İSİMLİ ÖGRENCİ -> "+ad_soyad+" MERTCAN İSİMLİ ÖGRENCİ OLARAK GÜNCELLENDİ!!!\n")
#ARAMA FONKSİYONU
def arama():
    dizi = []
    ad = []
    dosya = open("ogrenciler.txt", "r")
    lines = dosya.readlines()
    dosya.close()
    sayac = len(lines)
    for x in range(sayac):
        dizi.append(lines[x].split(":"))
        ad.append(dizi[x][0])
    ara = input("aramak istediginiz kelimeyi giriniz")
    kontrol = 0
    for x in range(len(ad)):
        if ara == ad[x]:
            kontrol = 1
            break

    if kontrol == 0:
        print("\n\t GİRİLEN İSİMDE ÖGRENCİ BULUNAMADI!!!\n")
    else:
        print("\n\t GİRİLEN İSİMDE ÖGRENCİ BİLGİLERİ!!!\n")
        for y in range(sayac):
            if dizi[y][0] == ara:
                print(dizi[y][0] + "\t" + dizi[y][1] + "\t" + dizi[y][2] + "\t" + dizi[y][3] + "\t" + dizi[y][4])

#OGR LERİN ORTLAMALARI İSTENİLEN KRİTERLERE GÖRE HESAPLANIYOR HEM ORTALAMASI HEMDE GEÇTİ KADLI BİLGİSİ EKLENİYOR
#BURADA BAŞKA BİR DOSYAYA YAZDIRDIM. KAYNAKLARIMIN ÜSÜTNE YAZILIP VERİLERİMİN GİTMESİNİ İSTEMEDİGİM İÇİN
def ortalama_hesapla():
    dizi = []
    sinif_durumu=[]
    dosya = open("ogrenciler.txt", "r")
    lines = dosya.readlines()
    dosya.close()
    for x in range(len(lines)):
        dizi.append(lines[x].split(":"))
    for y in range(len(dizi)):
        #ORTALAMA HESABI YAPILIYOR
        ort = (int(dizi[y][4]) * 0.4) + (int(dizi[y][3]) * 0.3) + (int(dizi[y][2]) * 0.3)
        dizi[y].append(ort)
        #HEM ORTALAMANIN 60 ÜZERİ HEMDE FİNAL NOTUNUN 60 VE ÜZERİ OLMA ŞARTINI SAGLAYAN ÖGRENCİLER GEÇTİ OLARAK DİGERLERİ KALDI OLARAK BELİRLENİYOR
        if int(dizi[y][4])>=60:
            if ort >= 60:
                gecti="GECTI"
                dizi[y].append(gecti)
                sinif_durumu.append(dizi[y])
            else:
                kaldi="KALDI"
                dizi[y].append(kaldi)
                sinif_durumu.append(dizi[y])
        else:
            kaldi = "KALDI"
            dizi[y].append(kaldi)
            sinif_durumu.append(dizi[y])
    dosya=open("ortalama.txt","w")
    #BU BİLGİLER KAYNAK DOSYAM HARİCİNDE BİR DSYADA KULLANIYA GÖSTERİLİYOR
    print("İSİM\tBOLUM\tV1\tV2\tF\tORT\tDURUM")
    for x in range(len(sinif_durumu)):
        dosya.write(sinif_durumu[x][0]+"\t"+sinif_durumu[x][1]+"\t"+str(sinif_durumu[x][2])+"\t"+str(sinif_durumu[x][3])+"\t"+str(sinif_durumu[x][4]).replace("\n","")+"\t"+str(sinif_durumu[x][5])+"\t"+sinif_durumu[x][6]+"\n")
    dosya.close()
    print("\nKALDI GEÇTİ HSAPLAMASI YAPILDI DOSYAYA YAZILDI\n")
    #DİZİ SIRALAMA FONKSİYONUNDA KULLANACAGIM İÇİN RETURN ETTİM
    return dizi

#KULLANICI İSTEDİGİ ZAMAN MEVCUT ÖGRENCİ BİLGİLERİNİ EKRANA BASTIRABİLİR
def listele():
    dosya = open("ogrenciler.txt", "r")
    lines = dosya.readlines()
    dosya.close()
    print("İSİM\tBOLUM\tV1\tV2\tF")
    for x in lines:
        print(x.replace(":","\t"))


#SIRALAMA FONSKİYONUMUZ
def siralama():
    #ORT HESAPLA FONSİYONUNDA ZATEN HESAPLAMIŞ OLDUGUMUZ ORTLAMA BİLGİSİ İÇEREN DİZİ DÖNDÜRÜLÜYRO VE BURADA KULLANILIYOR
    dizi=ortalama_hesapla()
    temp=[]
    #FONKSİYON İÇERİSİNDE FONKSİYON KULLARAK İKİ FARKLI SIRALAMA ALGORİTAMASINA YER VERDİM
    def k_b():
        for i in range(len(dizi)):
            for j in range(len(dizi)-1):
                if dizi[j][5]>dizi[j+1][5]:
                    temp=dizi[j+1]
                    dizi[j+1]=dizi[j]
                    dizi[j]=temp

        dosya= open("ortalama.txt", "w")
        for x in range(len(dizi)):
            dosya.write(dizi[x][0] + "\t" + dizi[x][1] + "\t" + str(dizi[x][2]) + "\t" + str(dizi[x][3]) + "\t" + str(dizi[x][4]).replace("\n", "") + "\t" + str(dizi[x][5]) + "\t" +"\n")
        dosya.close()

    def b_k():
        for i in range(len(dizi)):
            for j in range(len(dizi)-1):
                if dizi[j][5]<dizi[j+1][5]:
                    temp=dizi[j]
                    dizi[j]=dizi[j+1]
                    dizi[j+1]=temp
        dosya = open("ortalama.txt", "w")
        for x in range(len(dizi)):
            dosya.write(dizi[x][0] + "\t" + dizi[x][1] + "\t" + str(dizi[x][2]) + "\t" + str(dizi[x][3]) + "\t" + str(dizi[x][4]).replace("\n", "") + "\t" + str(dizi[x][5]) + "\t" +"\n")
        dosya.close()
    #YAPILAN SEÇİM DOGRU OLANA KADAR KULLANICADAN SEÇİM ALINIYOR
    while 1==1:
        #SEÇİM E GÖRE KÜÇÜKTEN BÜYÜGE VEYA BÜYÜKTEN KÜÇÜGE FONSİYONLAR ÇAGIRILIYOR
        islem=int(input("Kücükten-Büyüge siralama -> (1)\nBüyükten-Kücüge siralama -> (2)"))
        if islem==1:
            k_b()
            print("\nKÜCÜKTEN BÜYÜGE SİRALAMA YAPILDI!!!\n")
            break
        elif islem == 2:
            b_k()
            print("\nBÜYÜKTEN KÜÇÜG SIRALAMA YAPILDI\n")
            break
        else:
            print("\n!!!YANLIS İSLEM SECTİNİZ LÜTFEN DOGRU İSLEM SECİNİZ!!!\n")

#MENÜ İŞLEMLERİNİN OLDUGU BÖLÜM
secim=0
#ÇIKIŞ YAPLIANA KADAR MENÜ TEKRAR TAKRAR GÖSTERİLİYOR
while secim != 7:
    print("\t\t\t<<<   MENÜ   >>>")
    print("\tYAPMAK İSTEDİGİNİZ İŞLEMİ SEÇİNİZ!")
    print("[1]<=>KAYIT EKLEMEK\n[2]<=>KAYIT SİL\n[3]<=>KAYIT GÜNCELLE\n[4]<=>ORTLAMAYA GÖRE GEÇTİ-KALDI HESAPLA\n[5]<=>ORTALAMAYA GÖRE SİRALA\n[6]<=>KAYIT LİSTELE\n[7]<=>!!!ÇIKIŞ!!!")
    print("\t\t\t<<<---------->>>")

    secim= int(input("1-7 ARASINDA SEÇİM YAPINIZ -> "))

    if secim>=1 and secim<=7:
        if secim==1:
            ekle()
        elif secim == 2:
            sil()
        elif secim == 3:
            guncelle()
        elif secim== 4:
            ortalama_hesapla()
        elif secim == 5:
            siralama()
        elif secim == 6:
            listele()
        else:
            print("\nÇIKIŞ YAPILDI!\n")
            secim=6

    else:
        print("\n1-7 ARASINDA SEÇİM YAPINIZ -> ")