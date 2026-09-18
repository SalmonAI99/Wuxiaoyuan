from random import randint
game_map = []
print("Welcome to the game!")
rows = int(input("How many rows? "))
columns = int(input("How many columns? "))

# generate the game maps
for row in range(rows):
    game_map.append([])
    for column in range(columns):
        game_map[row].append("░░")

# pick the snake starting cordinate
snake_row = randint(0, rows - 1)
snake_column = randint(0, columns - 1)

snake_body = []
snake_body.append([snake_row, snake_column])

# pick the food cordinate
food_row = randint(0, rows - 1)
food_column = randint(0, columns - 1)

while True:
    # if the snake in our of the borders, the game end
    if snake_row < 0 or snake_row > rows - 1 or snake_column < 0 or snake_column > columns - 1:
        print("You lose!, since you can't teleport trough the walls")
        break
    # set the snake body
    for body_part in snake_body:
        game_map[body_part[0]][body_part[1]] = "██"
    
    # set the food
    game_map[food_row][food_column] = "🍎"

    # make every empty space a "░░"
    for row in range(rows):
        for column in range(columns):
            if [row, column] not in snake_body and [row, column] != [food_row, food_column]:
                game_map[row][column] = "░░"

    # print the game map
    for row in game_map:
        print("".join(row))
    print("\n")
    
    move = input("Enter your move: ")
    if move == "q":
        break
    elif move == "w":
        if [snake_row - 1, snake_column] in snake_body:
            print("You died!")
            break
        snake_body.append([snake_row - 1, snake_column])
        snake_row -= 1
        if [food_row, food_column] in snake_body:
            while [food_row, food_column] in snake_body:
                food_row = randint(0, rows - 1)
                food_column = randint(0, columns - 1)
        else:
            # remove the last body part if it's not eating the food
            snake_body.pop(0)
    
    elif move == "s":
        if [snake_row + 1, snake_column] in snake_body:
            print("You died!")
            break
        snake_body.append([snake_row + 1, snake_column])
        snake_row += 1
        if [food_row, food_column] in snake_body:
            while [food_row, food_column] in snake_body:
                food_row = randint(0, rows - 1)
                food_column = randint(0, columns - 1)
        else:
            snake_body.pop(0)
    
    elif move == "a":
        if [snake_row, snake_column - 1] in snake_body:
            print("You died!")
            break
        snake_body.append([snake_row, snake_column - 1])
        snake_column -= 1
        if [food_row, food_column] in snake_body:
            while [food_row, food_column] in snake_body:
                food_row = randint(0, rows - 1)
                food_column = randint(0, columns - 1)
        else:
            snake_body.pop(0)
    
    elif move == "d":
        if [snake_row, snake_column + 1] in snake_body:
            print("You died!")
            break
        snake_body.append([snake_row, snake_column + 1])
        snake_column += 1
        if [food_row, food_column] in snake_body:
            while [food_row, food_column] in snake_body:
                food_row = randint(0, rows - 1)
                food_column = randint(0, columns - 1)
        else:
            snake_body.pop(0)
    
    else:
        print("Invalid move!")
        continue
