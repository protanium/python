import sqlite3

baglanti = sqlite3.connect("veriler.vt")

cursor=baglanti.cursor()


cursor.execute("CREATE TABLE IF NOT EXISTS kitap "
               "(id INTEGER NOT NULL PRIMARY KEY,"
               "isim TEXT, yazar TEXT, yayin_evi TEXT, "
               "sayfa_sayisi INT)")
baglanti.commit()

baglanti.close()

