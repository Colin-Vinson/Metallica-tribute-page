'''Simple program that flips a two sided coin
while keeping track of the number of heads and tails 
that have occured'''

from microbit import *
import random

heads = Image("09990:"
              "90909:"
              "99999:"
              "09990:"
              "09990")
                 
tails = Image("99099:"
              "99999:"
              "00900:"
              "99999:"
              "99099")

coinFlip = Image("00000:"
                 "09990:"
                 "90009:"
                 "09990:"
                 "00000")
                 
coinSide = Image("00000:"
                 "00000:"
                 "99999:"
                 "00000:"
                 "00000")   
                 
countHeads = 0  #initial value for heads counter
countTails = 0  #initial value for tails counter
                 
display.scroll('COIN FLIP!', delay=100)    #scrolls once at beginning of program, with speed control
display.scroll('PRESS A TO FLIP!', delay=100)  #scrolls once at beginning of program, with spped control
while True: #continuous loop (true always true)
    sleep(50)   #button debounce to allow simultanious button pressing
    (a, b) = (button_a.is_pressed(), button_b.is_pressed())
    if a and b: #pressing button 'A' and 'B' simultaniously will reset counter
        countHeads = 0
        countTails = 0
    elif a:   #pressing button 'A' "flips" the "coin"
        display.show(heads)     #series of images to animate coin flip
        sleep(500)
        display.show(coinFlip)
        sleep(500)
        display.show(coinSide)
        sleep(500)
        display.show(coinFlip)
        sleep(500)
        display.show(tails)
        sleep(500)
        display.show(coinFlip)
        sleep(500)
        display.show(coinSide)
        sleep(500)
        display.show(coinFlip)
        sleep(500)
        flipped = random.choice([True, False])  #random boolean generator
        if flipped == (True):   #checks if random.choice returns 'True' 
            display.show(heads)
            sleep(3000)
            countHeads += 1 #number of heads occured + 1
        else:   #return of random.choice other than 'True'
            display.show(tails) 
            sleep(3000)
            countTails += 1 #number of tails occured + 1
    elif b: #pressing button 'B' will show number of occurances of heads and tails
        display.show(heads)
        sleep(1000)
        if countHeads <= 9:
            display.show(str(countHeads))   #displays number of heads occured
            sleep(1000)
        else:
            display.scroll('%s' % countHeads)
            
        display.show(tails)
        sleep(1000)
        
        if countTails <= 9:  
            display.show(str(countTails))   #displays number of tails occured
            sleep(1000)
        else:
            display.scroll('%s' % countTails)
    else:    
        display.show(Image.ARROW_W) #displays left facing arrow until button pressed
        