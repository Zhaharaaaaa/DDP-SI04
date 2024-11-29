print('--------gunakan modul-----------')
import P_hitung
P_hitung.tambah(5,2)
P_hitung.kurang(10,3)
P_hitung.kali(5,6)

print('\n--gunakan modul yg ada dgn alias--')
import P_hitung as hitung
hitung.bagi(20,2)
hitung.pangkat(2,3)

print('\n--gunakan modul dgn memanggil sebagian fungsinya--')
from P_hitung import tambah, kurang
tambah (20,30)
kurang (2,3)

print('\n--gunakan modul dgn memanggil seluruh fungsinya--')
from P_hitung import *
tambah (20,30)
kurang (2,3)
kali (5,6)
bagi (20,2)
pangkat (2,3)

print('\n--gunakan modul dgn memanggil sebagian fungsinya dengan alias--')
from P_hitung import tambah as add, kali as x, kurang as m
add (3,7)
x (10,10)
m (10,5)