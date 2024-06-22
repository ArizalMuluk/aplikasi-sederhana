from libs import selamat_datang, selamat_tinggal
from games import cuypyv1
from tools import warung

def pilihan_user():
    opsi = int(input("\nMenu Program\n1.Cuypy Game\n2.Warung Mini\n3.Akhiri Program\n\nSilahkan pilih opsi yang tersedia: "))
    if opsi == 1:
        cuypyv1.start()
    elif opsi == 2:
        warung.start()
    elif opsi == 3:
        selamat_tinggal()
    else:
        print("Pilihlah pilihan yang ada di menu!!")

def main():
    selamat_datang()
    pilihan_user()

if __name__ == '__main__':
    main()