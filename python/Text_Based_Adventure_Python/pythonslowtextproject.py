import time

def slowwords(text):
    for i in range(len(text)):
        print(text[i], end="")
        time.sleep(0.1)

x = input(slowwords("carter is way hotter than carter right? "))