class kendaraan: # Parent Class / Super Class
    def __init__(self, plat_nomor, merek, waktu_masuk, jenis):
        self.__plat_nomor = plat_nomor
        self.__merek = merek
        self.__waktu_masuk = waktu_masuk
        self.__jenis = jenis

    def tarif(self, durasi): # Base method for Polymorphism
        return 0

    @property # Implementing Encapsulation (Getter)
    def plat_nomor(self):
        return self.__plat_nomor
        
    @property
    def waktu_masuk(self):
        return self.__waktu_masuk
        
    @property
    def jenis(self):
        return self.__jenis
    
    @property
    def merek(self):
        return self.__merek
        
class motor(kendaraan): # Child Class (Inheritance)
    def __init__(self, plat_nomor, merek, waktu_masuk, jenis, cc):
        super().__init__(plat_nomor, merek, waktu_masuk, jenis)
        self.__cc = cc

    def tarif(self, durasi): # Overriding method (Polymorphism)
        return durasi * 2000 # Hourly rate

    @property 
    def cc(self):
        return self.__cc

class mobil(kendaraan): # Child Class (Inheritance)
    def __init__(self, plat_nomor, merek, waktu_masuk, jenis, tipe):
        super().__init__(plat_nomor, merek, waktu_masuk, jenis)
        self.__tipe = tipe

    def tarif(self, durasi): # Overriding method (Polymorphism)
        return durasi * 5000 # Hourly rate

    @property
    def tipe(self):
        return self.__tipe

class tempat_parkir: # Class to manage parking system
    def __init__(self, nama, kapasitas):
        self.__nama = nama
        self.__kapasitas = kapasitas
        self.__tampungan = []

    @property
    def nama(self):
        return self.__nama

    def header_project(self):
        print("=" * 50)    
        print(f"\t--🚦 welcome to the {self.nama} parking 🚦--\n".upper())

    def masuk_kendaraan(self, obj):
        print(f"[*] Processing {obj.jenis}: {obj.merek} [{obj.plat_nomor}] [*]")

        if len(self.__tampungan) < self.__kapasitas: # Check current capacity in the list
            self.__tampungan.append(obj)
            print(f"✅ Success.. {obj.jenis.capitalize()}: {obj.merek} is ready to enter {self.nama}\n")
    
        else:
            print(f"❌ Failed.. Sorry, {self.nama} parking is full!.".upper())

    def keluar(self, obj, durasi):
        print("\n" + "=" * 50)  
        print(f"\t--🎫 {self.nama.upper()} PARKING TICKET 🎫--\n")

        if obj in self.__tampungan: # Verify if the object exists in the list
            total = obj.tarif(durasi)

            print(f"""
                Type    : {obj.jenis}
                Brand   : {obj.merek}
                Plate   : {obj.plat_nomor}
                Duration: {durasi} Hours
                Total   : Rp. {total}
                  """)

            self.__tampungan.remove(obj) # Remove vehicle object after exiting
            print(f"\t----- drive safely -----".upper())

        else:
            print(f"⚠️  Vehicle {obj.plat_nomor} not found in the system!\n")

    def tampilkan(self): # Check parking status
        print("\n" + "=" * 50)  
        print(f"\t 📊 {self.nama.upper()} PARKING STATUS 📊\n")

        if not self.__tampungan:
            print(f"\t 🍃 The parking lot is currently empty.")
        
        else:
            for i, obj in enumerate(self.__tampungan, 1):
                print(f"\t{i}. {obj.jenis.capitalize()} - {obj.plat_nomor} ({obj.merek}) 🚘")

# --- Object Instantiation and Execution ---
parkir = tempat_parkir("rusdi", 3)
suzuki = motor("L 00 P", "Mio", "13.30", "motor", 80)
toyota = mobil("B 155 A", "Alphard", "13.12", "mobil", "suv")
yamaha = mobil("B 113 RO", "Mazda", "23.22", "mobil", "sedan")
honda = mobil("G 000 NG", "X-Pander", "11.11", "mobil", "sedan")

parkir.header_project()

parkir.masuk_kendaraan(toyota)
parkir.masuk_kendaraan(honda)
parkir.masuk_kendaraan(yamaha)
parkir.masuk_kendaraan(suzuki)

parkir.keluar(toyota, 2)

parkir.tampilkan()