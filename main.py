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
          "Masukan angka yang bernilai \n lebih dari 3 \n dan kurang dari 10 : "
      ))

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


def episodeOperatorBitwise():
  # Operator Bitwise adalah operator yang digunakan untuk melakukan operasi pada bit / binary digit
  # contoh :
  # 00000011 -> 2**1 + 2**0 = 3
  # 00000101 -> 2**2 + 2**0 = 5

  # 00000111 -> 2**2 + 2**1 + 2**0 = 7  Klo OR
  # 00000001 -> 2**0 = 1 klo AND
  # 00000110 -> 2**2 + 2**1 = 6 klo XOR
  a = 3
  b = 5
  print(format(a, '08b'))
  print(format(b, '08b'))

  print("a & b : ", a & b)
  print("a | b : ", a | b)
  print("a ^ b : ", a ^ b)
  c = ~a
  print("nilai a : ", a, " binary : ", format(a, '08b'))
  print("nilai ~a : ", c, " binary : ", format(c, '08b'))

  #shifting / geser
  #geser ke kanan (>>)
  c = a >> 2
  print("nilai a : ", a, " binary : ", format(a, '08b'))
  print("nilai c : ", c, " binary : ", format(c, '08b'))

  #geser ke kiri (<<)
  c = a << 2
  print("nilai a : ", a, " binary : ", format(a, '08b'))
  print("nilai c : ", c, " binary : ", format(c, '08b'))


def episodeOperatorAssignment():
  # operasi yg dapat dilakukan dengan penyingkatan
  # operasi ditambah dengan assignment
  a = 5  # adalah assignment
  print("Nilai a = ", a)

  a += 1  # adalah a = a + 1
  print("Nilai a += 1 : ", a)

  a -= 2  # adalah a = a - 2
  print("Nilai a -= 2 : ", a)

  a *= 5  # adalah a = a * 5
  print("Nilai a *= 5 : ", a)

  a /= 2  # adalah a = a / 2
  print("Nilai a /= 2 : ", a)

  b = a
  b %= 3  # adalah b = b % 3
  print("Nilai b %= 3 : ", b)

  b = a
  b //= 3  # adalah b = b // 3
  print("Nilai b //= 3 : ", b)

  b = 5
  b **= 3  # adalah b = b ** 3
  print("Nilai b **= 3 : ", b)

  # operasi bitwise
  c = True
  print("Nilai c : ", c)

  # AND
  c &= False  # adalah c = c & False
  print("c &= False : ", c)

  # OR
  c = True
  c != False  # adalah c = c ! False
  print("c != False : ", c)

  # XOR
  c = True
  c ^= False  # adalah c = c ^ False
  print("c ^= False : ", c)

  c = 0b0100
  print("Nilai c : ", format(c, '04b'))
  c >>= 2
  print("Nilai c >>= 2 : ", format(c, '04b'))
  c <<= 1
  print("Nilai c <<= 1 : ", format(c, '04b'))


def episodePengenalanString():
  data = "ini adalah string"
  print(data)
  print(type(data))

  # 1. cara membuat string

  # dengan menggunakan petik satu
  print('menggunakan single quote')

  # dengan menggunakan petik dua
  print("menggunakan double quote")

  # menggabungkan " dan '
  print('"Halo, apa kabar?"')
  print("'Halo, apa kabar?'")
  print("ini adalah hari jum'at")

  # dengan menggunakan tanda \
  print('mari shalat jum\'at')
  print('g\'day, isn\'t it ?')

  # backslash
  print("C:\\user\\Ucup")

  # tab
  print("ucup\t\totong, semakin jauhan")

  # backspace
  print("ucup \botong, jadi deketan")

  # newline
  print("baris pertama.\nbaris kedua.")  # LF -> line feed
  print("baris pertama.\rbaris kedua.")  # CR -> carriage return
  print("baris pertama.\r\nbaris kedua.")  # CRLF -> line feed carriage return

  # raw string
  print(r"C:\new folder")  # raw string

  # dengan menggunakan petik tiga / literal string
  print('''
  menggunakan petik tiga
  Nama : Ucup
  Kelas : 3 SD
  ''')
  # multiline literal string dan Raw
  print(r'''
  menggunakan petik tiga dan raw
  Nama : Ucup
  Kelas : 3 SD
  Website : www.ucup.com/newID
  ''')


def episodeOperasidanManipulasiString():
  # menghitung panjang string
  data = "Ini Adalah String"
  print("panjang string : ", len(data))

  # mengambil substring
  print("data[0:5] : ", data[0:5])
  print("data[:5] : ", data[:5])
  print("data[5:] : ", data[5:])
  print("data[:] : ", data[:])
  print("data[1] : ", data[1])
  print("data[-1] : ", data[-1])
  print("data[3:7] : ", data[3:7])
  print("data[0:len(data):2] : ", data[0:len(data):2])
  print("reversing data : ", data[::-1])

  # mengubah string menjadi huruf besar
  print("data.upper() : ", data.upper())

  # mengubah string menjadi huruf kecil
  print("data.lower() : ", data.lower())

  # mengganti string
  print("data.replace('a', 'b') : ", data.replace('a', 'b'))

  # menggabungkan string
  print("data + ' ini adalah string' : ", data + ' ini adalah string')

  # menggecek apakah ada karakter di string
  print("data.find('a') : ", data.find('a'))
  print("d" in data)
  print("d" not in data)

  # mengecek apakah lower case
  print("apakah lower case : ", data.islower())

  # mengecek apakah upper case
  print("apakah upper case : ", data.isupper())

  # mengecek apakah huruf
  print("apakah huruf : ", data.isalpha())

  # mengecek apakah angka
  print("apakah angka : ", data.isdigit())

  # mengecek apakah huruf dan angka
  print("apakah huruf dan angka : ", data.isalnum())

  # mengecek spasi, tab and newline
  print("apakah spasi, tab dan newline : ", data.isspace())

  # mengecek semua kata dimulai dengan huruf besar
  print("apakah semua kata dimulai dengan huruf besar : ", data.istitle())

  # mengecek komponen startswith endwith
  cek_start = "Sangjangnim Oppa".startswith("Sangjangnim")
  print("start = ", str(cek_start))

  cek_end = "Sangjangnim Oppak".startswith("Oppak")
  print("end = ", str(cek_end))

  # mengulang string
  print("data * 3 : ", data * 3)
  print(14 * "wk")

  # item paling kecil
  print("Item paling kecil : ", min(data))

  # item paling besar
  print("Item paling besar : ", max(data))

  # ascii
  print("char untuk ascii 117 adalah ", chr(117))
  print("ascii code untuk char t adalah ", str(ord("t")))

  # count character
  print("count char a : ", data.count("a"))

  # join
  print("join : ", " ".join(data))

  # split
  print("split : ", data.split(" "))

  # rjust, ljust, center
  print("rjust : ", "'" + data.rjust(21) + "'")

  print("ljust : ", "'" + data.ljust(21) + "'")

  print("center : ", "'" + data.center(21, "-") + "'")

  # strip
  print("strip : ", "'" + data.center(21, "-") + "'".strip(" "))


def episodeFormatString():
  # format string
  # format string adalah cara untuk menggabungkan string dengan nilai dari variabel
  # format string menggunakan karakter "{}"
  # format string menggunakan method format()
  # format string menggunakan f-string
  nama = "ucup"
  format_str = f"hello {nama}"
  print(format_str)

  # boolean
  boolean = True
  format_str = f"boolean = {boolean}"
  print(format_str)

  # angka
  angka = 2005.5
  format_str = f"angka = {angka}"
  print(format_str)

  # bilangan bulat
  angka = 15
  format_str = f"bilangan bulat = {angka:d}"
  print(format_str)

  # bilangan ribuan
  angka = 2000
  format_str = f"ribuan = {angka:,}"
  print(format_str)

  # bilangan desimal
  angka = 2005.54321
  format_str = f"desimal = {angka:.2f}"
  print(format_str)

  # menampilkan leading zero
  angka = 2005.54321
  format_str = f"leading zero = {angka:010.3f}"
  print(format_str)

  # menampilkan tanda minus atau pluss
  angka_minus = -10
  angka_plus = 10.1234
  format_minus = f"tanda minus = {angka_minus:-d}"
  format_plus = f"tanda plus = {angka_plus:+.2f}"
  print(format_minus)
  print(format_plus)

  # persen
  angka = 0.045
  format_str = f"persen = {angka:.2%}"
  print(format_str)

  # operasi aritmatika di dalam placeholder
  harga = 10000
  jumlah = 5
  format_str = f"harga = {harga} dan jumlah = {jumlah} maka total = Rp.{harga*jumlah:,.2f}"
  print(format_str)

  # format angka lain (binary, octal, hexadecimal)
  angka = 255
  format_str = f"binary = {bin(angka)}"
  print(format_str)

  format_str = f"octal = {oct(angka)}"
  print(format_str)

  format_str = f"hexadecimal = {hex(angka)}"
  print(format_str)


def main():
  print("Hello World")
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

  #print("\nEpisode Latihan logika dan komparasi --> \n")
  #latihanKomparasiDanLogika()

  #print("\nEpisode Operator Bitwise --> \n")
  #episodeOperatorBitwise()

  #print("\nEpisode Operator Assignment --> \n")
  #episodeOperatorAssignment()

  #print("\nEpisode Pengenalan String --> \n")
  #episodePengenalanString()

  #print("\nEpisode Operasi dan manipulasi String --> \n")
  #episodeOperasidanManipulasiString()
  print("\nEpisode Format String --> \n")


episodeFormatString()

#print("\nNumpy --> \n")
#bn.initNumpy()

#reverse_data("Hello")

if __name__ == "__main__":
  main()
