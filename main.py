from sudoku import Sudoku

# user_map = [[0, 9, 7, 2, 3, 0, 8, 0, 0],
#             [0, 3, 0, 1, 0, 0, 7, 0, 0],
#             [0, 5, 0, 0, 0, 0, 0, 0, 9],
#             [9, 0, 0, 7, 0, 0, 5, 2, 0],
#             [0, 2, 0, 0, 1, 0, 0, 6, 0],
#             [0, 4, 6, 0, 0, 2, 0, 0, 1],
#             [4, 0, 0, 0, 0, 0, 0, 9, 0],
#             [0, 0, 5, 0, 0, 9, 0, 8, 0],
#             [0, 0, 9, 0, 2, 8, 6, 0, 0]]


def print_grid(mapp):
    for ind1, item1 in enumerate(mapp):
        line1 = ind1 / 3
        if line1 == 1 or line1 == 2 or line1 == 3:
            print("\n+-------+-------+-------+")
        elif line1 == 0:
            print("+-------+-------+-------+")
        else:
            print("")
        for ind2, item2 in enumerate(item1):
            line2 = (ind2 + 1) / 3
            if line2 == 1 or line2 == 2 or line2 == 3:
                if item2 is None:
                    item2 = " "
                print(str(item2) + " |", end=' ')
            elif ind2 == 0:
                if item2 is None:
                    item2 = " "
                print("| " + str(item2), end=' ')
            else:
                if item2 is None:
                    item2 = " "
                print(str(item2), end=' ')
    print("\n+-------+-------+-------+")


def check_possible(row, col, num):
    global game_map

    # This will check if there are any matches in the rows and if there is, it will return False
    for i in range(0, 9):
        if game_map[row][i] == num:
            return False

    # This will check if there are any matches in the columns and if there is, it will return False
    for i in range(0, 9):
        if game_map[i][col] == num:
            return False

    # This will check if there are any matches in the boxes and if there is, it will return False
    x = (row // 3) * 3
    y = (col // 3) * 3
    for i in range(0, 3):
        for j in range(0, 3):
            if game_map[x + i][y + j] == num:
                return False

    # If there are no matches, it will assume its valid and return True which means the number belongs in this field
    return True


def answer():
    global game_map
    # Iterates through each of the suduko cells
    for i in range(0, 9):
        for j in range(0, 9):
            # Checks if the cell is empty
            if game_map[i][j] is None:
                # Brute forces num values 1-9 into the empty cell
                for num in range(1, 10):
                    # if possible, it updates the cell
                    if check_possible(i, j, num):
                        game_map[i][j] = num
                        # Calls the function again to do the next empty cell. If all num value fails, it is brought
                        # back to the previous recursion and the next possible num value is checked. It will keep doing
                        # this brute force until the valid num is chosen, and there is no other empty cells.
                        val = answer()
                        # Checks if the recursion result is 1 and if it is, then it keeps returning 1 otherwise if its
                        # 0, it will make the cell in question empty again since the num value is wrong and the next
                        # num value will be attempted next
                        if val == 1:
                            return 1
                        else:
                            game_map[i][j] = None
                # Returns 0 if all num values are used and no valid matches are found
                return 0
    # Returns 1 if the there is no more empty cells in the grid left, and it returns it to the previous recursion
    return 1


# Checks if the number passed is correct
def check_answer(row, col, num):
    if game_map[row][col] == num:
        return True
    else:
        return False


# Adds the answer to the game board
def add_answer(row, col, num):
    user_map[row][col] = num


# Checks if the game board matches the answer key
def check_win():
    if user_map == game_map:
        return True
    else:
        return False


print("Welcome to the Sudoku game!")
while True:
    ins = input("Press 1 to play, 2 for instruction and anything else to quit: \n")
    if ins == "1":
        # Asks user what difficulty they prefer
        while True:
            diff = input("How difficult do you want your suduko to be? (1-10): \n")
            if 0 < int(diff) <= 10:
                diff = int(diff) / 10
                break
            else:
                print("Invalid Input")
        # Creates a puzzle with the selected difficulty
        puzzle = Sudoku(3).difficulty(diff)
        user_map = puzzle.board
        # This is how to duplicate lists if it is two dimentional. Game_map is the answered suduko and user_map is
        # the user's game board
        game_map = [x[:] for x in user_map]
        answer()
        print("Problem:")
        puzzle.show()

        while True:
            if check_win():
                print("You beat the Suduko!")
                exit(0)

            ans = input("Enter the cell coordinates and then the number you want to put in it. EG: {x,y,number} {1,1,5} "
                        "is inputing 5 into top left cell. Enter G to give up or enter anything else to quit: \n")

            if ans == "g" or ans == "G":
                print("\nYou failed at completing the puzzle!\n")
                print("Solution:")
                print_grid(game_map)
                exit(0)

            elif ans.isalnum():
                exit(0)

            else:
                try:
                    value = []
                    ans = ans.split(",")
                    for item in ans:
                        value.append(int(item))

                    if check_answer((value[1] - 1), (value[0] - 1), value[2]):
                        print("Correct Answer!")
                        add_answer((value[1] - 1), (value[0] - 1), value[2])
                        print_grid(user_map)
                    else:
                        print("Incorrect Answer!")
                        print_grid(user_map)
                except:
                    print("Invalid Input")
    elif ins == "2":
        print("This is the Sudoku game. You will have to specify the cell column, row and the number you want to enter \n"
              "to play. The game will let you know if its a wrong number or a right number! You can also give up early \n"
              "and the solution will be given to you!\n")
    else:
        exit(0)
