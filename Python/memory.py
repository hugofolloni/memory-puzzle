import random
import time
import os

def startGame():

    numbers = list(range(10)) # Cria uma lista com os 10 primeiros números e reorganiza eles

    random.shuffle(numbers)

    numberstr = [str(number) for number in numbers] # Transforma os números em "palavras" para formatação
    
    print('Memorize esta sequência de números: ') 
    print(numberstr)
    time.sleep(10) # Mostra as números por 10 segundos e depois, além de limpar o terminal, mostra os asteriscos
    os.system('cls' if os.name == 'nt' else 'clear')
    asteriscos = ['*'] * 10
    print(asteriscos)

    def game():
        print('Caso queira recomeçar, digite "r"')
        inputlist = input('Me diga a posição do número do seguinte modo: "local na lista" e "número" => ') # Input para coletar a informação de localização e número que o usuário tentou
        if inputlist == 'r': # Restart1 do jogo
            os.system('cls' if os.name == 'nt' else 'clear')
            startGame()
        else: 
            splited = inputlist.split() # Separa a string em duas partes, adicionando à array local e número

            def avoidBlank():

                local = int(splited[0]) - 1 # Local indicado - 1, pois primeira posição = 0
                numberx = int(splited[1]) # Número chutado



                if numbers[local] == numberx: # Se o número chutado for igual ao número correto da posição
                    os.system('cls' if os.name == 'nt' else 'clear')
                    asteriscos[local] = str(numberx) # Substitui o asterisco pelo número
                    if '*' in asteriscos: # Caso ainda possuam asteriscos, coletar novamente os dados
                        print(asteriscos)
                        game()
                    else:  # Caso nao possuam mais asteriscos, o jogo acabou e você venceu
                        print("YOU WON")
                        print('------------------------')
                        playAgain = input("Quer jogar novamente? Responda com 'y' ou 'n' ")
                        if playAgain == 'y': # Restart2
                            startGame()
                        else:
                            exit()
                else: # Caso esteja errado, aviso de erro e Restart3
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("WRONG! YOU LOST!")
                    tryAgain = input("Tentar novamente? Responda com 'y' ou 'n' ")
                    if tryAgain == 'y':
                        os.system('cls' if os.name == 'nt' else 'clear')
                        startGame()
                    if tryAgain == 'n': 
                        exit()    
            
            if len(splited) < 2: # Caso ocorra erro de digutação e não separe por ' ' os números, computar erro e reinicar
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

    game() # Começar coleta de dados

startGame() # Começar jogo