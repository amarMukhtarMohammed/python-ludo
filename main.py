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
  
def displayBoard():
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
    (12, 58), (12, 64), (12, 70), (12, 74), (12, 78), (12, 82), 
    (12, 86), (13, 86), (14, 86), (16, 86), (16, 82), (16, 78), 
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
    
    while True:
        user_input = input("Press Enter to roll, or type 'exit' to stop: ")
        if user_input.lower() == 'exit':
            print("Exiting the loop.")
            break
        else:
            roll = random.randint(1, 6)
            setPlayerPositions(roll)
            #print(player_positions)
            printDictionary()
            for line in ludo_dictionary[roll]:
                print(line)

def getPlayerPositions(playerID):
    return player_positions[playerID]

def setPlayerPositions(roll):
    if player_positions["B1"][2] == 1:
        player_positions["B1"] = list(getTuplePosition(player_positions["B1"][:2], roll)) + [1]
    if roll == 6 and player_positions["B1"][2] == 0:
        player_positions["B1"] = [0, 52, 1]

def getTuplePosition(target_tuple, roll):
    currentPosition = coordinates.index(tuple(target_tuple))
    return coordinates[currentPosition + roll]

def updateDictionary(playerID, playerPosition):
    print(playerPosition)
    # dictionaryIndex = str(playerPosition[0])
    # indexPosition = playerPosition[1]
    # original_value = board_dictionary[dictionaryIndex]
    # board_dictionary[dictionaryIndex] = original_value[:max(0, indexPosition - 1)] + playerID + original_value[min(len(original_value), indexPosition + 1):]
    #print(player_positions["B1"])

# def updateDictionary(playerID, playerPosition):
#     # Get player's previous position (current position in the dictionary)
#     previous_position = player_positions[playerID]

#     # Clear the player's previous position
#     dictionaryIndex = str(previous_position[0])  # Row of the old position
#     indexPosition = previous_position[1]  # Column of the old position
#     original_value = board_dictionary[dictionaryIndex]

#     # Replace the old position with a space ' ' to "erase" the player
#     board_dictionary[dictionaryIndex] = original_value[:indexPosition] + ' ' + original_value[indexPosition+1:]

#     # Update player's new position
#     dictionaryIndex = str(playerPosition[0])  # Row of the new position
#     indexPosition = playerPosition[1]  # Column of the new position
#     original_value = board_dictionary[dictionaryIndex]

#     # Update the board with the player's new position
#     board_dictionary[dictionaryIndex] = original_value[:indexPosition] + playerID + original_value[indexPosition+1:]
    
#     # Update the player's position in player_positions dictionary
#     player_positions[playerID] = playerPosition

#     # Print the updated positions to check
#     print(f"Updated {playerID} position to: {playerPosition}")
    



def displayCoordinates():
    print(coordinates[5][5])

    # # Function to iterate through coordinates and return each one
    # def get_coordinates_iteratively(coords):
    #     for index, coord in enumerate(coords):
    #         yield index, coord  # Yielding the index and coordinate

#     # Usage
#     for index, coord in get_coordinates_iteratively(coordinates):
#         print(f"Coordinate {index}: {coord}")


# # Print the updated board
# for row in board_dictionary.values():
#     print(row)

def main():
    try:
        #startLudo()
        #rollDice()
        #displayBoard()

        printDictionary()
        rollDice()
        #displayCoordinates()
        #updateDictionary("B1", "12", 46)
        #printDictionary()
    except IndexError as e:
        print("An error occurred: Index out of bounds.", e)
    except KeyError as e:
        print("An error occurred: Invalid dictionary index.", e)
        
    except KeyboardInterrupt:
        confirmation = input("\n**********CONFIRM YOU WOULD LIKE TO QUIT (yes/no)**********\n")
        if confirmation == 'yes':
            print("**********EXITING THE GAME**********")
        else:
            print("**********RESUMING THE GAME**********")
            main() 

if __name__ == "__main__":
    main()