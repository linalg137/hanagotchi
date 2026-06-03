from machine import Pin, I2C
import ssd1306
import time

# using default address 0x3C
i2c = I2C(sda=Pin(6), scl=Pin(7))
display = ssd1306.SSD1306_I2C(128, 64, i2c)

button_a = Pin(2, Pin.IN)
button_b = Pin(3, Pin.IN)
button_c = Pin(4, Pin.IN)

def type(text, x= 0, y=0, delay = 0.05, max_width = 21):
    display.fill(0)
    
    cx, cy  = x, y
    line_height = 10
    
    word_buffer = ""
    
    def draw_char(ch, cx, cy):
            display.text(ch,cx,cy,1)
            display.show()
            time.sleep(delay)
    
    def draw_word(word, cx, cy):
        for ch in word:
            draw_char(ch, cx, cy)
            cx += 6
        return cx, cy
    
    for char in text:
        word_buffer += char
      
        if char == " ":
            word = word_buffer
            word_len = len(word)
            
            if cx + word_len * 6 > x + max_width * 6:
                cx = x
                cy += line_height
            
            cx, cy = draw_word(word, cx, cy)
            word_buffer = " "
    if word_buffer != " ":
        word = word_buffer
        word_len = len(word)
        
        if cx + word_len * 6 > x + max_width * 6:
            cx = x
            cy += line_height
            
        draw_word(word, cx, cy)

type("you walk into a dark dark room.", 0, 0, 0.05)
time.sleep(0.5)
type("a empty cage sits in the middle. what were you here for again?", 0, 0, 0.05)
time.sleep(0.5)
type("ohhh right. to guard a dangerous criminal.", 0, 0, 0.05)
time.sleep(0.5)
type("where..? you walk closer to the cage.", 0, 0, 0.05)
time.sleep(0.5)
type("suddenly, a gust of wind blows at you. AAAA-", 0, 0, 0.05)
time.sleep(0.5)
type("'whoaa!!! hello there....'", 0, 10, 0.05)
time.sleep(0.7)
type("'it seems  like you've found something interesting...'", 0, 10,0.05)
type("'me~!!' (you can refer to me as <the thing>)", 0, 0, 0.05)
time.sleep(0.5)
type("'that's right!! i know you can't see me... i-i'm trapped in this.. god-forsaken screen!!'", 0, 0, 0.05)     
type("'--that little human thinks that it can TRAP me in this small cage...'", 0, 0, 0.05)
time.sleep(0.5)
type("'does she know who I am??--'", 0, 0, 0.05)
time.sleep(0.5)
type("'--I AM THE DEMON OF H---'", 0, 0, 0.05)
time.sleep(0.7)
type("*ahem.*", 0, 0, 0.05)
time.sleep(0.7)
type("...", 0,0,0.07)
type("'well!! fortunately for you, the creator has.. uh.. disappeared, if you will..'", 0,0,0.05)
time.sleep(0.5)
type("'so it's up to you to take care of... this!!'", 0,0,0.05)
time.sleep(0.5)
type("'and make sure i dont escape.. heheh. or, if you want, you could let me free!'", 0,0,0.05)
time.sleep(0.5)
type("'the key is right there.'", 0,0,0.1)
time.sleep(0.5)
type("\na: take the key, let it free \nb: look around \nc: pour peanut butter inside", 0,0,0.05)

while True:
    if button_a.value() == 0:
        choice = "A"
        break
        
    if button_b.value() == 0:
        choice = "B"
        break
        
    if button_c.value() == 0:
        choice = "C"
        break
    

if choice == "A":
    type("'mwahahAHAHAHAHAHAAAAAA'", 0,0, 0.05)
    time.sleep(0.5)
    type("'stupid. stupid little human.'", 0,0, 0.1)
    time.sleep(1)
    type("'you just let the strongest evil DEMON free. i will END your world.'")
    time.sleep(0.5)
    type("--hurryy!! stop it!! memorize the code:")
    time.sleep(0.2)
    type("acbabcbab")
    time.sleep(1)
    type("what was the 5th letter?")
    
    while True:
        if button_a.value() == 0:
            choice = "A"
            break
        
        if button_b.value() == 0:
            choice = "B"
            break
        
        if button_c.value() == 0:
            choice = "C"
            break
        
    if choice == "B":
        type("'AAAAaa*mf*'",0,0, 0.05)
        time.sleep(0.5)
        type("--thank goodness!! you barely just saved the world. for now...",0,0, 0.05)
        time.sleep(0.5)
        type("but... um.. i'm afraid we want a more reliable guard.",0,0, 0.5)
        time.sleep(0.5)
        type("i'm sorry but.. you're fired. >.<",0,0, 0.5)
        type("you look down. a knife has been stuffed through you. wha-", 0, 0, 0.5)
        time.sleep(0.5)
        type("game over. you lose.", 0, 0, 0.5)
        
    if choice == "A" or choice == "C":
        type("WRONG.",0,0, 0.1)
        time.sleep(0.5)
        type("--well. good. try? i guess? is it really impossible to escape this fate?....",0,0, 0.1)
        time.sleep(0.5)
        type("game over. you lose.", 40, 34, 0.5)

if choice == "B":
    type("you see a can of tuna (is this thing a cat??), a bottle of red fluid, and a green slime.", 0, 0, 0.05)
    time.sleep(0.5)
    type("\na: feed the tuna and fluid to the thing. \nb: eat the tuna. \nc: pick up the green slime.", 0,0, 0.05)
    while True:
        if button_a.value() == 0:
            choice = "A"
            break
        
        if button_b.value() == 0:
            choice = "B"
            break
        
        if button_c.value() == 0:
            choice = "C"
            break
    
    if choice == "A":
        type("'slurp!! mmmm. i haven't had tuna blood soup in quite a while. much appreciated!!'", 0, 0, 0.05)
        time.sleep(0.5)
        type("'you wouldn't mind giving me that totally normal slime object too, right?", 0, 0, 0.05)
        type("\na: give it the slime. \nb: no. \nc: take the slime for yourself", 0, 0, 0.05)
       
        while True:
            if button_a.value() == 0:
                choice = "A"
                break
                
            if button_b.value() == 0:
                choice = "B"
                break
                
            if button_c.value() == 0:
                choice = "C"
                break
            
        if choice == "A":
            type("the green slime is floating in midair. suddenly, it stretches, its slimy body falling right on the key.", 0, 0, 0.05)
            time.sleep(0.5)
            type("it bounces back up as if controlled by magic. the key fits right into the lock, and the cage door opens.", 0, 0, 0.05)
            time.sleep(0.5)
            type("'MWAHAHHAHA!! TOO EASY!! see yall in hell, suckas.", 0, 0, 0.1)
            time.sleep(1)
            type("--you just.. brought the universe to its end. jeeez, we shouldn't have hired you.", 0, 0, 0.05)
            time.sleep(0.5)
            type("suddenly, everything goes dark. everything is gone.", 0 , 0, 0.25)
            time.sleep(2)
            type("game over. you lose.", 40, 34, 0.5)
            
        if choice == "B":
            type("'pleaseeeeeeeeeeeeee'", 0, 0, 0.05)
            time.sleep(0.5)
            type("\na: fine. \nb: fine. \nc: fine", 0, 0, 0.05)
            time.sleep(0.5)
            
            while True:
                if button_a.value() == 0:
                    choice = "A"
                    break
                
                if button_b.value() == 0:
                    choice = "B"
                    break
                
                if button_c.value() == 0:
                    choice = "C"
                    break
    
            type("the green slime is floating in midair. suddenly, it stretches, its slimy body falling right on the key.", 0, 0, 0.05)
            time.sleep(0.5)
            type("it bounces back up as if controlled by magic. the key fits right into the lock, and the cage door opens.", 0, 0, 0.05)
            time.sleep(0.5)
            type("'MWAHAHHAHA!! TOO EASY!! see yall in hell, suckas.", 0, 0, 0.1)
            time.sleep(1)
            type("--you just.. brought the universe to its end. jeeez, we shouldn't have hired you.", 0, 0, 0.05)
            time.sleep(0.5)
            type("suddenly, everything goes dark. everything is gone.", 0 , 0, 0.25)
            time.sleep(2)
            type("game over. you lose.", 40, 34, 0.5)
            
        if choice == "C":
            type("the slime is.. warm", 0, 0, 0.05)
            time.sleep(0.5)
            type("too warm. blisters form on your hands", 0, 0, 0.05)
            time.sleep(0.5)
            type("ouchh!! you melt to death.", 0, 0, 0.05)
            time.sleep(1)
            type("game over. you lose.", 40, 34, 0.5)
        
    if choice == "B":
        type("you feel queasy.", 0, 0, 0.05)
        time.sleep(0.5)
        type("the expiry date reads '1590 BC'",0, 0, 0.05)
        time.sleep(0.5)
        type("crapppppppppp", 0, 0, 0.05)
        time.sleep(0.5)
        type("lame. you die of food poisoning. ", 0, 0, 0.5)
        time.sleep(0.5)
        type("game over. you lose.", 40, 34, 0.5)
        
    if choice == "C":
        type("the slime is.. warm", 0, 0, 0.05)
        time.sleep(0.5)
        type("too warm. blisters form on your hands", 0, 0, 0.05)
        time.sleep(0.5)
        type("ouchh!! you melt to death.", 0, 0, 0.05)
        time.sleep(1)
        type("game over. you lose.", 40, 34, 0.5)

if choice == "C":
    type("where did you get that peanut butter from?", 0, 0, 0.05)
    time.sleep(0.5)
    type("clean that up!!", 0, 0, 0.05)
    type("\na: clean it up. \nb: no.", 0, 0, 0.05)
    
    while True:
        if button_a.value() == 0:
            choice = "A"
            break
                
        if button_b.value() == 0:
            choice = "B"
            break
        
    
    if choice == "A":
        type("you try to clean it up with your shoes.", 0, 0, 0.05)
        time.sleep(0.5)
        type("the peanut butter is weirdly oily. you slip.", 0, 0, 0.05)
        time.sleep(0.5)
        type("you fall on the edge of the key... sending it catapulting..", 0, 0, 0.05)
        time.sleep(0.5)
        type("right into the keyhole.", 0, 0, 0.05)
        time.sleep(0.5)
        type("'mwAHAHAHAHA. thank you, human. if only i could keep you alive...'", 0, 0, 0.05)
        time.sleep(0.5)
        type("'say, would you betray humanity and join me in ending the world?'", 0, 0, 0.09)
        time.sleep(1)
        type("\na: yes!! \nb: absolutely not.", 0, 0, 0.5)
        
        while True:
            if button_a.value() == 0:
                choice = "A"
                break
                
            if button_b.value() == 0:
                choice = "B"
                break
        
        if choice == "A":
            type("ugh. seriously? i had better hopes for you.", 0, 0, 0.05)
            time.sleep(0.5)
            type("you look down. a knife has been stuffed through you. wha-", 0, 0, 0.5)
            time.sleep(0.5)
            type("game over. you lose.", 0, 0, 0.5)
            
        if choice == "B":
            type("awhh.. well, that's too bad.", 0, 0, 0.05)
            time.sleep(0.5)
            type("might as well rid of you now.", 0, 0, 0.05)
            time.sleep(0.5)
            type("an immense pressure fills your head.", 0, 0, 0.05)
            time.sleep(0.5)
            type("you explode.", 0, 0, 0.5)
            time.sleep(0.5)
            type("you die an honorable death. good job!", 0, 0, 0.5)
            time.sleep(0.5)
            type("you win :)", 0, 0, 0.5)
