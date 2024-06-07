def main() :
    # membuka file 
    f = open('data.txt', 'r')

    #membaca data dari dalam file 
    data = f.read()

    #mengkonversi data ke dalam bentuk raw.string 
    rawData = data.encode('unicode-escape')

    #menampilkan isi rawData ke layar
    print(rawData)

    #menutup file 
    f.close()

if __name__ == '__main__' :
    main()