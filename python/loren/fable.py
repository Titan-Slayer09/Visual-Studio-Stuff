import time
import random
def typing_print(text, delay=0.01, end=''):
    for letter in text:
        print(letter, end=end, flush=True)
        time.sleep(delay)
Player_Money = 0
Player_HP = 20
health= "Your health is, "
money = "Your gold count is, "
health_potion = {
    "Health Potion": "500",
    "Placebo Health Potion":"200",
    "Children's Health Potion": "400",
    "Cure-All Health Potion": "600",
    "Live Forever Health Potion": "700",
    }
chest=["Health Potion","Apple","Mutton","Amethyst", "Emerald", "Fake Wedding Ring","Perfume","Sapphire","Wedding Ring","Lamp"]
#0-100
easy_enemies={
    "Black Beetle": "1",
    "Red Beetle":"5",
    "Balverine":"50",
    "Bandits":"5",
    "Hobbe Grunt" : "20",
    "Hobbe Lieutenant":"25",
    "Minion Dreadwing":"50-100",
    "Minion Wardog":"50-75",
    "Screamer":"30",
    "Succubus Nymph":"25",
    "Earth Troll":"50-100",
    "Undead Soilder":"40",
    "Wraith":"80",
    "Red Wasp":"2",
    "Blue Wasp":"5",
    "Wasp Queen":"10",
    "Water Nymph":"20",
    "Wood Nymph":"25",
    }

#100-500
medium_enemies={
    "Rock Troll":"100-150",
    "Ice Troll":"100-150",
    "":"",
    "":"",
    }
#500-up
hard_enemies={
    "":"",
    "":"",
    "":"",
    }
#Special:Arachanox, White Balverine, Jack Blades, Kraken, scorpian, Twinblade.
black_beetle = 10

typing_print("Welcome to Albion\n")

while True:
    play=input("Would you like to play? y/n: ")
    if play== "y":
        sure=input("Are you sure? You must commit to this decision! y/n: ")
        if sure =="y":
            break
        elif sure=="n":
            continue
        else:
            print("Please put either y/n")
            continue
   


typing_print("Our journey begins in Oakvale. A simple, small developing village on the southern shores of Albion. There is a little blue, house in the meadows.")
print()
typing_print("As the fairy tales are told, the makings of a young hero, never begins with a happy childhood. As time will tell...\n")
time.sleep(0.5)
typing_print("\"Why haven't you collected firewood yet?\" saids father, \"If we are to eat tonight, you must gather some wood. Go into the forest and collect some.\"\n")
time.sleep(0.5)
typing_print("The woods of Oakvale, while safe still hold beetles and bugs, trying to farm off of the land.\n")
#Fix this
typing_print("While you go enter the forest, a black beetle appears! Which weapon will you use a Rusty Longsword, or a Rusty Flinklock Pistol? Enter l for the sword, or f for the gun: ")
begin = input('')
while black_beetle > 0:
    if begin == "l":
            damage = random.randint(1,10)
            if damage < 5:
                typing_print("\nYou have missed the beetle.")
                time.sleep(0.5)
                typing_print("\nThe beetle attacked!")
                time.sleep(0.5)
                typing_print("\nYou have lost 1 health.")
                time.sleep(0.5)
                typing_print("\nYou take another hit at the beetle.")
                continue
            elif damage > 5:
                typing_print("\nYou have defeated the beetle! This is the beginning of this heroic tale.")
                break
           
    elif begin == "f":
            damage = random.randint(1,10)
            if damage < 5:
                typing_print("\n You have missed the beetle.")
                time.sleep(0.5)
                typing_print("\n The beetle attacked!")
                time.sleep(0.5)
                typing_print("\n You have lost 1 health.")
                Player_HP -= 1
                time.sleep(0.5)
                typing_print("\n You take another hit at the beetle.")
                continue
            elif damage > 5:
                typing_print("\n You have defeated the beetle! This is the beginning of this heroic tale.")
                break
    elif begin == "m":
            typing_print("\n information about the weapons")
            Hit_Chance = random.randint(1,10)
            #(see if you land a hit on the beetle)
            if Hit_Chance < 5:
                typing_print("\n You have missed the beetle.")
                time.sleep(0.5)
                typing_print("\n The beetle attacked!")
                Player_HP -= 1
                typing_print(Player_HP)
                time.sleep(0.5)
                Beetle_Hit_Chance = random.randint(1,2)
                #hit
                if Beetle_Hit_Chance == 1:
                    typing_print(f"\n You have lost {damage} health.")
                    Player_HP -= 1
                    time.sleep(0.5)
                    typing_print("\n You take another swing at the beetle.")
                    typing_print("\n you defeat the beetle!")
                #missed
                elif Beetle_Hit_Chance == 2:
                    typing_print("The Beetle Missed!")
                    time.sleep(0.5)
                    typing_print("\n You take another swing at the beetle.")
                    typing_print("\n you defeat the beetle! This is the beginning of this heroic tale.")
                else:
                    print("Error in code")
                    exit()
               
                continue
            elif Hit_Chance >= 5:
                typing_print("\n You have defeated the beetle! This is the beginning of this heroic tale.")
                break
typing_print("\n Congratulations on your victory. To reward you, I present for you a chest, these were hidden around the world by the previous heros. These chests hold important gifts and potions to help heros in their adventures. So I present mine to you.")
choice_of_random = (random.choice(chest))
typing_print(f"\n You have received a... {choice_of_random} \n")
if choice_of_random =="Health Potion":
    Player_HP += 200
    typing_print("You have gained health.")
    typing_print(" You now have, ")
    print(Player_HP)
    typing_print("hp.")
elif choice_of_random == "Apple":
    Player_HP += 10
    typing_print("You have gained health.")
    typing_print(" You now have, ")
    print(Player_HP)
    typing_print("hp.")
elif choice_of_random == "Mutton":
    Player_HP += 30
    typing_print("You have gained health.")
    typing_print(" You now have, ")
    print(Player_HP)
    typing_print("hp.")
elif choice_of_random == "Amethyst":
    Player_Money += 400
    typing_print("You have earned money.")
    typing_print(" You now have, ")
    print(Player_Money)
    typing_print("gold.")
elif choice_of_random == "Wedding Ring":
    Player_Money += 100
    typing_print("You have earned money.")
    typing_print(" You now have, ")
    print(Player_Money)
    typing_print("gold.")
elif choice_of_random == "Emerald":
    Player_Money += 700
    typing_print("You have earned money.")
    typing_print(" You now have, ")
    print(Player_Money)
    typing_print("gold.")
elif choice_of_random == "Fake Wedding Ring":
    Player_Money += 1
    typing_print("You have earned money.")
    typing_print(" You now have, ")
    print(Player_Money)
    typing_print("gold.")
elif choice_of_random == "Lamp":
    Player_Money += 10
    typing_print("You have earned money.")
    typing_print(" You now have, ")
    print(Player_Money)
    typing_print("gold.")
    print(Player_Money)
    typing_print("gold.")
elif choice_of_random == "Perfume":
    Player_Money += 120
    typing_print("You have earned money.")
    typing_print(" You now have, ")
    print(Player_Money)
    typing_print("gold.")
elif choice_of_random == "Sapphire":
    Player_Money += 550
    typing_print("You have earned money.")
    typing_print(" You now have, ")
    print(Player_Money)
    typing_print("gold.")