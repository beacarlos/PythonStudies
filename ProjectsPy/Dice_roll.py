from random import randrange
import msvcrt
quit = [0]
while(quit[0] != 113):
    x = randrange(1, 7)
    if(x == 1):
        print("[-----------]\n"
              "[           ]\n"
              "[     0     ]\n"
              "[           ]\n"
              "[-----------]\n")
    elif(x == 2):
        print("[-----------]\n"
              "[           ]\n"
              "[    0  0   ]\n"
              "[           ]\n"
              "[-----------]\n")
    elif(x == 3):
        print("[-----------]\n"
              "[     0     ]\n"
              "[     0     ]\n"
              "[     0     ]\n"
              "[-----------]\n")
    elif(x == 4):
        print("[-----------]\n"
              "[  0     0  ]\n"
              "[           ]\n"
              "[  0     0  ]\n"
              "[-----------]\n")
    elif(x == 5):
        print("[-----------]\n"
              "[  0     0  ]\n"
              "[     0     ]\n"
              "[  0     0  ]\n"
              "[-----------]\n")
    elif(x == 6):
        print("[-----------]\n"
              "[  0     0  ]\n"
              "[  0     0  ]\n"
              "[  0     0  ]\n"
              "[-----------]\n")

    print("Digite 'a' se deseja iniciar jogar o dado novamente ou 'q' se deseja sair: ")
    quit = msvcrt.getch()
    # input("")
