from animal import *

class ular (animal):
    warna_sisik = " "
    jenis_racun = " "
    
    def __init__(self, nama, makanan, hidup, berkembang_biak, warna_sisik, jenis_racun):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.warna_sisik = warna_sisik
        self.jenis_racun = jenis_racun
        
    def cetak_ular (self):
        super().cetak()
        print(f"Hewan ini bersisik {self.warna_sisik}, hewan ini memiliki racun {self.jenis_racun} ")

print ("--------------- Object Pertama -----------------")     
cobra = ular ("ular cobra", "daging", "darat", "bertelur", "hitam", "berbisa")
cobra.cetak_ular()

print ("--------------- Object Kedua -----------------")
sanca = ular ("ular sanca", "daging", "darat", "bertelur", "coklat dan hitam", "tidak berbisa")
sanca.cetak_ular()