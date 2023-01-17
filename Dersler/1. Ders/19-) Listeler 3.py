meyveler = ["Kivi","Muz","Ejder Meyvesi"]

meyveler.sort(reverse=True)
print(meyveler)

def Fonksiyon(sayi):
    return abs(sayi)

sayiListesi = [-5,-10,1,2]
sayiListesi.sort(key=Fonksiyon)
print(sayiListesi)