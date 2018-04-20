def tambah():
    print('1.Penjumlahan')
    a = int(input('Masukan nilai x='))
    b = int(input('Masukan nilai y= '))
    c = a+b
    print ('x+y=',c)
    tanya()
def kurang():
    print('2.Pengurangan')
    a = int(input('Masukan nilai x= '))
    b = int(input('Masukan nilai y= '))
    c = a-b
    print ('x-y=',c)
    tanya ()
def bagi ():
    print ('3.Pembagian')
    a = int(input('Masukan nilai x= '))
    b = int(input('Masukan nilai y= '))
    c = a/b
    print ('x/y=',c)
    tanya ()
def kali ():
    print ('4.Perkalian')
    a = int(input('Masukan nilai x= '))
    b = int(input('Masukan nilai y= '))
    c = a*b
    print ('x*y=',c)
    tanya()
def tanya():
    tanya = input("\nKembali ke menu (y/t)? ")
    if tanya == "y":
        menu_kal()
    elif tanya =="t":
        exit
    else:
        print ("nSalah input.........!!!")
def menu_kal():
    print("===================================================")
    print("Pemograman Kalkulator Sederhana")
    print("===================================================")
    print("\t1. Penjumlahan")
    print("\t2. Pengurangan")
    print("\t3. Pembagian")
    print("\t4. Perkalian")
    print("===================================================")
    print("Silahlkan pilih 1-4")
    print(" ")
    pil = input("Masukan pilihan : ")
    if pil == '1':
        tambah()
    elif pil == '2':
        kurang()
    elif pil == '3':
        bagi()
    elif pil == '4':
        kali()
    else:
    
        tanya()

               
