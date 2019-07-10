""""
Sayıları tek ve çift olarak gösterme
"""

liste = [33,45,48,67,64,22]

for eleman in liste:
    if eleman % 2 == 0:
        print("{} çift sayıdır".format(eleman))
    else :
        print("{} tek sayıdır".format(eleman))
        
