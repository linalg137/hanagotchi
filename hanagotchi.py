from pololu_3pi_2040_robot.display import Display
from pololu_3pi_2040_robot import robot
import time
display = robot.Display()
a = robot.ButtonA()
b = robot.ButtonB()
c = robot.ButtonC()


def type(display, text, x= 0, y=0, delay = 0.05, max_width = 21):
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
  
type(display, "whoaa!!! hello there....", 0, 10, 0.05)
time.sleep(0.7)
type(display, "it seems  like you've found something (someone?) interesting...", 0, 10,0.05)
type(display, "me~!! (haiii~)", 50, 30, 0.3)
time.sleep(0.3)
type(display, "that's right!! i know you can't see me... i-i'm trapped in this.. god-forsaken screen!!", 0, 0, 0.05)     
type(display, "--that little human thinks that it can TRAP me in this small cage... does she know who I am??--", 0, 0, 0.05)
type(display, "--I AM THE DEMON OF H---", 0, 0, 0.05)
time.sleep(0.7)
type(display, "*ahem.*", 0, 0, 0.05)

if a.check():
    type(display, "lkJLkjldkjlakjalfkjf", 0, 0, 0.05)

if b.check():
    type(display, "m too bro", 0, 0, 0.05)
    
else:
    display.fill(0)
