from gpiozero import LED, Button
from time import sleep
import random

led = LED(4)

player1 = input("Enter player1's name:")
player2 = input("Enter player 2's name:")

left_button = Button(14, bounce_time=0.2)
right_button = Button(15, bounce_time=0.2)

player1_scores = 0
player2_scores = 0

winner_detected = False
led_on = False

def pressed(button):
    
    if winner_detected:
        return
    
    winner_detected = True
    
    
    if not led_on:
        
        if button.pin.number == 14:
            player1_score -= 1
            print(player1 + "pressed too early! -1 point.")
            
        else:
            player2_score -= 1
            print(player2 + "pressed too early! -1 point.")
            
        print(player1 + "score is" + player1_score + "." player2 + "score is" + player2_score + ".")
        
        
    led.off()
    led.on = False
    
    if button.pin.number == 14:
        print(player + "pressed first!")
        player1_score += 1
        
    else:
        print(player2 + "pressed first!")
        player2_score += 1
        
    print(player1 + "score is" + player1_score + "." player2 + "score is" + player2_score + ".")
    
    if player1_score == 5:
        print(player1 + "wins the game!")
        sys.exit()
        
    if player2_score == 5:
        print(player2 + "wins the game!")
        sys.exit()
        
left_button.when.pressed = pressed
right_button.when.pressed = pressed

while True:
    winner_detected = False
    
    print("Get ready...")
    sleep(random.randrange(2,8)
          
    print("GO!")
    led.on()
    led_on = True
          
    while not winner_detected:
          sleep(0.01)
