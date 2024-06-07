def main() :
    # membuka file 
    f = open('data.txt', 'r')

    #membaca data dari dalam file 
    data = f.read()

    #menampilkan isis data ke layar
    f.close()

    #menutup file

if __name__ == "__main__" :
    main()