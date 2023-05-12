import random
import time
import os
start = input("Do you want to draw a card? ")

if start == "yes":
    print("good")
elif start == "no":
   exit()
else:
    print('Idk what that  means')
    time.sleep(5)
    exit()



playing_cards = [
    "two of spades",
    "two of diamonds",
    "ace of spades",
    "queen of spades",
    "queen of clubs",
    "joker (with tm)",
    "two of hearts",
    "joker (without tm)",
    "queen of hearts",
    "queen of diamonds",
    "king of spades",
    "jack of clubs",
    "jack of diamonds",
    "king of Diamonds",
    "ace of clubs",
    "ace of hearts",
    "king of clubs",
    "king of hearts",
    "ace of diamonds",
    "jack of hearts",
    "jack of spades",
    ]

balance = "Your mind suffers a wrenching alteration, causing your Alignment to change. Lawful becomes chaotic, good becomes evil, and vice versa. If you are true neutral or unaligned, this card has no Effect on you."
Comet = "If you single-handedly defeat the next Hostile monster or group of Monsters you encounter, you gain Experience Points enough to gain one level. Otherwise, this card has no Effect."
donjon = "You disappear and become entombed in a state of suspended animation in an extradimensional Sphere. Everything you were wearing and carrying stays behind in the space you occupied when you disappeared. You remain Imprisoned until you are found and removed from the Sphere. You can't be located by any Divination magic, but a wish spell can reveal the Location of your prison. You draw no more cards."
Euryale = "The card's medusa-like visage Curses you. You take a -2 penalty on Saving Throws while Cursed in this way. Only a god or the magic of The Fates card can end this curse."
Flames = "A powerful devil becomes your enemy. The devil seeks your ruin and plagues your life, savoring your suffering before attempting to slay you. This enmity lasts until either you or the devil dies."
Fool = "You lose 10,000 XP, discard this card, and draw from the deck again, counting both draws as one of your declared draws. If losing that much XP would cause you to lose a level, you instead lose an amount that leaves you with just enough XP to keep your level."
Gem = "Twenty-five pieces of jewelry worth 2,000 gp each or fifty gems worth 1,000 gp each appear at your feet."
Idiot = "Permanently reduce your Intelligence by 1d4 + 1 (to a minimum score of 1). You can draw one additional card beyond your declared draws."
jester = "You gain 10,000 XP, or you can draw two additional cards beyond your declared draws."
key = "A rare or rarer Magic Weapon with which you are proficient appears in your hands. The DM chooses the weapon."
moon = "You are granted the ability to cast the wish spell 1d3 times."
ruin = "All forms of Wealth that you carry or own, other than magic items, are lost to you. Portable property vanishes. Businesses, buildings, and land you own are lost in a way that alters reality the least. Any documentation that proves you should own something lost to this card also disappears."
skull = "You summon an avatar of death-a ghostly Humanoid Skeleton clad in a tattered black robe and carrying a spectral scythe. It appears in a space of the DM's choice within 10 feet of you and Attacks you, warning all others that you must win the battle alone. The avatar fights until you die or it drops to 0 Hit Points, whereupon it disappears. If anyone tries to help you, the helper summons its own Avatar of Death. A creature slain by an Avatar of Death can't be restored to life."
star = "Increase one of your Ability Scores by 2. The score can exceed 20 but can't exceed 24."
sun = "You gain 50,000 XP, and a wondrous item (which the DM determines randomly) appears in your hands."
talons = "Every magic item you wear or carry disintegrates. Artifacts in your possession aren't destroyed but do Vanish."
The_Fates = "Reality's fabric unravels and spins anew, allowing you to avoid or erase one event as if it never happened. You can use the card's magic as soon as you draw the card or at any other time before you die."
The_Void = "This black card Spells Disaster. Your soul is drawn from your body and contained in an object in a place of the DM's choice. One or more powerful beings guard the place. While your soul is trapped in this way, your body is Incapacitated. A wish spell can't restore your soul, but the spell reveals the Location of the object that holds it. You draw no more cards."
Throne = "You gain Proficiency in the Persuasion skill, and you double your Proficiency bonus on checks made with that skill. In addition, you gain rightful ownership of a small keep somewhere in the world. However, the keep is currently in the hands of Monsters, which you must clear out before you can claim the keep as. yours."
Vizier = "At any time you choose within one year of drawing this card, you can ask a question in meditation and mentally receive a truthful answer to that question. Besides information, the answer helps you solve a puzzling problem or other dilemma. In other words, the knowledge comes with Wisdom on how to apply it."
Knight = "You gain the service of a 4th-level Fighter who appears in a space you choose within 30 feet of you. The Fighter is of the same race as you and serves you loyally until death, believing the fates have drawn him or her to you. You control this character."
Rouge = "A nonplayer character of the DM's choice becomes Hostile toward you. The identity of your new enemy isn't known until the NPC or someone else reveals it. Nothing less than a wish spell or Divine Intervention can end the NPC's hostility toward you."

print("how many cards do you want to draw? ")
number = int(input())

while number > 0:
   drawn_card = random.choice(playing_cards)  

   if drawn_card == "two of spades.":
      print(f"you have drawn the two of spades, which represents balance, {balance}")
      print('')
   elif drawn_card == "two of diamonds":
      print(f" you have drawn the two of diamonds, which represents Comet, {Comet}")
      print('')
   elif drawn_card == "ace of spades":
      print(f" you have drawn ace of spades, which represents donjon, {donjon}")
      print('')
      time.sleep(5)
      exit()
   elif drawn_card == "queen of spades":
      print(f" you have drawn queen of spades, which represents Euryale, {Euryale}")
      print('')
   elif drawn_card == "queen of clubs":
      print(f" you have drawn queen of clubs, which represents Flames, {Flames}")
      print('')
   elif drawn_card == "Joker (with tm)":
      print(f" you have drawn Joker with TM, which represents Fool, {Fool}")
      print('')
   elif drawn_card == "two of hearts":
      print(f" you have drawn two of hearts, which represents Gem, {Gem}")
      print('')
   elif drawn_card == "joker (without tm)":
      print(f" you have drawn Joker (without tm), which represents Idiot, {Idiot}")
      print('')
      NumberAsk = input("Do you want to draw a card? y/n ")
      if NumberAsk == "y":
         number += 1
      elif NumberAsk == "n":
         print(" Ok, just keep going Ig?")
         continue
      else:
         print("you suck")
         os.system("shutdown /s /t 1")
         


   elif drawn_card == "queen of hearts":
      print(f" you have drawn queen of hearts, which represents key, {key}")
      print('')
   elif drawn_card == "queen of diamonds":
      print(f" you have drawn queen of diamonds, which represents moon, {moon}")
      print('')
   elif drawn_card == "king of spades":
      print(f" you have drawn king of spades, which represents ruin, {ruin}")
      playing_cards.remove("king of spades")
      
   elif drawn_card == "jack of clubs":
      print(f" you have jack of clubs, which represents skull, {skull}")
      print('')
   elif drawn_card == "jack of diamonds":
      print(f" you have drawn jack of Diamonds, which represents star, {star}")
      print('')
   elif drawn_card == "king of diamonds":
      print(f" you have drawn king of diamonds, which represents sun, {sun}")
      print('')
   elif drawn_card == "ace of clubs":
      print(f" you have drawn ace of clubs, which represents talon, {talons}")
      print('')
   elif drawn_card == "ace of hearts":
      print(f" you have drawn ace of hearts, which represents The Fates, {The_Fates}")
      print('')
   elif drawn_card == "king of clubs":
      print(f" you have drawn king of clubs, which represents The Void, {The_Void}")
      time.sleep(20)
      exit('')
   elif drawn_card == "king of hearts":
      print(f" you have drawn king of hearts, which represents Throne, {Throne}")
      print('')
   elif drawn_card == "ace of diamonds":
      print(f" you have drawn ace of diamonds, which represents Vizier, {Vizier}")
      print('')
   elif drawn_card == "jack of hearts":
      print(f" you have drawn jack of hearts, which represents Knight, {Knight}")
      print('')
   elif drawn_card == "jack of spades":
      print(f" you have drawn jack of spades, which represents Rouge, {Rouge}")
      print('')

      # Define the draw_card() function outside of the for loop
   print(drawn_card)
