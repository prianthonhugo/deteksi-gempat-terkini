"""
Aplikasi deteksi gempa terkini
Modularisasi dengan function
Modularisasi dengan package
"""
from gempaterkini import ekstraksi_data, tampilkan_data

if __name__ == '__main__':
    print('Aplikasi utama')
    result = ekstraksi_data()
    tampilkan_data(result)
