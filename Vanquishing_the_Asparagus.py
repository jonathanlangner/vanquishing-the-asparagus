#Jonathan Langner

#Text based input game, alpha version 0.12.
#Player moves through rooms, collects items before moving to the end.
#If the player arrives at the end without six items, the game is lost.

#Provides dictionary data for the gameplay map, the logic, and the interface.
#Recommended data structure for this game would be a list instead of a dictionary, as it allows the game to be extended.
#Additionally, to make the game more fun, it would be ideal to add random generation of dishes, text outputs, and mini-games like Simon Says.

#Print function which provides the player with guidance for how to play the game.
#print_game_tutorial is called from the game menu.
def print_game_tutorial():
    line_output_string = "------------------------------------------------------------------------------" # simplifies adjustments to frequently used code.
    print(line_output_string)
    print("* Story *") #Prints the story and theme for the game.
    print("Greetings. You work for Aardvark's and Suns Analytical Systems LLC.")
    print("It is your task to be able to eat the famous Lemon Asparagus Coffee Stew in front of the office board of Kilocalories LLC to show respect and trust.")
    print("To be able to show respect, you must be able to eat the stew without showing disgust or unhappiness to conclude this imperative business deal.")
    print("Unfortunately, your psychological profile indicates you are very picky eater.")
    print("To remedy this troubling issue, our company's creative ideation department has proposed a personal improvement plan to aid you in this task.")
    print("To succeed: you must travel to various locations in the local area and eat at least six unique dishes prior to entering the board meeting.")
    print("Failure to meet your personal improvement plan will result in your employment being terminated at Aardvark's and Suns Analytical Systems LLC.")
    print("Additionally, if you fail, you will also forfeit the Christmas Bonus of the Graham Cracker Custard Strawberry Rhubarb Pie.")
    print(line_output_string)
    print("* Ingame Controls *") #Provides the player controls.
    print(f"type \"help\" and then press enter at any time for help.") # the \" provides tells print to not process the parathesis as code.
    print(f"Press \"0\" and then press enter to move north.")
    print(f"Press \"1\" and then press enter to move east.")
    print(f"Press \"2\" and then press enter to move south.")
    print(f"Press \"3\" and then press enter to move west.")
    print(f"type \"eat\" and then press enter to eat a dish.")
    print(f"Type \"exit\" and then enter at anytime to exit the game.")
    print(line_output_string)
    print_menu_interface_graphics() # Calls the menu interface after the tutorial so the player can see the menu inputs again immediately after the tutorial.

#Prints possible controls, which are mapped in the get_player_input function.
#Can be called at anytime in the main game using the help command, cannot be called from the game menu.
def print_help_interface():
    print(f"type \"help\" and then press enter at any time for help.") #Reminds player of basic help command.
    print(f"Press \"0\" and then press enter to go north.") #Player move direction controls.
    print(f"Press \"1\" and then press enter to go east.")
    print(f"Press \"2\" and then press enter to go south.")
    print(f"Press \"3\" and then press enter to go west.")
    print(f"Type \"map\" and then press enter to a rough overview of the locations. ") #Prints the map.
    print(f"Type \"eat\" and then press enter to eat a dish.") #Eats a dish.
    print(f"Type \"exit\" and then enter to exit the game.") #Exits game with a polite message.

#Provides a print out of the main menu graphics functionality for game.
def print_menu_interface_graphics():
    print("------------------------------------------------------------------------------")
    print("                          Vanquishing The Asparagus                           ") #Game title
    print("__--------------------------------------------------------------------------__")
    print("Welcome to Vanquishing The Asparagus!")
    print("To Begin Playing: please type \"start\" on your keyboard, and then press enter.") #Provides command to start game
    print("To Learn How to Play: please type \"tutorial\" on your keyboard, and then press enter.") #Provides command to read story and see controls for game
    print("To Exit: please type \"exit\" on your keyboard, and then press enter.") #Provides opportunity to exit.
    print("Please enter an option:")

#Prints a readout of the game map.
#Left locations intentionally blank in most cases, to allow the player the opportunity for discovery.
# Gave basic layout of the game however to allow the player to see possible locations without certainty of victory.
def print_game_map():
    print("#############################     ################     ########################")
    print("#                           # --> #              # --> #                      #") # --> indicates a move west possibility. <-- indicates a move east possibility.
    print("############################# <-- ########^^###### <-- ##################^^####") # ^^ indicates a north or south possibility.
    print("#############################      #######^^################     ########^^#######")
    print("#                           # -->  #Aardvark's and Suns LLC# --> #               #")
    print("###########^^################ <--  ############^^########### <-- #################")
    print("###########^^##################     ###########^^###########     ###########################")
    print("#                             # --> #                      # --> #                         #")
    print("############################### <-- ######################## <-- ###########################")


#Gets player input and cleans it.
#ingame provides a boolean value to indicate whether one is on the menu or not.
#current_location_list_value tells passes the present location for usage with move validation.
#consumed_dish_list is used to print what has been consumed or eaten so far.
def get_player_input(ingame, current_location_value, consumed_dish_list):
    if ingame: #If the game has started, and if this is NOT the menu
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~") #Formatting for the interface
        print(f"Your current room is {current_location_value}") #Prints current location value.
        print(f"Dishes consumed so far: {consumed_dish_list}") #Prints the list of consumed dishes so far.
        print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(f"                                    Compass                                     ")#Compass print out to make directional controls more practical.
        print(f"                    Type 0 and press enter to move North")
        print(f"                                       |")
        print(f"Type 3 and press enter to move West ~~~~~~~ Type 1 and press enter to move East")
        print(f"                                       |")
        print(f"                     Type 2 and press enter to move South")
        print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(f"For more help type \"help\" and press enter any at time for help.") #Gives player the command to call the function.
        print(f"Please enter a move:") #Asks player next move or command.
    player_input = input() # Gets player input.
    #Checks player_input to runs specific tutorial function from the game menu.
    if (player_input.lower() == "tutorial") and (ingame == False):
        print_game_tutorial() # prints game tutorial from the menu interface if the game hasn't started, and the player is still on the menu.

    # Checks Player Input to return a value for running other functions in main.
    if player_input.lower() == "exit":
        return "exit" #If the player is done playing, and they type exit, they can exit the game.
    elif (player_input.lower() == "start") and ingame == False:
        return "start" #Starts game from the menu. Can only start game, if the game hasn't started yet.
    elif (str(player_input) == "0") and (ingame == True):
        return "North" #Maps player player input 0 if ingame, and returns it as the direction North for the checking values in the location_list
    elif (str(player_input) == "1") and (ingame == True):
        return "East" #Maps player input 1 if ingame, and returns it as the direction East for the checking values in the location_list
    elif (str(player_input) == "2") and (ingame == True):
        return "South" #Maps player input 2 if ingame, and returns it as the direction South for the checking values in the location_list
    elif (str(player_input) == "3") and (ingame == True):
        return "West" #Maps player 3 if ingame, and returns it as the direction North for the checking values in the location_list
    elif (player_input.lower() == "eat") and (ingame == True):
        return "Eat" # Returns the value eat for running the consume_dish function in main loop.
    elif player_input.lower() == "help" and (ingame == True):
        print_help_interface() #prints help text, if player enters help, and if the game has started and the player is not on the menu.
    elif player_input.lower() == "map":
        print_game_map()  # prints game map out, on either the menu, or in game.
    else: #If it isn't any type of known command, direction or value, then it is not a valid control.
        return "Unknown Command" #Narrows the interface possibilities significantly for easier validation

#Checks if player has won or lost the game.
def win_loss_check(consumed_dish_list): #takes in the consumed_dish_list which is a list of dishes which have been consumed.
    if len(consumed_dish_list) >= 6: #if the number of consumed dishes within the list are greater than or equal to six, than the player wins the game.
        print(f"You have entered the Head Office of Kilocalorie LLC.")
        print(f"They place the Lemon Asparagus Coffee Stew in front of you.")
        print(f"You take a bite without hesitation and begin chewing... ")
        print(f"You look up from the Stew and Comment: This absolutely delicious. This company clearly has a highly refined pallet. Thank you.")
        print(f"You spend the next two days off eating the 50lbs of Graham Cracker Custard Strawberry Rhubarb Pie, and sharing it with the bear at Unconstitutional foods.")
        print("You have won the game!")
        return True # Game is won.
    else:
        print(f"You have entered the Head Office of Kilocalorie LLC.")
        print(f"They place the Lemon Asparagus Coffee Stew in front of you.")
        print(f"You take a bite and begin chewing... ")
        print(f"Your expression changes... uncontrollably. It's surprisingly disgusting.")
        print(f"The board immediately calls Aardvark's and Suns Analytical Systems LLC to report your disrespect.")
        print("You are fired, and worst of all: you lose the Christmas Bonus of the Graham Cracker Custard Strawberry Rhubarb Pie.") # The worst case scenario for any player.
        print("You have lost the game.")
        return False #Game is lost.


#Primary location move function and logic.
#current_player_location, where the player is at present. player_move_attempt defines where the player is trying to move to, move_dictionary passes location list to function
def location_move(current_player_location, player_move_attempt, move_dictionary):
    if current_player_location in move_dictionary.keys():  #If a room exists in the location_list which was past as move_dictionary.
        possible_moves = move_dictionary[current_player_location] #If the current_player_location is in the dictionary, assign it to the value of current_player_location.
        if player_move_attempt in possible_moves.keys(): #Checks if the player move is within the value list for room.
            new_location = possible_moves[player_move_attempt] # Assigns the new_location value to room name at the locations value.
            return new_location # Returns the new location value to function.
    print("You walk into a wall. Strange thing to do. Sorry, that is not a valid move direction.") #Lets player know they can't move that way.
    return current_player_location #Returns current_player_location to keep player in the same room.

#Functionality user getting item for consuming a dish.
# current_room passes the value of current room to the function.
# dish_list_data passes the consumed_dish_checklist to the consume dish function to validate eating.
# dish dictionary passes the location list for validating what dishes, if any, are in given location.
def consume_dish(current_room, dish_list_data, dish_dictionary):
    if current_room in dish_dictionary.keys():  # Verifies the existence of current location given the dictionary.
        possible_dish = dish_dictionary[current_room] #Assigns the possible dish space to the current location room.
        if "Dish" in possible_dish.keys(): #Checks to see if a Dish key is actually in the current location
            new_dish = possible_dish["Dish"] #If a dish exists, assign it to new_dish.
            if new_dish in dish_list_data: #If the dish is already in the dish_list_data (consumed_dish_checklist)
                print(f"{new_dish} has already consumed, so it won't help you.") #Lets user know this dish has already been eaten on the list
                return False #returns False for checking in game loop.
            else: #If the dish is not on the list, eat it, and add it to the consumed_dish_checklist
                print(f"You have consumed {new_dish}.") #Let's player know dish was eaten.
                return new_dish
        else: #If there is no dish to eat at a location. #Gives player an error.
            print("There is nothing to eat here.")
            return False
    else:
        return False
def main(): #Main function declaration.
    # Gamemap, Location and Item(Dish) Layout
    # location_list = {} provides a container for the entire dictionary or game space.
    # "Coffees, Toffees, and Squids": {} provides the location name, and the values of possible directions and dishes for the space.
    location_list = {
        "Coffees, Toffees, and Squids": {
            "East": "Spacious Foods", #"Possible Move Direction":"Location Name To Move To in That Direction"
            "Dish": "Squid Ink Rice and Tofu Toffee"}, #"Dish-Item": "Name of Dish - Item to Consume."
        "Spacious Foods": {
            "West": "Coffees, Toffees, and Squids", #"Possible Move Direction":"Location Name To Move To in That Direction"
            "East": "Unconstitutional Foods", #"Possible Move Direction":"Location Name To Move To in That Direction"
            "South": "Aardvark's and Suns Analytical Systems LLC", #"Possible Move Direction":"Location Name To Move To in That Direction"
            "Dish": "Freeze Dried Sushi with Sesame Oil and Marshmallows"}, #"Dish-Item": "Name of Dish - Item to Consume."
        "Unconstitutional Foods": {
            "West": "Spacious Foods",
            "South": "Saluting Salads",
            "Dish": "Tomato Garlic Cucumber Yellow Squash Soup"},
        "Shruthi's Didactic Nutrition": {
            "East": "Aardvark's and Suns Analytical Systems LLC",
            "South": "Almond Solvents Sandwich Shop",
            "Dish": "Cinnamon Scorpion Peppercorn Pickled Lemon"},
        "Aardvark's and Suns Analytical Systems LLC": { #Starting location for the game, so no dish.
            "North": "Spacious Foods",
            "West": "Shruthi's Didactic Nutrition",
            "East": "Saluting Salads",
            "South": "Grate Walls of Waffles"},
        "Saluting Salads": {
            "West": "Aardvark's and Suns Analytical Systems LLC",
            "North": "Unconstitutional Foods",
            "Dish": "Apple Cider Cabbage and Raw Onion Salad"},
        "Almond Solvents Sandwich Shop": {
            "North": "Shruthi's Didactic Nutrition",
            "East": "Grate Walls of Waffles",
            "Dish": "Mustard Peanut Butter Mayo Reuben Sandwich"},
        "Grate Walls of Waffles": {
            "West": "Almond Solvents Sandwich Shop",
            "North": "Aardvark's and Suns Analytical Systems LLC",
            "East": "Head Office of Kilocalorie LLC",
            "Dish": "Whipped Cream Triple Chocolate Cookie Crumb Waffle"},
        "Head Office of Kilocalorie LLC": { #Final Boss.
            "West": "Grate Walls of Waffles",
            "Dish": "Asparagus Stew Respect and Trust Test"}
    }
    consumed_dish_checklist = []  # Data storage for tracking what dishes have been consumed for the consume_dish and print_consumed_dishes functions.

    current_location = "Aardvark's and Suns Analytical Systems LLC"  # Gives a variable to use for defining where the player presently is.
    game_started = False #Value for if the player is on the main menu or not.
    print_menu_interface_graphics() #Prints the game menu, prior to entering the main game loop.

    # Main Game Loop
    while current_location != "exit": #Ends game loop if the player wants to quit game.
        cleaned_input = get_player_input(game_started, current_location, consumed_dish_checklist) #IMPORTANT Gets the cleaned command or value from get_player_input Cleaned refers to direction.
        if cleaned_input == "exit": #If the player input was exit
            current_location = "exit" #End game loop
        elif cleaned_input == "start": #If the player input was start, then set game_started to True, start game.
            game_started = True
        if cleaned_input == "Unknown Command":
            print("Sorry, command was not recognised. Please try again.")
        if (cleaned_input == "North") or (cleaned_input == "East") or (cleaned_input == "South") or (
                cleaned_input == "West"): #If player input was a valid numeric move of 0, 1,2, or 3.
            player_move = cleaned_input #Reassigns a temporary value of player_move to the cleaned input direction.
            current_location = location_move(current_location, player_move, location_list) #Assigns current location, based on move attempt, and passes the location_list for validation purposes.
        elif current_location == "Coffees, Toffees, and Squids": #Checks to see where the player currently is.
            print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~") #Flavor text for this space.
            print("Your eyes water from a very strong dry aged fish smell, with hundreds of smells from the toffee section. ")
            print("You order and get the Squid Ink Rice and Tofu Toffee.")
            print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        elif current_location == "Spacious Foods":
            print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~") #Formatting and flavor text for this space.
            print("You sit down, and roll your eyes, as you read the catch phrase: \"Plenty of space in our foods\". ")
            print("You order the Freeze Dried Sushi with Sesame Oil and Marshmallows.")
            print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        elif current_location == "Unconstitutional Foods":
            print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~") #Formatting and flavor text for this space.
            print("This place looks surprisingly normal, aside from the owner's bear fifteen hundred pound bear which is used to remove ungrateful customers.")
            print("You order the Tomato Garlic Cumber Yellow Squash Soup, and attempt to hide behind the menu from the gaze of that bear.")
            print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        elif current_location == "Shruthi's Didactic Nutrition":
            print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~") #Formatting and flavor text for this space.
            print("You aren't sure who Shruthi is or was. The foods nature is didactic in this place. You feel a strange sense of excitement.")
            print("You order the Cinnamon Scorpion Peppercorn Brine Pickled Lemon and begin crying due to the instructive nature of the place.")
            print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        elif current_location == "Saluting Salads":
            print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~") #Formatting and flavor text for this space.
            print("This place and the salads look very military, with the walls lined with lettuce, radishes, all made to look like aircraft.")
            print("You order the Apple Cider Cabbage and Raw Onion Salad.")
            print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        elif current_location == "Almond Solvents Sandwich Shop":
            print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~") #Formatting and flavor text for this space.
            print("You read the sign at the front of the shop: \"Our almonds will dissolve gold, diamond, and the of course the table.\" ")
            print("You order the Mustard Peanut Butter Mayo Reuben Sandwich.")
            print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        elif current_location == "Grate Walls of Waffles":
            print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~") #Formatting and flavor text for this space.
            print("You see walls lined with rainbow sprinkles, waffles, cookies epoxied into various parabolic shapes and patterns. ")
            print("You order the Whipped Cream Triple Chocolate Cookie Crumb Waffle.")
            print(f"~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        if cleaned_input == "Eat": # Gets the Eat command from the cleaned_input return
            consumed_dish_attempt = consume_dish(current_location, consumed_dish_checklist, location_list) #Gets the consumed dish attempt based the current_location, consumed_dish_checklist, and the location list.
            if consumed_dish_attempt != False: #If the returned value from consume dish doesn't equal false. # False meaning, no dish to consume, and dish not already consumed.
                consumed_dish_checklist.append(consumed_dish_attempt) #Appends new_dish(the return) to consumed_dish_checklist.
        if current_location == "Head Office of Kilocalorie LLC": # The final boss.
            win_loss_check(consumed_dish_checklist) #Call the win_loss_check to verify if the player has the required number of dishes, and prints if the game is won or lost.
            break #Ends the game loop, and goes to Game Exit Message.

    # Game Exit Message
    print("Thank you for playing! Please enjoy the rest of your day.") #Polite Message to Exit Game.

if __name__ == "__main__": #checks if the name main is in the function list for the current file, and prevents the other code from running.
    main() #Calls main function
