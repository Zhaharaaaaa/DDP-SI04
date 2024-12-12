from animal import *

class burung (animal):
    bulu = " "
    bunyi = " "
    
    def __init__(self, nama, makanan, hidup, berkembang_biak, bulu, bunyi):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.bulu = bulu
        self.bunyi = bunyi
        
    def cetak_burung (self):
        super().cetak()
        print(f"Hewan ini berbulu {self.bulu}, hewan ini berbunyi {self.bunyi}")

print ("--------------- Object Pertama -----------------")
Nuri= burung ("Burung Nuri", " biji-bijian", "darat", "bertelur", "hijau dan kuning ", "pitpitpit")
Nuri.cetak_burung()

print ("--------------- Object Kedua -----------------")
Beo= burung ("Burung Beo", " biji-bijian", "darat", "bertelur", "biru dan kuning ", "kamu cantik")
Nuri.cetak_burung()