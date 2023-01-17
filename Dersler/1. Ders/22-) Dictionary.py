sozluk = {
    "ad":"ahmet",
    "soyad": "güngördü",
    "yas":10
}

print(sozluk)
print(sozluk.keys())
print(sozluk.values())

print(sozluk["ad"])
sozluk["ad"] = "sezgin"

for item in sozluk.keys():
    print(item)