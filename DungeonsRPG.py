# --- Imports --- #
import random


# --- Constants --- #
MAX_INTERACTIONS = 7
PORTAL_ROOM = -1
VICTORY_ROOM = 9
INVALID_ROOM = 0
DUNGEON_MAP = {
    1: [3, 2],
    2: [4, 3],
    3: [5, 4],
    4: [6, 5],
    5: [7, 6],
    6: [8, INVALID_ROOM],
    7: [VICTORY_ROOM, 8],
    8: [PORTAL_ROOM, VICTORY_ROOM]
}


# --- Global Variables --- #
interactions = 0
currentRoom = 1


# --- Functions --- #
def informLocationContext():
    print("Você está na sala {}".format(currentRoom))
    print("Ainda restam {}".format(MAX_INTERACTIONS - interactions))
    print("Pode seguir para: ")
    print(DUNGEON_MAP[currentRoom][0], " - Esquerda")
    print(DUNGEON_MAP[currentRoom][1], " - Direita")


def roomTransition(turnsRight):
    global interactions
    global currentRoom
    
    if turnsRight:
        currentRoom = DUNGEON_MAP[currentRoom][1]
    else:
        currentRoom = DUNGEON_MAP[currentRoom][0]
    interactions += 1


def queryRoom():
    query = ""
    while(True):
        query = input("\nQual sala deseja ir?: ").lower()
        if query != "esquerda" and query != "direita" :
            print("Escolha Incorreta, digite denovo")
            continue
        elif DUNGEON_MAP[currentRoom][query == "direita"] == INVALID_ROOM:
            print("\n***Verificando no mapa***\n")
            print("Esta sala não aparece no mapa, melhor tentar por outro caminho")
            continue
        else:
            break
    return query == "direita"


def handleSpecialCases():
    global currentRoom

    if (interactions >= MAX_INTERACTIONS):
        print("Seu tempo acabou. As rochas cobriram sua única saída. Seu grupo morreu de fome.")
        return True

    if (currentRoom == PORTAL_ROOM):
        print("Você entrou no portal de distorção espaço-temporal!")
        currentRoom = random.randint(1, 5)
    elif (currentRoom == VICTORY_ROOM):
        print("Você alcançou a sala final! Parabéns!")
        return True

    return False


def gameLoop():
    while (True):
        informLocationContext()
        roomTransition(queryRoom())
        if (handleSpecialCases()):
            break

def starGame():
    print(r"""                   ,  ,
                   \\ \\
                   ) \\ \\    _p_
                   )^\))\))  /  *\
                    \_|| || / /^`-'
           __       -\ \\--/ /
         <'  \\___/   ___. )'
              `====\ )___/\\
                   //     `"
                   \\    /  \
                   `" +========+
UAM                   |Hawkin  |
    Vision            |Cesar   |
          Apresent    |RPG     |
                      '''''''""")
    print("Star Game?")
    print("0 - Sim\n1 - Não")
    star= input()


# --- Main Calls/External Calls --- #
starGame()
gameLoop()