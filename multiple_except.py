def main():
    fileName = input('masukan nama file data :')
    abbr = input('masukan singkatan yang dicari :').upper()

    try :
        f = open(fileName)
        lst =f.read().split('\n')[:-1]

        data = {}
        for e in lst:
            key, val = e.split('=')
            data[key] = val

        print('\n%s singkatan dari %s' %(abbr, data[abbr]))

    except FileNotFoundError :
        print('\nKesalahan : file \'%$\' tidak ditemukan.' % fileName)

    except KeyError :
        print('\n%s tidak ditemukan.' % abbr)

if __name__ =="__main__" :
    main()