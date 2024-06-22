import socket

from time import sleep
PC_NAME = socket.gethostname()

def selamat_datang():
    style = "=" * (len (PC_NAME) + 6)
    print(style)
    print(f"== {PC_NAME} ==")
    print(style)

def selamat_tinggal():
    print("Program dihentikan dalam hitungan:")
    sleep(1)
    print("3....")
    sleep(1)
    print("2....")
    sleep(1)
    print("1....")
    sleep(1)
    print("Program berhasil dihentikan!!")

