class gempa:
    #Variabel
    lokasi = " "
    skala = " "
    GEMPA = "GEMPA YANG TERJADI DI"
    
    #konstruktor
    def __init__(self, lokasi, skala):
        self.lokasi = lokasi
        self.skala = skala
    
    #methood penentu skala gempa
    def dampak(self):
        if self.skala < 2 :
            print ("Gempa tidak berasa")
        elif 2 <= self.skala <= 4 :
            print ("Gempa berdampak bangunan retak-retak")
        elif 4 <= self.skala <= 6 :
            print ("Gempa berdampak bangunan roboh")
        elif self.skala > 6 :
            print ("Gempa berdampak bangunan roboh dan berpontensi tsunami")
        else :
            print ("data tidak tersedia")
        
        #menampilkan lokasi dan skala
        print (self.GEMPA)
        print (f"Lokasi Gempa : {self.lokasi}")
        print (f"Skala Gempa : {self.skala}")
        