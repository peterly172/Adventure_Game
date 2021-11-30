import time
import random

weapons = []
enemies = []

weapons = ["Eightfold Longblade", "Fireball", "Claymore", 
"Edge of Duality"]

enemies = ["bison", "devil", "gargoyle", "rattlesnake", "goblin"]

weapon = random.choice(weapons)
enemy = random.choice(enemies)


def print_pause(string):
    print(string)
    time.sleep(2)

def intro():
    print_pause("You find yourself standing in an open field, " 
                "filled with grass and yellow wildflowers.")
    print_pause("Rumor has it that a" + " " + (enemy) + " " + 
                "is somewhere around here, " 
                "and has been terrifying the nearby village.")
    print_pause("In front of you is a beautiful castle.")
    print_pause("To your right is a tunnel leading"
                " to a box with a weapon inside.")
    print_pause("In your hand you hold your trustworthy "
                "(but not very effective) pocket-knife.")

def house1():
    print_pause("You approach the door of the castle.")
    print_pause("You are about to knock when the door" 
                " opens and out steps a" + " " + (enemy) + ".")
    print_pause("The" + " " + (enemy) + " " + "is not messing around and it attacks you!")
    print_pause("You feel somewhat confident, however you only have the pocket-knife as your weapon.")
    first_move = input("Would you like to (1) fight or (2) flee?")
    if '1' in first_move:
        fight()
    if '2' in first_move:
        field()

def house2():
    print_pause("You approach the door of the castle.")
    print_pause("You are about to knock when the door opens and out steps a" + " " + (enemy) + ".")
    print_pause("The" + " " + (enemy) + " " + "is not messing around and it attacks you!")
    first_move = input("Would you like to (1) fight or (2) flee?")
    if '1' in first_move:
        fight()
    if '2' in first_move:
        field()


def cave():
    if 'weapon' in weapons:
        print_pause("You have entered the tunnel already," 
                    " you open the box, no new weapons inside the box.")
        print_pause("Nothing to do here now.") 
        print_pause("You walk back out onto the field")
        valid_input()
    else:
        print_pause("You slowly enter the tunnel")
        print_pause("It is very dark, so you walk as slowly as you can and turn on the pocket torch.")
        print_pause("You see a box with a sticker on it, seems like there could be a weapon inside this box.")
        print_pause("You open the box. You have found a magical" + " " +(weapon) + "!")
        print_pause("You throw away your pocket-knife and you take the" + " " + (weapon) + " " + "with you")
        print_pause("You now have a trustworthy weapon, just in case.")
        print_pause("You walk back out to the field.")
        weapons.append("weapon")
        valid_input()

def field():
    print_pause("You run back as fast as you can. " 
                "The" + " " + (enemy) + " " + "chases you, but due to your speed, you got away safely")
    valid_input()

def fight():
    if "weapon" in weapons:
        print_pause("The" + " " + "makes his first move, but due to your immense reflex skills, "
                    "you manage to dodge the attack.")
        print_pause("You get your" + " " + (weapon) + " " + "out")
        print_pause("The" + " " + (weapon) + " " + "shines brightly in your hand as you brace yourself for the attack.")
        print_pause("You aim for the" + (enemy) + " " + "and it is a direct hit!!")
        print_pause("The" + " " + (enemy) + " " + "is defeated. You are the champion!")
        weapons.remove("weapon")
        
        
    else:
        print_pause("You tried to attack using the pocket-knife, it is not effective...")
        print_pause("The" + " " + (enemy) + " " + "launches an attack on you. It's super effective!")
        print_pause("You lose!")
        
    
def play_again():
    play_again = input("Would you like to play again? (y/n)")
    if 'n' in play_again:
        print_pause("Thank you for playing, see you again soon!")
    elif 'y' in play_again:
        play_game()
        
def valid_input():
    print_pause("Enter 1 to knock on the door of the castle.")
    print_pause("Enter 2 to enter the tunnel.")
    response = input("What would you like to do?\n"
                    "(Please enter 1 or 2)")
    if '1' in response:
        if 'weapon' in weapons:
            house2()
        else:
            house1()
    elif '2' in response:
        cave()
    else:
        print_pause("Invalid response")
        valid_input()
        


def play_game():
    intro()
    valid_input()
    play_again()

play_game()