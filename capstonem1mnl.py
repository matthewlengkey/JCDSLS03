###MATTHEW NICHOLAS LENGKEY###
###INTIAL DATA###

menu=('1. Display Stok',
      '2. Tambah Stok',
      '3. Update Stok',
      '4. Delete Stok',
      '5. Exit Program')
gudang=[{'Kode Barang':'A1','Nama Barang':'Botol Minum','Satuan':'3','Harga Pokok':'50000','Harga Jual':'65000'},
        {'Kode Barang':'A2','Nama Barang':'Botol Kecap','Satuan':'5','Harga Pokok':'13000','Harga Jual':'20000'}
]

###WELCOME###
def welcome():
    print("STOK GUDANG MEMET")
    print("SELAMAT DATANG DI MENU UTAMA")
    print(menu)

###FUNCTIONS###

###DISPLAY FUNCTION###
def tampil():
    print('''
    DISPLAY STOK GUDANG
    1. DISPLAY SEMUA STOK
    2. DISPLAY STOK TERTENTU
    3. KEMBALI KE MENU UTAMA
    ''')
    angkasub=input('Silahkan pilih sub-menu 1-3: ')

    if angkasub=='1':
        if len(gudang)!=0:
            print('Stok Gudang: ')
            for i in range(len(gudang)):
                print('No.{} Kode Barang: {}, Nama Barang: {}, Satuan: {}, Harga Pokok: {}, Harga Jual: {}'.format(i+1, gudang[i]['Kode Barang'], gudang[i]['Nama Barang'], gudang[i]['Satuan'], gudang[i]['Harga Pokok'], gudang[i]['Harga Jual']))
        else:
            print('Stok Gudang Tidak Ada')
        return tampil()

    elif angkasub=='2':
        if len(gudang)!=0:
            kode=input('Masukkan Kode Barang: ').capitalize()
            for i in range(len(gudang)):
                if kode==gudang[i]['Kode Barang']:
                    print('No.{} Kode Barang: {}, Nama Barang: {}, Satuan {}, Harga Pokok: {}, Harga Jual: {}'.format(i+1, gudang[i]['Kode Barang'], gudang[i]['Nama Barang'], gudang[i]['Satuan'], gudang[i]['Harga Pokok'], gudang[i]['Harga Jual']))   
                    break            
            if kode!=gudang[i]['Kode Barang']:       
                print('Stok Tidak Ada')
        else:
            print('Stok Gudang Tidak Ada')
        return tampil()

    elif angkasub=='3':
        return 0

    else:
        print('Salah!')
        return tampil()

def tampilsemua():
    print('Stok Gudang: ')
    for i in range(len(gudang)):
        print('No.{} Kode Barang: {}, Nama Barang: {}, Satuan: {}, Harga Pokok: {}, Harga Jual: {}'.format(i+1, gudang[i]['Kode Barang'], gudang[i]['Nama Barang'], gudang[i]['Satuan'], gudang[i]['Harga Pokok'], gudang[i]['Harga Jual']))
    if len(gudang)==0:
        print('Tidak ada')

# ###ADD FUNCTION###
def tambah():
    print('''
    TAMBAH STOK GUDANG
    1. TAMBAH STOK GUDANG
    2. KEMBALI KE MENU UTAMA
    ''')
    angkasub=input('Silahkan pilih sub-menu 1-2: ')
    if angkasub=='1':
        kode=input('Masukkan Kode Barang: ').capitalize()
        for i in range(len(gudang)):
            if kode==gudang[i]['Kode Barang']:
                print('Maaf Barang Sudah Ada... ')
                return tambah()
        nama=input('Nama Barang: ')
        satuan=input('Satuan Barang? ')
        hpokok=input('Harga Pokok: ')
        hjual=input('Harga Jual: ')
        gudangbaru={'Kode Barang': kode,'Nama Barang': nama,'Satuan': satuan,'Harga Pokok': hpokok,'Harga Jual':hjual}
        confirm=input(f'Apakah anda yakin ingin tambah data ini? \n {gudangbaru} \n Y/N: ')
        if confirm=='y' or confirm=='Y':
            gudang.append(gudangbaru)
            print('Data Sudah Ditambahkan!')
            return tambah()
        elif confirm=='n' or confirm=='N':
            print('Data tidak jadi ditambah!')
            return tambah()
        
    elif angkasub=='2':
        return 0
    else:
        print('Salah!')
        return tambah()

# ###UPDATE FUNCTION###
def perubahan():
    print('''
    UPDATE STOK GUDANG
    1. UPDATE STOK GUDANG
    2. KEMBALI KE MENU UTAMA
    ''')
    angkasub=input('Silahkan pilih sub-menu 1-2: ')
    if angkasub=='1':
        tampilsemua()
        if len(gudang)!=0:
            rubah=input('Masukkan Kode Barang yang Mau di Ubah: ').capitalize()
            for i in range(len(gudang)):
                if rubah==gudang[i]['Kode Barang']:
                    nanyaupdate=input(
            '''Apa yang mau diubah?
        1. Nama Barang
        2. Satuan Barang
        3. Harga Pokok
        4. Harga Jual
        5. Semuanya
        Pilih sub-menu 1-5: ''')
                    if nanyaupdate=='1':
                        nama=input('Nama Barang: ')
                        print(f'Data yang ingin anda update adalah \n {gudang[i]}')
                        confirm=input('Apakah anda yakin ingin update data ini? Y/N: ')
                        if confirm=='y' or confirm=='Y':
                            gudang[i]['Nama Barang'] = nama
                            print('Data berhasil diubah')
                            return perubahan()
                        elif confirm=='n' or confirm=='N':
                            print('Data tidak terupdate')
                            return perubahan()
                            
                    elif nanyaupdate=='2':
                        satuan=input('Satuan Barang: ')
                        print(f'Data yang ingin anda update adalah \n {gudang[i]}')
                        confirm=input('Apakah anda yakin ingin update data ini? Y/N: ')
                        if confirm=='y' or confirm=='Y':
                            gudang[i]['Satuan'] = satuan
                            print('Data berhasil diubah')
                            return perubahan()
                        elif confirm=='n' or confirm=='N':
                            print('Data tidak terupdate')
                            return perubahan()

                    elif nanyaupdate=='3':
                        hpokok=input('Harga Pokok: ')
                        print(f'Data yang ingin anda update adalah \n {gudang[i]}')
                        confirm=input('Apakah anda yakin ingin update data ini? Y/N: ')
                        if confirm=='y' or confirm=='Y':
                            gudang[i]['Harga Pokok'] = hpokok   
                            print('Data berhasil diubah')
                            return perubahan()
                        elif confirm=='n' or confirm=='N':
                            print('Data tidak terupdate')
                            return perubahan()

                    elif nanyaupdate=='4':
                        hjual=input('Harga Jual: ')
                        print(f'Data yang ingin anda update adalah \n {gudang[i]}')
                        confirm=input('Apakah anda yakin ingin update data ini? Y/N: ')
                        if confirm=='y' or confirm=='Y':
                            gudang[i]['Harga Jual'] = hjual
                            print('Data berhasil diubah')
                            return perubahan()
                        elif confirm=='n' or confirm=='N':
                            print('Data tidak terupdate')
                            return perubahan()

                    elif nanyaupdate=='5':
                        nama=input('Nama Barang: ')
                        satuan=input('Satuan Barang? ')
                        hpokok=input('Harga Pokok: ')
                        hjual=input('Harga Jual: ')
                        print(f'Data yang ingin anda update adalah \n {gudang[i]}')
                        confirm=input('Apakah anda yakin ingin update data ini? Y/N: ')
                        if confirm=='y' or confirm=='Y':
                            gudang[i]['Nama Barang'] = nama
                            gudang[i]['Satuan'] = satuan
                            gudang[i]['Harga Pokok'] = hpokok
                            gudang[i]['Harga Jual:'] = hjual
                            print('Data berhasil diubah')
                            return perubahan()
                        elif confirm=='n' or confirm=='N':
                            print('Data tidak terupdate')
                            return perubahan()
                    else:
                        print('Salah nomor, ulang lagi. ')
                        return perubahan()
            return print('Data tidak ada!'), perubahan()
        else:
            return perubahan()
    elif angkasub=='2':
        return 0
    else:
        print('Salah!')
        return perubahan()

# ###DELETE FUNCTION###
def hapus():
    print('''
    HAPUS STOK GUDANG
    1. HAPUS STOK GUDANG
    2. KEMBALI KE MENU UTAMA
    ''')
    angkasub=input('Silahkan pilih sub-menu 1-2: ')
    if angkasub=='1':
        tampilsemua()
        if len(gudang)!=0:
            kode=input('Masukkan Kode Barang yang Ingin di Hapus: ').capitalize()
            for i in range(len(gudang)):
                if gudang[i]['Kode Barang']==kode:
                    print(f'Data yang ingin anda hapus adalah \n {gudang[i]}')
                    confirm=input('Apakah anda yakin ingin menghapus data ini? Y/N: ')
                    if confirm=='y' or confirm=='Y':
                        del gudang[i]
                        print('Data berhasil dihapus')
                        return hapus()
                    elif confirm=='n' or confirm=='N':
                        print('Data tidak terhapus')
                        return hapus()
            return print('Data tidak ada!'), hapus()
        else:
            return hapus()
    elif angkasub=='2':
        return 0
    else:
        print('Salah!')
        return hapus()


###OPTION###
while True:
    welcome()
    angka=input('Silahkan pilih menu 1-5: ')
    if angka=='1':
        tampil()
    elif angka=='2':
        tambah()
    elif angka=='3':
        perubahan()
    elif angka=='4':
        hapus()
    elif angka=='5':
        print('bye-bye!')
        break
    else:
        print('Pilihan yang Anda Masukkan Salah!')
