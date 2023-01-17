"""
1 - Klavyeden girilen 5 tane sayıyı bir listeye atarak
    bunların karelerinden 20 çıktığında ortaya çıkan sonuca
    göre sıralayan
    ve listeyi buna göre yazdıran programı yazınız.
"""

listem = list()
for i in range(4):
    sayi = int(input())
    listem.append(sayi)

def Siralayici(sayi):
    return sayi*sayi - 20

listem.sort(key=Siralayici)
print(listem)