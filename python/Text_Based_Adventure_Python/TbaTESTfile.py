import time

def sp(text, delay=0.02, end=''):
    for letter in text:
        print(letter, end=end, flush=True)
        time.sleep(delay)
sp("Messanger: You have one message from nines, he says: 'I have left you one of my spells, it is called Fireball.exe use it wisely in fights to defeat enemies, also I leave you TrainingDummy.svg for you to use to learn.'")
sp("System: to summon a training dummy, type trainingdummy.svg, .svg files can only be used once but .exe files and some other types can be used multiple times")
tf = False
while tf == False:
    first_spell = input('\n ')
    if first_spell == 'trainingdummy.svg':
        tf = True
                       
    else:
        print('try again')
        continue