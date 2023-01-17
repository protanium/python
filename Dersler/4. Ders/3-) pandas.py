import pandas as pd

veri = pd.read_csv("iris.data")

print(veri.head())


print(veri.columns)


print(veri[1:6])



veri = veri.sort_values(by="sepal_length")
print(veri.head())

toplam_veri = veri["sepal_length"].sum()
ortanca_veri = veri["sepal_length"].median()

ortalama_veri = veri["sepal_length"].mean()

print("Sum:", toplamVeri,
      "\nMean:", ortalamaVeri,
      "\nMedian:", ortancaVeri)