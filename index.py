
import os 
#Funsi ascending
def urutasc(a):
    for i in range(len(a)-1,0,-1):
        for j in range(i):
            if a[j]>a[j+1]:
                simpan = a[j]
                a[j]=a[j+1]
                a[j+1]=simpan
        print(a)

#funsi descending
def urutdesc(a):
    for i in range(len(a)-1,0,-1):
        for j in range(i):
            if a[j]<a[j+1]:
                simpan = a[j]
                a[j]=a[j+1]
                a[j+1]=simpan
        print(a)
            
#pengulangan
while(True):
    os.system('cls') 
     #tampil judul
    print("=================")
    print("Program mengurutkan Data")
    print("Dengan metode Bublle SHort")
    print("=================")
     
     #input 5 bilangan
     
    angka1= int(input("Masukan angka 1 :"))
    angka2= int(input("Masukan angka 2 :"))
    angka3= int(input("Masukan angka 3 :"))
    angka4= int(input("Masukan angka 4 :"))
    angka5= int(input("Masukan angka 5 :"))
     
     #tampil pilihan urut
    print("==================")
    print("Pilihan metode pengurutan : ")
    print("1.Ascending")
    print("2.Descending")
     
     
     #merubah input angka menjadi list(array)
    bill=[angka1,angka2,angka3,angka4,angka5]
     
     #tampil hasil
    pilih=input("Metode yang dipilih :")
    print("===================")
     
    print("Data sebelum diurutkan")
    print(bill)
    print("Nilai Maksimal",max(bill))
    print("Nilai Minimal",min(bill))
    print("Nilai Rata-Rata",sum(bill)/len(bill))
    print("Data sedudah di urutkan :")
     
     #pemilihan pengurutan dengan percabangan
    if pilih=="1":
         urutasc(bill)
    elif pilih=="2":
         urutdesc(bill)
    else:
         print("Pilihan ra ono")
         
    #perulangan
    menu=input("kembali ke menu awal (Y/N)?")
    
    #pilihan pengulangan
    if menu=="N" or menu=="n":
        print("Selesai,Terimakasih!!")
        break
    elif menu=="Y" or menu=="y":
        print("Pilihan tidak ada!!!")
        break
     
     
     
