a = float(input('masukan nilai a :'))
b = float(input('masukan nilai b :'))

try:
    c = a/b
except ZeroDivisionError as e :
    print(e)
    import sys
    sys.exit(1) # menghentikan eksekusi program 

    #tidak dieksekusi jika salah 
print('%.2f / %.2f = %.2f' % (a, b, c))
