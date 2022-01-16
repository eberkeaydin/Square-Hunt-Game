from string import ascii_uppercase as letter
from colorama import Fore
from colorama import Style

print(f"{Fore.BLUE}*************************************{Style.RESET_ALL}")
print(f"{Fore.YELLOW}**** WELCOME TO THE SQUARE HUNT ****{Style.RESET_ALL}")
print(f"{Fore.BLUE}*************************************{Style.RESET_ALL}")

while True:
    try:
        horizontal_line = int(input(f"{Fore.CYAN}Enter the number of horizontal line(3, 7) : "))
    except ValueError:
        print("You entered invalid value. Please enter the number of horizontal line again.")
        continue
    if horizontal_line in [3, 4, 5, 6, 7]:
        break
    else:
        print("You entered invalid value. Please enter the number of horizontal line again.")
        continue


vertical_line = horizontal_line + 1
whitepieces = blackpieces = horizontal_line * vertical_line / 2
possible_inputs = {"A1", "B1", "C1", "D1", "E1", "F1", "G1", "H1", "A2", "B2", "C2", "D2", "E2", "F2", "G2", "H2", "A3",
                   "B3", "C3", "D3", "E3", "F3", "G3", "H3", "A4", "B4", "C4", "D4", "E4", "F4", "G4", "H4", "A5", "B5",
                   "C5", "D5", "E5", "F5", "G5", "H5", "A6", "B6", "C6", "D6", "E6", "F6", "G6", "H6", "A7", "B7", "C7",
                   "D7", "E7", "F7", "G7", "H7"}

letters = letter[:vertical_line]
game_field = [['  *  ' for i in range(vertical_line)] for i in range(horizontal_line)]


def ShowGameField():
    numbers = iter(range(1, vertical_line))
    print("Game Field : \n")
    print('    ' + '  -  '.join(letters))
    for i in game_field:
        print(next(numbers), end=' ')
        print('|'.join(i))
    print('    ' + '  -  '.join(letters) + "\n")
    return game_field


def WhitePlacingPiece():  # Taş yerleştirmek
    while True:
        placing = input("Enter the placing move for your piece(eg. D3) :")
        if placing in possible_inputs:
            break
        else:
            print("You entered invalid value. Please enter the placing move for your piece again.")

    placing = list(placing)  # Girilen inputu karakter karakter ayırarak bir listeye atar.
    game_field[int(placing[1]) - 1][letters.index(placing[0])] = '  W  '
    ShowGameField()


def BlackPlacingPiece():  # Taş yerleştirmek
    while True:
        placing = input("Enter the placing move for your piece(eg. D3) :")
        if placing in possible_inputs:
            break
        else:
            print("You entered invalid value. Please enter the placing move for your piece again.")

    placing = list(placing)  # Girilen inputu karakter karakter ayırarak bir listeye atar.
    game_field[int(placing[1]) - 1][letters.index(placing[0])] = '  B  '
    ShowGameField()


def FieldIsFull(controll):
    if controll != "  -  ":
        return False
    else:
        return True


def BoardIsFull():
    emptyFields = 0
    for i in range(len(game_field)):
        for j in range(len(game_field[i])):
            if game_field[i][j] == "  *  ":
                emptyFields += 1
    if emptyFields > 1:
        return False
    else:
        return True


def RemovePiece():
    while True:
        removing = input("Enter the removing move for opponent's piece(eg. D3) :")
        if removing in possible_inputs:
            break
        else:
            print("You entered invalid value. Please Enter the removing move for opponent's piece again.")
    removing = list(removing)  # Girilen inputu karakter karakter ayırarak bir listeye atar.
    game_field[int(removing[1]) - 1][letters.index(removing[0])] = '  *  '
    ShowGameField()


def SquareCalculatorBlack():
    n = len(game_field)
    m = len(game_field[1])
    map = {}
    blacksquares = 0

    for i in range(0, n):
        for j in range(0, m):
            if game_field[i][j] == "  B  ":
                for k in range(j + 1, m):
                    if game_field[i][k] == "  B  ":
                        if (j, k) in map:
                            blacksquares += 1
                        else:
                            map[(j, k)] = 0
    return blacksquares


def SquareCalculatorWhite():
    n = len(game_field)
    m = len(game_field[1])
    map = {}
    whitesquares = 0

    for i in range(0, n):
        for j in range(0, m):
            if game_field[i][j] == "  W  ":
                for k in range(j + 1, m):
                    if game_field[i][k] == "  W  ":
                        if (j, k) in map:
                            whitesquares += 1
                        else:
                            map[(j, k)] = 0
    return whitesquares

def MovePiece():
    move = input("Enter the coordinate of your piece and target location of your piece(eg. A1 D4) :")
    move_list = move.split()
    move = list(move_list)
    current_location = move[0]
    target_location = move[1]
    str = game_field[int(current_location[1]) - 1][letters.index(current_location[0])]
    game_field[int(current_location[1]) - 1][letters.index(current_location[0])] = " - "
    game_field[int(target_location[1]) - 1][letters.index(target_location[0])] = str
    ShowGameField()


ShowGameField()
print("Game is started. First move is from Player White. \n")

boardIsFull = False
while boardIsFull is False:
    print("Player White piece placing move")
    WhitePlacingPiece()
    print("*******************************\n")
    print("Player Black piece placing turn")
    BlackPlacingPiece()
    print("*******************************\n")
    boardIsFull = BoardIsFull()

print("Piece placing is over. Players ready to remove the opponent's pieces")
print("White is removing Black's pieces.\n")

whiteiter = SquareCalculatorWhite()
if horizontal_line > 3:
    whiteiter -= 1
for i in range(whiteiter + 1):
    RemovePiece()
    whitepieces -= 1

print("Black is removing White's pieces.\n")


blackiter = SquareCalculatorBlack()
if horizontal_line > 3:
    blackiter -= 1
for i in range(blackiter + 1):
    RemovePiece()
    blackpieces -= 1

print("Piece removing turns are done. Lets play moves! \n")

while blackpieces > 3 or whitepieces > 3:
    print("White's move turn\n")
    MovePiece()
    anySquareWhite = SquareCalculatorWhite()
    for i in range(anySquareWhite):
        RemovePiece()
        whitepieces -= 1

    print("Black's move turn\n")
    MovePiece()
    anySquareBlack = SquareCalculatorBlack()
    for i in range(anySquareBlack):
        RemovePiece()
        blackpieces -= 1


if whitepieces > blackpieces:
    print("Winner is WHITE PLAYER !! \n")
else:
    print("Winner is BLACK PLAYER !! \n")

print("Program by Emin Berke Aydın")











