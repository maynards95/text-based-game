# Ezra Maynard

# Sample function showing the goal of the game and move commands
def show_instructions():
    # print a main menu and the commands
    print("Dragon Text Adventure Game")
    print("Collect 6 items to win the game, or be eaten by the dragon.")
    print("Move commands: go South, go North, go East, go West")
    print("Add to Inventory: get 'item name'")


# In this solution, the player’s status would be shown in a separate function.
# You may organize your functions differently.

def main():
    # calling function in order to display instructions for player
    show_instructions()
    # create dictionary with all the rooms and items inside
    rooms = {'Great Hall': {'South': 'Kitchen', 'North': 'Sunroom', 'West': 'Morgue', 'East': 'Dungeon', 'item': None},
             'Morgue': {'East': 'Great Hall', 'item': 'Death Element'},
             'Sunroom': {'South': 'Great Hall', 'East': 'Chapel', 'item': 'Light Element'},
             'Chapel': {'West': 'Sunroom', 'item': 'Life Element'},
             'Kitchen': {'North': 'Great Hall', 'East': 'Study', 'item': 'Fire Element'},
             'Study': {'West': 'Kitchen', 'item': 'Earth Element'},
             'Dungeon': {'West': 'Great Hall', 'North': 'Throne Room', 'item': 'Shadow Element'},
             'Throne Room': {'South': 'Dungeon', 'item': 'Gandor'}
             }

    location = 'Great Hall'

    # create list for inventory
    inventory = []

    # Loop to move player based on user input
    while True:

        # If player goes to Throne Room without all 6 items, game is over.
        if location == 'Throne Room':
            print("\nYou are in the", location)
            print("You see Gandor!", )
            if len(inventory) == 6:
                print("\nYou watch as the elements weaken Gandor...")
                print("Congratulations! You have defeated Gandor!!")
            else:
                print("\nHe's too powerful...GAME OVER!")
            break

        # updating location
        print("\nYou are in the", location)

        # Taking user input for items
        if rooms[location]['item'] != None:
            print("You see the", rooms[location]['item'])
            user_input = input("Grab " + rooms[location]['item'] + "?(Y/N): ").upper()

            # Validating input
            while user_input not in ['Y', 'N']:
                print("Invalid input. Try again")
                user_input = input("Grab " + rooms[location]['item'] + "?(Y/N): ").upper()
            if user_input == 'Y':
                inventory.append(rooms[location]['item'])
                rooms[location]['item'] = None
        else:
            print("You already grabbed item or there's nothing here")

        # Printing inventory after input
        print("Inventory:", inventory)

        # Taking user input for direction
        direction = input("\nWhere would you like to move?(East,West,North,South): ").title()
        directions = list(rooms[location].keys())
        directions.remove('item')

        # Validating input
        while direction not in directions:
            print("Invalid move from " + location + ". Try again")
            direction = input("\nWhere would you like to move?(East,West,North,South): ").title()

        # Set next_location
        next_location = rooms[location][direction]
        print("You are in the", next_location)
        print("------------------------------------------------")

        # Updating location
        location = next_location

    # Printing end message
    print("\nThanks for playing the game. Hope you enjoyed it.")


# call main function
main()