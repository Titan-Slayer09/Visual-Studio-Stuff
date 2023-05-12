import time

def Ten_counter():
    number = 0
    while True:
        yield number
        
        time.sleep(1)
        
        number += 1

        if number >= 11:
            number = 0 
            
for number in Ten_counter():
    print(number, end=' ')