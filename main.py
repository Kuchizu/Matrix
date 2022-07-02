from os import system
from random import randint, choice
from threading import Thread
from time import sleep
from string import printable

GREEN = '\033[92m'
CYAN = '\033[96m'
ENDC = '\033[0m'

def print_char(x, y, char):
    # > |
    print("\033[" + str(y) + ";" + str(x + 10) + "H" + char)

system('cls')

def rand_put():
    x, y, n = randint(-10, 200), randint(0, 22), randint(5, 20)
    Thread(target=clear_put, args=(x, y, n)).start()
    for i in range(n):
        print_char(x, y + i - (i != 0), f'{GREEN}{choice(printable)}{ENDC}')
        print_char(x, y + i, f'{CYAN}{choice(printable)}{ENDC}')
        for j in range(randint(1, 3)):
            Thread(target=change_put, args=(x, y + i, (j + 1) / 10)).start()
        sleep(0.03)

def change_put(x, y, s):
    sleep(s)
    print_char(x, y, f'{GREEN}{choice(printable)}{ENDC}')

def clear_put(x, y, n):
    sleep(1)
    for i in range(n):
        print_char(x, y + i, ' ')
        sleep(0.03)

while True:
    for _ in range(randint(100, 200)):
        Thread(target=rand_put).start()
        sleep(0.001)
