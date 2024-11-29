import math

def kubus (sisi):
    hasil = 6 * (sisi * sisi)
    print ("hasil luas kubus dari", 6 , "x", "(" ,sisi, "x",sisi, ")", "=" ,hasil)
    
def balok (p, l, t):
    hasil = 2 * ((p*l) + (p*t) + (l*t))
    print ("hasil luas balok dari",2, "x", "(", "(", p, "x", l, ")", "+","(", p, "x", t, ")","+" ,"(", l, "x", t, ")", ")" ,"=", hasil)
    
def tabung (r, t):
    hasil = 2 * 3.14 * r * (t + r)
    print ("hasil luas tabung dari", 2,"x", 3.14, r ,"x","(" ,t, "+" ,r, ")", "=",hasil)
    
def bola (r):
    hasil = 4 * 3.14 * r * r
    print ("hasil luas bola dari", 4, "x" ,3.14, "x" ,r, "x" ,r, "=", hasil)
    
def kerucut (r, s):
    hasil = 3.14 * r * (s + r)
    print ("hasil luas kerucut dari",3.14, "x", r, "x", "(", s , "+", r , ")",hasil)
    