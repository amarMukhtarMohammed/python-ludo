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
        addPlayer()

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

player_positions = {
    "B1": [4, 71, 0],
    "B2": [4, 76, 0],
    "B3": [6, 71, 0],
    "B4": [6, 76, 0],
    "Y1": [4, 14, 0],
    "Y2": [4, 19, 0],
    "Y3": [6, 14, 0],
    "Y4": [6, 19, 0],
    "G1": [22, 14, 0],
    "G2": [22, 19, 0],
    "G3": [24, 14, 0],
    "G4": [24, 19, 0],
    "R1": [22, 71, 0],
    "R2": [22, 76, 0],
    "R3": [24, 71, 0],
    "R4": [24, 76, 0]
}

board_dictionary = {
    "0": "#                                   #     |     |     # |                                 #",
    "1": "#            YELLOW                 #-----#-----#-----# V              BLUE               #",
    "2": "#                                   #     #     #     #                                   #",
    "3": "#          -----------              #-----#-----#-----#             -----------           #",
    "4": "#          |    |    |              #     #     #     #             |    |    |           #",
    "5": "#          -----------              #-----#-----#-----#             -----------           #",
    "6": "#          |    |    |              #     #     #     #             |    |    |           #",
    "7": "#          -----------              #-----#-----#-----#             -----------           #",
    "8": "#                                   #     #     #     #                                   #",
    "9": "#                                   #-----#-----#-----#                                   #",
    "10": "# -->                               #     #     #     #                                   #",
    "11": "#####################################-----#-----#-----#####################################",
    "12": "#     |     |     |     |     |     |     #     #     |     |     |     |     |     |     #",
    "13": "#-----#####################################-----#####################################-----#",
    "14": "#     |     |     |     |     |     |     |  X  |     |     |     |     |     |     |     #",
    "15": "#-----#####################################-----#####################################-----#",
    "16": "#     |     |     |     |     |     |     #     #     |     |     |     |     |     |     #",
    "17": "#####################################-----#-----#-----#####################################",
    "18": "#                                   #     #     #     #                               <-- #",
    "19": "#             GREEN                 #-----#-----#-----#                RED                #",
    "20": "#                                   #     #     #     #                                   #",
    "21": "#          -----------              #-----#-----#-----#             -----------           #",
    "22": "#          |    |    |              #     #     #     #             |    |    |           #",
    "23": "#          -----------              #-----#-----#-----#             -----------           #",
    "24": "#          |    |    |              #     #     #     #             |    |    |           #",
    "25": "#          -----------              #-----#-----#-----#             -----------           #",
    "26": "#                                   #     #     #     #                                   #",
    "27": "#                                 ^ #-----#-----#-----#                                   #",
    "28": "#                                 | #     |     |     #                                   #",
    }

coordinates = [
    (0, 52), (2, 52), (4, 51), (6, 52), (8, 52), (10, 52), (12, 52), 
    (12, 58), (12, 64), (12, 70), (12, 76), (12, 82),  
     (12, 88), (14, 86), (16, 86), (16, 80), 
    (16, 74), (16, 70), (16, 64), (16, 58), (16, 52), (18, 52), 
    (20, 52), (22, 52), (24, 52), (26, 52), (28, 52), (28, 46), 
    (28, 40), (26, 40), (24, 40), (22, 40), (20, 40), (18, 40), 
    (16, 40), (16, 34), (16, 28), (16, 22), (16, 16), (16, 10), 
    (16, 4), (14, 4), (12, 4), (12, 10), (12, 16), (12, 22), 
    (12, 28), (12, 34), (12, 40), (10, 40), (8, 40), (6, 40), 
    (4, 40), (2, 40), (0, 40), (0, 46), (2, 46), (4, 46), 
    (6, 46), (8, 46), (10, 46), (12, 46), (14, 46)
]

def printDictionary():
    for player in player_positions:
        updateDictionary(player, getPlayerPositions(player))
    for key, value in board_dictionary.items():
         print(f"{key}: {value}")

def rollDice():
    dice_dictionary = {
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
    
    while True:
        user_input = input("Press Enter to roll, or type 'exit' to stop: ")
        if user_input.lower() == 'exit':
            print("Exiting the loop.")
            break
        else:
            roll = random.randint(5, 6)
            for line in dice_dictionary[roll]:
                print(line)
            setPlayerPositions(roll)
            printDictionary()

def getPlayerPositions(playerID):
    return player_positions[playerID]

def getKeysStartingWith(char):
    return [key for key in player_positions if key.startswith(char)]

def getAvailablePieces(player):
    availablePlayers = []
    for inSpawnPlayer in player_positions:
        if player_positions[player][2] == 1 and inSpawnPlayer.startswith(player):
            availablePlayers.append(inSpawnPlayer)
    return availablePlayers

def removePlayerOldPosition(player):
    dictionaryIndex = getPlayerPositions(player)
    original_value = board_dictionary[str(dictionaryIndex[0])]
    new_value = original_value.replace(player, '  ')
    board_dictionary[str(dictionaryIndex[0])] = new_value

def setPlayerPositions(roll):
    piece = 'B1'
    availablePiece = getAvailablePieces(piece)
    if roll == 6:
        if len(availablePiece) == 0:
            removePlayerOldPosition(piece)
            player_positions[piece] = [0, 52, 1]
        elif len(availablePiece) == 1:
            removePlayerOldPosition(availablePiece[0])
            player_positions[availablePiece[0]] = list(getTuplePosition(player_positions[availablePiece[0]][:2], roll)) + [1]
        else:
            print("Available to move: " + getKeysStartingWith(piece[0])[0])
            availableToMoveChoice = input("Select an available player to move: ")
            removePlayerOldPosition(availableToMoveChoice)
            player_positions[availableToMoveChoice] = list(getTuplePosition(player_positions[availableToMoveChoice][:2], roll)) + [1]
    else:
        if len(availablePiece) == 1:
            removePlayerOldPosition(availablePiece[0])
            player_positions[availablePiece[0]] = list(getTuplePosition(player_positions[availablePiece[0]][:2], roll)) + [1]
        if len(availablePiece) > 1:
            print("Available to move: " + ', '.join(availablePiece))
            availableToMoveChoice = input("Select an available player to move: ")
            removePlayerOldPosition(availableToMoveChoice)
            player_positions[availableToMoveChoice] = list(getTuplePosition(player_positions[availableToMoveChoice][:2], roll)) + [1]

def getTuplePosition(target_tuple, roll):
    currentPosition = coordinates.index(tuple(target_tuple))
    return coordinates[currentPosition + roll]

def updateDictionary(playerID, playerPosition):
    dictionaryIndex = str(playerPosition[0])
    indexPosition = playerPosition[1]
    original_value = board_dictionary[dictionaryIndex]
    board_dictionary[dictionaryIndex] = original_value[:max(0, indexPosition - 1)] + playerID + original_value[min(len(original_value), indexPosition + 1):]

def main():
    try:
        #startLudo()
        #rollDice()
        #displayBoard()
        printDictionary()
        rollDice()
        
    except IndexError as e:
        print("An error occurred: Index out of bounds.", e)
    except KeyError as e:
        print("An error occurred: Invalid dictionary index.", e)
        
    except KeyboardInterrupt:
        confirmation = input("\n**********CONFIRM YOU WOULD LIKE TO QUIT (y/n)**********\n")
        if confirmation == 'y':
            print("**********EXITING THE GAME**********")
        else:
            print("**********RESUMING THE GAME**********")
            main() 

if __name__ == "__main__":
    main()