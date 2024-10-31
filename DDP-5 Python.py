
#Buat variabel list 
list_kendaraan = ["Ferrari 458","Mobil", 4499, "Hitam", "Beroda empat"]
print(list_kendaraan)

list_kendaraan.append("Rp. 2.802.171.159")
print(list_kendaraan)

list_kendaraan.append("Mobil Sport")
print(list_kendaraan)

list_kendaraan.insert(2, "Ferrari")
print(list_kendaraan)


print("____________________________________________________________________")
print("====================================================================")


#Buat program python dengan match case 
# untuk menghitung luas bangun datar :
pilih = int(input("""Selamat datang diaplikasi menghitung
                  1. Untuk menghitung luas persegi
                  2. Untuk menghitung luas lingkaran
                  3. Untuk menghitung luas segitiga 
                  masukan pilihan anda : """))

match pilih:
    case 1 :
        print("Kamu memilih 1 untuk menghitung luas persegi")
        sisi = int(input("masukan sisi persegi : "))
        luas_persegi = sisi * sisi
        print("Hasil luas persegi sisinya", sisi,"adalah",luas_persegi)
    
    case 2 :
        print("kamu memilih 2 untuk menghitung luas lingkaran")
        jari_jari = int(input("masukan jari jari :"))
        luas_lingkaran = 3.14 * jari_jari * jari_jari
        print("Hasil luas lingkaran jari jarinya", jari_jari, "adalah", luas_lingkaran)
    
    case 3 :
        print("kamu memilih 3 untuk menghitung luas segitiga")
        alas = int(input("masukan alas :"))
        tinggi = int(input("masukan tinggi :"))
        luas_segitiga = 0.5 * alas * tinggi
        print("Hasil luas segitiga alas", alas, "dan tinggi", tinggi, "adalah", luas_segitiga)
    
    case _ :
        print("Anda salah pilih")