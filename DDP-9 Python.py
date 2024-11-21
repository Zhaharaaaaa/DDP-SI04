#Buatlah sebuah fungsi bernama celcius_ke_fahrenheit yang menerima satu argumen: suhu dalam celcius. Fungsi ini harus mengembalikan suhu yang dikonversi ke Fahrenheit
def celcius_ke_fahrenheit(celcius):
    print ( (9/5 * celcius) + 32 )
    
celcius_ke_fahrenheit(0)
celcius_ke_fahrenheit(100)

#Buatlah sebuah fungsi bernama is_genap yang menerima satu argumen: bilangan bulat. Fungsi ini harus mengembalikan True jika bilangan tersebut genap, dan False jika bilangan tersebut ganjil.
def is_genap(bilangan_bulat):
    print ( bilangan_bulat % 2 == 0 )
    
is_genap(4)
is_genap(7)

#Buatlah fungsi untuk melihat ketrangan lulus atau tidak lulus : 
def nilai(angka):
    if angka > 60:
        print ("lulus")
    else :
        print ("gagal")

nilai(80)
nilai(60)

#Buatlah fungsi untuk menampilkan bilangan ganjil yang kurang argumens
def bilangan (ganjil):
    for i in range (1, ganjil + 1, 2):
        print (i, end=" ")

bilangan(20)