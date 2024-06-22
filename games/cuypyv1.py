import random
import main

def start():
    while True:
        output_angka = random.randint(1, 4)
        bentuk_goa = "|_|"
        goa_kosong = [bentuk_goa] * 4
        goa = goa_kosong.copy()
        goa_kosong[output_angka - 1] = "|0.0|"
    
        s = " "
        finish = s.join(goa)
        finish2 = s.join(goa_kosong)
    
        cuypy_goa = int(input(f"""Pilihlah salah satu goa yang menjadi tempat tinggal cuypy 
{finish}
 1   2   3   4
JAWAB:"""))
    
        if cuypy_goa == output_angka:
            print(f"Selamat, posisi CUYPY ada di {finish2} \nKAMU MENANG!🏆")
        else:
            print(f"Wah, posisi CUYPY ada di {finish2} \nKAMU KALAH!🙈")
            
        play_again = input("Apakah kamu ingin bermain lagi? [y/n]: ").lower()
        if play_again == 'y':
            return start()
        elif play_again == 'n':
            main.pilihan_user()
        else:
            print("Masukan input yang sesuai")

if __name__ == '__main__':
    start()