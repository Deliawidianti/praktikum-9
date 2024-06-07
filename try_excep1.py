a = float(input('masukan nilai a :'))
b = float(input('masukan nilai b :'))

try:
    c = a/b
except ZeroDivisionError as e :
    print(e)
else : 
    print('%.2f / %.2f = %.2f' % (a, b, c))