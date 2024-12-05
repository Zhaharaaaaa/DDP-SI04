from Gempa import *

# Membuat objek gempa dengan lokasi dan skala
gempa1 = gempa ("Banten", 1.2)
gempa2 = gempa ("Palu", 6.1)
gempa3 = gempa ("Cianjur", 5.6)
gempa4 = gempa ("Jayapura", 3.3)
gempa5 = gempa ("Garut", 4.0)

# Info Gempa
print ("## Info Gempa Bumi ##")
gempa1.dampak()
print ("=============================")
print ("## Info Gempa Bumi ##")
gempa2.dampak()
print ("=============================")
print ("## Info Gempa Bumi ##")
gempa3.dampak()
print ("=============================")
print ("## Info Gempa Bumi ##")
gempa4.dampak()
print ("=============================")
print ("## Info Gempa Bumi ##")
gempa5.dampak()
print ("=============================")