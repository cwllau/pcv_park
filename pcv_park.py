# Add your Python code here. E.g.
# jan 26 for pcv parking -COCO
from microbit import *

index = 0
while True:
    # display.scroll('Hello, World!')
    # display.show(Image.HEART)
    # sleep(2000)
    
    #pcv parking floors
    #index keeps track of what floor
    #accelerometer very junk :/
    #pin 0 + gnd hold microbit is weak
    on = True
    pcv = ['1', '2', '3', '4', '5', '6']
    if button_a.is_pressed():
        index = index - 1
        if index < 0 :
            index = 4
        display.show(pcv[index])
        sleep(300) #500 milliseconds
        
    if button_b.is_pressed():
        on = not on
        if on == False:
            display.off()
        else:
            display.on()
        #for plus incrementing with button B
        #display.scroll("2!")
        # index += 1
        # if index > (len(pcv) - 1):
        #     index = 0
        # display.show(pcv[index])
        # sleep(500)
 
