def ToplaHepsini(*sayilar):
    toplam=0
    for item in sayilar:
        toplam += item
    return toplam


print(ToplaHepsini(1,2,3))
