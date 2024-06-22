import main

def start():
    while True:
        print("Warung mini cui")
        play_again = input("Mau kembali ke menu?[y/n]")
        if play_again == 'y':
            main.pilihan_user()
        
if __name__ == "__main__":
    start()