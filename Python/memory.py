import random
import time
import os

def startGame():

    numbers = list(range(10))

    random.shuffle(numbers)

    print('Memorize esta sequência de números: ')
    print(numbers)
    time.sleep(10)
    os.system('cls' if os.name == 'nt' else 'clear')
    asteriscos = ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*']
    print(asteriscos)

    def game():
        print('Caso queira recomeçar, digite "r"')
        inputlist = input('Me diga a posição do número do seguinte modo: "local na lista" e "número" => ')
        if inputlist == 'r':
            os.system('cls' if os.name == 'nt' else 'clear')
            startGame()
        else: 
            splited = inputlist.split()

            def avoidBlank():

                local = int(splited[0]) - 1
                numberx = int(splited[1])



                if numbers[local] == numberx:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    asteriscos[local] = numberx 
                    if '*' in asteriscos:
                        print(asteriscos)
                        game()
                    else: 
                        print("YOU WON")
                        print('------------------------')
                        playAgain = input("Quer jogar novamente? Responda com 'y' ou 'n' ")
                        if playAgain == 'y':
                            startGame()
                        else:
                            exit()
                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("WRONG! YOU LOST!")
                    tryAgain = input("Tentar novamente? Responda com 'y' ou 'n' ")
                    if tryAgain == 'y':
                        os.system('cls' if os.name == 'nt' else 'clear')
                        startGame()
                    if tryAgain == 'n': 
                        exit()    
            
            if len(splited) < 2:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("WRONG! YOU LOST!")
                tryAgain = input("Tentar novamente? Responda com 'y' ou 'n' ")
                if tryAgain == 'y':
                    os.system('cls' if os.name == 'nt' else 'clear')
                    startGame()
                if tryAgain == 'n': 
                    exit()    
        
            else: 
                avoidBlank()

    game()

startGame()