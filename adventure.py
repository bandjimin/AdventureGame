import random
# We getting lit in here
# BASIC FUNCTIONS

def is_dead(odds_of_death): # Using random.randint() to give a boolean output
    '''
    PARAMS
    --------
    odds_of_death : int

    RETURNS
    --------
    boolean : stating if dead or alive
    '''
    if random.randint(1, 100) <= odds_of_death:
        return True
    else:
        return False
    
def roll_dice(dice=1): # Able to roll multiple die
    # The sad part is that I have no idea how dice probability works
    '''
    PARAMS
    --------
    dice : int if none, dice=1
    RETURNS
    --------
    int : sum of all dice rolls
    '''
    sum = 0
    for roll in range(dice):
        sum += random.randint(1, 6)
    return sum

def english(list, con): # turning lists into phrases cuz reasons
    '''
    Recieve a list of strings
    Return a string
    '''
    phrase = ""
    new_list = ["a " + x for x in list]
    if not type(list) == type([]) or len(list) == 0:
        print("Why did you try to do that?")
    elif len(list) > 2:
        for word in list[:-1]:
            phrase += word + ", "
        phrase += f"{con} " + list[-1]
    elif len(list) == 2:
        phrase = list[0] + f" {con} " + list[1]
    elif len(list) == 1:
        phrase += list[0]

    return phrase

# GAME FUNCTIONS
# TODO make a function for... 
# entering rooms (restrict which rooms you can enter + is_dead()) 
# and mini games (use roll_dice() & be creative)

'''
def list_numbers(list_of_nums):
    if len(list_of_nums) == 1:
        return f"{list_of_nums[0]}"
    elif len(list_of_nums) == 2:
        return 
'''

def enter_room(room, items):
    # Acts as the main center where my game is played
    '''
    PARAMS
    --------
    room : str
    items : list

    RETURNS
    --------
    boolean : did you die in the room?
    str : next_room
    '''
    dead = False
    new_items = []
    if room == "Room 1": # Choose your weapon... or not
        chosen = False # I want the player to choose a weapon
        weapons = ["wand", "sword", "bow"]
        print("In front of you, three weapons float in an ominous light")
        if is_dead(10): 
            print("You trip on a rock and hit your head")
            print("Some adventures are shorter than others")
            return(True, "hell", new_items)
        while len(weapons) > 0: # will run forever if I don't get rid of weapons
            if len(weapons) >= 2:
                print(f"The weapons are {english(weapons, 'and')}")
            elif len(weapons) == 1:
                print(f"Now we're left with a {weapons[0]}")
            while True: # iterates if the answer is not a weapon
                if len(weapons) == 1:
                    answer = weapons[0]
                    print(f"With nothing else to reach for you pick the {answer}")
                else:
                    answer = input(f"You reach for the ")
                if answer in weapons:
                    print(f"You must roll higher than a 4 to weild the {answer}")
                    break
                else:
                    print("That is not a valid weapon")  
            # once a weapon is chosen we roll to see if we can take it
            roll = roll_dice()
            print(f"You rolled a {roll}")
            if roll > 4:
                new_items += [answer]
                if answer == "wand":
                    print("You're a wizard, Harry!")
                print(f"You now weild the {answer}")
                break
            else:
                weapons.remove(answer)
                print(f"The {answer} shatters and the light from underneath dims")
        else: # if you run out of weapons
            print("I guess we're using our fists now")
            print("As all weapons have shattered the ground underneath crumbles")
            while True: # only breaks when given a correct answer either by returning a value or by the 'break'
                answer = input("Would you like to go down the pit (Y/N)? ")
                if answer == "Y":
                    print("Being prone to adventure is a virtue for adventurers")
                    print("Without looking back, you jump into the pit")
                    return(False, "Room 4", new_items) # Room 4 only available when u fail to get a weapon
                elif answer == "N":
                    print("Holes in the ground are quite suspicious")
                    print("So it makes sense that you would try to avoid them")
                    break
                else:
                    print("Give a valid answer")
        print("Moving away from front of the room, a door opens up")
        print("With nowhere else to go, you choose to enter")
        print("And, after you enter, the door promptly shuts")
        return(False, "Room 2", new_items)
    elif room == "Room 2": # A Treasure Chest?!
        # Apple side quest
        print("An apple falls from the ceiling")
        answer = input("Without any time to think, do you wish to eat the apple (Y/N)? ")
        if answer == "Y":
            print("You immediately pick up the apple and take a bite")
            print("You need two 6s for something fun")
            if roll_dice(2) == 12:
                print("Woah, you rolled two 6s")
                print("You're one lucky bastard")
                print("Wait, why is it getting so dark")
                print("The room is spinning and the last sight you see \nare purple clouds encapsulating your body")
                new_items += ["half-eaten apple"]
                return(False, "Room 3", new_items)
            if is_dead(20):
                return(True, "hell", new_items)
            print("...")
            print("Nothing happened")
            print("...")
        else:
            print("Wrong answer, bozo")
            print("The apple disappears and a purple gas is left in its absence")
            print("...")
            print("Maybe you made the right decision")
            print("...")
        answer = input("Do you think you made the right choice (Y/N)? ") # Purpose of slowing down code
        # Surprise attack mofo
        print("Damn, out of nowhere a goblin jumps in your face and you see a dagger in its hand")
        roll = roll_dice()
        print("You need to roll a die higher than 4 to come out unscathed")
        print(f"You rolled a {roll}")
        if roll > 4:
            new_items += ["goblin tooth"]
            print(f"You beat the ever loving shit out of that goblin")
            if len(items) > 0:
                print(f"The goblin had no chance against your {items[0]}")
                print("You made it through your first fight unscathed")
            else:
                print("Your fists are left bloodied by the goblin's blue blood")
        else:
            if is_dead(30):
                print("The goblin swings at your head and splits it in two")
                print("I didn't know skulls were that thin")
                print("They shouldn't be that thin")
                print("That goblin was probably on steroids")
                return(True, "hell", new_items)
            print("You turn to the left and blood drips from your shoulder")
            print("The goblin runs away, possibly proparing for another attack")
            print("You look in the direction of the goblin and see three paths")
            print("The areas where the goblin did not go seems a lot brighter")
            answer = input("Do you wish to chase after the goblin (Y/N)? ")
            if answer == 'Y':
                print("You choose to chase after the goblin")
                return(False, "Room 5", new_items) # We move onto the next fight
            else:
                print("You're no fun")
        print("...")
        print("A room to the right exudes warmth")
        print("and you can hear noises in the other room")
        answer = input("Do you pick the room to the right or left(R/L)? ")
        if answer == 'R':
            return(False, "Room 6", new_items)
        else:
            print("Your time for adventure is now over")
            print("You've experienced violence and you liked it?")
            print("As you leave, the exit has a sign saying...")
            print("'Take care! Come back soon!'")
            return(False, "exit", new_items)
    elif room == "Room 3": # Special Pokemon Level
        # TODO this room
        print("Suddenly, you're outside of the dungeon")
        print("You're in tall grass")
        print("You approach a man in a white coat")
        print("The man speaks 'Hello, I'm Professor Oak'")
        while True:
            answer = int(input("'Pick one of these balls (1, 2, 3)' "))
            if answer in range(1,4):
                break
            else:
                print("'You better pick one of these balls to grab'")
        if answer == 1:
            new_items += ['Charmander']
            print("You got Charmander")
        elif answer == 2:
            new_items += ['Squirtle']
            print("You got Squirtle")
        else:
            new_items += ['Bulbasaur']
            print("You got Bulbasaur")
        print("'Since I love children so much, here are some more balls'")
        print("...")
        print("The professor disappears in the tall grass")
        print("...")
        print("You see the purple clouds of gas appearing in front of you")
        answer = input("Do you wish to go enter the purple cloud (Y/N)? ")
        if answer == "N":
            print("You choose to stay in this new world for a bit longer")
            print("This means that your dungeon adventure is no more")
            print("NOTE: stay turned for adventure game 2")
            return(False, "exit", new_items)
        else:
            print("The cloud starts sucking in all of its surroundings")
            print("With no escape, you submit to these unnatural forces")
            return(False, "Room 6", new_items) # Lead to boss battle
    elif room == "Room 4": # Become Spider-man... or not
        # Dark dungeons are cool
        # This room is all luck and text
        print("You're walking in the dark and the air is thick")
        print("A spider crawls up your leg, across your arm,")
        print("and its fangs sink into your skin")
        if is_dead(50):
            print("You faint and fall to the floor")
            print("Your body couldn't handle the venom")
            return(True, "hell", new_items)
        print("You feel the bite as you walk into some light")
        answer = input("Do you feel like a merciful person right now (Y/N)? ")
        if answer == "N":
            print("You smack the spider into the dark ages")
            print("The spider weirdly falls upward")
        else:
            print("You place the spider on the ground")
        print("You witness water dripping from the floor to the ceiling")
        print("Webs start flowing out from your wrists")
        answer = input("What the hell is going on? ")
        print("After finding that you have all these powers,")
        print("you move forward seeking a foe to smackdown")
        print("You reach a cave and hear loud growls from the outside")
        new_items += ['spider powers']
        return(False, "Room 6", new_items) # Lead to boss battle
    elif room == "Room 5": # Pre-Boss Fight against an army of goblins
        # This is gonna be a lame room cuz I left it for last
        # Which is quite sad
        print("You've entered the goblin's den")
        print("Waves of green surround you and you turn to run")
        print("Roll a 6 to escape")
        roll = roll_dice()
        print(f"You rolled a {roll}")
        if roll == 6:
            print("Luckily you find a nice cave to hide in and the goblins all rush along")
            return(False, "Room 6", new_items) # Lead to boss battle
        else:
            new_items += ['ass-whooping']
            if is_dead(80):
                print("The goblins gang up on you and your mangled body lies on the floor")
                print("The goblins can't help but take a bite")
                print("After a short period of time, all that's left is a pile of bones")
                return(True, "hell", new_items)
            else:
                print("You lie on the floor and the goblins trample over your body")
                print("...")
                print("You wake up and realize that you are alive")
                print("You crawl towards sounds of speaking")
                print("You reach a sign that says 'exit'")
                print("You've escaped the horrors of the dungeon")
                print("But at what cost?")
                return(False, "exit", new_items)
    elif room == "Room 6": # Boss Battle
        valid_rooms = ["exit"]
        print("You've entered the dragon's lair")
        print("Prepare to die, naive little human")
        dragon_breath = 0
        while True:
            dragon_breath += 1
            if "spider powers" in items: # If extremely lucky, you get an advantage
                print("Using your spider powers, you web up the dragon's mouth")
                dragon_breath = 0
                print("With fists 10x stronger than a normal person,")
                print("the dragon will go down quickly")
                odds = 5
            else:
                odds = 9 # TODO Add items to make end fight easier
            print(f"The dragon growls, it has a {dragon_breath*10}% chance of attacking")
            print(f"For a critical hit, roll two die with a sum higher than {odds}")
            attack = input("Do you wish to attack or run (A/R)? ")
            if attack == "A":
                roll = roll_dice(2) # sum of two die
                print(f"You rolled a sum of {roll}")
                if roll > odds: # roll higher than 
                    print("Wait, did you just kill a dragon?")
                    new_items += ["Dragon's Head"]
                    print("Congrats brave adventurer on this incredible feat!")
                    return(False, "the Treasure Room", new_items) # Treasure Room triggers end sequence
            elif attack == "R":
                print("Congrats you've protected your fragile existence")
                print("Run away and never come back")
                return(False, "exit", new_items) # No need to ask where to go next because you choose to run
            else:
                print("What the hell did you just say?")
            print("The dragon prepares an attack")
            dragon_attack = random.randint(1,10)
            if dragon_attack <= dragon_breath:
                print("The dragon's breath fires out from its mouth")
                if is_dead(80): # 80% of being burnt to a crisp
                    dead = True # if true u dead
                    print("As you attempt to dodge, you are burnt to a crisp")
                    break
                print("You barely dodge the attack")
    else: # if used in other code and room input is incorrect
        print("What just happened?") 
    
    if dead: # death is easier to have here
        return(dead, "hell", new_items)
    
    return(False, "exit", ["error bunny"])

    # Below, I had the thought of letting them choose a room
    # But, since it is a dungeon I made the route more linear
    # So therefore, less control and freedom for the player
    # Easier for me and also ways of ending the game is...
    # End cases: completing, exiting, or dying in the dungeon
    '''
    print("You have access to ", end = " ")
    for room in valid_rooms:
        print(f"{room}")
    next_room = input("Where do you want to go into next? ")
    while next_room != valid_rooms:
        print(f"What is {next_room}? You don't have access to that room.")
        next_room = input("Choose a room you can enter: ")

    return(dead, next_room, new_items)
    '''

if __name__ == "__main__":
    '''
    TEST CASES for BASIC FUNCTIONS
    print(is_dead(0))
    print(is_dead(50))
    print(is_dead(100))
    print(roll_dice())
    print(roll_dice(3))
    '''
    # TODO create a compelling storyline that moves the user
    # think of 6 creative mini games
    # think of alternate endinds // not including death
    # endings: 
    # - hero (save the princess) 
    # - escape (leave the castle) 
    # - king (take the crown)
    # - friend (leave with a buddy)
    # create a game map to solidify my thoughts

    # Test cases
    # dead, next_room, new_items = enter_room("Room 2", [])
    # print(dead)
    # print(next_room)

    
    print("You wake up and find that you're in a dungeon")
    print("The only way out is to move forward")
    print("In front of your face you see a door")
    print("With nothing better to do, you enter")
    items = []
    dead = False
    next_room = 'Room 1'
    while not dead and next_room != "exit" and next_room != "the Treasure Room":
        dead, next_room, new_items = enter_room(next_room, items)
        items += new_items
    else:
        if dead:
            print("You dead")
        elif "Dragon's Head" in items:
            print("For your brave actions, you gain access to the Treasure Room")
        else: # 
            print("Goodbye brave adventurer")
        print()

        # Achievements
        print("GAMEOVER")
    
    