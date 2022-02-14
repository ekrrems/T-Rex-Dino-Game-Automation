import keyboard
import uuid
import time
from PIL import Image
from mss import mss

path = 'https://www.trex-game.skipser.com/'

mon = {'top':530,'left':650,'width':250,'height':100}
sct = mss()

i=0

def record_screen(record_id,key):
    global i 
    
    i += 1
    print('{}:{}'.format(key,i))
    img = sct.grab(mon)
    im = Image.frombytes('RGB',img.size,img.rgb)
    im.save('C:\\Users\\ekrem\\OneDrive\\Masaüstü\\ML Projects\\T-rex Game\\im\{}_{}_{}.png'.format(key,record_id,i))
    
is_exit = False

def exit():
    global is_exit
    
    is_exit = True
    
keyboard.add_hotkey('esc',exit)

record_id = uuid.uuid4()

while 1:
    
    if is_exit ==True:
        break
    
    if keyboard.is_pressed(keyboard.KEY_UP):
        record_screen(record_id,'up')
    elif keyboard.is_pressed(keyboard.KEY_DOWN):
        record_screen(record_id,'down')
    elif keyboard.is_pressed('right'):
        record_screen(record_id,'right')
        
    


    
    