"""
Aplikasi deteksi gempa terkini
Modularisasi dengan function
"""


def ekstraksi_data():
    """
    Tanggal: 17 September 2024
    Waktu: 08:15:21 WIB
    Magnitudo: 3.0
    Kedalaman: 8 km
    Lokasi: LS=7.27 BT=109.66
    Pusat Gempa: Pusat gempa berada di darat 16 Km BaratLaut BANJARNEGARA
    Dirasakan: Dirasakan (Skala MMI): II Banjarnegara
    :return:
    """
    hasil = dict()
    hasil['tanggal'] = '17 September 2024'
    hasil['waktu'] = '08:15:21 WIB'
    hasil['magnitudo'] = 3.0
    hasil['kedalaman'] = '8 km'
    hasil['lokasi'] = {'ls': 7.27, 'bt': 109.66}
    hasil['pusat'] = 'Pusat gempa berada di darat 16 Km BaratLaut BANJARNEGARA'
    hasil['dirasakan'] = 'Dirasakan (Skala MMI): II Banjarnegara'

    return hasil


def tampilkan_data(result):
    print('Gempa terakhir berdasarkan BMKG')
    print(f"Tanggal: {result['tanggal']}")
    print(f"Waktu: {result['waktu']}")
    print(f"Magnitudo: {result['magnitudo']}")
    print(f"Kedalaman: {result['kedalaman']}")
    print(f"Lokasi: LS={result['lokasi']['ls']}, BT={result['lokasi']['bt']}")
    print(f"Pusat: {result['pusat']}")
    print(f"Dirasakan: {result['dirasakan']}")


if __name__ == '__main__':
    print('Aplikasi utama')
    result = ekstraksi_data()
    tampilkan_data(result)
