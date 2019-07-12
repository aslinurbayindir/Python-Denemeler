"""
Bu kısımda listeleri birbirine
uzun yol ve kısa yol ile
nasıl aktara biliriz bunu görüyoruz.

"""

liste1 = [1,2,3,4,5]
liste2 = list()  # Boş bir liste oluşturduk.

for i in liste1:
    liste2.append(i)

print(liste2)

liste3 = [5,6,9,7,8,64]

liste4 = [i for i in liste3]
print(liste4)

# İlk bölüm bitti

liste4 = [3,8,7]
liste1 = [i * 2 for i in liste4] # her bir elemanı 2 ile çarpıp o şeklide ekliyor diğer listeye
print("Her elemanı 2 ile çarpıp atama: ",liste1)

# İkinci bölüm bitti

#demet üzerinde gezinme
liste = [(1,2),(3,4),(5,6)]
liste1 = [i*j for i,j in liste]  # her demeti kendi içinde çarpar ve listeye eleman olarak atar

print("her demeti kendi içinde çarpıp tek elemana atama: ",liste1)

# üçüncü kısım sonu

#String üzerinde gezinme

s = "Python"
liste = [i * 3 for i in s] # Her bir elemanı 3 kere tekrar edip listeye atar

print(liste)

print("\n")

#bitti

# Aşağıdaki listeyi tek boyutte ekrana yazdırma

print("******listeyi tek boyuta indirgeme ****** ")
liste = [[1,2,3],[4,5,6,7,8],[9,10,11,12,13,14,15]]
BosYeniListe = list()

print("liste = ",liste)

print("Listenin her elemanını yazdırma : ")  #her bir elemanın kendisi liste
for i in liste:
    print(i)

print("Liste içindeki her bir elemanda gezinme : ")

for i in liste:
    for x in i:
        print(x)
        BosYeniListe.append(x)

print("liste içindeki listeleri tek boyuta indirip yeni listeye atama:")
print("Boş Yeni Liste içindekiler: ",BosYeniListe)

# ---> List Comprehension ile Yazma

liste = [[1,2,3],[4,5,6,7,8],[9,10,11,12,13,14,15]]
liste1 = [x for i in liste for x in i]
print("List Comprehension ile içindekiler: ",liste1)
