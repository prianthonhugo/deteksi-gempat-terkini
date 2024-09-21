"""
Aplikasi deteksi gempa terkini
Modularisasi dengan function
Modularisasi dengan package
"""
import gempaterkini
from gempaterkini import ekstraksi_data, tampilkan_data

if __name__ == '__main__':
    print(f'Aplikasi utama menggunakan package yang memiliki deskripsi {gempaterkini.description}')
    result = ekstraksi_data()
    tampilkan_data(result)
