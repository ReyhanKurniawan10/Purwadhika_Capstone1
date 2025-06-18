listData = [
    ['Toyota', 'Calya', '2020', 'B 2450 EVR', '200000', 'Tersedia'],
    ['Nissan', 'Livina', '2015', 'B 1467 POR', '350000', 'Tersedia'],
    ['Honda', 'Jazz', '2011', 'B 4596 SRT', '300000', 'Tersedia'],
    ['Toyota', 'Supra', '2019', 'B 1476 TYR', '2000000', 'Tersedia'],
    ['Toyota', 'GR86', '2021', 'B 8671 GR', '1000000', 'Tersedia'],
    ['Nissan', 'GTR', '2020', 'B 35 GTR', '5000000', 'Tersedia'],
    ['Honda', 'CRV', '2015', 'B 8765 FGR', '200000', 'Tersedia'],
    ['Honda', 'Civic', '2020', 'B 4397 REW', '500000', 'Tersedia'],
    ['Mazda', 'Mazda 3', '2020', 'B 3496 DSG', '500000', 'Tersedia'],
    ['Mazda', 'CX5', '2019', 'B 5600 PLK', '400000', 'Tersedia'],
    ['Toyota', 'Calya', '2017', 'B 2678 PJK', '100000', 'Tersedia'],
    ['Toyota', 'Raize', '2020', 'B 5432 JGB', '200000', 'Tersedia']
]

listDataPeminjaman = []

listDataCustomer = [['Reyhan Kurniawan', 'Jl. Pondok Indah 3', '31256701965890001', 0],
                    ['Reyhan Pratama', 'Jl. Mekar Sari 11', '30001205697650004', 0],
                    ['Reyhan Wijaya', 'Jl. Ujung Panjang 2', '300123856743960007', 0],
                    ['Dian Rahma', 'Jl. Mawar Mekar 5', '30001345679280006', 0],
                    ['Dian Mawar', 'Jl. Melati Wangi 7', '30001563486920007', 0],
                    ['Mawar Rahayu', 'Jl. Alam Segar 2', '30004156782390009', 0],
                    ['Marco', 'Jl. Perak 2', '30005134128560004', 0],
                    ['Zidan Maradona', 'Jl. Perak Emas 3', '30002314567910002', 0],]

def menu():
    print('''Selamat datang di Database Rey's Car Rental
          
          1. Tambahkan Data
          2. Tampilkan Data
          3. Update Data
          4. Hapus Data
          5. Sewa Mobil
          6. Data Pelanggan dan Data Peminjaman
          7. Keluar dari program''')

def menuTambahMobil():
    global listData
    flag = 0
    while flag != 1:
        merkMobil = input('Masukkan merk mobil yang ingin ditambahkan : ')
        namaMobil = input('Masukkan nama mobil yang ingin ditambahkan : ')
        tahunMobil = inputanTahunMobil()
        duplikasiPlat = 0
        platMobil = ''
        statusMobil = ''
        while True:
            platMobil = inputanPlatMobil()
            duplikasiPlat = cekDuplikasiPlat(platMobil)
            if(duplikasiPlat == 1):
                break
        while True:
            hargaSewaMobil = input('Masukkan harga sewa mobil perhari yang ingin ditambahkan : ')
            if(hargaSewaMobil.isdigit()):
                break
            else:
                print('Maaf, data harga yang anda masukkan tidak sesuai')
            hargaSewaMobilINT = int(hargaSewaMobil)
        statusMobil = 'Tersedia'
        newList = [merkMobil, namaMobil, tahunMobil, platMobil, hargaSewaMobil, statusMobil]
        print('Merk\t|Nama\t|Tahun\t|Plat\t\t|Harga Sewa/Hari\t|Status')
        print(f'{newList[0]}\t|{newList[1]}\t|{newList[2]}\t|{newList[3]}\t|{newList[4]}\t\t\t|{newList[5]}')
        while True:
            validasiInput = input('Apakah data yang anda masukkan sudah benar? [ya / tidak] : ')
            validasiInputLower = validasiInput.lower()
            if(validasiInputLower == 'ya'):
                listData.append(newList)
                flag = 1
                break
            elif(validasiInputLower == 'tidak'):
                flag1 = 0
                while True:
                    validasiInputUlang = input('Apakah anda ingin melakukan input ulang? [ya / tidak] : ')
                    validasiInputUlangLower = validasiInputUlang.lower()
                    if(validasiInputUlangLower == 'ya'):
                        flag1 = 1
                        break
                    elif(validasiInputUlangLower == 'tidak'):
                        flag1 = 1
                        flag = 1
                        break
                    else:
                        print('Maaf, inputan yang anda masukkan tidak sesuai dengan yang diminta, silahkan input lagi!')
                if(flag1 == 1):
                    break
            else :
                print('Maaf, inputan yang anda masukkan tidak sesuai dengan yang diminta, silahkan input lagi!')

def menuKe2():
    while True:
        flagKeluar = 0
        hasil = 0
        print('''\n---Tampilkan Data---
              
1. Menampilkan semua data
2. Menampilkan data mobil berdasarkan plat mobil yang diinput
3. Menampilkan data mobil berdasarkan index yang diinput
4. Menampilkan semua mobil dengan merk yang diinput
5. Menampilkan semua mobil dengan nama yang diinput
6. Menampilkan semua mobil dengan tahun yang diinput
7. Menampilkan semua mobil dengan status yang diinput
8. Kembali ke menu utama''')
        pilihan = input('Silahkan masukkan pilihan anda sesuai dengan angka yang dituju [1 - 8] : ')
        if(pilihan == '1'):
            tampilSemuaData()
        elif(pilihan == '2'):
            tampilDataBerdasarkanPlat()
        elif(pilihan == '3'):
            tampilDataBerdasarkanIndex()
        elif(pilihan == '4'):
            merkMobil = input('Masukkan merk mobil yang dicari : ')
            merkMobilLower = merkMobil.lower()
            tampilDataMobilDenganMerkYangSama(merkMobilLower)
        elif(pilihan == '5'):
            namaMobil = input('Masukkan nama mobil yang dicari : ')
            namaMobilLower = namaMobil.lower()
            tampilDataMobilDenganNamaYangSama(namaMobilLower)
        elif(pilihan == '6'):
            flag = 0
            while True:
                tahunMobil = input('Masukkan tahun mobil yang dicari : ')
                if(tahunMobil.isdigit() and int(tahunMobil) > 1800 and int(tahunMobil) <= 2025):
                    flag = 1
                    break
                else:
                    print('Maaf, tahun yang anda masukkan tidak sesuai.')
                    konfirmasiKeMenuUtama = input('Apakah anda ingin mencari lagi dengan tahun mobil? Jika tidak akan kembali ke menu utama. [ya / tidak] : ')
                    konfirmasiKeMenuUtamaLower = konfirmasiKeMenuUtama.lower()
                    if(konfirmasiKeMenuUtamaLower == 'ya'):
                        break
                    elif(konfirmasiKeMenuUtamaLower == 'tidak'):
                        flagKeluar = 1
                        break
                    else:
                        print('Maaf, inputan anda tidak sesuai')
            if(flag == 1):
                tampilDataMobilDenganTahunYangSama(tahunMobil)
        elif(pilihan == '7'):
            while True:
                statusMobil = input('Status mobil yang dicari [Tersedia / Disewa] : ')
                statusMobilLower = statusMobil.lower()
                if(statusMobilLower == 'tersedia' or statusMobilLower == 'disewa'):
                    tampilDataMobilDenganStatusYangSama(statusMobilLower)
                    break
                else:
                    print('Maaf, status yang anda masukkan tidak sesuai.')
        elif(pilihan == '8'):
            break
        else:
            print('Maaf inputan yang anda masukkan tidak sesuai.')
        if(flagKeluar == 1):
            break

def tampilDataMobilDenganMerkYangSama(merkMobil):
    flag = 0
    print('Index\t|Merk\t|Nama\t|Tahun\t|Plat\t\t|Harga Sewa/Hari\t|Status')
    for i in range(len(listData)):
        if(merkMobil == listData[i][0].lower()):
            flag = 1
            print(f'{i}\t|{listData[i][0]}\t|{listData[i][1]}\t|{listData[i][2]}\t|{listData[i][3]}\t|{listData[i][4]}\t\t\t|{listData[i][5]}')
    if(flag == 0):
        print(f'\nTidak ada data mobil dengan merk {merkMobil}.\n')

def tampilDataMobilDenganNamaYangSama(namaMobil):
    flag = 0
    print('Index\t|Merk\t|Nama\t|Tahun\t|Plat\t\t|Harga Sewa/Hari\t|Status')
    for i in range(len(listData)):
        if(namaMobil == listData[i][1].lower()):
            flag = 1
            print(f'{i}\t|{listData[i][0]}\t|{listData[i][1]}\t|{listData[i][2]}\t|{listData[i][3]}\t|{listData[i][4]}\t\t\t|{listData[i][5]}')
    if(flag == 0):
        print(f'\nTidak ada data mobil dengan nama {namaMobil}.\n')

def tampilDataMobilDenganTahunYangSama(tahunMobil):
    flag = 0
    print('Index\t|Merk\t|Nama\t|Tahun\t|Plat\t\t|Harga Sewa/Hari\t|Status')
    for i in range(len(listData)):
        if(tahunMobil == listData[i][2].lower()):
            flag = 1
            print(f'{i}\t|{listData[i][0]}\t|{listData[i][1]}\t|{listData[i][2]}\t|{listData[i][3]}\t|{listData[i][4]}\t\t\t|{listData[i][5]}')
    if(flag == 0):
        print(f'\nTidak ada data mobil dengan tahun {tahunMobil}.\n')

def tampilDataMobilDenganStatusYangSama(statusMobil):
    flag = 0
    print('Index\t|Merk\t|Nama\t|Tahun\t|Plat\t\t|Harga Sewa/Hari\t|Status')
    for i in range(len(listData)):
        if(statusMobil == listData[i][5].lower()):
            flag = 1
            print(f'{i}\t|{listData[i][0]}\t|{listData[i][1]}\t|{listData[i][2]}\t|{listData[i][3]}\t|{listData[i][4]}\t\t\t|{listData[i][5]}')
    if(flag == 0):
        print(f'\nTidak ada data mobil dengan status {statusMobil}.\n')

def tampilDataBerdasarkanIndex():
    flag1 = 0
    while True:
        inputUlang = ''
        indexCari = input('Masukkan index dari data yang ingin dilihat : ')
        if(indexCari.isdigit() == True and int(indexCari) < len(listData)):
            indexCariINT = int(indexCari)
            print('Index\t|Merk\t|Nama\t|Tahun\t|Plat\t\t|Harga Sewa/Hari\t|Status')
            print(f'{indexCariINT}\t|{listData[indexCariINT][0]}\t|{listData[indexCariINT][1]}\t|{listData[indexCariINT][2]}\t|{listData[indexCariINT][3]}\t|{listData[indexCariINT][4]}\t\t\t|{listData[indexCariINT][5]}')
            break
            # lihatLagi = input('Apakah anda ingin melihat data lagi? [ya/ tidak] : ')
            # if(lihatLagi == 'tidak'):
            #     flag2 = 1
            #     break
            # elif(lihatLagi == 'ya'):
            #     break
            # else:
            #     print('Maaf inputan yang anda masukkan tidak sesuai.')
        elif(indexCari.isdigit() == True and int(indexCari) >= len(listData)):
            print('Maaf, data yang anda cari tidak ditemukan')
            while True:
                inputUlang = input('Apakah anda ingin mencari ulang? [ya / tidak] : ')
                inputUlangLower = inputUlang.lower()
                if(inputUlangLower == 'tidak'):
                    flag1 = 1
                    break
                elif(inputUlangLower == 'ya'):
                    break
                else:
                    print('Maaf inputan yang anda masukkan tidak sesuai.')
            if(flag1 == 1):
                break
        else:
            print('Maaf inputan yang anda masukkan tidak sesuai.')
            # while True:
            #     inputUlang = input('Apakah anda ingin mencari ulang? [ya / tidak] : ')
            #     inputUlangLower = inputUlang.lower()
            #     if(inputUlangLower == 'tidak'):
            #         flag1 = 1
            #         break
            #     elif(inputUlangLower == 'ya'):
            #         break
            #     else:
            #         print('Maaf inputan yang anda masukkan tidak sesuai.')
            # if(flag1 == 1):
            #     break

def tampilDataBerdasarkanPlat():
    flag = 0
    flag1 = 0
    inputUlang = ''
    validasiPlatMobilTDBP = 0
    lihatLagi = ''
    while True:
        platMobilTDBP = input('Masukkan plat mobil dari data yang ingin dilihat : ')
        validasiPlatMobilTDBP = cekPlatMobilUpdt(platMobilTDBP)
        if(validasiPlatMobilTDBP == 1):
            for i in range(len(listData)):
                if(platMobilTDBP == listData[i][3]):
                    print('Index\t|Merk\t|Nama\t|Tahun\t|Plat\t\t|Harga Sewa/Hari\t|Status')
                    print(f'{i}\t|{listData[i][0]}\t|{listData[i][1]}\t|{listData[i][2]}\t|{listData[i][3]}\t|{listData[i][4]}\t\t\t|{listData[i][5]}')
                    flag = 1
                    break
            if(flag == 1):
                break
                # lihatLagi = input('Apakah anda ingin melihat data lagi? [ya / tidak] : ')
                # if(lihatLagi == 'tidak'):
                #     break
                # elif(lihatLagi == 'ya'):
                #     break
                # else:
                #     print('Maaf inputan yang anda masukkan tidak sesuai.')
            else:
                print('Maaf, data yang anda cari tidak ditemukan')
                while True:
                    inputUlang = input('Apakah anda ingin mencari ulang? [ya / tidak] : ')
                    inputUlang.lower()
                    if(inputUlang == 'tidak'):
                        flag1 = 1
                        break
                    elif(inputUlang == 'ya'):
                        break
                    else:
                        print('Maaf inputan yang anda masukkan tidak sesuai.')
            if(flag1 == 1):
                break

def tampilSemuaData():
    print('Index\t|Merk\t|Nama\t|Tahun\t|Plat\t\t|Harga Sewa/Hari\t|Status')
    for i in range(len(listData)):
        print(f'{i}\t|{listData[i][0]}\t|{listData[i][1]}\t|{listData[i][2]}\t|{listData[i][3]}\t|{listData[i][4]}\t\t\t|{listData[i][5]}')

def inputanTahunMobil():
    tahunMobilVIT = ''
    while True:
        tahunMobilVIT = input('Masukkan tahun mobil yang ingin ditambahkan : ')
        panjangTahun = len(tahunMobilVIT)
        if(panjangTahun == 4):
            if(tahunMobilVIT.isdigit() == True):
                cekTahun = int(tahunMobilVIT)
                if(cekTahun > 1800 and cekTahun <= 2025):
                    break
                else:
                    print('Maaf, data tahun yang anda masukkan tidak sesuai.')
                    continue
            else:
                print('Maaf, data tahun yang anda masukkan tidak sesuai.')
                continue
        else:
            print('Maaf, data tahun yang anda masukkan tidak sesuai.')
    return tahunMobilVIT

def inputanPlatMobil():
    platMobilVIP = ''
    while True:
        platMobilVIP = input('Masukkan plat mobil yang ingin ditambahkan [cth : B 1234 CED] : ')
        if(platMobilVIP[0:1].isalpha() and platMobilVIP[0:1].isupper() and platMobilVIP[1:2] == ' ' and len(platMobilVIP) <= 10):
            if(platMobilVIP[2:6].isdigit()):
                if(platMobilVIP[6:7] == ' ' and (platMobilVIP[7:].isalpha()) and (platMobilVIP[7:].isupper())):
                    break
                else:
                    print('Maaf, plat mobil yang anda masukkan tidak sesuai dengan ketentuan')
            elif(platMobilVIP[2:5].isdigit() and len(platMobilVIP) <= 9):
                if(platMobilVIP[5:6] == ' ' and (platMobilVIP[6:].isalpha()) and (platMobilVIP[6:].isupper())):
                    break
                else:
                    print('Maaf, plat mobil yang anda masukkan tidak sesuai dengan ketentuan')
            elif(platMobilVIP[2:4].isdigit() and len(platMobilVIP) <= 8):
                if(platMobilVIP[4:5] == ' ' and (platMobilVIP[5:].isalpha()) and (platMobilVIP[5:].isupper())):
                    break
                else:
                    print('Maaf, plat mobil yang anda masukkan tidak sesuai dengan ketentuan')
            elif(platMobilVIP[2:3].isdigit() and len(platMobilVIP) <= 7):
                if(platMobilVIP[3:4] == ' ' and (platMobilVIP[4:].isalpha()) and (platMobilVIP[4:].isupper())):
                    break
                else:
                    print('Maaf, plat mobil yang anda masukkan tidak sesuai dengan ketentuan')
            else:
                print('Maaf, plat mobil yang anda masukkan tidak sesuai dengan ketentuan')
        elif(platMobilVIP[0:2].isalpha() and platMobilVIP[0:2].isupper() and platMobilVIP[2:3] == ' ' and len(platMobilVIP) <= 11):
            if(platMobilVIP[3:7].isdigit()):
                if(platMobilVIP[7:8] == ' ' and (platMobilVIP[8:].isalpha()) and (platMobilVIP[8:].isupper())):
                    break
                else:
                    print('Maaf, plat mobil yang anda masukkan tidak sesuai dengan ketentuan')
            elif(platMobilVIP[3:6].isdigit() and len(platMobilVIP) <= 10):
                if(platMobilVIP[6:7] == ' ' and (platMobilVIP[7:].isalpha()) and (platMobilVIP[7:].isupper())):
                    break
                else:
                    print('Maaf, plat mobil yang anda masukkan tidak sesuai dengan ketentuan')
            elif(platMobilVIP[3:5].isdigit() and len(platMobilVIP) <= 9):
                if(platMobilVIP[5:6] == ' ' and (platMobilVIP[6:].isalpha()) and (platMobilVIP[6:].isupper())):
                    break
                else:
                    print('Maaf, plat mobil yang anda masukkan tidak sesuai dengan ketentuan')
            elif(platMobilVIP[3:4].isdigit() and len(platMobilVIP) <= 8):
                if(platMobilVIP[4:5] == ' ' and (platMobilVIP[5:].isalpha()) and (platMobilVIP[5:].isupper())):
                    break
                else:
                    print('Maaf, plat mobil yang anda masukkan tidak sesuai dengan ketentuan')
            else:
                print('Maaf, plat mobil yang anda masukkan tidak sesuai dengan ketentuan')
        else:
            print('Maaf, plat mobil yang anda masukkan tidak sesuai dengan ketentuan')
    return platMobilVIP

def cekPlatMobilUpdt(platMobil):
    if(platMobil[0:1].isalpha() and platMobil[0:1].isupper() and platMobil[1:2] == ' ' and len(platMobil) <= 10):
        if(platMobil[2:6].isdigit()):
            if(platMobil[6:7] == ' ' and (platMobil[7:].isalpha()) and (platMobil[7:].isupper())):
                return 1
            else:
                print('Maaf, plat mobil yang anda masukkan tidak sesuai dengan ketentuan')
        elif(platMobil[2:5].isdigit() and len(platMobil) <= 9):
            if(platMobil[5:6] == ' ' and (platMobil[6:].isalpha()) and (platMobil[6:].isupper())):
                return 1
            else:
                print('Maaf, plat mobil yang anda masukkan tidak sesuai dengan ketentuan')
        elif(platMobil[2:4].isdigit() and len(platMobil) <= 8):
            if(platMobil[4:5] == ' ' and (platMobil[5:].isalpha()) and (platMobil[5:].isupper())):
                return 1
            else:
                print('Maaf, plat mobil yang anda masukkan tidak sesuai dengan ketentuan')
        elif(platMobil[2:3].isdigit() and len(platMobil) <= 7):
            if(platMobil[3:4] == ' ' and (platMobil[4:].isalpha()) and (platMobil[4:].isupper())):
                return 1
            else:
                print('Maaf, plat mobil yang anda masukkan tidak sesuai dengan ketentuan')
        else:
            print('Maaf, plat mobil yang anda masukkan tidak sesuai dengan ketentuan')
    elif(platMobil[0:2].isalpha() and platMobil[0:2].isupper() and platMobil[2:3] == ' ' and len(platMobil) <= 11):
        if(platMobil[3:7].isdigit()):
            if(platMobil[7:8] == ' ' and (platMobil[8:].isalpha()) and (platMobil[8:].isupper())):
                return 1
            else:
                print('Maaf, plat mobil yang anda masukkan tidak sesuai dengan ketentuan')
        elif(platMobil[3:6].isdigit() and len(platMobil) <= 10):
            if(platMobil[6:7] == ' ' and (platMobil[7:].isalpha()) and (platMobil[7:].isupper())):
                return 1
            else:
                print('Maaf, plat mobil yang anda masukkan tidak sesuai dengan ketentuan')
        elif(platMobil[3:5].isdigit() and len(platMobil) <= 9):
            if(platMobil[5:6] == ' ' and (platMobil[6:].isalpha()) and (platMobil[6:].isupper())):
                return 1
            else:
                print('Maaf, plat mobil yang anda masukkan tidak sesuai dengan ketentuan')
        elif(platMobil[3:4].isdigit() and len(platMobil) <= 8):
            if(platMobil[4:5] == ' ' and (platMobil[5:].isalpha()) and (platMobil[5:].isupper())):
                return 1
            else:
                print('Maaf, plat mobil yang anda masukkan tidak sesuai dengan ketentuan')
        else:
            print('Maaf, plat mobil yang anda masukkan tidak sesuai dengan ketentuan')
    else:
        print('Maaf, plat mobil yang anda masukkan tidak sesuai dengan ketentuan')

def cekDuplikasiPlat(platMobil):
    flag = 1
    for i in range(len(listData)):
        if(platMobil == listData[i][3]):
            print('Index\t|Merk\t|Nama\t|Tahun\t|Plat\t\t|Harga Sewa/Hari\t|Status')
            print(f'{i}\t|{listData[i][0]}\t|{listData[i][1]}\t|{listData[i][2]}\t|{listData[i][3]}\t|{listData[i][4]}\t\t\t|{listData[i][5]}')
            print('Mohon maaf, terdapat kesamaan plat nomor dengan data mobil tersebut.')
            print('Jika terjadi kesalahan pada data tersebut, mohon update atau delete data tersebut terlebih dahulu')
            flag = 0
            break
    return flag

def updateList():
    global listData
    while True:
        bagianYangdiUpdate = 0
        idxUpdtSTR = input('Silahkan pilih index data yang ingin diubah : ')
        if(idxUpdtSTR.isdigit() == True and int(idxUpdtSTR) < len(listData)):
            idxUpdtINT = int(idxUpdtSTR)
            print('Merk\t|Nama\t|Tahun\t|Plat\t\t|Harga Sewa/Hari\t|Status')
            print(f'{listData[idxUpdtINT][0]}\t|{listData[idxUpdtINT][1]}\t|{listData[idxUpdtINT][2]}\t|{listData[idxUpdtINT][3]}\t|{listData[idxUpdtINT][4]}\t\t\t|{listData[idxUpdtINT][5]}')
            dataUpdate = input('Pilih data mana yang ingin diUpdate : ')
            dataUpdate.lower()
            if(dataUpdate == 'merk'):
                merkUpdate = ''
                validasiDataBaru = ''
                flag = 0
                flag2 = 0
                flag3 = 0
                inputUlang = ''
                while True:
                    merkUpdate = input('Masukan nama merk mobil yang baru : ')
                    print('Merk\t|Nama\t|Tahun\t|Plat\t\t|Harga Sewa/Hari\t|Status')
                    print(f'{merkUpdate}\t|{listData[idxUpdtINT][1]}\t|{listData[idxUpdtINT][2]}\t|{listData[idxUpdtINT][3]}\t|{listData[idxUpdtINT][4]}\t\t\t|{listData[idxUpdtINT][5]}')
                    while True:
                        validasiDataBaru = input('Apakah data yang anda isikan sudah benar? [ya / tidak] : ')
                        if(validasiDataBaru == 'ya'):
                            flag = 1
                            flag3 = 1
                            listData[idxUpdtINT][0] = merkUpdate
                            break
                        elif(validasiDataBaru == 'tidak'):
                            while True:
                                inputUlang = input('Apakah anda ingin memasukkan ulang? [ya / tidak] : ')
                                if(inputUlang == 'ya'):
                                    flag = 0
                                    flag2 = 1
                                    break
                                elif(inputUlang == 'tidak'):
                                    flag = 1
                                    flag2 = 1
                                    flag3 = 1
                                    break
                                else:
                                    print('Maaf inputan yang anda masukkan tidak sesuai.')
                        else:
                            print('Maaf inputan yang anda masukkan tidak sesuai.')
                        if(flag2 == 1):
                            break
                    if(flag == 1):
                        break
            elif(dataUpdate == 'nama'):
                namaUpdate = ''
                validasiDataBaru = ''
                flag = 0
                flag2 = 0
                flag3 = 0
                inputUlang = ''
                while True:
                    namaUpdate = input('Masukan nama mobil yang baru : ')
                    print('Merk\t|Nama\t|Tahun\t|Plat\t\t|Harga Sewa/Hari\t|Status')
                    print(f'{listData[idxUpdtINT][0]}\t|{namaUpdate}\t|{listData[idxUpdtINT][2]}\t|{listData[idxUpdtINT][3]}\t|{listData[idxUpdtINT][4]}\t\t\t|{listData[idxUpdtINT][5]}')
                    while True:
                        validasiDataBaru = input('Apakah data yang anda isikan sudah benar? [ya / tidak] : ')
                        if(validasiDataBaru == 'ya'):
                            flag = 1
                            flag3 = 1
                            listData[idxUpdtINT][1] = namaUpdate
                            break
                        elif(validasiDataBaru == 'tidak'):
                            while True:
                                inputUlang = input('Apakah anda ingin memasukkan ulang? [ya / tidak] : ')
                                if(inputUlang == 'ya'):
                                    flag = 0
                                    flag2 = 1
                                    break
                                elif(inputUlang == 'tidak'):
                                    flag = 1
                                    flag2 = 1
                                    flag3 = 1
                                    break
                                else:
                                    print('Maaf inputan yang anda masukkan tidak sesuai.')
                        else:
                            print('Maaf inputan yang anda masukkan tidak sesuai.')
                        if(flag2 == 1):
                            break
                    if(flag == 1):
                        break
            elif(dataUpdate == 'tahun'):
                tahunUpdate = ''
                validasiDataBaru = ''
                flag = 0
                flag2 = 0
                flag3 = 0
                inputUlang = ''
                while True:
                    tahunUpdate = input('Masukkan tahun keluaran mobil yang baru [cth : 2025] :')
                    panjangTahun = len(tahunUpdate)
                    if(panjangTahun == 4):
                        if(tahunUpdate.isdigit() == True):
                            cekTahun = int(tahunUpdate)
                            if(cekTahun <= 2025):
                                print('Merk\t|Nama\t|Tahun\t|Plat\t\t|Harga Sewa/Hari\t|Status')
                                print(f'{listData[idxUpdtINT][0]}\t|{listData[idxUpdtINT][1]}\t|{tahunUpdate}\t|{listData[idxUpdtINT][3]}\t|{listData[idxUpdtINT][4]}\t\t\t|{listData[idxUpdtINT][5]}')
                                while True:
                                    validasiDataBaru = input('Apakah data yang anda isikan sudah benar? [ya / tidak] : ')
                                    if(validasiDataBaru == 'ya'):
                                        flag = 1
                                        flag3 = 1
                                        listData[idxUpdtINT][2] = tahunUpdate
                                        break
                                    elif(validasiDataBaru == 'tidak'):
                                        while True:
                                            inputUlang = input('Apakah anda ingin memasukkan ulang? [ya / tidak] : ')
                                            if(inputUlang == 'ya'):
                                                flag = 0
                                                flag2 = 1
                                                break
                                            elif(inputUlang == 'tidak'):
                                                flag = 1
                                                flag2 = 1
                                                flag3 = 1
                                                break
                                            else:
                                                print('Maaf inputan yang anda masukkan tidak sesuai.')
                                    else:
                                        print('Maaf inputan yang anda masukkan tidak sesuai.')
                                    if(flag2 == 1):
                                        break
                                if(flag == 1):
                                    break
                            else:
                                print('Maaf inputan "tahun keluaran mobil" yang anda masukkan tidak sesuai.')
                                continue
                        else:
                            print('Maaf inputan "tahun keluaran mobil" yang anda masukkan tidak sesuai.')
                            continue
                    else:
                        print('Maaf inputan "tahun keluaran mobil" yang anda masukkan tidak sesuai.')
                break
            elif(dataUpdate == 'plat'):
                bagianYangdiUpdate = 3
                platUpdate = ''
                validasiDataBaru1 = 0
                flag = 0
                flag2 = 0
                flag3 = 0
                inputUlang = ''
                while True:
                    platUpdate = input('Masukkan plat mobil yang baru [cth : B 1234 CDE] : ')
                    hasilCekPenulisanPlat = cekPlatMobilUpdt(platUpdate)
                    if(hasilCekPenulisanPlat == 1):
                        hasilCekDuplikatPlat = cekDuplikasiPlat(platUpdate)
                        if(hasilCekDuplikatPlat == 1):
                            print('Merk\t|Nama\t|Tahun\t|Plat\t\t|Harga Sewa/Hari\t|Status')
                            print(f'{listData[idxUpdtINT][0]}\t|{listData[idxUpdtINT][1]}\t|{listData[idxUpdtINT][2]}\t|{platUpdate}\t|{listData[idxUpdtINT][4]}\t\t\t|{listData[idxUpdtINT][5]}')
                            validasiDataBaru1 = fungsiValidasiDataBaru(idxUpdtINT, bagianYangdiUpdate, platUpdate)
                    if(validasiDataBaru1 == 1):
                        flag3 = 1
                        break
                    elif(validasiDataBaru1 == 2):
                        flag3 = 1
                        break
            elif(dataUpdate == 'harga sewa/hari' or dataUpdate == 'harga'):
                bagianYangdiUpdate = 4
                hargaUpdate = ''
                flag3 = 0
                while True:
                    hargaUpdate = input('Masukkan harga sewa mobil per hari yang baru : ')
                    if(hargaUpdate.isdigit()):
                        print('Merk\t|Nama\t|Tahun\t|Plat\t\t|Harga Sewa/Hari\t|Status')
                        print(f'{listData[idxUpdtINT][0]}\t|{listData[idxUpdtINT][1]}\t|{listData[idxUpdtINT][2]}\t|{listData[idxUpdtINT][3]}\t|{hargaUpdate}\t\t\t|{listData[idxUpdtINT][5]}')
                        fungsiValidasiDataBaru(idxUpdtINT, bagianYangdiUpdate, hargaUpdate)
                        flag3 = 1
                        break
                    else:
                        print('Maaf, inputan yang anda masukkan tidak sesuai')
            else:
                print('Maaf, inputan yang anda masukkan tidak sesuai')
        else:
            print('Maaf, inputan yang anda masukkan tidak sesuai')
        if(flag3 == 1):
            break

def fungsiValidasiDataBaru(idxUpdtINT, bagianYangdiUpdate, inputanUpdate):
    global listData
    hasilPengecekkan = ''
    flag = 0
    nilai = 0
    while True:
        hasilPengecekkan = input('Apakah data yang anda isikan sudah benar? [ya / tidak] : ')
        if(hasilPengecekkan == 'ya'):
            listData[idxUpdtINT][bagianYangdiUpdate] = inputanUpdate
            nilai = 1
            break
        elif(hasilPengecekkan == 'tidak'):
            while True:
                inputUlang = input('Apakah anda ingin memasukkan ulang? [ya / tidak] : ')
                if(inputUlang == 'ya'):
                    flag = 1
                    nilai = 0
                    break
                elif(inputUlang == 'tidak'):
                    flag = 1
                    nilai = 2
                    break
                else:
                    print('Maaf inputan yang anda masukkan tidak sesuai.')
        else:
            print('Maaf inputan yang anda masukkan tidak sesuai.')
        if(flag == 1):
            break
    return nilai

def menuKe4():
    while True:
        hasilCek = 0
        print('''---Hapus Data---
            1. Hapus data mobil berdasarkan index
            2. Hapus semua data mobil
            3. Kembali ke menu utama''')
        pilihan = input('Silahkan masukkan pilihan sesuai dengan angka yang ingin dituju [1 - 3] : ')
        if(pilihan == '1'):
            hasilCek = cekListMobilBerisiAtauTidak()
            if(hasilCek == 0):
                deleteList()
        elif(pilihan == '2'):
            hasilCek = cekListMobilBerisiAtauTidak()
            if(hasilCek == 0):
                deleteSemuaListMobil()
        elif(pilihan == '3'):
            break
        else:
            print('Maaf, inputan anda tidak sesuai.')

def cekListMobilBerisiAtauTidak():
    global listData
    if(len(listData) == 0):
        print('\nMaaf, list data mobil saat ini sedang kosong, tidak ada yang bisa dihapus\n')
        return 1
    return 0

def deleteList():
    global listData
    tampilSemuaData()
    while True:
        flag = 0
        flagKeluarDelete = 0
        indexHapus = input('Masukkan index data mana yang ingin dihapus : ')
        if(indexHapus.isdigit() and int(indexHapus) < len(listData)):
            indexHapusINT = int(indexHapus)
            flag = 1
        else:
            print('Maaf, inputan yang anda masukkan tidak sesuai')
            while True:
                keluarMenu = input('Apakah anda ingin keluar dari menu delete? [ya / tidak]')
                keluarMenuLower = keluarMenu.lower()
                if(keluarMenuLower == 'ya'):
                    flagKeluarDelete = 1
                    break
                elif(keluarMenuLower == 'tidak'):
                    break
                else:
                    print('Maaf, inputan yang anda masukkan tidak sesuai.')
        if(flag == 1):
            if(listData[indexHapusINT][5] == 'Tersedia'):
                print('Merk\t|Nama\t|Tahun\t|Plat\t\t|Harga Sewa/Hari\t|Status')
                print(f'{listData[indexHapusINT][0]}\t|{listData[indexHapusINT][1]}\t|{listData[indexHapusINT][2]}\t|{listData[indexHapusINT][3]}\t|{listData[indexHapusINT][4]}\t\t\t|{listData[indexHapusINT][5]}')
                while True:
                    validasiHapus = input('Apakah anda yakin ingin menghapus data ini? [ya / tidak] : ')
                    validasiHapus.lower()
                    if(validasiHapus == 'ya'):
                        del listData[indexHapusINT]
                        flagKeluarDelete = 1
                        break
                    elif(validasiHapus == 'tidak'):
                        while True:
                            inputUlang = input('Apakah anda ingin memilih ulang data yang ingin dihapus? [ya / tidak] : ')
                            inputUlangLower = inputUlang.lower()
                            if(inputUlangLower == 'ya'):
                                break
                            elif(inputUlangLower == 'tidak'):
                                flagKeluarDelete = 1
                                break
                            else:
                                print('Maaf, inputan yang anda masukkan tidak sesuai.')
                        break
                    else:
                        print('Maaf, inputan yang anda masukkan tidak sesuai.')
            elif(listData[indexHapusINT][5] == 'Disewa'):
                print('Index\t|Merk\t|Nama\t|Tahun\t|Plat\t\t|Harga Sewa/Hari\t|Status')
                print(f'{listData[indexHapusINT][0]}\t|{listData[indexHapusINT][1]}\t|{listData[indexHapusINT][2]}\t|{listData[indexHapusINT][3]}\t|{listData[indexHapusINT][4]}\t\t\t|{listData[indexHapusINT][5]}')
                print('Maaf, anda tidak dapat menghapus data ini, karena mobilnya sedang disewa.')
                print('Jika terdapat kesalahan pada data, mohon diupdate data peminjaman terlebih dahulu.')
                while True:
                    inputUlang = input('Apakah anda ingin memilih ulang data yang ingin dihapus? [ya / tidak] : ')
                    inputUlangLower = inputUlang.lower()
                    if(inputUlangLower == 'ya'):
                        break
                    elif(inputUlangLower == 'tidak'):
                        flagKeluarDelete = 1
                        break
                    else:
                        print('Maaf, inputan yang anda masukkan tidak sesuai.')
        if(flagKeluarDelete == 1):
            break

def deleteSemuaListMobil():
    global listData
    flagStatusMobil = 0
    flagKeluar = 0
    while True:
        konfirmasi = input('Apakah anda yakin ingin menghapus semua data? [ya / tidak] : ')
        konfirmasiLower = konfirmasi.lower()
        if(konfirmasiLower == 'ya'):
            for i in range(len(listData)):
                if(listData[i][5] == 'Disewa'):
                    flagStatusMobil = 1
                    break
            if(flagStatusMobil == 1):
                print('Mohon maaf, terdapat data yang sedang dalam status Disewa, sehingga tidak bisa dihapus')
                # while True:
                #     konfirmasiHapusTersedia = input('Apakah anda ingin menghapus semua yang berstatus Tersedia? [ya / tidak] : ')
                #     konfirmasiHapusTersediaLower = konfirmasiHapusTersedia.lower()
                #     if(konfirmasiHapusTersediaLower == 'ya'):
                #         for j in range(len(listData)):
                #             if(listData[j][5] == 'Tersedia'):
                #                 del listData[j]
                #         flagKeluar = 1
                #         break
                #     elif(konfirmasiHapusTersediaLower == 'tidak'):
                #         flagKeluar = 1
                #         break
                #     else:
                #         print('Maaf, inputan anda tidak sesuai.')
                # if(flagKeluar == 1):
                #     break
                break
            elif(flagStatusMobil == 0):
                listData.clear()
                break
        elif(konfirmasiLower == 'tidak'):
            break
        else:
            print('Maaf, inputan anda tidak sesuai.')

def cekDuplikasiNoKTP(NoKTP):
    flag = 1
    for i in range(len(listDataCustomer)):
        if(NoKTP == listDataCustomer[i][2]):
            print(f'''
Nama    : {listDataCustomer[i][0]}
Alamat  : {listDataCustomer[i][1]}
No KTP  : {listDataCustomer[i][2]}''')
            print('Mohon maaf, terdapat kesamaan nomor KTP dengan data pelanggan tersebut.')
            print('Jika terdapat kesalahan pada data pelanggan tersebut, mohon update atau delete data tersebut terlebih dahulu')
            flag = 0
            break
    return flag

def menuKe5():
    global listDataCustomer
    while True:
        flagKeluarMenu = 0
        bertanya = input('Apakah anda ingin melakukan input data pelanggan terlebih dahulu? [ya / tidak] : ')
        bertanyaLower = bertanya.lower()
        if(bertanyaLower == 'ya'):
            indexCustomer = inputDataCustomer()
            sewaMobil(indexCustomer)
            break
        elif(bertanyaLower == 'tidak'):
            if(len(listDataCustomer) == 0):
                flag1 = 0
                while True:
                    flag1 = 0
                    konfirmasi = input('Maaf, belum ada data pelanggan, apakah anda ingin input data pelanggan terlebih dahulu? [ya / tidak] : ')
                    konfirmasiLower = konfirmasi.lower()
                    if(konfirmasiLower == 'ya'):
                        flag1 = 1
                        indexCustomer = inputDataCustomer()
                        sewaMobil(indexCustomer)
                        flagKeluarMenu = 1
                        break
                    elif(konfirmasiLower == 'tidak'):
                        while True:
                            konfirmasiKeluar = input('Apakah anda ingin kembali ke menu utama? [ya / tidak] : ')
                            konfirmasiKeluarLower = konfirmasiKeluar.lower()
                            if(konfirmasiKeluarLower == 'ya'):
                                flag1 = 1
                                flagKeluarMenu = 1
                                break
                            elif(konfirmasiKeluarLower == 'tidak'):
                                flag1 = 1
                                break
                            else:
                                print('Maaf, inputan anda tidak sesuai.')
                    if(flag1 == 1):
                        break
                if(flagKeluarMenu == 1):
                    break
            else:
                while True:
                    flag = 0
                    flagKTP = 0
                    flagKeluarInputKTP = 0
                    noKTPPelanggan = input('Masukkan nomor KTP Pelanggan yang akan menyewa mobil : ')
                    if(noKTPPelanggan.isdigit() and len(noKTPPelanggan) == 17):
                        for i in range(len(listDataCustomer)):
                            if(noKTPPelanggan == listDataCustomer[i][2]):
                                flagKTP = 1
                                flag = 1
                                indexCustomer = i
                                break
                        if(flagKTP == 1):
                            flagKeluarMenu = 1
                            sewaMobil(indexCustomer)
                        elif(flagKTP == 0):
                            print('Maaf, pelanggan dengan nomor KTP tersebut tidak ditemukan')
                            while True:
                                print('''Apakah anda ingin
                                      1. Memasukkan Nomor KTP lagi
                                      2. Kembali ke awal menu Sewa Mobil untuk input data
                                      3. Kembali ke menu utama''')
                                pilih = input('Silahkan pilih [1 - 3] : ')
                                if(pilih == '1'):
                                    break
                                elif(pilih == '2'):
                                    flagKeluarInputKTP == 1
                                    break
                                elif(pilih == '3'):
                                    flagKeluarInputKTP = 1
                                    flagKeluarMenu = 1
                                    break
                                else:
                                    print('Maaf, inputan anda tidak sesuai.')
                        if(flagKeluarInputKTP == 1):
                            break
                    else:
                        print('Maaf, inputan anda tidak sesuai.')
                    if(flag == 1):
                        break
                if(flagKeluarMenu == 1):
                    break
        else:
            print('Maaf, inputan anda tidak sesuai.')

def inputDataCustomer():
    global listDataCustomer
    newListCustomer = []
    while True:
        while True:
            namaCustomer = input('Silahkan masukkan nama lengkap pelanggan : ')
            if(namaCustomer.isalpha()):
                break
            else:
                print('Maaf, inputan anda tidak sesuai.')
        while True:
            flag = 0
            alamatCustomer = input('Silahkan masukkan alamat pelanggan : ')
            print(f'Alamat : {alamatCustomer}')
            while True:
                konfirmasiAlamat = input('Apakah anda sudah yakin alamatnya benar? [ya / tidak] : ')
                konfirmasiAlamatLower = konfirmasiAlamat.lower()
                if(konfirmasiAlamatLower == 'ya'):
                    flag = 1
                    break
                elif(konfirmasiAlamatLower == 'tidak'):
                    break
                else:
                    print('Maaf, inputan anda tidak sesuai.')
            if(flag == 1):
                break
        while True:
            noKTPCustomer = input('Silahkan masukkan nomor KTP pelanggan : ')
            if(noKTPCustomer.isdigit()):
                if(len(noKTPCustomer) == 17):
                    print(f'Nomor KTP : {noKTPCustomer}')
                    hasilCekNoKTP = cekDuplikasiNoKTP(noKTPCustomer)
                    if(hasilCekNoKTP == 1):
                        while True:
                            flag1 = 0
                            konfirmasiNoKTP = input('Apakah anda sudah yakin Nomor KTPnya benar? [ya / tidak] : ')
                            konfirmasiNoKTPLower = konfirmasiNoKTP.lower()
                            if(konfirmasiNoKTPLower == 'ya'):
                                flag1 = 1
                                break
                            elif(konfirmasiNoKTPLower == 'tidak'):
                                break
                            else:
                                print('Maaf, inputan anda tidak sesuai.')
                        if(flag1 == 1):
                            break
                else:
                    print('Maaf, inputan anda tidak sesuai.')
            else:
                print('Maaf, inputan anda tidak sesuai.')
        print(f'''
Data customer yang akan diinput:
Nama    : {namaCustomer}
Alamat  : {alamatCustomer}
No Ktp  : {noKTPCustomer}''')
        while True:
            flagDisini = 0
            validasiData = input('Apakah data pelanggan yang diinput sudah benar? [ya / tidak] : ')
            validasiDataLower = validasiData.lower()
            if(validasiDataLower == 'ya'):
                indexCustomer = 0
                statusSewa = 0
                newListCustomer = [namaCustomer, alamatCustomer, noKTPCustomer, statusSewa]
                listDataCustomer.append(newListCustomer)
                for i in range(len(listDataCustomer)):
                    if(noKTPCustomer == listDataCustomer[i][2]):
                        indexCustomer = i
                        return indexCustomer
                        break
                break
            elif(validasiDataLower == 'tidak'):
                flag2 = 0
                while True:
                    inputUlangDataCustomer = input('Apakah anda ingin melakukan input ulang data pelanggan? [ya / tidak] : ')
                    inputUlangDataCustomerLower = inputUlangDataCustomer.lower()
                    if(inputUlangDataCustomerLower == 'ya'):
                        flagDisini = 1
                        break
                    elif(inputUlangDataCustomerLower == 'tidak'):
                        flagDisini = 1
                        flag2 = 1
                        return -1
                        break
                    else:
                        print('Maaf, inputan anda tidak sesuai.')
            else:
                print('Maaf, inputan anda tidak sesuai.')
            if(flagDisini == 1):
                break
        if(flag2 == 1):
            return -1
            break

def sewaMobil(indexCustomer):
    global listDataPeminjaman
    global listData
    global listDataCustomer
    newListDataPeminjaman = []
    if(indexCustomer != -1):
        flag = 0
        while True:
            akanMenyewa = input('Apakah pelanggan akan melakukan penyewaan? [ya / tidak] : ')
            akanMenyewaLower = akanMenyewa.lower()
            if(akanMenyewaLower == 'ya'):
                flag = 1
                break
            elif(akanMenyewaLower == 'tidak'):
                break
            else:
                print('Maaf, inputan anda tidak sesuai.')
        if(flag == 1):
            while True:
                flagAkhir = 0
                pilihMobil = ''
                tampilSemuaData()
                # penentuPilihan = input('Silahkan tentukan anda memilih berdasarkan index atau plat mobil : ')
                penentuPilihanLower = 'index' # penentuPilihan.lower()
                if(penentuPilihanLower == 'index'):
                    pilihMobil = input('Silahkan pilih mobil mana yang ingin disewa : ')
                    if(pilihMobil.isdigit() and int(pilihMobil) < len(listData)):
                        pilihMobilInt = int(pilihMobil)
                        if(listData[pilihMobilInt][5] == 'Tersedia'):
                            print('Index\t|Merk\t|Nama\t|Tahun\t|Plat\t\t|Harga Sewa/Hari\t|Status')
                            print(f'{pilihMobilInt}\t|{listData[pilihMobilInt][0]}\t|{listData[pilihMobilInt][1]}\t|{listData[pilihMobilInt][2]}\t|{listData[pilihMobilInt][3]}\t|{listData[pilihMobilInt][4]}\t\t\t|{listData[pilihMobilInt][5]}')
                            while True:
                                flagKonfirmasiPilihan = 0
                                konfirmasiPilihan = input('Apakah benar mobil ini yang ingin disewa? [ya / tidak] : ')
                                konfirmasiPilihanLower = konfirmasiPilihan.lower()
                                if(konfirmasiPilihanLower == 'ya'):
                                    while True:
                                        flagBanyakHariSewa = 0
                                        banyakHariSewa = input('Silahkan masukkan berapa lama waktu sewa (hitungan hari) : ')
                                        if(banyakHariSewa.isdigit()):
                                            banyakHariSewaINT = int(banyakHariSewa)
                                            hargaSewaINT = int(listData[pilihMobilInt][4])
                                            totalBayar = banyakHariSewaINT * hargaSewaINT
                                            print(f'''
Nama Penyewa        : {listDataCustomer[indexCustomer][0]}
Nomor KTP Penyewa   : {listDataCustomer[indexCustomer][2]}
Mobil yang Disewa   :
                        Merk    : {listData[pilihMobilInt][0]}
                        Nama    : {listData[pilihMobilInt][1]}
                        Tahun   : {listData[pilihMobilInt][2]}
                        Plat    : {listData[pilihMobilInt][3]}
Harga Sewa/Hari     : {listData[pilihMobilInt][4]}
Jumlah Hari Sewa    : {banyakHariSewaINT}
Total Pembayaran    : {totalBayar}''')
                                            while True:
                                                flag1 = 0
                                                flag2 = 0
                                                flagKonfirmasiAkir = 0
                                                konfirmasiAkhir = input('Apakah data sudah sesuai? [ya / tidak] : ')
                                                konfirmasiAkhirLower = konfirmasiAkhir.lower()
                                                if(konfirmasiAkhirLower == 'ya'):
                                                    while True:
                                                        while True:
                                                            jumlahUangBayar = input('Masukkan jumlah uang untuk membayar : ')
                                                            if(jumlahUangBayar.isdigit):
                                                                jumlahUangBayarINT = int(jumlahUangBayar)
                                                                break
                                                            else:
                                                                print('Maaf, inputan anda tidak sesuai, hanya boleh mengandung angka')
                                                        if(jumlahUangBayarINT >= totalBayar):
                                                            listDataCustomer[indexCustomer][3] = 1
                                                            listData[pilihMobilInt][5] = 'Disewa'
                                                            newListDataPeminjaman = [listDataCustomer[indexCustomer][0], listDataCustomer[indexCustomer][2],
                                                                                     listData[pilihMobilInt][0], listData[pilihMobilInt][1], listData[pilihMobilInt][2],
                                                                                     listData[pilihMobilInt][3], listData[pilihMobilInt][4], banyakHariSewaINT, totalBayar]
                                                            listDataPeminjaman.append(newListDataPeminjaman)
                                                            print('Transaksi berhasil')
                                                            kembalian = jumlahUangBayarINT - totalBayar
                                                            print(f'Kembalian : {kembalian}\n')
                                                            flag1 = 1
                                                            flagBanyakHariSewa = 1
                                                            flagKonfirmasiPilihan = 1
                                                            flagAkhir = 1
                                                            break
                                                        elif(jumlahUangBayarINT < totalBayar):
                                                            print('Mohon maaf, uang anda tidak cukup.')
                                                            while True:
                                                                konfirmasiBayarUlang = input('Apakah anda ingin melakukan pembayaran ulang? [ya / tidak] : ')
                                                                konfirmasiBayarUlangLower = konfirmasiBayarUlang.lower()
                                                                if(konfirmasiBayarUlangLower == 'ya'):
                                                                    break
                                                                # BELUM SELESAI
                                                                elif(konfirmasiBayarUlangLower == 'tidak'):
                                                                    flag1 = 1
                                                                    flag2 = 1
                                                                    flagBanyakHariSewa = 1
                                                                    flagKonfirmasiPilihan = 1
                                                                    flagAkhir = 1
                                                                    break
                                                                else:
                                                                    print('Maaf, inputan anda tidak sesuai')
                                                        if(flag2 == 1):
                                                            break
                                                    if(flag1 == 1):
                                                        break
                                                elif(konfirmasiAkhirLower == 'tidak'):
                                                    while True:
                                                        inputUlang = input('Apakah anda ingin memilih ulang? [ya / tidak] : ')
                                                        inputUlangLower = inputUlang.lower()
                                                        if(inputUlangLower == 'ya'):
                                                            flagKonfirmasiAkir = 1
                                                            flagBanyakHariSewa = 1
                                                            flagKonfirmasiPilihan = 1
                                                            break
                                                        elif(inputUlangLower == 'tidak'):
                                                            flagKonfirmasiAkir = 1
                                                            flagBanyakHariSewa = 1
                                                            flagKonfirmasiPilihan = 1
                                                            flagAkhir = 1
                                                            break
                                                        else:
                                                            print('Maaf, inputan anda tidak sesuai.')
                                                    if(flagKonfirmasiAkir == 1):
                                                        break
                                                else:
                                                    print('Maaf, inputan anda tidak sesuai.')
                                            if(flagBanyakHariSewa == 1):
                                                break
                                        else:
                                            print('Maaf, inputan anda tidak sesuai.')
                                    if(flagKonfirmasiPilihan == 1):
                                        break
                                elif(konfirmasiPilihanLower == 'tidak'):
                                    while True:
                                        pilihUlang = input('Apakah anda ingin memilih ulang? [ya / tidak] : ')
                                        pilihUlangLower = pilihUlang.lower()
                                        if(pilihUlangLower == 'ya'):
                                            flagKonfirmasiPilihan = 1
                                            break
                                        elif(pilihUlangLower == 'tidak'):
                                            flagKonfirmasiPilihan = 1
                                            flagAkhir = 1
                                            break
                                    if(flagKonfirmasiPilihan == 1):
                                        break
                                else:
                                    print('Maaf, inputan anda tidak sesuai.')
                        elif(listData[pilihMobilInt][5] == 'Disewa'):
                            print('Index\t|Merk\t|Nama\t|Tahun\t|Plat\t\t|Harga Sewa/Hari\t|Status')
                            print(f'{pilihMobilInt}\t|{listData[pilihMobilInt][0]}\t|{listData[pilihMobilInt][1]}\t|{listData[pilihMobilInt][2]}\t|{listData[pilihMobilInt][3]}\t|{listData[pilihMobilInt][4]}\t\t\t|{listData[pilihMobilInt][5]}')
                            print('Maaf, mobil ini sedang disewa, sehingga tidak bisa menyewa mobil ini')
                            print('Jika terdapat kesalahan, mohon update datanya.')
                            while True:
                                menginputUlang = input('Apakah anda ingin memilih mobil lain? Jika tidak, akan kembali ke menu utama. [ya / tidak] :')
                                menginputUlangLower = menginputUlang.lower()
                                if(menginputUlangLower == 'ya'):
                                    break
                                elif(menginputUlangLower == 'tidak'):
                                    flagAkhir = 1
                                    break
                                else:
                                    print('Maaf, inputan anda tidak sesuai.')
                        if(flagAkhir == 1):
                            break

# Menu ke 6
def menuKe6():
    while True:
        print('''---Data Pelanggan dan Data Peminjaman---
              
              1. Menampilkan data pelanggan
              2. Update data pelanggan
              3. Hapus data pelanggan
              4. Menampilkan data peminjaman
              5. Hapus data peminjaman
              6. Kembali ke menu utama''')
        pilihan = input('Silahkan masukkan pilihan anda sesuai angka yang dituju [1 - 6] : ')
        if(pilihan == '1'):
            tampilDataCustomer()
        elif(pilihan == '2'):
            tampilSemuaDataCustomer()
            updateDataPelanggan()
        elif(pilihan == '3'):
            menuHapusDataPelanggan()
        elif(pilihan == '4'):
            tampilDataPeminjaman()
        elif(pilihan == '5'):
            menuHapusDataPeminjaman()
        elif(pilihan == '6'):
            break
# Menu 6 Submenu 1
def tampilDataCustomer():
    while True:
        print('''---Menampilkan Data Pelanggan---
              1. Menampilkan data berdasarkan index
              2. Menampilkan data berdasarkan nama
              3. Menampilkan data berdasarkan Nomor KTP
              4. Menampilkan semua data pelanggan
              5. Kembali ke menu sebelumnya''')
        pilihan = input('Silahkan masukkan pilihan anda sesuai angka yang dituju [1 - 5] : ')
        if(pilihan == '1'):
            tampilDataCustomerBerdasarkanIndex()
        elif(pilihan == '2'):
            namaPelanggan = input('Masukkan nama pelanggan yang ingin dicari : ')
            tampilDataCustomerBerdasarkanNama(namaPelanggan)
        elif(pilihan == '3'):
            flag = 0
            flag1 = 0
            while True:
                noKTP = input('Masukkan nomor KTP pelanggan yang ingin dicari : ')
                if(noKTP.isdigit() and len(noKTP) == 17):
                    flag = 1
                    break
                else:
                    print('Maaf, inputan anda tidak sesuai.')
                    while True:
                        inputUlang = input('Apakah anda ingin melakukan input ulang? [ya / tidak] : ')
                        inputUlangLower = inputUlang.lower()
                        if(inputUlangLower == 'ya'):
                            break
                        elif(inputUlangLower == 'tidak'):
                            flag1 = 1
                            break
                        else:
                            print('Maaf, inputan anda tidak sesuai.')
                if(flag1 == 1):
                    break
            if(flag == 1):
                tampilDataCustomerBerdasarkanNoKTP(noKTP)
        elif(pilihan == '4'):
            tampilSemuaDataCustomer()
        elif(pilihan == '5'):
            break

def tampilDataCustomerBerdasarkanIndex():
    flag1 = 0
    while True:
        inputUlang = ''
        indexCustomer = input('Masukkan index dari data yang ingin dicari : ')
        if(indexCustomer.isdigit() == True and int(indexCustomer) < len(listDataCustomer)):
            indexCustomerINT = int(indexCustomer)
            print('Index\t|Nama\t|Tahun\t|No KTP')
            print(f'{indexCustomerINT}\t|{listDataCustomer[indexCustomerINT][0]}\t|{listDataCustomer[indexCustomerINT][1]}\t|{listDataCustomer[indexCustomerINT][2]}')
            break
        elif(indexCustomer.isdigit() == True and int(indexCustomer) >= len(listDataCustomer)):
            print('Maaf, data yang anda cari tidak ditemukan')
            while True:
                inputUlang = input('Apakah anda ingin mencari ulang? [ya / tidak] : ')
                inputUlangLower = inputUlang.lower()
                if(inputUlangLower == 'tidak'):
                    flag1 = 1
                    break
                elif(inputUlangLower == 'ya'):
                    break
                else:
                    print('Maaf inputan yang anda masukkan tidak sesuai.')
            if(flag1 == 1):
                break
        else:
            print('Maaf inputan yang anda masukkan tidak sesuai.')

def tampilDataCustomerBerdasarkanNama(namaPelanggan):
    global listDataCustomer
    flag = 0
    namaData = ''
    print('Index\t|Nama\t|Tahun\t|No KTP')
    for i in range(len(listDataCustomer)):
        namaData = listDataCustomer[i][0]
        namaDataLower = namaData.lower()
        if(namaPelanggan in namaDataLower):
            flag = 1
            print(f'{i}\t|{listDataCustomer[i][0]}\t|{listDataCustomer[i][1]}\t|{listDataCustomer[i][2]}')
    if(flag == 0):
        print(f'\nTidak ada data pelanggan dengan nama {namaPelanggan}\n')

def tampilDataCustomerBerdasarkanNoKTP(noKTP):
    flag = 0
    for i in range(len(listDataCustomer)):
        if(noKTP == listDataCustomer[i][2]):
            print('Index\t|Nama\t|Tahun\t|No KTP')
            print(f'{i}\t|{listDataCustomer[i][0]}\t|{listDataCustomer[i][1]}\t|{listDataCustomer[i][2]}')
            flag = 1
            break
    if(flag == 0):
        print('\nTidak ada data pelanggan dengan nomor KTP tersebut\n')

def tampilSemuaDataCustomer():
    print('Index\t|Nama\t|Tahun\t|No KTP')
    for i in range(len(listDataCustomer)):
        print(f'{i}\t|{listDataCustomer[i][0]}\t|{listDataCustomer[i][1]}\t|{listDataCustomer[i][2]}')
# =========================================================================================

# Menu 6 Submenu 2
def updateDataPelanggan():
    global listDataCustomer
    while True:
        bagianYangdiUpdate = 0
        hasilUpdate = 0
        idxUpdtSTR = input('Silahkan pilih index data yang ingin diubah : ')
        if(idxUpdtSTR.isdigit() == True and int(idxUpdtSTR) < len(listDataCustomer)):
            idxUpdtINT = int(idxUpdtSTR)
            print('Nama\t|Alamat\t|Nomor KTP')
            print(f'{listDataCustomer[idxUpdtINT][0]}\t|{listDataCustomer[idxUpdtINT][1]}\t|{listDataCustomer[idxUpdtINT][2]}')
            dataUpdate = input('Pilih data mana yang ingin diupdate : ')
            dataUpdateLower = dataUpdate.lower()
            if(dataUpdateLower == 'nama'):
                flag = 0
                bagianYangdiUpdate = 0
                namaUpdate = ''
                while True:
                    namaUpdate = input('Masukkan nama pelanggan yang baru : ')
                    print('Nama\t|Alamat\t|Nomor KTP')
                    print(f'{namaUpdate}\t|{listDataCustomer[idxUpdtINT][1]}\t|{listDataCustomer[idxUpdtINT][2]}')
                    hasilUpdate = validasiDataBaruPelanggan(idxUpdtINT, bagianYangdiUpdate, namaUpdate)
                    if(hasilUpdate == 1):
                        flag = 1
                        break
            elif(dataUpdateLower == 'alamat'):
                flag = 0
                bagianYangdiUpdate = 1
                alamatUpdate = ''
                while True:
                    alamatUpdate = input('Masukkan alamat pelanggan yang baru : ')
                    print('Nama\t|Alamat\t|Nomor KTP')
                    print(f'{listDataCustomer[idxUpdtINT][0]}\t|{alamatUpdate}\t|{listDataCustomer[idxUpdtINT][2]}')
                    hasilUpdate = validasiDataBaruPelanggan(idxUpdtINT, bagianYangdiUpdate, alamatUpdate)
                    if(hasilUpdate == 1):
                        flag = 1
                        break
            elif(dataUpdateLower == 'nomor ktp' or dataUpdateLower == 'ktp'):
                flag = 0
                bagianYangdiUpdate = 2
                noKTPUpdate = ''
                while True:
                    noKTPUpdate = input('Masukkan nomor KTP pelanggan yang baru : ')
                    hasilCekDuplikasiKTP = cekDuplikasiNoKTP(noKTPUpdate)
                    if(noKTPUpdate.isdigit() and len(noKTPUpdate) == 17 and hasilCekDuplikasiKTP == 1):
                        print('Nama\t|Alamat\t|Nomor KTP')
                        print(f'{listDataCustomer[idxUpdtINT][0]}\t|{listDataCustomer[idxUpdtINT][1]}\t|{noKTPUpdate}')
                        hasilUpdate = validasiDataBaruPelanggan(idxUpdtINT, bagianYangdiUpdate, noKTPUpdate)
                        if(hasilUpdate == 1):
                            flag = 1
                            break
                    else:
                        print('Maaf, inputan anda tidak sesuai.')
        if(flag == 1):
            break

def validasiDataBaruPelanggan(idxUpdt, bagianYangdiUpdate, inputanUpdate):
    global listDataCustomer
    hasilPengecekkan = ''
    flag = 0
    nilai = 0
    while True:
        hasilPengecekkan = input('Apakah data yang anda isikan sudah benar? [ya / tidak] : ')
        if(hasilPengecekkan == 'ya'):
            listDataCustomer[idxUpdt][bagianYangdiUpdate] = inputanUpdate
            nilai = 1
            break
        elif(hasilPengecekkan == 'tidak'):
            while True:
                inputUlang = input('Apakah anda ingin memasukkan ulang? [ya / tidak] : ')
                if(inputUlang == 'ya'):
                    flag = 1
                    nilai = 0
                    break
                elif(inputUlang == 'tidak'):
                    flag = 1
                    nilai = 1
                    break
                else:
                    print('Maaf inputan yang anda masukkan tidak sesuai.')
        else:
            print('Maaf inputan yang anda masukkan tidak sesuai.')
        if(flag == 1):
            break
    return nilai
# =========================================================================================

# Menu 6 Submenu 3
def menuHapusDataPelanggan():
    while True:
        hasilCek = 0
        print('''---Hapus Data Pelanggan---
              1. Hapus data pelanggan berdasarkan index
              2. Hapus semua data pelanggan
              3. Kembali ke menu sebelumnya''')
        pilihan = input('Silahkan masukkan pilihan anda sesuai angka yang dituju [1 - 3] : ')
        if(pilihan == '1'):
            hasilCek = cekListDataCustomerBerisiAtauTidak()
            if(hasilCek == 0):
                hapusDataPelangganIndex()
        if(pilihan == '2'):
            hasilCek = cekListDataCustomerBerisiAtauTidak()
            if(hasilCek == 0):
                hapusSemuaDataPelanggan()
        if(pilihan == '3'):
            break

def cekListDataCustomerBerisiAtauTidak():
    global listDataCustomer
    if(len(listDataCustomer) == 0):
        print('\nMaaf, list data pelanggan saat ini sedang kosong, tidak ada yang bisa dihapus\n')
        return 1
    return 0

def hapusDataPelangganIndex():
    global listDataCustomer
    tampilSemuaDataCustomer()
    while True:
        flag = 0
        flagKeluarDelete = 0
        indexHapus = input('Masukkan index data mana yang ingin dihapus : ')
        if(indexHapus.isdigit() and int(indexHapus) < len(listDataCustomer)):
            indexHapusINT = int(indexHapus)
            flag = 1
        else:
            print('Maaf, inputan yang anda masukkan tidak sesuai')
            while True:
                keluarMenu = input('Apakah anda ingin keluar dari menu delete? [ya / tidak]')
                keluarMenuLower = keluarMenu.lower()
                if(keluarMenuLower == 'ya'):
                    flagKeluarDelete = 1
                    break
                elif(keluarMenuLower == 'tidak'):
                    break
                else:
                    print('Maaf, inputan yang anda masukkan tidak sesuai.')
        if(flag == 1):
            if(listDataCustomer[indexHapusINT][3] == 0):
                print('Nama\t|Alamat\t|Nomor KTP')
                print(f'{listDataCustomer[indexHapusINT][0]}\t|{listDataCustomer[indexHapusINT][1]}\t|{listDataCustomer[indexHapusINT][2]}')
                while True:
                    validasiHapus = input('Apakah anda yakin ingin menghapus data ini? [ya / tidak] : ')
                    validasiHapus.lower()
                    if(validasiHapus == 'ya'):
                        del listDataCustomer[indexHapusINT]
                        flagKeluarDelete = 1
                        break
                    elif(validasiHapus == 'tidak'):
                        while True:
                            inputUlang = input('Apakah anda ingin memilih ulang data yang ingin dihapus? [ya / tidak] : ')
                            inputUlangLower = inputUlang.lower()
                            if(inputUlangLower == 'ya'):
                                break
                            elif(inputUlangLower == 'tidak'):
                                flagKeluarDelete = 1
                                break
                            else:
                                print('Maaf, inputan yang anda masukkan tidak sesuai.')
                        break
                    else:
                        print('Maaf, inputan yang anda masukkan tidak sesuai.')
            elif(listDataCustomer[indexHapusINT][3] == 1):
                print('Nama\t|Alamat\t|Nomor KTP')
                print(f'{listDataCustomer[indexHapusINT][0]}\t|{listDataCustomer[indexHapusINT][1]}\t|{listDataCustomer[indexHapusINT][2]}')
                print('Maaf, anda tidak dapat menghapus data ini, karena pelanggan ini sedang menyewa mobil')
                print('Jika terdapat kesalahan pada data, mohon diupdate data peminjaman terlebih dahulu.')
                while True:
                    inputUlang = input('Apakah anda ingin memilih ulang data yang ingin dihapus? [ya / tidak] : ')
                    inputUlangLower = inputUlang.lower()
                    if(inputUlangLower == 'ya'):
                        break
                    elif(inputUlangLower == 'tidak'):
                        flagKeluarDelete = 1
                        break
                    else:
                        print('Maaf, inputan yang anda masukkan tidak sesuai.')
        if(flagKeluarDelete == 1):
            break

def hapusSemuaDataPelanggan():
    global listDataCustomer
    flagStatusPelanggan = 0
    while True:
        konfirmasi = input('Apakah anda yakin ingin menghapus semua data? [ya / tidak] : ')
        konfirmasiLower = konfirmasi.lower()
        if(konfirmasiLower == 'ya'):
            for i in range(len(listDataCustomer)):
                if(listDataCustomer[i][3] == 1):
                    flagStatusPelanggan = 1
                    break
            if(flagStatusPelanggan == 1):
                print('Mohon maaf, terdapat data yang sedang dalam status Disewa, sehingga tidak bisa dihapus')
                break
            elif(flagStatusPelanggan == 0):
                listDataCustomer.clear()
                break
        elif(konfirmasiLower == 'tidak'):
            break
        else:
            print('Maaf, inputan anda tidak sesuai.')
# =========================================================================================

# Menu 6 Submenu 4
def tampilDataPeminjaman():
    while True:
        print('''---Menampilkan Data Peminjaman---
              1. Menampilkan semua data peminjaman
              2. Menampilkan data peminjaman berdasarkan plat mobil
              3. Menampilkan data peminjaman berdasarkan no KTP pelanggan
              4. Kembali ke menu sebelumnya''')
        pilihan = input('Silahkan masukkan pilihan anda sesuai dengan angka yang dituju [1 - 4] : ')
        if(pilihan == '1'):
            tampilSemuaDataPeminjaman()
        elif(pilihan == '2'):
            tampilDataPeminjamanBerdasarkanPlatMobil()
        elif(pilihan == '3'):
            tampilDataPeminjamanBerdasarkanNoKTP()
        elif(pilihan == '4'):
            break

def tampilSemuaDataPeminjaman():
    print('Index\t|Nama\t|No KTP\t|Merk Mobil\t|Nama Mobil\t|Tahun Mobil\t|Plat Mobil\t|Harga Sewa/Hari\t|Jumlah Hari Sewa\t|Total')
    for i in range(len(listDataPeminjaman)):
        print(f'{i}\t|{listDataPeminjaman[i][0]}\t|{listDataPeminjaman[i][1]}\t|{listDataPeminjaman[i][2]}\t|{listDataPeminjaman[i][3]}\t|{listDataPeminjaman[i][4]}\t|{listDataPeminjaman[i][5]}\t|{listDataPeminjaman[i][6]}\t|{listDataPeminjaman[i][7]}\t|{listDataPeminjaman[i][8]}\t')

def tampilDataPeminjamanBerdasarkanPlatMobil():
    while True:
        platKetemu = 0
        flag = 0
        inputanPlatMobil = input('Masukkan plat mobil untuk data yang dicari : ')
        hasilCek = cekPlatMobilUpdt(inputanPlatMobil)
        if(hasilCek == 1):
            for i in range(len(listDataPeminjaman)):
                if(inputanPlatMobil == listDataPeminjaman[i][5]):
                    print('Nama\t|No KTP\t|Merk Mobil\t|Nama Mobil\t|Tahun Mobil\t|Plat Mobil\t|Harga Sewa/Hari\t|Jumlah Hari Sewa\t|Total')
                    print(f'{listDataPeminjaman[i][0]}\t|{listDataPeminjaman[i][1]}\t|{listDataPeminjaman[i][2]}\t|{listDataPeminjaman[i][3]}\t|{listDataPeminjaman[i][4]}\t|{listDataPeminjaman[i][5]}\t|{listDataPeminjaman[i][6]}\t|{listDataPeminjaman[i][7]}\t|{listDataPeminjaman[i][8]}\t')
                    platKetemu = 1
                    flag = 1
                    break
            if(platKetemu == 0):
                print(f'Data dengan plat mobil {inputanPlatMobil} tidak ditemukan')
                break
            if(flag == 1):
                break

def tampilDataPeminjamanBerdasarkanNoKTP():
    while True:
        hasilCek = 0
        noKTPKetemu = 0
        flag = 0
        while True:
            inputanNoKTP = input('Masukkan no KTP pelanggan untuk data yang dicari : ')
            if(inputanNoKTP.isdigit() and len(inputanNoKTP) == 17):
                hasilCek = 1
                break
            else:
                print('Maaf, inputan anda tidak sesuai.')
        if(hasilCek == 1):
            for i in range(len(listDataPeminjaman)):
                if(inputanNoKTP == listDataPeminjaman[i][1]):
                    print('Nama\t|No KTP\t|Merk Mobil\t|Nama Mobil\t|Tahun Mobil\t|Plat Mobil\t|Harga Sewa/Hari\t|Jumlah Hari Sewa\t|Total')
                    print(f'{listDataPeminjaman[i][0]}\t|{listDataPeminjaman[i][1]}\t|{listDataPeminjaman[i][2]}\t|{listDataPeminjaman[i][3]}\t|{listDataPeminjaman[i][4]}\t|{listDataPeminjaman[i][5]}\t|{listDataPeminjaman[i][6]}\t|{listDataPeminjaman[i][7]}\t|{listDataPeminjaman[i][8]}\t')
                    noKTPKetemu = 1
                    flag = 1
                    break
            if(noKTPKetemu == 0):
                print(f'Data dengan plat mobil {inputanNoKTP} tidak ditemukan')
                break
            if(flag == 1):
                break

# Menu 6 Submenu 5
def menuHapusDataPeminjaman():
    while True:
        hasilCek = 0
        print('''---Hapus Data Peminjaman---
              1. Hapus data peminjaman berdasarkan index
              2. Kembali ke menu sebelumnya''')
        pilihan = input('Silahkan masukkan pilihan anda sesuai angka yang dituju [1 - 2] : ')
        if(pilihan == '1'):
            hasilCek = cekListDataPeminjamanBerisiAtauTidak()
            if(hasilCek == 0):
                hapusDataPeminjamanIndex()
        elif(pilihan == '2'):
            break

def cekListDataPeminjamanBerisiAtauTidak():
    global listDataPeminjaman
    if(len(listDataPeminjaman) == 0):
        print('\nMaaf, list data peminjaman saat ini sedang kosong, tidak ada yang bisa dihapus\n')
        return 1
    return 0

def hapusDataPeminjamanIndex():
    global listDataPeminjaman
    global listDataCustomer
    global listData
    tampilSemuaDataPeminjaman()
    while True:
        flag = 0
        flagKeluarDelete = 0
        indexHapus = input('Masukkan index data mana yang ingin dihapus : ')
        if(indexHapus.isdigit() and int(indexHapus) < len(listDataPeminjaman)):
            indexHapusINT = int(indexHapus)
            flag = 1
        else:
            print('Maaf, inputan yang anda masukkan tidak sesuai')
            while True:
                keluarMenu = input('Apakah anda ingin keluar dari menu delete? [ya / tidak]')
                keluarMenuLower = keluarMenu.lower()
                if(keluarMenuLower == 'ya'):
                    flagKeluarDelete = 1
                    break
                elif(keluarMenuLower == 'tidak'):
                    break
                else:
                    print('Maaf, inputan yang anda masukkan tidak sesuai.')
        if(flag == 1):
            print('Nama\t|No KTP\t|Merk Mobil\t|Nama Mobil\t|Tahun Mobil\t|Plat Mobil\t|Harga Sewa/Hari\t|Jumlah Hari Sewa\t|Total')
            print(f'{listDataPeminjaman[indexHapusINT][0]}\t|{listDataPeminjaman[indexHapusINT][1]}\t|{listDataPeminjaman[indexHapusINT][2]}\t|{listDataPeminjaman[indexHapusINT][3]}\t|{listDataPeminjaman[indexHapusINT][4]}\t|{listDataPeminjaman[indexHapusINT][5]}\t|{listDataPeminjaman[indexHapusINT][6]}\t|{listDataPeminjaman[indexHapusINT][7]}\t|{listDataPeminjaman[indexHapusINT][8]}\t')
            while True:
                flagPinjamanLain = 0
                validasiHapus = input('Apakah anda yakin ingin menghapus data ini dan pelanggan sudah selesai waktunya dalam menyewa mobil? [ya / tidak] : ')
                validasiHapus.lower()
                if(validasiHapus == 'ya'):
                    for i in range(len(listDataPeminjaman)):
                        if(listDataPeminjaman[indexHapusINT][1] == listDataPeminjaman[i][1] and listDataPeminjaman[indexHapusINT][5] != listDataPeminjaman[i][5]):
                            flagPinjamanLain = 1
                    for i in range(len(listData)):
                        if(listDataPeminjaman[indexHapusINT][5] == listData[i][3]):
                            listData[i][5] = 'Tersedia'
                            break
                    if(flagPinjamanLain == 0):
                        for i in range(len(listDataCustomer)):
                            if(listDataPeminjaman[indexHapusINT][1] == listDataCustomer[i][2]):
                                listDataCustomer[i][3] = 0
                                break
                    del listDataPeminjaman[indexHapusINT]
                    flagKeluarDelete = 1
                    break
                elif(validasiHapus == 'tidak'):
                    while True:
                        inputUlang = input('Apakah anda ingin memilih ulang data yang ingin dihapus? [ya / tidak] : ')
                        inputUlangLower = inputUlang.lower()
                        if(inputUlangLower == 'ya'):
                            break
                        elif(inputUlangLower == 'tidak'):
                            flagKeluarDelete = 1
                            break
                        else:
                            print('Maaf, inputan yang anda masukkan tidak sesuai.')
                    break
                else:
                    print('Maaf, inputan yang anda masukkan tidak sesuai.')
        if(flagKeluarDelete == 1):
            break

inputan = ''

while True :
    hasilCekDataMobil = 0
    menu()
    inputan = input('Pilih menu yang ingin anda tuju sesuai dengan angkanya [1 - 7] : ')

    if(inputan == '1'):
        menuTambahMobil()
        tampilSemuaData()
    elif(inputan == '2'):
        menuKe2()
    elif(inputan == '3'):
        hasilCekDataMobil = cekListMobilBerisiAtauTidak()
        if(hasilCekDataMobil == 0):
            tampilSemuaData()
            updateList()
    elif(inputan == '4'):
        menuKe4()
    elif(inputan == '5'):
        hasilCekDataMobil = cekListMobilBerisiAtauTidak()
        if(hasilCekDataMobil == 0):
            menuKe5()
        elif(hasilCekDataMobil == 1):
            print('Anda harus mengisi list data mobil terlebih dahulu sebelum melakukan menu ini\n')
    elif(inputan == '6'):
        menuKe6()
    elif(inputan == '7'):
        break
    else:
        print('Mohon maaf, inputan yang anda masukkan tidak sesuai.')