# untuk mendefinisikan library yang akan kita pakai nanti
import mysql.connector
import os
from prettytable import PrettyTable

os.system('cls')

mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = ''
)

mycursor = mydb.cursor()

# ========================================================================================
# membuat fungsi yang nantinya akan kita pakai
# ========================================================================================

# ---------------------------------------------------------------------------------------
# bagian bagian untuk memanipulasi database
# ---------------------------------------------------------------------------------------

# membuat perintah lagi atau tidak
def yesorno():
    pass
    # ya = input('lagi (y/t) : ')
    # if ya != 'y':
    #     break
    #     print('terima kasih')
        
    
# membuat fungsi melihat database
def melihatdatabase():
    os.system('cls')

    mycursor.execute('show databases')

    tabel1 = PrettyTable(['databases'])
    
    for j in mycursor:
        
        tabel1.add_row([j])
    
    print(tabel1)


# membuat database
def membuatdatabase():
    try:
        os .system('cls')
        print('jika nama database mengandung spasi maka diganti dengan underscore ( _ )')
        nama_db = input('masukkan nama database : ')
        sql = 'create database {}'.format(nama_db)
        mycursor.execute(sql)
        print(mycursor)
    except:
        print('nama yang dimasukkan tidak bisa dijadikan database')

# menghapus database 
def menghapusdatabase():
    try:
        os.system('cls')
        melihatdatabase()

        pilih = input('tuliskan database mana yang ingin dihapus : ')

        mycursor.execute('drop database {}'.format(pilih))

        print(mycursor)
    except:
        print('nama yang dimasukkan tidak ada didalam database')

# tabel pil 1 
def tabelpilihan(a):
    tabelpil1 = PrettyTable(['no','daftar pilihan'])
    # menampilkan pilihan ke-1
    for i in range(len(a)):
        if i == len(a)-1:
            tabelpil1.add_row(['0',a[i]])
            break
        tabelpil1.add_row([i+1,a[i]])
    print(tabelpil1)

# ---------------------------------------------------------------------------------------


# ---------------------------------------------------------------------------------------
# fungsi fungsi untuk memanipulasi table
# ---------------------------------------------------------------------------------------

# melihat table
def melihattable():
    os.system('cls')
    mycursor.execute('show tables')
    tabel1 = PrettyTable(['tables'])
    for i in mycursor:
        tabel1.add_row([i])
    print(tabel1)

# membuat table
def membuattable():
    os.system('cls')
    mycursor.execute('show tables')
    for k in mycursor:
        print(k)
    nabel = input('masukkan nama tabel : ')

    

    tipedata = ['int','text','enum("laki-laki","perempuan")','timestamp']

    pilihan = ['untuk angka','untuk huruf','untuk jenis kelamin','untuk tanggal']

    angka = 1

    ya = 'y'

    while ya == 'y':
        
        if angka == 1:
            try:
                print('-'*50,'\napa bila nama kolom ada spasinya maka diganti dengan underscore( _ )\n','-'*50)
                tapil = PrettyTable(['no','daftar pilihan'])
                a = input('masukkan kolom ke-%s : '%(angka))
                print('-'*50)

                print('kolom yang dipakai untuk apa')

                for i in range(len(pilihan)):
                    tapil.add_row([i+1,pilihan[i]])
                print(tapil)
                while True:
                    try:    
                        b = int(input('masukkan pilihan : '))
                        print('-'*50)
                        break
                    except:
                        print('pilihan yang dimasukkan harus angka')
                        continue

                for j in range(len(tipedata)):
                    if b-1 == 0:
                        bb = tipedata[j]

                        while True:
                            try:
                                c = int(input('jika data kosong apa yang ingin anda isikan : '))
                                print('-'*50)
                                break
                            except:
                                print('isi yang dimasukkan harus angka')
                                continue
                        
                        mycursor.execute('create table %s(%s %s not null default %i)'%(nabel,a,bb,c))

                        print('-'*50)
                        d = input('apakah ingin di beri primary key (y/t) : ')
                        print('-'*50)
                        if d == 'y':
                            mycursor.execute('alter table %s add primary key (%s)'%(nabel,a))
                        angka += 1
                        ya = input('ingin membuat kolom lagi (y/t) : ')
                        if ya != 'y':
                            break
                        break
                        
                    elif b-1 == 1:
                        bb = tipedata[1]
                        
                        c = input('jika data kosong apa yang ingin anda isikan : ')
                        print('-'*50)

                        hasil = 'create table {}({} {} not null default "{}")'.format(nabel,a,bb,c)
                        
                        mycursor.execute(hasil)
                        print('-'*50)
                        d = input('apakah ingin di beri primary key (y/t) : ')
                        print('-'*50)
                        if d == 'y':
                            mycursor.execute('alter table %s add primary key (%s)'%(nabel,a))
                        angka += 1
                        ya = input('ingin membuat kolom lagi (y/t) : ')
                        if ya != 'y':
                            break
                        break
                        
                    elif b-1 == 2:
                        bb = tipedata[2]

                        c = input('jika data kosong apa yang ingin anda isikan : ')
                        print('-'*50)

                        hasil   = 'create table {}({} {} not null default "{}")'.format(nabel,a,bb,c)

                        mycursor.execute(hasil)
                        print('-'*50)
                        d = input('apakah ingin di beri primary key (y/t) : ')
                        print('-'*50)
                        if d == 'y':
                            mycursor.execute('alter table %s add primary key (%s)'%(nabel,a))
                        angka += 1
                        ya = input('ingin membuat kolom lagi (y/t) : ')
                        if ya != 'y':
                            break

                        break

                    elif b-1 == 3:
                        bb = tipedata[3]

                        hasil = 'create table {}({} {} not null default current_timestamp)'.format(nabel,a,bb)
                        mycursor.execute(hasil)
                        print('-'*50)
                        d = input('apakah ingin di beri primary key (y/t) : ')
                        print('-'*50)
                        if d == 'y':
                            mycursor.execute('alter table %s add primary key (%s)'%(nabel,a))
                        angka += 1
                        ya = input('ingin membuat kolom lagi (y/t) : ')
                        if ya != 'y':
                            break
                        break
                    else:
                        print('kode yang dimasukkan salah')
                        break
            except:
                print('-'*50)
                print('kolom yang dimasukkan salah, menggunakan angka saja, atau dengan spasi')
                print('-'*50)
                ya = input('ingin membuat kolom lagi (y/t) : ')
                if ya != 'y':
                    break
        
        else:
            try:
                print('-'*50,'\napa bila nama kolom ada spasinya maka diganti dengan underscore( _ )\n','-'*50)
                a = input('masukkan kolom ke-%s : '%(angka))
                
                tapil1 = PrettyTable(['no','daftar pilihan'])
                print('kolom yang dipakai untuk apa')
                for i in range(len(pilihan)):
                    tapil1.add_row([i+1,pilihan[i]])
                print(tapil1)
                while True:
                    try:    
                        b = int(input('masukkan pilihan : '))
                        break
                    except:
                        print('pilihan yang dimasukkan harus angka')
                        continue
                print('-'*50)
                for j in range(len(tipedata)):
                    if b-1 == 0:
                        bb = tipedata[j]

                        while True:
                            try:
                                c = int(input('jika data kosong apa yang ingin anda isikan : '))
                                print('-'*50)
                                break
                            except:
                                print('isi yang dimasukkan harus angka')
                                continue
                        
                        hasil = 'alter table %s add %s %s not null default %i'%(nabel,a,bb,c)


                        mycursor.execute(hasil)
                        


                        d = input('apakah ingin di beri primary key (y/t) : ')
                        c = int(input('jika data kosong apa yang ingin anda isikan : '))
                        print('-'*50)
                        if d == 'y':
                            mycursor.execute('alter table %s add primary key (%s)'%(nabel,a))
                        else:
                            pass
                        angka += 1
                        ya = input('ingin membuat kolom lagi (y/t) : ')
                        print('-'*50)
                        if ya != 'y':
                            break
                        break
                        
                    elif b-1 == 1:
                        bb = tipedata[1]
                        
                        c = input('jika data kosong apa yang ingin anda isikan : ')
                        print('-'*50)
                        hasil = 'alter table {} add {} {} not null default "{}"'.format(nabel,a,bb,c)
                        
                        
                        mycursor.execute(hasil)
                        


                        d = input('apakah ingin di beri primary key (y/t) : ')
                        print('-'*50)
                        if d == 'y':
                            mycursor.execute('alter table %s add primary key (%s)'%(nabel,a))
                        else:
                            pass
                        angka += 1
                        ya = input('ingin membuat kolom lagi (y/t) : ')
                        print('-'*50)
                        if ya != 'y':
                            break
                        break
                        
                    elif b-1 == 2:
                        bb = tipedata[2]

                        c = input('jika data kosong apa yang ingin anda isikan : ')
                        print('-'*50)

                        hasil   = 'alter table {} add {} {} not null default "{}"'.format(nabel,a,bb,c)
                        
                        mycursor.execute(hasil)
                        


                        d = input('apakah ingin di beri primary key (y/t) : ')
                        print('-'*50)
                        if d == 'y':
                            mycursor.execute('alter table %s add primary key (%s)'%(nabel,a))
                        else:
                            pass
                        angka += 1
                        ya = input('ingin membuat kolom lagi (y/t) : ')
                        if ya != 'y':
                            break
                        
                        

                        break

                    elif b-1 == 3:
                        bb = tipedata[3]

                        hasil = 'alter table {} add {} {} not null default current_timestamp'.format(nabel,a,bb)
                        
                        mycursor.execute(hasil)
                        print(mycursor)


                        d = input('apakah ingin di beri primary key (y/t) : ')
                        if d == 'y':
                            mycursor.execute('alter table %s add primary key (%s)'%(nabel,a))
                        else:
                            pass
                        angka += 1
                        ya = input('ingin membuat kolom lagi (y/t) : ')
                        if ya != 'y':
                            break
                        break
                    else:
                        print('tidak ada pilihan')
                        break
            except:
                print('kolom yang dimasukkan salah, menggunakan angka saja, atau dengan spasi')
                ya = input('ingin membuat kolom lagi (y/t) : ')
                if ya != 'y':
                    break
            

# menghapus table-
def menghapustable():
    try:
        os.system('cls')
        melihattable()

        pilih = input('tuliskan table mana yang ingin dihapus : ')

        mycursor.execute('drop table {}'.format(pilih))

        print(mycursor)
    except:
        print('nama yang dimasukkan tidak ada didalam table')
# melihat struktur kolom
def strukturkolom():
    os.system('cls')

    melihattable()
    tabel6 = PrettyTable(['field','type','null','key','default','extra'])
    try:
        tablee = input('masukkan nama table : ')
        mycursor.execute('desc %s'%(tablee))
        for i in mycursor:
            tabel6.add_row([i[0],i[1],i[2],i[3],i[4],i[5]])
        print(tabel6)
        # for i in mycursor:
        #     tabel.add_row([i[0],i[1],i[2],i[3].i[4],i[5]])
        # print(tabel)
    except:
        print('tabel yang dimasukkan tidak ada')

# melihat cara membuat kolom
def caramembuatkolom():
    os.system('cls')

    melihattable()
    tabel7 = PrettyTable(['struktur cara membuat tabelnya'])
    try:
        tablee = input('masukkan nama table : ')
        mycursor.execute('show create table %s'%(tablee))
        print(mycursor)
        for i in mycursor:
            for j in range(len(i)):
                if i[j] == i[0]:
                    tabel7.add_row(['---------------\nnama tabel : %s\n---------------'%(i[j])])
                    continue
                tabel7.add_row([i[j]])
        
        print(tabel7)
        

    except:
        print('tabel yang dimasukkan tidak ada')
# ---------------------------------------------------------------------------------------

#  memanipulasi kolom
def menampilkankolom(namatabel):
    ta = PrettyTable(['nama kolom','type','null','key','default','tambahan'])
    mycursor.execute('desc %s'%(namatabel))

    for i in mycursor:
        ta.add_row([i[0],i[1],i[2],i[3],i[4],i[5]])
    print(ta)

# menambah kolom
def menambahkolom():
    os.system('cls')
    mycursor.execute('show tables')

    tipedata = ['int','text','enum("laki-laki","perempuan")','timestamp']

    pilihan = ['untuk angka','untuk huruf','untuk jenis kelamin','untuk tanggal']

    tabl = []

    a = 0
    for i in mycursor:
        tabl.append(i[a])
    yaa = 'y'
    while yaa == 'y':
        try:
            os.system('cls')
            t = PrettyTable(['no','nama tabel'])
            
            for j in range(len(tabl)):
                t.add_row([j+1,tabl[j]])
            print(t)

            

            namatable = input('masukkan nama table yang dipilih : ')

            for k in range(len(tabl)):
                
                
                if namatable == tabl[k]:
                    ya = 'y'
                    while ya == 'y':
                        os.system('cls')
                        menampilkankolom(namatable)
                        print('ket : jika nama kolom ada spasinya maka diganti dengan underscore( _ )')
                        kolombaru = input('masukkan nama kolom baru : ')

                        c = PrettyTable(['no','daftar pilihan'])
                        for l in range(len(pilihan)):
                            c.add_row([l+1,pilihan[l]])
                        print(c)
                        
                        while True:
                            try:
                                tipdat = int(input('pilih tipe data : '))
                                break
                            except:
                                print('pilihan yang dimasukkan harus angka')
                                continue
                        
                        
                        if tipdat-1 == 0:

                            while True:
                                try:
                                    defalt = int(input('jika data kosong apa yang ingin diisikan : '))
                                    break
                                except:
                                    print('isi yang dimasukkan harus angka')
                                    continue
                                
                            mycursor.execute('alter table %s add %s %s not null default %s'%(namatable,kolombaru,tipedata[0],defalt))
                            
                            ya = input('ingin menambah kolom lagi (y/t) : ')
                            if ya != 'y':
                                break
                        elif tipdat-1 == 1:
                                
                            defalt = input('jika data kosong apa yang ingin diisikan : ')
                            mycursor.execute('alter table %s add %s %s not null default "%s"'%(namatable,kolombaru,tipedata[1],defalt))
                            
                            

                            ya = input('ingin menambah kolom lagi (y/t) : ')
                            if ya != 'y':
                                break
                            else:
                                continue
                                

                        elif tipdat-1 == 2:
                            defalt = input('jika data kosong apa yang ingin diisikan : ')

                            mycursor.execute('alter table %s add %s %s not null default "%s"'%(namatable,kolombaru,tipedata[2],defalt))

                            

                            ya = input('ingin menambah kolom lagi (y/t) : ')
                            if ya != 'y':
                                break
                            
                        elif tipdat-1 == 3:

                            mycursor.execute('alter table %s add %s %s not null default current_timestamp'%(namatable,kolombaru,tipedata[3]))

                            


                            yaa = input('ingin menambah kolom lagi (y/t) : ')
                            if yaa != 'y':
                                break
                        else:
                            print('angka yang dimasukkan tidak ada didalam pilihan')
                            yaa = input('ingin menambah kolom lagi (y/t) : ')
                            if yaa != 'y':
                                break
            else:
                print('nama tabel yang dimasukkan tidak ada didalam pilihan')
                yaa = input('ingin mencoba menambah kolom lagi (y/t): ')
                if yaa != 'y':
                    break
        except:
            print('nama kolom yang dimasukkan mengandung spasi\nuntuk mengantisipasinya ganti dengan underscore ( _ )')
            print('nama tabel yang dimasukkan tidak ada didalam pilihan')
            yaa = input('ingin mencoba menambah kolom lagi (y/t): ')
            if yaa != 'y':
                break

# menghapus kolom
def menghapuskolom():
    os.system('cls')
    ya = 'y'
    while ya == 'y':
        mycursor.execute('show tables')

        tabl = []
        a = 0
        b = PrettyTable(['no','nama table'])
        for i in mycursor:
            tabl.append(i[a])
        for j in range(len(tabl)):
            b.add_row([j+1,tabl[j]])
        print(b)

        namatabel = input('masukkan nama table yang kolomnya ingin dihapus : ')

        for k in range(len(tabl)):
            if namatabel == tabl[k]:
                mycursor.execute('desc %s'%(namatabel))
                a = 0
                tabl1 = []
                # for l in mycursor:
                #     tabl1.append(i[)
                c = PrettyTable(['no','nama kolom'])
                for i in mycursor:
                    tabl1.append(i[0])
                    c.add_row([a+1,i[0]])
                    a += 1
                print(c)
                    
                namakolom = input('kolom mana yang ingin dihapus namanya : ')
                for l in range(len(tabl1)):
                    if namakolom == tabl1[l]:
                        what = input('apakah benar benar ingin menghapus kolom "%s" (y/t) : '%(namakolom))
                        if what == 'y':
                            mycursor.execute('alter table %s drop column %s'%(namatabel,namakolom))
                            print('data sudah di hapus')
                            ya = input('ingin menghapus kolom lagi')
                            if ya != 'y':
                                break
                        else:
                            print('terima kasih')
                            break
                        
                else:
                    print('nama kolom yang dimasukkan tidak ada di daftar kolom')
                    ya = input('ingin menghapus kolom lagi')
                    if ya != 'y':
                        break
        else:
            print('nama table yang dimasukkan tidak ada di daftar table')
            ya = input('ingin menghapus kolom lagi')
            if ya != 'y':
                break

# mengganti nama kolom
def menggantinamakolom():
    os.system('cls')
    ya = 'y'
    while ya == 'y':
        mycursor.execute('show tables')

        tab = []
        a = PrettyTable(['no','nama table'])
        b = 0
        for i in mycursor:
            tab.append(i[0])
            a.add_row([b+1,i])
            b +=1
        print(a)

        namatabel = input('masukkan nama tabel yang kolomnya ingin diganti : ')

        for j in range(len(tab)):
            if namatabel == tab[j]:
                mycursor.execute('desc %s'%(namatabel))
                kol = []
                c = PrettyTable(['no','nama kolom'])
                e = 0
                for k in mycursor :
                    kol.append(k)
                    c.add_row([e+1,k[0]])
                    e+=1
                print(c)
                namakolom = input('masukkan nama kolom yang ingin diganti : ')
                for l in range(len(kol)):
                    print(kol)
                    if namakolom == kol[l][0]:
                        namabaru = input('masukkan nama kolom baru untuk mengganti nama yang lama : ')

                        sungguh = input('apakah sungguh ingin merubah nama kolom  (y/t): ')
                        if sungguh == 'y':
                            mycursor.execute('alter table %s change %s %s %s not null default %s'%(namatabel,namakolom,namabaru,kol[l][1],kol[l][4]))

                        
                        ya = input('apakah ingin mengubah nama lagi (y/t) : ')
                        if ya != 'y':
                            break
                        else:
                            continue
                else:
                    print('tidak ada kolom dengan nama %s'%(namakolom))
                    ya = input('apakah ingin mencoba mengubah nama lagi (y/t) : ')
                    if ya != 'y':
                        break
                    else:
                        continue
        else:
            print('tidak ada tabel dengan nama %s'%(namatabel))       
            ya = input('apakah ingin mencoba mengubah nama lagi (y/t) : ')
            if ya != 'y':
                break
            else:
                continue

# mengganti tipe data kolom
def menggantitipedatakolom():
    os.system('cls')

    tipedata = ['int','text','enum("laki-laki","perempuan")','timestamp']

    pilihan = ['untuk angka','untuk huruf','untuk jenis kelamin','untuk tanggal']
    ya  = 'y'
    while ya == 'y':
        mycursor.execute('show tables')
        
        tab = []
        a = 0
        b = PrettyTable(['no','nama table'])
        for i in mycursor:
            tab.append(i[0])
            b.add_row([a+1,i])
            a+=1
        print(b)

        nama_table = input('masukkan nama table : ')
        
        for j in range(len(tab)):
            if nama_table == tab[j]:
                mycursor.execute('desc %s'%(nama_table))
                tab1 = []
                c = 0
                d = PrettyTable(['no','nama kolom'])
                for k in mycursor:
                    tab1.append(k[0])
                    d.add_row([c+1,k[0]])
                    c+=1
                print(d)
                
                nama_kolom = input('masukkan nama kolom : ')
                for l in range(len(tab1)):
                    if nama_kolom == tab1[l]:
                        e = PrettyTable(['no','jenis tipe data'])
                        for m in range(len(pilihan)):
                            e.add_row([m+1,pilihan[m]])
                        print(e)
                        print('nama kolomnya : %s'%(nama_kolom))
                        while True:
                            try:
                                tipe_data_baru = int(input('masukkan tipe data baru : '))
                                break
                            except:
                                print('pilihan yang dimasukkan harus angka')
                                continue
                        if tipe_data_baru-1 == 0:
                            yakin = input('yakin ingin mengganti tipe datanya (y/t): ')
                            if yakin == 'y':
                                try:
                                    mycursor.execute('alter table %s modify %s %s not null default 0'%(nama_table,nama_kolom,tipedata[0]))
                                except:
                                    print('kolom yang dimasukkan mengandung primary key jadi tidak bisa diubah tipedatanya')
                                    hapus = input('apakah ingin menghapus primary key nya (y/t) : ')
                                    if hapus == 'y':
                                        mycursor.execute('alter table %s drop primary key'%(nama_table))
                                        print('primary key sudah di kolom %s sudah dihapus')
                                        lanjut = input('apakah ingin mengganti tipe datanya (y/t) : ')
                                        if lanjut == 'y':
                                            mycursor.execute('alter table %s modify %s %s not null default 0'%(nama_table,nama_kolom,tipedata[0]))

                                ya = input('ingin mengganti tipe data lagi : ')
                                if ya != 'y':
                                    break
                        if tipe_data_baru-1 == 1:
                            yakin = input('yakin ingin mengganti tipe datanya (y/t): ')
                            if yakin == 'y':
                                try:
                                    mycursor.execute('alter table %s modify %s %s not null default " "'%(nama_table,nama_kolom,tipedata[1]))
                                except:
                                    print('kolom yang dimasukkan mengandung primary key jadi tidak bisa diubah tipedatanya')
                                    hapus = input('apakah ingin menghapus primary key nya (y/t) : ')
                                    if hapus == 'y':
                                        mycursor.execute('alter table %s drop primary key'%(nama_table))
                                        print('primary key sudah di kolom %s sudah dihapus')
                                        lanjut = input('apakah ingin mengganti tipe datanya (y/t) : ')
                                        if lanjut == 'y':
                                            mycursor.execute('alter table %s modify %s %s not null default " "'%(nama_table,nama_kolom,tipedata[1]))
                                ya = input('ingin mengganti tipe data lagi : ')
                                if ya != 'y':
                                    break
                        if tipe_data_baru-1 == 2:
                            yakin = input('yakin ingin mengganti tipe datanya (y/t): ')
                            if yakin == 'y':
                                try:
                                    for i in range(2):
                                        if i == 0:
                                            mycursor.execute('alter table %s drop %s'%(nama_table,nama_kolom))
                                        else:
                                            mycursor.execute('alter table %s add %s %s after %s'%(nama_table,nama_kolom,tipedata[2],tab1[l-1]))
                                except:
                                    print('kolom yang dimasukkan mengandung primary key jadi tidak bisa diubah tipedatanya')
                                    hapus = input('apakah ingin menghapus primary key nya (y/t) : ')
                                    if hapus == 'y':
                                        mycursor.execute('alter table %s drop primary key'%(nama_table))
                                        print('primary key sudah di kolom %s sudah dihapus')
                                        lanjut = input('apakah ingin mengganti tipe datanya (y/t) : ')
                                        if lanjut == 'y':
                                            mycursor.execute('alter table %s modify %s %s after %s'%(nama_table,nama_kolom,tipedata[2],tab1[l-1]))
                                ya = input('ingin mengganti tipe data lagi : ')
                                if ya != 'y':
                                    break
                        if tipe_data_baru-1 == 3:
                            yakin = input('yakin ingin mengganti tipe datanya (y/t): ')
                            if yakin == 'y':
                                try:
                                    mycursor.execute('alter table %s modify %s %s not null default current_timestamp'%(nama_table,nama_kolom,tipedata[3]))
                                except:
                                    print('kolom yang dimasukkan mengandung primary key jadi tidak bisa diubah tipedatanya')
                                    hapus = input('apakah ingin menghapus primary key nya (y/t) : ')
                                    if hapus == 'y':
                                        mycursor.execute('alter table %s drop primary key'%(nama_table))
                                        print('primary key sudah di kolom %s sudah dihapus')
                                        lanjut = input('apakah ingin mengganti tipe datanya (y/t) : ')
                                        if lanjut == 'y':
                                            mycursor.execute('alter table %s modify %s %s not null default current_timestamp'%(nama_table,nama_kolom,tipedata[3]))
                                ya = input('ingin mengganti tipe data lagi : ')
                                if ya != 'y':
                                    break
                            
                else:
                    print('nama kolom yang dimasukkan tidak ada didalam pilihan')
                    ya = input('ingin menggganti tipe data lagi : ')
                    if ya != 'y':
                        break
        else:
            print('nama table yang dimasukkan tidak ada dalam pilihan')
            ya = input('ingin menggganti tipe data lagi : ')
            if ya != 'y':
                break


    

    
    

# ---------------------------------------------------------------------------------------
#  C.R.U.D DENGAN PYTHON

# ---------------------------------------------------------------------------------------
# ========================================================================================
# ========================================================================================


# pilihan tampilan ke-1 
pilihan1 = ['masuk kedalam database','melihat database','membuat database','menghapus database','selesai']

# pilihan tampilan ke-2
pilihan2 = ['masuk ke dalam table','melihat table','membuat table dan kolom','menghapus table','melihat struktur table','keluar']

# pilihan tampilnan ke 3
pilihan3 = ['insert data','select data','update data','delete data','selesai']

# pilihan tampilnan ke 4
pilihan4 = ['menambah kolom','menghapus kolom','mengganti nama kolom','mengganti tipe data kolom','mengganti nilai default kolom','menentukan di baris berapa kolomnya','membuat kolom menjadi primary key','selesai']

ya = 'y'

while ya == 'y':
    tabelpilihan(pilihan1)
    
    while True:
        try:
            pilih = int(input('masukkan pilihan : '))
            break
        except:
            print('pilihan yang dimasukkan harus angka')
            continue


    if pilih >= 0 and pilih <= len(pilihan1)-1:

        # masuk ke dalam database
        if pilih == 1:
            melihatdatabase()

            try:
                db = input('database mana yang ingin dimasuki : ')
                mycursor.execute('use {}'.format(db))
                print(mycursor)
            except:
                os.system('cls')
                print('tidak ada database dengan nama :',db)
                break

        
            while ya == 'y':

                tabelpilihan(pilihan2)
                while True:
                    try:
                        pilih = int(input('masukkan pilihan : '))
                        break
                    except:
                        print('pilihan yang dimasukkan harus angka')
                        continue
                
                if pilih >= 0 and pilih <= len(pilihan2)-1:

                    # masuk kedalam table
                    if pilih == 1:
                        print('1 memanipulasi kolom')
                        print('2 memanipulasi data')

                        while True:
                            try:
                                pilih = int(input('masukkan pilihan : '))
                                break
                            except:
                                print('pilihan yang dimasukkan harus angka')
                                continue
                    
                        # memanipulasi kolom
                        if pilih == 1:
                            os.system('cls')
                            
                            tabelpilihan(pilihan4)
                            
                            while True:
                                try:
                                    pilih = int(input('masukkan pilihan : '))
                                    break
                                except:
                                    print('pilihan yang dimasukkan harus angka')
                                    continue
                            
                            if pilih >= 0 and pilih <= len(pilihan4):
                                if pilih == 0:
                                    break
                                elif pilih == 1:
                                    menambahkolom()
                                elif pilih == 2:
                                    menghapuskolom()
                                elif pilih == 3:
                                    menggantinamakolom()
                                elif pilih == 4:
                                    menggantitipedatakolom()
                                elif pilih == 5:
                                    pass
                                elif pilih == 6:
                                    pass
                                elif pilih == 7:
                                    pass
                            else:
                                print('angka yang dimasukkan salah')
                                break

                        
                        # memanipulasi data
                        elif pilih == 2:
                            os.system('cls')
                            
                            tabelpilihan(pilihan3)
                            
                            while True:
                                try:
                                    pilih = int(input('masukkan pilihan : '))
                                    break
                                except:
                                    print('pilihan yang dimasukkan harus angka')
                                    continue
                            
                            if pilih >= 0 and pilih <= len(pilihan3):
                                if pilih == 0:
                                    break
                                elif pilih == 1:
                                    pass
                                elif pilih == 2:
                                    pass
                                elif pilih == 3:
                                    pass
                                elif pilih == 4:
                                    pass

                            else:
                                print('angka yang dimasukkan salah')
                                break
                            



                        else:
                            print('angka yang dimasukkan tidak ada dalam pilihan')
                    # melihat table .
                    elif pilih == 2:
                        melihattable()
                        ya = input('lagi (y/t) : ')
                        if ya != 'y':
                            break
                            print('terima kasih')
        
                    # membuat table
                    elif pilih == 3:
                        membuattable()
                        ya = input('ingin memilih lagi (y/t) : ')
                        if ya != 'y':
                            break
                            print('terima kasih')

                    # menghapus table
                    elif pilih == 4:
                        menghapustable()
                        ya = input('lagi (y/t) : ')
                        if ya != 'y':
                            break
                            print('terima kasih')
  
                    # melihat struktur table
                    elif pilih == 5:
                        print('1 melihat kolom tablenya')
                        print('2 melihat cara membuat kolomnya')
                        pilih = input('masukkan pilihan : ')

                        if pilih == '1':
                            strukturkolom()
                            ya = input('lagi (y/t) : ')
                            if ya != 'y':
                                break
                                print('terima kasih')
                        elif pilih == '2':
                            caramembuatkolom()
                            ya = input('lagi (y/t) : ')
                            if ya != 'y':
                                break
                                print('terima kasih')
                        else:
                            print('angka yang dimasukkan tidak ada dalam pilihan')
                    # keluar
                    elif pilih == 0:
                        break
                else:
                    print('angka yang dimasukkan tidak ada dalam pilihan')
                    


        # melihat database
        elif pilih == 2:
            melihatdatabase()
            ya = input('lagi (y/t) : ')
            if ya != 'y':
                print('terima kasih')
                break
      
        # membuat database
        elif pilih == 3:
            membuatdatabase()

        # menghapus database
        elif pilih == 4:
            menghapusdatabase()

        # selesai
        elif pilih == 0:
            print('terima kasih :)')
            break

    else:
        print('angka tidak ada dalam pilihan')
        break