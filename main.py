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
  reverse_data("Hello")


if __name__ == "__main__":
  main()
