import math

def persegi (sisi):
    luas = sisi * sisi
    print ("hasil luas persegi dari", sisi, "x", sisi, "=" ,luas)
    
def persegi_panjang (panjang, lebar):
    hasil = panjang * lebar
    print ("hasil luas persegi panjang dari", panjang, "x", lebar, "=" ,hasil)
       
def segitiga (alas, tinggi):
    hasil = 0.5 * alas * tinggi
    print ("hasil luas segitiga dari", 0.5, "x" , alas, "x", tinggi, "=" ,hasil)   
    
def jajar_genjang (alas, tinggi):
    hasil = alas * tinggi
    print ("hasil luas jajar genjang dari", alas, "x", tinggi, "=" ,hasil)
    
def layang_layang (d1, d2):
    hasil = 0.5 * d1 * d2
    print ("hasil luas layang-layang dari", 0.5,"x",d1, "x", d2, "=" ,hasil)
    