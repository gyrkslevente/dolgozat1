jelszo="Szivecske<3"
felhasz="bori99"

proba=input("Add meg a felhasználó neved! ")
proba2=input("Add meg a jelszavad! ")

while len(proba) < len(felhasz):
  print("Sikertelen bejelentkezés")
  proba=input("Add meg a felhasználó neved! ")
  proba2=input("Add meg a jelszavad! ")
  while len(proba) > len(felhasz):
    print("Sikertelen bejelentkezés")
    proba=input("Add meg a felhasználó neved! ")
    proba2=input("Add meg a jelszavad! ")
    while len(proba2) <  len(jelszo):
      print("Sikertelen bejelentkezés")
      proba=input("Add meg a felhasználó neved! ")
      proba2=input("Add meg a jelszavad! ")
      while len(proba2) <  len(jelszo):
        print("Sikertelen bejelentkezés")
        proba=input("Add meg a felhasználó neved! ")
        proba2=input("Add meg a jelszavad! ")
if proba==felhasz and jelszo==proba2:
  print("Sikeres bejelentkezés")