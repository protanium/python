import csv

baslik = ["ad", "soyad", "yaz"]
veri = [["ahmet", "gültekin", 12], ["sezgin", "gültekin", 26]]

with open('kisiler.csv','w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(baslik)
    writer.writerows(veri)