def main():
    # membuka file 
    f = open('data.txt', 'w')

    data = ['Python\n', 'C++\n', 'PHP\n', 'Ruby\n']

    # menulis data ke dalam file 
    f.writelines(data)

    #menutup file
    f.close()

if __name__ =='__main__' :
    main()