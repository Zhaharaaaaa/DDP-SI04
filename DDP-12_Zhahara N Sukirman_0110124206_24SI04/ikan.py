from animal import *

class ikan (animal):
    sisik = " "
    jenis_ikan = " "
    
    def __init__(self, nama, makanan, hidup, berkembang_biak, sisik, jenis_ikan):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.sisik = sisik
        self.jenis_ikan = jenis_ikan
        
    def cetak_ikan (self):
        super().cetak()
        print(f"Hewan ini bersisik {self.sisik}, hewan ini berjenis ikan {self.jenis_ikan}")

print ("--------------- Object Pertama -----------------")     
koki = ikan ("ikan koki", "pelet", "air", "bertelur", "orange dan merah", "air tawar")
koki.cetak_ikan()

print ("--------------- Object Kedua -----------------")
nemo = ikan ("ikan nemo", "plankton", "air", "bertelur", "orange dan putih", "air laut")
nemo.cetak_ikan()