"""
Aplikasi deteksi gempa terkini
Modularisasi dengan function
Modularisasi dengan package
"""
# from gempaterkini import GempaTerkini
import gempaterkini

if __name__ == '__main__':
    gempa_di_indonesia = gempaterkini.GempaTerkini('https://bmkg.go.id/')
    print(f'Aplikasi utama menggunakan package yang memiliki deskripsi {gempa_di_indonesia.description}')
    gempa_di_indonesia.tampilkan_keterangan()
    gempa_di_indonesia.run()
