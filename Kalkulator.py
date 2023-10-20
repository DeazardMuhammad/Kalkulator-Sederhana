print("")
print("<----- Kalkulator ----->")
print("------------------------")
print("")

print("1. Penjumlahan")
print("2. pengurangan")
print("3. Perkalian")
print("4. Pembagian")
print("------------------------")

#Proses
def penjumlahan(x,y):
    return x+y

def pengurangan(x,y):
    return x-y

def perkalian(x,y):
    return x*y

def pembagian(x,y):
    return x/y

tipe = input("Silahkan masukan nomor yang kalian pilih: ")
print("------------------------")
print("Proses Perhitungan")
print("------------------------")

if tipe in ('1', '2', '3', '4'):
    angka1 = float(input("angka pertama :"))
    angka2 = float(input("angka kedua:"))
    print("------------------------")
    if tipe == '1':
        print("Jawaban Penjumlahan Tersebut adalah adalah :", penjumlahan(angka1, angka2))
    if tipe == '2':
        print("Jawaban Pengurangan Tersebut adalah adalah :", pengurangan(angka1, angka2))
    if tipe == '3':
        print("Jawaban Perkalian Tersebut adalah adalah :", perkalian(angka1, angka2))
    if tipe == '4':
        print("Jawaban Pembagian Tersebut adalah adalah :", pembagian(angka1, angka2))
print("-- Perhitungan Selesai --")
print("")
