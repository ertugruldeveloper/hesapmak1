# hesapmak1

print("\nSürüm  kontrolü yapıldı, 3.X sürümü kullanılıyor\n")

karşılama = open("karşılama.txt","r")
print("\n",karşılama.read())
karşılama.close()


def kimlik():
    #KİMLİK FONKSİYONU
    print("1.) Merhabalar Yeni Kullanıcı Detaylı Kimlik Kartını Oluşturmak\n\
    ister misin?  Evet için 'E', Hayır için 'H' Olarak Cevap veriniz.")
    
    cevap = input("Cevap :")
    # BURADA LOWER() VE UPPER() İLE GİRİLEN VERİYİ BÜYÜK HARF KÜÇÜK HARF KONTROLÜNÜ SAĞLADIK
    cevap = cevap.lower().upper()
    
    if cevap == "EVET":
    # kimlik fonk başladı
        try: 
            # Hata kontrolü başladı
            ad = input("\nAD :")
            ad = ad.lower().upper()
            #-------------------------------------------------------------
            soyad = input("SOYAD :")
            soyad = soyad.lower().upper()
            #-------------------------------------------------------------
            tc = input("TC :")
            doğum = int(input("DOĞUM YIL :"))
            #-------------------------------------------------------------
            ana_ad = input("ANA ADI :")
            ana_ad = ana_ad.lower().upper()
            #-------------------------------------------------------------
            baba_ad = input("BABA ADI :")
            baba_ad = baba_ad.lower().upper()
            #-------------------------------------------------------------
            memleket = input("MEMLEKET :")
            memleket = memleket.lower().upper()
            #-------------------------------------------------------------
            doğum_yer = input("DOĞUM YERİ :")
            doğum_yer = doğum_yer.lower().upper()
    
            print(
"""
 |-------------------------------------------------|
 |              | KİMLİK BİLGİSİ |                 |
 |-------------------------------------------------|
 |                                                 |
 |   TC       = {}                
 |                                                 |
 |                                                 |
 |                                                 |
 |   AD                    = {}   
 |   SOYAD                 = {}   
 |   DOĞUM TARİH           = {}   
 |   ANA AD                = {}   
 |   BABA                  = {}   
 |   MEMLEKET              = {}   
 |   DOĞUM YER             = {}   
 --------------------------------------------------
 \n""".format(tc,ad,soyad,doğum,ana_ad,baba_ad,memleket,doğum_yer))
    
        except (ValueError,ZeroDivisionError):
            hata1 = "Girdiyi kontrol ediniz. Rakam veya özel kaakter kullanımına dikkat ediniz"
            çiz = (len(hata1)*"-")
            print(çiz,"\n",hata1,"\n",çiz,sep="")
    
        except:
            hata = "Nedeni bilinmeyen bir hata oluştu..."
            çiz = (len(hata)*"-")
            print(çiz,"\n",hata,"\n",çiz,sep="")
        
    # kimlik fonk bitti
    else:
        print("Kimlik aşaması atlandı...\n",("-"*50),sep="")
        exit
#-------------------------------------------------------------------------------------                   
def kayıtlı_kullanıcı():
#------------------------------------------------------------------------------------- 
    try:
        kaydet = open("kaydet.txt","w")
        ad = input("Kullanıcı AD :")
        ad = ad.lower().upper()
        kaydet.write(ad)
        parola = input("Parola :")
        kaydet.write("  ")
        kaydet.write(parola)
        havuz = "ALI","VELI","AHMET","CENGİZ","ŞEKER"
         
        if ad in havuz and len(parola) in range(3,8):
            tanım = open("tanım.txt","r")
            print("\nGiriş başarılı bir şekilde sağlandı...{}\n".format(ad),tanım.read())
            tanım.close() 
        elif ad not in havuz or len(parola) not in range(3,8):
            yeni_kullanıcı()
        else:
            exit

    except(ValueError,ZeroDivisionError):
        hata1="Hata oluştu, ya sayı girmediniz yada 2. rakamı '0' girdiniz."
        print(("-"*len(hata1)),"\n",hata1,"\n",("-"*len(hata1)),sep="")
    except:
        hata2="Beklenmeyen bir hata oluştu."
        print(("-"*len(hata2)),"\n",hata2,"\n",("-"*len(hata2)),sep="")
#-------------------------------------------------------------------------------------       
def yeni_kullanıcı():
    try:
        
        kaydet = open("kaydet.txt","w")
        print("Yeni Kulanıcı Kayıt Ekranına Hoş Geldin...\n")
        
        ad = input("Kullanıcı AD :")
        ad = ad.lower().ad.upper()
        kaydet.write(ad)
        e_posta = input("E-posta :")
        e_posta = e_posta.lower().upper()
        kaydet.write(e_posta)
        kaydet.write("  ")
        parola = input("Parola :")
        kaydet.write("  ")
        kaydet.write(parola)
        havuz = ad
        kaydet.close()
 
        if ad in havuz and len(parola) in range(3,8):
            tanım = open("tanım.txt","r")
            print("Giriş başarılı bir şekilde sağlandı...{}".format(ad),tanım.read())
            tanım.close()
        else:
            print("Hatallı Giriş")
            exit

    except(ValueError,ZeroDivisionError):
        hata1="Hata oluştu, ya sayı girmediniz yada 2. rakamı '0' girdiniz."
        print(("-"*len(hata1)),"\n",hata1,"\n",("-"*len(hata1)),sep="")
    except:
        hata2="Beklenmeyen bir hata oluştu."
        print(("-"*len(hata2)),"\n",hata2,"\n",("-"*len(hata2)),sep="")
#-------------------------------------------------------------------------------------  
def dos_uzantı_sıralama():
    try:
        print("2.) Merhabalar, dosya uzantısına göre sıralanacak ögeleriniz var\n\
        bu sıralamayı yapmak için Evet için 'E', Hayır için 'h' basınız...\n")
    
        girdi = input("Cevanınız nedir ? = ")
        girdi = girdi.lower().upper()
    
        if girdi == "E":     
            dosyalar =open("dosyalar.txt","r")
            liste = dosyalar.read()
            liste = liste.split()

            print("\n\n'dosyalar.txt' içerisinde en çok tekrar eden uzantılı\n\
            karakter dizilerini istedik...")
            for i in liste:
                if i.endswith(".com"):
                    print(("-"*15),i,sep="\n")
            print("\n")
            dosyalar.close()
        else:
            print("Dosya uzantısı sıralama uygulamasındna çıkıldı...\n",("-"*30),sep="")
            exit
    except(ValueError,ZeroDivisionError):
        hata ="Hata oluştu, harf veya 2. sayıyı '0' olarak girdiniz , lütfen kontrol ediniz"
        print((len(hata)*"-"),"\n",hata,"\n",(len(hata)*"-"),sep="")
    except:
        hata ="Bir hata oluştu üzgünüm"
        print((len(hata)*"-"),"\n",hata,"\n",(len(hata)*"-"),sep="")
#-------------------------------------------------------------------------------------         
def dos_baslangıc_sıralama():
    try:
        print("3.) Merhabalar, dosya uzantısına göre sıralanacak ögeleriniz var\n\
        bu sıralamayı yapmak için Evet için 'E', Hayır için 'h' basınız...\n")
        girdi = input("Cevanınız nedir ? = ")
        girdi = girdi.lower().upper()
        if girdi =="E":
            dosyalar = open("dosyalar.txt","r")
            liste = dosyalar.read()
            liste = liste.split()
            print("\nDosyaları ilk harfine göre sıralama yapıyoruz\n")
            for i in liste:
                if i.startswith("d"):
                    print(("-"*15),i,sep="\n")
            print("\n")
            dosyalar.close()
        else:
            print("Dosyanın ilk harfine göre sıralama uygulamasıdnan çıkıldı...\n",("-"*30),sep="")
            exit
    except(ValueError,ZeroDivisionError):    
        hata ="Hata oluştu, harf veya 2. sayıyı '0' olarak girdiniz , lütfen kontrol ediniz"
        print((len(hata)*"-"),"\n",hata,"\n",(len(hata)*"-"),sep="")
    except:
        hata ="Bir hata oluştu üzgünüm"
        print((len(hata)*"-"),"\n",hata,"\n",(len(hata)*"-"),sep="")
#-------------------------------------------------------------------------------------          
def toplama():
    try:
        bilgi1 = open("toplama.txt","r")
        print("\nAÇIKLAMA METNİ :\n",bilgi1.read(),"\n",sep="")
        sayı1 = int(input("1. sayıyı gir :"))
        sayı2 = int(input("2. sayıyı gir :"))
        print("\n","\t",sayı1,"\n","\t",sayı2,"\n","+","\n",("-"*20),"\n\
        ","\t",(sayı1+sayı2),"\n",sep="",end="\n\n----FİNİŞ----\n\n")
        bilgi1.close
    except(ZeroDivisionError,ValueError):
        hata ="Hata oluştu, harf veya 2. sayıyı '0' olarak girdiniz , lütfen kontrol ediniz"
        print((len(hata)*"-"),"\n",hata,"\n",(len(hata)*"-"),sep="")
    except:
        hata ="Bir hata oluştu üzgünüm"
        print((len(hata)*"-"),"\n",hata,"\n",(len(hata)*"-"),sep="")
#------------------------------------------------------------------------------------- 
def çıkartma():
    try:
        bilgi2 = open("çıkartma.txt","r")
        print("\nÇıkartma işlemine hoşgeldiniz...\n",bilgi2.read(),"\n",sep="")
        sayı1 = int(input("1. sayıyı gir :"))
        sayı2 = int(input("2. sayıyı gir :"))
        print(("-"*50),"\n","\t",sayı1,"\n","\t",sayı2,"\n","-","\n",("-"*20),"\n\
        ","\t",(sayı1-sayı2),"\n",sep="",end="\n\n----FİNİŞ----\n\n")
        bilgi2.close()
    except(ValueError,ZeroDivisionError):
        hata ="Hata oluştu, harf veya 2. sayıyı '0' olarak girdiniz , lütfen kontrol ediniz"
        print((len(hata)*"-"),"\n",hata,"\n",(len(hata)*"-"),sep="")
    except:
        hata ="Bir hata oluştu üzgünüm"
        print((len(hata)*"-"),"\n",hata,"\n",(len(hata)*"-"),sep="")
#------------------------------------------------------------------------------------- 
def çarpma():
    try:
        çarpma = open("çarpma.txt","r")
        print("\nÇarpma işlemine hoşgeldiniz...\n",çarpma.read(),sep="")
        sayı1 = int(input("1. sayıyı gir :"))
        sayı2 = int(input("2. sayıyı gir :"))
        print(("-"*50),"\n","\t",sayı1,"\n","\t",sayı2,"\n","*","\n",("-"*20),"\n\
        ","\t",(sayı1*sayı2),"\n",sep="",end="\n\n----FİNİŞ----\n\n")
        çarpma.close()
    except(ZeroDivisionError,ValueError):
        hata ="Hata oluştu, harf veya 2. sayıyı '0' olarak girdiniz , lütfen kontrol ediniz"
        print((len(hata)*"-"),"\n",hata,"\n",(len(hata)*"-"),sep="")
    except:
        hata ="Bir hata oluştu üzgünüm"
        print((len(hata)*"-"),"\n",hata,"\n",(len(hata)*"-"),sep="")    
def bölme():
    try:
        bölme = open("bölme.txt","r")
        print("\nBölme işlemine hoşgeldiniz...\n",bölme.read(),sep="")
        sayı1 = int(input("1. sayıyı gir :"))
        sayı2 = int(input("2. sayıyı gir :"))
        print(("-"*50),"\n","\t",sayı1,"\n","\t",sayı2,"\n","/","\n",("-"*20),"\n\
        ","\t",(sayı1/sayı2),"\n",sep="",end="\n\n----FİNİŞ----\n\n")
    except(ZeroDivisionError,ValueError):
        hata ="Hata oluştu, harf veya 2. sayıyı '0' olarak girdiniz , lütfen kontrol ediniz"
        print((len(hata)*"-"),"\n",hata,"\n",(len(hata)*"-"),sep="")
    except:
        hata ="Bir hata oluştu üzgünüm"
        print((len(hata)*"-"),"\n",hata,"\n",(len(hata)*"-"),sep="")        
def ü_alan():
    try:
        sayı1=int(input("'a' köşesini gir :"))
        sayı2=int(input("'b' köşesini gir :"))
        print("Sonuç :",(sayı1*sayı2)/2)
    except(ValueError,ZeroDivisionError):
        hata ="Hata oluştu, harf veya 2. sayıyı '0' olarak girdiniz , lütfen kontrol ediniz"
        print((len(hata)*"-"),"\n",hata,"\n",(len(hata)*"-"),sep="")
    except:
        hata ="Bir hata oluştu üzgünüm"
        print((len(hata)*"-"),"\n",hata,"\n",(len(hata)*"-"),sep="")       
#------------------------------------------------------------------------------------- 
def hacim():
    #HACİM FONKSİYONU
    try:
        print ("""Hacim formül = π.r.r.h \n(π=3,14 alırız, r taban yarıçapı, h yükseklik)""")
        sayı_r =int(input("r taban yarıçapı :"))
        sayı_h =int(input("h yükseklik :"))
        sayı_π = 3.14
        sonuç = (sayı_π*sayı_h*pow(sayı_r,2))
        print("'r'taban yarıçap :",str(sayı_r),str(sayı_r),"'h' yükseklik :",sayı_h,sonuç,sep="")
    except(ValueError,ZeroDivisionError):
        hata ="Hata oluştu, harf veya 2. sayıyı '0' olarak girdiniz , lütfen kontrol ediniz"
        print((len(hata)*"-"),"\n",hata,"\n",(len(hata)*"-"),sep="")
    except:
        hata ="Bir hata oluştu üzgünüm"
        print((len(hata)*"-"),"\n",hata,"\n",(len(hata)*"-"),sep="")
    #HACİM FONKSİYONU
def üs_al():
    #KAREE AL FONKSİYONU
    try:
        print("Üs alma işlemine hoş geldiniz...")
        sayı1 = int(input("Sayı gir :"))
        print(sayı1,"  girilen sayısının üssü ",(sayı1*sayı1))
    except(ValueError,ZeroDivisionError):
        hata ="Hata oluştu, harf veya 2. sayıyı '0' olarak girdiniz , lütfen kontrol ediniz"
        print((len(hata)*"-"),"\n",hata,"\n",(len(hata)*"-"),sep="")
    except:
        hata ="Bir hata oluştu üzgünüm"
        print((len(hata)*"-"),"\n",hata,"\n",(len(hata)*"-"),sep="")
    #KAREE AL FONKSİYONU
def yardım():
    #YARDIM FONKSİYONU
    print("Yardım menüsü çalıştı...")
    yardım = input("Yardım alam istediğin işlemi gir :")
    print("\n",help(yardım))
    #YARDIM FONKSİYONU
#------------------------------------------------------------------------------------- 

while True:
    kimlik()
    kayıtlı_kullanıcı()
    girdi = input ("Yapmak istediğiniz işlemi giriniz  :")
    
    # İf bloğu ile girdi değerlendirmesi yapılacak    
    if girdi == "+":
        toplama()
    elif girdi == "-":
        çıkartma()
    elif girdi == "*":
        çarpma()
    elif girdi == "/":
        bölme()
    elif girdi == "a":
        ü_alan()
    elif girdi == "h":
        hacim()
    elif girdi == "k":
        üs_al()
    elif girdi == "y":
        yardım()
    else:
        print("\nProgramdan Tamamen Çıkıldı...")
        exit                
