import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def reverse_data(data):
  if len(data) <= 5:
    print(data[::-1])
  else:
    print(data)


def main():
  print("Hello World")

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

  # Episode casting tipe data / merubah tipe data
  nilai_int = int(10.5)
  print("Nilai int = ", nilai_int)

  nilai_float = float(10)
  print("Nilai float = ", nilai_float)
  nilai_boolean = bool(0)
  print("Nilai boolean = ", nilai_boolean)

  # Episode input data

  # data yg dimasukkan pasti string
  data = input("Masukan data: ")
  print("data = ", data, ", type = ", type(data))

  # jika kita ingin mengambil int, maka
  angka = int(input("Masukan angka: "))
  print("angka = ", angka, ", type = ", type(angka))

  # jika kita ingin mengambil float, maka
  angkafloat = float(input("Masukan angka float : "))
  print("angka float = ", angkafloat, ", type = ", type(angkafloat))

  # jika kita ingin mengambil boolean, maka
  boolValue = bool(int(input("Masukan boolean : ")))
  print("boolean = ", boolValue, ", type = ", type(boolValue))

  #reverse_data("Hello")


if __name__ == "__main__":
  main()
