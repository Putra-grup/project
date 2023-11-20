import csv 

def Register() :
    import sys
    username = input("Masukkan Username Baru : ")
    password = input("Masukkan Password Baru : ")

    datalogin = []

    with open("E:\project_akhir\data login.csv", 'r') as file :
        csv_reader = csv.reader(file, delimiter= ",")
        for row in csv_reader :
            datalogin.append({'username' : row[0], 'password' : row[1]})

        username_ada = False

        for akun in datalogin : 
           if username == akun['username'] :
                print("Username sudah ada! Ganti yang lain!")
                sys.exit()

        if username_ada == False :
            databaru = {'username' : username, 'password' : password}
            with open("E:\project_akhir\data login.csv", 'a', newline='') as file :
                writer = csv.DictWriter(file, fieldnames=databaru.keys())
                writer.writerow(databaru)
                print("Registrasi berhasil")

def login() :
    import sys
    username = input("Masukkan Username : ")
    password = input("Masukkan Password : ")
 
    datalogin = []
    with open("E:\project_akhir\data login.csv", 'r') as file :
        csv_reader = csv.reader(file, delimiter= ",")
        for row in csv_reader :
            datalogin.append({'username' : row[0], 'password' : row[1]})
        
        dataakun = []
        
        for i in datalogin : 
           if username == i['username'] and password == i['password'] :
                dataakun.append(i)
                print("Berhasil Login")
                break
                
        if len(dataakun) == 0 :
                print("Akun Tidak Ditemukan")
                sys.exit()

                           
import sys
pilihan = input("Login / Register? (L/R) : ")
if pilihan == "R" :
    Register()
elif pilihan == "L" :
    login()
else : 
    print("Tidak Sesuai")
    sys.exit()

import os

def dashboard():
    print('='*40)
    print("|     Selamat datang di PEDIGMA        |")
    print("|     Pecel Digital Management         |")
    print("="*40)
    H = (input("\nketik enter untuk melanjutkan"))
dashboard() 

def menu():
 while True :
    import pandas as pd
    list_produk = "E:\project_akhir\produk.csv"
    df = pd.read_csv(list_produk)
    # df.index = df.index+1

    pilihan = input("\n1. Melihat produk\n2. Tambah produk\n3. Hapus produk\n4. Edit barang\n\nMasukkan pilihan = ")
    
   
    if pilihan == '1':
        print(df)
    elif pilihan == '2':
        print(df)
        nama_sayur = input("masukkan nama sayur/lauk: ") 
        harga_sayur = input("masukkan harga: ")
        stok_produk = input("masukkan stok produk : ")
        panjang_df = len(df)
        df.loc[panjang_df] = [nama_sayur,harga_sayur,stok_produk]
        df.to_csv("E:\project_akhir\produk.csv",index=False)
        print(df)
    elif pilihan == '3':
        print(df)
        index = input("masukkan nomor: ") 
        df.drop(int(index),inplace=True)
        df.index = [i for i in range(len(df))]
        print(df)
        df.to_csv("E:\project_akhir\produk.csv",index=False)
        
    elif pilihan == '4' :
       print("Sebelum mengedit")
       print(df)
       baris_edit = int(input("masukkan baris yang ingin diubah : "))
       kolom_edit = int(input("masukkan kolom yang ingin diubah : "))
       stok_produk =int(input("masukkan stok baru : "))
       df.iloc[baris_edit, kolom_edit] = stok_produk
       df.to_csv("E:\project_akhir\produk.csv",index=False)
       print("Setelah mengedit")
       print(df)
       break
    # elif pilihan == '5' :
    #     program_berjalan = True

    #     while program_berjalan:
    #         user_input = input("Ketik 'exit' untuk keluar: ")

    #         if user_input.lower() == 'exit':
    #             print("Program keluar.")
    #             break
    #         else:
    #             print("Program berlanjut.")
                


menu()