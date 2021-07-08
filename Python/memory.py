import random
import time
import sys
import os

def startGame():

    numbers = list(range(10))

    random.shuffle(numbers)

    print('Memorize isto: ')
    print(numbers)
    time.sleep(10)
    sys.stdout.write("\033[F")
    asteriscos = ['*', '*', '*', '*', '*', '*', '*', '*', '*']
    print(asteriscos)

    def game():
        print('Caso queira recomeçar, digite "r"')
        inputlist = input('Me diga a posição do número do seguinte modo: "local na lista" e "número" => ')
        if inputlist == 'r':
            os.system('cls' if os.name == 'nt' else 'clear')
            startGame()
        else: 
            splited = inputlist.split()

            print(splited)

            local = int(splited[0]) - 1
            numberx = int(splited[1])

            print(local)

            if numbers[local] == numberx:
                asteriscos[local] = numberx 
                print(asteriscos)
                game()
            else:
                print("Wrong!")
                os.system('cls' if os.name == 'nt' else 'clear')
                tryAgain = input("Tentar novamente? Responda com 'y' ou 'n' ")
                if tryAgain == 'y':
                    startGame()
                if tryAgain == 'n': 
                    exit()    

    game()

startGame()
