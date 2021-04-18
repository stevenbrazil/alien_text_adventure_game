import sys

# A dictionary for the simplified dragon text game
# The dictionary links a room to other rooms.
rooms = {
    'Lounge': {'South': 'Sick Bay', 'North': 'Observation Deck', 'East': 'Transporter Room', 'West': 'Florp\'s Cabin'},
    'Sick Bay': {'North': 'Lounge', 'East': 'Engine Room', 'item': 'Florpian Helmet'},
    'Engine Room': {'West': 'Sick Bay', 'item': 'Jet-Pack'},
    'Bridge': {'South': 'Transporter', 'item': 'General Florp Jiggawatt'},  # villain
    'Observation Deck': {'South': 'Lounge', 'East': 'Operation Room', 'item': 'Reflector Shield'},
    'Operation Room': {'West': 'Observation Deck', 'item': 'Proton Blaster'},
    'Florp\'s Cabin': {'East': 'Lounge', 'item': 'Anti-Gravity Boots'},
    'Transporter Room': {'West': 'Lounge', 'North': 'Bridge', 'item': 'Florpian Snack'}
}


# intro to game with available moves
def show_instructions():
    add_space()
    print("Alien Text Adventure Game")
    print('===========================\n')
    print('How to play:\n')
    print('    You have been abducted by an Alien and trapped on its Spaceship.\n')
    print("    Collect 6 items to win the game, or be vaporized by General Florp Jiggawatt.")
    print("    Move commands: go South, go North, go East, go West")
    print("    Add to Inventory: get 'item name'")
    add_space()


# function for user to enter a valid entry
def not_valid_prompt():
    print('Please Enter a valid move - go South, go North, go West, go East -')
    add_space()


# function to have user enter valid moves that
# can be used to navigate through rooms
def enter_move_prompt():
    return input('Enter move: ')


# function that lets player know that room does not
# have the direction that they specified
def direction_invalid():
    print('You cannot go that way! Please try another direction')
    add_space()


# check to see if player has input a valid move and return the direction
def get_move(move):
    while True:

        if move == 'go South':
            move = 'South'
            break
        elif move == 'go North':
            move = 'North'
            break
        elif move == 'go East':
            move = 'East'
            break
        elif move == 'go West':
            move = 'West'
            break
        elif 'get' in move:
            move = move
            break
        else:
            not_valid_prompt()
            move = enter_move_prompt()
            continue

    return move


# check if player move or direction is in the current room
def change_room(move, room):
    while True:

        if move in room:
            room = room[move]
            break

        elif move not in room:
            direction_invalid()
            move = get_move(enter_move_prompt())
            continue

    return room


# check if item is in player's current room
def see_item(room):
    if 'item' in room:
        # check if item is anti gravity boots or the General. Will not need 'a' in front
        anti_boots = '' if room['item'] == 'Anti-Gravity Boots' or 'General Florp Jiggawatt' else 'a '
        print('You see {}{}'.format(anti_boots, room['item']))
        print('---------------------------')
        if room['item'] == 'General Florp Jiggawatt':
            if len(inventory) < 6:
                print('PEW PEW...you have been vaporized...GAME OVER')
                print('Thanks for playing the game. Hope you enjoyed it.')
                play_again()
            else:
                print('Congratulations! You have collected all items and defeated the General!')
                print('Thanks for playing the game. Hope you enjoyed it.')
                play_again()
    else:
        add_space()


# Check if item exists in room. If so add item to inventory and remove item from room
def get_item(move, room):
    move = move.split()
    move.pop(0)
    move = ' '.join(move)
    if 'item' in room:
        if move == room['item']:
            inventory.append(room['item'])
            print('\n---------------------------')
            print('You have picked up', room['item'])
            print('---------------------------')
            print('Inventory: {}\n'.format(inventory))
            del room['item']
        else:
            print('Please enter valid item name...')

    else:
        print('That item is not in this room!')


# Add space between lines
def add_space():
    print()


# check if player wants to play game again
def play_again():
    print('---------------------------')
    response = input('Would you like to play again... Y or N?: ')
    print('---------------------------')
    if response == 'Y' or response == 'y':
        main()
    elif response == 'N' or response == 'n':
        sys.exit()
    else:
        print('Please enter Y or N')
        play_again()


def main():
    # Make character start in Lounge
    current_room = rooms['Lounge']

    # Start Game
    show_instructions()

    while True:
        player_move = get_move(enter_move_prompt())

        # check if player is trying to get item
        if 'get' in player_move:
            get_item(player_move, current_room)
        # check if player is trying to move through rooms
        else:
            current_room = change_room(player_move, current_room)
            add_space()
            print('You are in the -{}-'.format(current_room))
            print('Inventory: {}'.format(inventory))
            print('---------------------------')
            current_room = rooms[current_room]
            see_item(current_room)


# =======Program Start=======
inventory = []
main()
# =============================
