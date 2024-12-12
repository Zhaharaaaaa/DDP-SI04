class animal:
    nama = " "
    makanan = " "
    hidup = " "
    berkembang_biak = " "
    
    def __init__(self, nama, makanan, hidup, berkembang_biak):
        self.nama = nama
        self.makanan = makanan
        self.hidup = hidup
        self.berkembang_biak = berkembang_biak
        
    def cetak (self):
        print(f"Hewan {self.nama} ini memakan {self.makanan}, hewan ini juga hidup di {self.hidup} dan berkembang biak dengan cara {self.berkembang_biak}")
        
# c1= animal ("Buaya", "daging", "amphibi", "bertelur") 
# c1.cetak()
        

        
        