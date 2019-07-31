print ("****************** Programlama Örnekleri ********************")

print ("""
Programlar

1- Mükemmel Sayı Bulma Programı (bölmeden kalan elde etme)
2- Armstrong Sayısı Bulma Programı (len fonksiyonu)
3- Çarpım Tablosu Programı (range fonksiyonu, print fonksiyonunda yan yana yazdırma)
4- Kullanıcıdan istediği kadar sayı aldırıp en son toplam değer verdiren Program
5- List Comprehension Programı

Programdan 'q' tuşu ile çıkabilirsiniz.

""")
while True:
    secim=(input("Çalıştırmak istediğiniz program kodunu seçin :"))
    print ("""*************************************************************
    
    """)

    if (secim == "q"):
        print("Yine bekleriz....")
        break

    elif (secim == "1"):
        """
        Kullanıcıdan aldığımız bir sayının mükemmel olup olmadığını bulmaya çalışıcaz

        Bir sayının kendi hariç bölenlerinin toplamı kendine eşitse bu sayıya "mükemmel sayı" denir.
        Örnek olarak, 6 mükemmel bir sayıdır. (1 + 2 + 3 = 6)
        """

        print("""------ Mükemmel Sayı Bulma Programı ------
        
        """)
        sayi = int(input("Bir sayı giriniz: "))

        i = 1
        m = 0

        for i in range(1, sayi):

            if sayi % i == 0:
                m = m + i

        if (m == sayi):
            print(sayi, "sayısı mükemmel bir sayıdır.")

        else:
            print(sayi, "sayısı mükemmel bir sayı değildir !!!")

        print("""

                ------Bitti-------
        """)

    elif (secim == "2"):
        """Kullanıcıdan aldığınız bir sayının "Armstrong" sayısı olup olmadığını bulmaya çalışıcaz.
        
        Örnek olarak, Bir sayı eğer 4 basamaklı ise ve 
        oluşturan rakamlardan herbirinin 4. kuvvetinin toplamı
        ( 3 basamaklı sayılar için 3.kuvveti ) 
        o sayıya eşitse bu sayıya "Armstrong" sayısı denir.
        
        Örnek olarak : 1634 = 1^4 + 6^4 + 3^4 + 4^4"""

        print("""------ Armstrong Sayısı Bulma Programı ------

        """)
        sayi = (input("Bir sayı giriniz: "))


        print("Sayı {} basamaklıdır".format(len(sayi)))
        i = 0
        arm = 0

        while len(sayi) > i:

            arm += (int(sayi[i])**4)
            i += 1

        if arm == int(sayi):
            print( "Bu sayı armstrong sayısıdır.")

        else :
            print("Bu sayı armstrong sayısı DEĞİLDİR.")

        print("""

        ------Bitti-------

        """)

    elif (secim == "3"):

        """1'den 10'kadar olan sayılarla ekrana çarpım tablosu bastırmaya çalışın.
        İpucu: İç içe 2 tane for döngüsü kullanın. 
        Aynı zamanda sayıları range() fonksiyonunu kullanarak elde edin."""

        print("""------ Çarpım Tablosu Programı ------

                """)

        for i in range(1, 11):
            for j in range(1,11):
                print(i*j, end= ' | ')
            print()



        print("""

        ------Bitti-------

        """)


    elif (secim == "4"):

        """Her bir while döngüsünde kullanıcıdan bir sayı alın ve 
        kullanıcının girdiği sayıları "toplam" isimli bir değişkene ekleyin. 
        Kullanıcı "q" tuşuna bastığı zaman döngüyü sonlandırın ve 
        ekrana "toplam değişkenini" bastırın."""
        print("""------ Toplam Bulma Programı ------

                """)

        toplam = 0

        while True:

            sayı = input("Sayı:")

            if (sayı == "q"):
                break
            sayı = int(sayı)

            toplam += sayı

        print("Girdiğiniz Sayıların Toplamı:", toplam)


        print("""

        ------Bitti-------

        """)
    elif (secim == "5"):
        """List Comprehension ile 1 den 100 e kadar olan sayılardan çift olanları
        listeye atıp ekrana bastırma
        """
        print("""------ List Comprehension Programı ------
        """)
        liste = [x for x in range(1,101) if x % 2 == 0]
        print(liste)

        print("""

        ------Bitti-------

        """)
        
    else:
        print("Lütfen geçerli bir işlem giriniz.")
