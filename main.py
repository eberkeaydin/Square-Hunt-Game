from string import ascii_uppercase as letter
from colorama import Fore
from colorama import Style

print(f"{Fore.BLUE}*************************************{Style.RESET_ALL}")
print(f"{Fore.YELLOW}**** WELCOME TO THE SQUARE HUNT ****{Style.RESET_ALL}")
print(f"{Fore.BLUE}*************************************{Style.RESET_ALL}")

while True:  # Input exception handling.
    try:
        horizontal_line = int(input(f"{Fore.CYAN}Enter the number of horizontal line(3, 7) : "))
    except ValueError:
        print("You entered invalid value. Please enter the number of horizontal line again.")
        continue
    if horizontal_line in [3, 4, 5, 6, 7]: # Horizontal line(rows) must be 3-7
        break
    else:
        print("You entered invalid value. Please enter the number of horizontal line again.")
        continue


vertical_line = horizontal_line + 1
whitepieces = blackpieces = horizontal_line * vertical_line / 2
possible_inputs = {"A1", "B1", "C1", "D1", "E1", "F1", "G1", "H1", "A2", "B2", "C2", "D2", "E2", "F2", "G2", "H2", "A3",  # CONSTANT possible input set
                   "B3", "C3", "D3", "E3", "F3", "G3", "H3", "A4", "B4", "C4", "D4", "E4", "F4", "G4", "H4", "A5", "B5",
                   "C5", "D5", "E5", "F5", "G5", "H5", "A6", "B6", "C6", "D6", "E6", "F6", "G6", "H6", "A7", "B7", "C7",
                   "D7", "E7", "F7", "G7", "H7"}

letters = letter[:vertical_line]
game_field = [['  *  ' for i in range(vertical_line)] for i in range(horizontal_line)]


def ShowGameField():   # This function provides showing game board in the beginning of program execution and every posiible changes
    numbers = iter(range(1, vertical_line))
    print("Game Field : \n")
    print('    ' + '  -  '.join(letters))
    for i in game_field:
        print(next(numbers), end=' ')
        print('|'.join(i))
    print('    ' + '  -  '.join(letters) + "\n")
    return game_field


def WhitePlacingPiece():  # When the white player is placing pieces this method will call.
    while True:
        placing = input("Enter the placing move for your piece(eg. D3) :")
        if placing in possible_inputs:
            break
        else:
            print("You entered invalid value. Please enter the placing move for your piece again.")

    placing = list(placing)  # Input is transformed to an array character by character
    game_field[int(placing[1]) - 1][letters.index(placing[0])] = '  W  '  # Piece placing with addressing the coordinate and filling by player sign.
    ShowGameField()


def BlackPlacingPiece():  # When the black player is placing pieces this method will call.
    while True:
        placing = input("Enter the placing move for your piece(eg. D3) :")
        if placing in possible_inputs:
            break
        else:
            print("You entered invalid value. Please enter the placing move for your piece again.")

    placing = list(placing)  # Input is transformed to an array character by character
    game_field[int(placing[1]) - 1][letters.index(placing[0])] = '  B  '  # Piece placing with addressing the coordinate and filling by player sign.
    ShowGameField()


def FieldIsFull(controll): # Board field controlling: If the field is not empty("  *  ") players cannot fill fields.
    if controll != "  *  ":
        return False
    else:
        return True


def BoardIsFull(): # Players fill all fields on beginning of game. This method checks is board full or not.
    emptyFields = 0
    for i in range(len(game_field)):
        for j in range(len(game_field[i])):
            if game_field[i][j] == "  *  ":
                emptyFields += 1
    if emptyFields > 1:
        return False
    else:
        return True


def RemovePiece(): # After filling all pieces on board, players remove their opponent's pieces according to their nummber of squares.
    while True:
        removing = input("Enter the removing move for opponent's piece(eg. D3) :")
        if removing in possible_inputs:
            break
        else:
            print("You entered invalid value. Please Enter the removing move for opponent's piece again.")
    removing = list(removing)  # Input is transformed to an array character by character
    game_field[int(removing[1]) - 1][letters.index(removing[0])] = '  *  '  # Piece removing with addressing the coordinate and remove the sign.
    ShowGameField()


def SquareCalculatorBlack():  # This method calculate player black's number of black squares.
    n = len(game_field)
    m = len(game_field[1])
    map = {}
    blacksquares = 0

    for i in range(0, n):  # Iterating among the game board and specify the player's sign.
        for j in range(0, m):
            if game_field[i][j] == "  B  ": # Find the sign
                for k in range(j + 1, m):
                    if game_field[i][k] == "  B  ": # Check is it square
                        if (j, k) in map:
                            blacksquares += 1
                        else:
                            map[(j, k)] = 0
    return blacksquares # Return the number of squares


def SquareCalculatorWhite():  # This method calculate player white's number of white squares.
    n = len(game_field)
    m = len(game_field[1])
    map = {}
    whitesquares = 0

    for i in range(0, n):  # Iterating among the game board and specify the player's sign.
        for j in range(0, m):
            if game_field[i][j] == "  W  ": # Find the sign
                for k in range(j + 1, m):
                    if game_field[i][k] == "  W  ": # Check is it square
                        if (j, k) in map:
                            whitesquares += 1
                        else:
                            map[(j, k)] = 0
    return whitesquares # Return the number of squares

def MovePiece(): # This method provides to player can move its piece coordinate to coordinate.
    while True:
        move = input("Enter the coordinate of your piece and target location of your piece(eg. A1 D4) :")
        move_list = move.split()
        move = list(move_list)
        current_location = move[0]  # Input is splitted and listed properly for index addressing and chance coordinates by moving.
        target_location = move[1]
        if current_location and target_location in possible_inputs:
            break
        else:
            print("You entered invalid value. Please Enter the coordinate of your piece and target location of your piece again.")

    str = game_field[int(current_location[1]) - 1][letters.index(current_location[0])]
    game_field[int(current_location[1]) - 1][letters.index(current_location[0])] = "  *  "  # Field will be empty when the piece is moved somewhere else.
    game_field[int(target_location[1]) - 1][letters.index(target_location[0])] = str # Piece new location
    ShowGameField()


ShowGameField() # Game is started with show game board in the beginning of game
print("Moving turns is started. First move is from Player White. \n")

boardIsFull = False
while boardIsFull is False:
    print("Player White piece placing move") # Piece placing is started with player white
    WhitePlacingPiece()
    print("*******************************\n")
    print("Player Black piece placing turn")
    BlackPlacingPiece()
    print("*******************************\n")
    boardIsFull = BoardIsFull() # If game board is full next to other part of the game.

print("Piece placing is over. Players ready to remove the opponent's pieces")
print("White is removing Black's pieces.\n")

whiteiter = SquareCalculatorWhite()  # PLayers ready to remove their opponent's pieces.
if horizontal_line > 3:
    whiteiter -= 1
for i in range(whiteiter + 1):
    RemovePiece() # Players can take out the opponent's pieces as many as the number of squares.
    whitepieces -= 1 # For every removing player's number of pieces is decrementing

print("Black is removing White's pieces.\n")


blackiter = SquareCalculatorBlack()
if horizontal_line > 3:
    blackiter -= 1
for i in range(blackiter + 1):
    RemovePiece() # Players can take out the opponent's pieces as many as the number of squares.
    blackpieces -= 1 # For every removing player's number of pieces is decrementing

print("Piece removing turns are done. Lets play moves! \n")

while blackpieces > 3 or whitepieces > 3:  # Until any player has 3 pieces left players move their pieces to make squares.
    print("White's move turn\n")
    MovePiece()
    anySquareWhite = SquareCalculatorWhite() # Checking squares after all movings
    for i in range(anySquareWhite):
        RemovePiece() # If there are any squares player white can remove player black's any pieces to outside of game
        whitepieces -= 1

    print("Black's move turn\n")
    MovePiece()
    anySquareBlack = SquareCalculatorBlack()
    for i in range(anySquareBlack):
        RemovePiece() # If there are any squares player black can remove player white's any pieces to outside of game
        blackpieces -= 1


if whitepieces > blackpieces:
    print("Winner is WHITE PLAYER !! \n")
else:
    print("Winner is BLACK PLAYER !! \n")

print("Program by Emin Berke Aydın")
