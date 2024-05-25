import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def reverse_data(data):
  if len(data) <= 5:
    print(data[::-1])
  else:
    print(data)


def tempCalculator():
  celcius = float(input("Masukan suhu di dalam celcius: "))

  # reamur
  reamur = (4 / 5) * celcius
  print("suhu dalam reamur: ", reamur)

  # farenheit
  fahreinheit = ((9 / 5) * celcius) + 32
  print("suhu dalam fahreinheit: ", fahreinheit)

  # kelvin
  kelvin = celcius + 273
  print("suhu dalam kelvin: ", kelvin)


def episodeVariable():
  # Episode variable (tempat menyimpan data)

  # menaruh / assignment nilai
  a = 10
  x = 5
  panjang = 1000

  print("Nilai a = ", a, "Nilai x = ", x, "Panjang = ", panjang)

  # penamaan
  nilai_y = 15  # dengan menggunakan underscore
  juta10 = 10000000  # dengan menggunakan nilai dibelakang
  nilaiZ = 17.5  # denagan menggunakan camelCase

  # pemanggilan kedua
  print("Nilai a = ", a)
  a = 7
  print("Nilainya sekarang = ", a)

  # assignment indirect
  b = a
  print("Nilai b = ", b)


def episodeTypeData():
  # Episode type data
  # integer / angka satuan yang tidak ada koma
  nilai_int = 10
  print("nilai int = ", nilai_int)

  # float / angka yang ada koma
  nilai_float = 1.5
  print("nilai float = ", nilai_float)

  # string / kumpulan karakter
  nama = "Ahmad"
  print("Nama = ", nama)

  # boolean / True / False
  nilai_boolean = True
  print("Nilai boolean = ", nilai_boolean)

  # complex / bilangan kompleks
  nilai_complex = complex(2, 3)
  print(nilai_complex)

  # tipe data dari bahasa c
  from ctypes import c_double

  data_c_double = c_double(2.5)
  print("Nilai dari data c_double = ", data_c_double)


def episodeCastingTypedata():
  # Episode casting tipe data / merubah tipe data
  nilai_int = int(10.5)
  print("Nilai int = ", nilai_int)

  nilai_float = float(10)
  print("Nilai float = ", nilai_float)
  nilai_boolean = bool(0)
  print("Nilai boolean = ", nilai_boolean)


def episodeInputdata():
  # Episode input data

  # data yg dimasukkan pasti string
  data = input("Masukan data: ")
  print("data = ", data, ", type = ", type(data))

  # jika kita ingin mengambil int, maka
  try:
    angka = int(input("Masukan angka: "))
    print("angka = ", angka, ", type = ", type(angka))
  except ValueError as e:
    print(e)

  # jika kita ingin mengambil float, maka
  try:
    angkafloat = float(input("Masukan angka float : "))
    print("angka float = ", angkafloat, ", type = ", type(angkafloat))
  except ValueError as e:
    print(e)

  # jika kita ingin mengambil boolean, maka
  boolValue = bool(int(input("Masukan boolean : ")))
  print("boolean = ", boolValue, ", type = ", type(boolValue))


def episodeOperasiAritmatika():
  a = 10
  b = 3
  # Penjumlahan
  hasil = a + b
  print("Hasil = ", hasil)

  # Pengurangan
  hasil = a - b
  print("Hasil = ", hasil)

  # Perkalian
  hasil = a * b
  print("Hasil = ", hasil)

  # Pembagian
  hasil = a / b
  print("Hasil Pembagian = ", hasil)

  # Pangkat
  hasil = a**b
  print("Hasil Pangkat = ", hasil)

  # Modulus / sisa bagi
  hasil = a % b
  print("Hasil Modulus = ", hasil)

  # Floor Division / pembagian bulat
  hasil = a // b
  print("Hasil Floor Division = ", hasil)

  # Prioritas Operasi / yang mana di dahulukan
  '''
  Urutan :
    1. ()
    2. pangkat / exponen : **
    3. perkalian / pembagian / modulus / floor division : * / % //
    4. perjumlahan / pengurangan : + -
  '''

  x = 3
  y = 2
  z = 4

  hasil = x**y * z + x / y - y % z // x
  print("Hasil ", x, '**', y, '*', z, '+', x, '/', y, '-', y, '%', z, '//', x,
        " = ", hasil)

  hasil = x**y * (z + x) / y - y % z // x
  print("Hasil ", x, '**', y, '* (', z, '+', x, ') /', y, '-', y, '%', z, '//',
        x, " = ", hasil)

  hasil = x + y * z
  print("Hasil ", x, ' + ', y, ' * ', z, " = ", hasil)

  hasil = (x + y) * z
  print("Hasil (", x, ' + ', y, ') * ', z, " = ", hasil)


def episodeOperasiKomparasi():
  # setiap hasil dari operasi komparasi adalah boolean
  x = 5
  y = 7
  z = 5
  # sama dengan
  hasil = x == y
  print("Hasil x == y = ", hasil)

  # tidak sama dengan
  hasil = x != y
  print("Hasil x != y = ", hasil)

  # lebih besar dari
  hasil = x > y
  print("Hasil x > y = ", hasil)

  # lebih besar sama dengan
  hasil = x >= y
  print("Hasil x >= y = ", hasil)

  # lebih kecil dari
  hasil = x < y
  print("Hasil x < y = ", hasil)

  # lebih kecil sama dengan
  hasil = x <= y
  print("Hasil x <= y = ", hasil)

  # pembanding object identity
  # object identity yang sama
  hasil = x is z
  print("Hasil x is z = ", hasil)
  # cek id di memory
  print("id x = ", id(x))
  print("id z = ", id(z))
  # object identity yang tidak sama
  hasil = x is not y
  print("Hasil x is not y = ", hasil)


def episodeOperasiLogika():
  # not / kebalikan
  hasil = not (True)
  print("Hasil not(True) = ", hasil, "\n")

  # and / jika ada false maka false
  hasil = True and True
  print("Hasil True and True = ", hasil)

  hasil = True and False
  print("Hasil True and False = ", hasil)

  hasil = False and True
  print("Hasil False and True = ", hasil)

  hasil = False and False
  print("Hasil False and False = ", hasil, "\n")

  # or / jika ada true maka true
  hasil = True or True
  print("Hasil True or True = ", hasil)

  hasil = True or False
  print("Hasil True or False = ", hasil)

  hasil = False or True
  print("Hasil False or True = ", hasil)

  hasil = False or False
  print("Hasil False or False = ", hasil, "\n")

  # xor / jika beda maka true
  hasil = True ^ True
  print("Hasil True ^ True = ", hasil)

  hasil = True ^ False
  print("Hasil True ^ False = ", hasil)

  hasil = False ^ True
  print("Hasil False ^ True = ", hasil)

  hasil = False ^ False
  print("Hasil False ^ False = ", hasil, "\n")

  # not xor
  hasil = not (True ^ True)
  print("Hasil not(True ^ True) = ", hasil)


def latihanKomparasiDanLogika():
  # +++++3---------10+++++++
  inputUser = int(
      input(
          "Masukan angka yang bernilai \n kurang dari 3 \n atau lebih besar dari 10 : "
      ))
  # memeriksa apakah angka yang dimasukkan kurang dari 3
  hasilKurangDari = inputUser < 3
  print("Hasil inputUser < 3 = ", hasilKurangDari)

  # memeriksa apakah angka yang dimasukkan lebih besar dari 10
  hasilLebihDari = inputUser > 10
  print("Hasil inputUser > 10 = ", hasilLebihDari)

  # memeriksa apakah angka yang dimasukkan kurang dari 3 atau lebih dari 10
  hasilKurangDariAtauLebihDari = hasilKurangDari or hasilLebihDari
  print("Hasil inputUser < 3 atau > 10 = ", hasilKurangDariAtauLebihDari, "\n")


# -----3++++++10-------
inputUser = int(
    input(
        "Masukan angka yang bernilai \n lebih dari 3 \n dan kurang dari 10 : ")
)

# memeriksa apakah angka yang dimasukkan lebih dari 3
hasilLebihDari = inputUser > 3
print("Hasil inputUser > 3 = ", hasilLebihDari)

# memeriksa apakah angka yang dimasukkan kurang dari 10
hasilKurangDari = inputUser < 10
print("Hasil inputUser < 10 = ", hasilKurangDari)

# memeriksa apakah angka yang dimasukkan lebih dari 3 dan kurang dari 10
hasilLebihDariDanKurangDari = hasilLebihDari and hasilKurangDari
print("Hasil inputUser > 3 dan < 10 = ", hasilLebihDariDanKurangDari, "\n")

# ----- 0 +++++ 5 ------- 8 ++++++ 11 ------

inputUser = int(
    input(
        "Masukan angka yang bernilai \n lebih dari 0 dan kurang dari 5 atau lebih dari 8 dan kurang dari 11 : "
    ))

# memeriksa apakah angka yang dimasukkan lebih dari 0 dan kurang dari 5
hasilLebihDari0 = inputUser > 0 and inputUser < 5
print("Hasil inputUser > 0 dan < 5 = ", hasilLebihDari0)
# memeriksa apakah angka yang dimasukkan lebih dari 8 dan kurang dari 11
hasilLebihDari8 = inputUser > 8 and inputUser < 11
print("Hasil inputUser > 8 dan < 11 = ", hasilLebihDari8)

# memeriksa apakah angka yang dimasukkan lebih dari 0 dan kurang dari 5 atau lebih dari 8 dan kurang dari 11
hasil = hasilLebihDari0 or hasilLebihDari8
print("Hasil inputUser > 0 dan < 5 atau > 8 dan < 11 = ", hasil, "\n")

# +++++ 0 ----- 5 +++++++ 8 ------ 11 ++++++
inputUser = int(
    input(
        "Masukan angka yang bernilai \n kurang dari 0 atau lebih dari 5 dan kurang dari 8 atau lebih dari 11 : "
    ))
# memeriksa apakah angka yang dimasukkan kurang dari 0
hasilKurangDari0 = inputUser < 0
print("Hasil inputUser < 0 = ", hasilKurangDari0)
# memeriksa apakah angka yang dimasukkan lebih dari 5 and kurang dari 8
hasilLebihDari5 = inputUser > 5 and inputUser < 8
print("Hasil inputUser > 5 dan < 8 = ", hasilLebihDari5)
# memeriksa apakah angka yang dimasukkan lebih dari 11
hasilLebihDari11 = inputUser > 11
print("Hasil inputUser > 11 = ", hasilLebihDari11)
# hasilnya
hasil = hasilKurangDari0 or hasilLebihDari5 or hasilLebihDari11
print("Hasil inputUser < 0 atau > 5 dan < 8 atau > 11 = ", hasil, "\n")

# memeriksa apakah angka yang dimasukkan lebih dari 0 dan kurang dari 5
hasilLebihDari0 = inputUser > 0 and inputUser < 5
print("Hasil inputUser > 0 dan < 5 = ", hasilLebihDari0)
# memeriksa apakah angka yang dimasukkan lebih dari 8 dan kurang dari 11
hasilLebihDari8 = inputUser > 8 and inputUser < 11
print("Hasil inputUser > 8 dan < 11 = ", hasilLebihDari8)

# memeriksa apakah angka yang dimasukkan lebih dari 0 dan kurang dari 5 atau lebih dari 8 dan kurang dari 11
hasil = hasilLebihDari0 or hasilLebihDari8
print("Hasil inputUser > 0 dan < 5 atau > 8 dan < 11 = ", hasil, "\n")


def main():
  # print("Hello World")
  #print("\nEpisode Variable --> \n")
  #episodeVariable()

  #print("\nEpisode Type Data --> \n")
  #episodeTypeData()

  #print("\nEpisode Casting Typedata --> \n")
  #episodeCastingTypedata()

  #print("\nEpisode Input Data --> \n")
  #episodeInputdata()

  #print("\nEpisode Operasi Aritmatika --> \n")
  #episodeOperasiAritmatika()

  #print("\nEpisode latihan konversi satuan temperature --> \n")
  #tempCalculator()

  #print("\nEpisode Operasi Komparasi --> \n")
  #episodeOperasiKomparasi()

  #print("\nEpisode Operasi Logika --> \n")
  #episodeOperasiLogika()

  print("\nEpisode Latihan logika dan komparasi --> \n")
  latihanKomparasiDanLogika()


#reverse_data("Hello")

if __name__ == "__main__":
  main()
