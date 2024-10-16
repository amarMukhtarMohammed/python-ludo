import random;

players = []

def startLudo():
    print("\n**********START/CONTINUE GAME**********")
    print("0 - START NEW GAME")
    print("1 - CONTINUE GAME")
    startLudoPrompt = input()
    if (startLudoPrompt == "0"):
        setNumberOfPlayers()
        addPlayer()
        displayPlayers()

def setNumberOfPlayers():
    print("\n**********SELECT NUMBER OF PLAYERS (2-4)**********")
    numberOfPlayers = input()
    for i in range(int(numberOfPlayers)):
        addPlayer()  # Change to loop correctly based on the number of players

def addPlayer():
    print("\n**********ADD PLAYER {}**********".format(len(players)))
    print("*******CHOOSE PLAYER TYPE*******")
    print("0 - COMPUTER")
    print("1 - HUMAN")
    addPlayerPrompt = input()
    players.append(addPlayerPrompt)

def playerOrComputer(player):
    if players[player] == "0":
        return "COMPUTER"
    else:
        return "HUMAN"

def displayPlayers():
    colors = ["RED", "BLUE", "GREEN", "YELLOW"]
    for i in range(len(players)):
        print("PLAYER {} - {} - {}".format(i, playerOrComputer(i), colors[i]))

def rollDice():
    # Define the dictionary with dice faces
    ludo_dictionary = {
        1: [
            "############",
            "#          #",
            "#     0    #",
            "#          #",
            "############"
        ],
        2: [
            "############",
            "#          #",
            "#  0    0  #",
            "#          #",
            "############"
        ],
        3: [
            "############",
            "#    0     #",
            "#    0     #",
            "#    0     #",
            "############"
        ],
        4: [
            "############",
            "#          #",
            "#  0    0  #",
            "#  0    0  #",
            "############"
        ],
        5: [
            "############",
            "#     0    #",
            "#  0    0  #",
            "#  0    0  #",
            "############"
        ],
        6: [
            "############",
            "#  0    0  #",
            "#  0    0  #",
            "#  0    0  #",
            "############"
        ]
    }

    roll = random.randint(1, 6)
    for line in ludo_dictionary[roll]:
        print(line)
  
def generateBoard():
    board = [
        "###########################################################################################",
        "#                                   #     |     |     # |                                 #",
        "#            YELLOW                 #-----#-----#-----# V              BLUE               #",
        "#                                   #     #     #     #                                   #",
        "#          -----------              #-----#-----#-----#             -----------           #",
        "#          | Y1 | Y2 |              #     #     #     #             | B1 | B2 |           #",
        "#          -----------              #-----#-----#-----#             -----------           #",
        "#          | Y3 | Y4 |              #     #     #     #             | B3 | B4 |           #",
        "#          -----------              #-----#-----#-----#             -----------           #",
        "#                                   #     #     #     #                                   #",
        "#                                   #-----#-----#-----#                                   #",
        "# -->                               #     #     #     #                                   #",
        "#####################################-----#-----#-----#####################################",
        "#     |     |     |     |     |     |     #     #     |     |     |     |     |     |     #",
        "#-----#####################################-----#####################################-----#",
        "#     |     |     |     |     |     |     |  X  |     |     |     |     |     |     |     #",
        "#-----#####################################-----#####################################-----#",
        "#     |     |     |     |     |     |     #     #     |     |     |     |     |     |     #",
        "#####################################-----#-----#-----#####################################",
        "#                                   #     #     #     #                               <-- #",
        "#             GREEN                 #-----#-----#-----#                RED                #",
        "#                                   #     #     #     #                                   #",
        "#          -----------              #-----#-----#-----#             -----------           #",
        "#          | G1 | G2 |              #     #     #     #             | R1 | R2 |           #",
        "#          -----------              #-----#-----#-----#             -----------           #",
        "#          | G3 | G4 |              #     #     #     #             | R3 | R4 |           #",
        "#          -----------              #-----#-----#-----#             -----------           #",
        "#                                   #     #     #     #                                   #",
        "#                                 ^ #-----#-----#-----#                                   #",
        "#                                 | #     |     |     #                                   #",
        "###########################################################################################"
        ]

    for row in board:
        print("".join(row))

def main():
    try:
        #startLudo()
        #rollDice()
        generateBoard()
        
    except KeyboardInterrupt:
        confirmation = input("\n**********CONFIRM YOU WOULD LIKE TO QUIT (yes/no)**********\n")
        if confirmation == 'yes':
            print("**********EXITING THE GAME**********")
        else:
            print("**********RESUMING THE GAME**********")
            main() 

if __name__ == "__main__":
    main()