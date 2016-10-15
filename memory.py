# implementation of card game - Memory

import simplegui
import random

deck = range(0, 8)* 2
exposed = [False] * len(deck)
print exposed
w = 50
h = 100
WIDTH = w * 16 + 2
HEIGHT = 102
first_card = -1
second_card = -1
exp_ind = []
turn = 0

# helper function to initialize globals
def new_game():
    global exposed, state, exp_ind, turn
    random.shuffle(deck)
    exposed = [False] * len(deck)
    state = 0
    turn = 0
    label.set_text("Turns = " + str(turn))
    exp_ind = []
    print deck
    print exposed

     
# define event handlers
def mouseclick(pos):
    global state, exposed, first_card, second_card, exp_ind, turn
    position = pos[0] // 50
    
    
    for index in range(len(deck)):
    #if position == index  and exposed[index] != True:
        if exposed[position] != True:
            #turn += 1
            if state == 0:
                #exposed = [False] * len(deck)
                first_card = position
                exposed[first_card] = True
                #exp_ind.append(first_card)
                state = 1
            elif state == 1:
                #exposed = [False] * len(deck)
                second_card = position
                exposed[second_card] = True               
                state = 2   
            elif state == 2:
                if deck[first_card] == deck[second_card]:
                    exposed = [False] * len(deck)
                    exp_ind.append(first_card)
                    exp_ind.append(second_card)
                    first_card = position
                    exposed[first_card] = True
                    second_card = - 1
                    state = 1                    
                else:
                    exposed = [False] * len(deck)
                    first_card = position
                    exposed[first_card] = True
                    second_card = - 1
                    state = 1
                turn += 1
                print "turn", turn
                label.set_text("Turns = " + str(turn))
    print exp_ind         
    for i in exp_ind:
        exposed[i] = True
        
    print state
    print "first card", first_card
    print "second card", second_card
    print exposed
                      
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global first_card, second_card, text_color    
    line = 1
    #coordinates
    x = 1
    y = 1
    for i in range(len(deck)):
        if exposed[i] == True:
            if i in exp_ind:
                text_color = "Green"
            else:
                text_color = "Black"
            canvas.draw_text(str(deck[i]), [(0.3* w) + w * i, (y + h) * 0.66], 40, text_color)
        else:
            canvas.draw_polygon([[x, y], [x + w, y], [x + w, y + h], [x, y + h]], line, "White", '#55aa55')
        x += w
        
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", WIDTH, HEIGHT)
frame.add_button("Reset", new_game)
#label = frame.add_label("Turns = 0")
frame.set_canvas_background("White")
# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)
label = frame.add_label("Turns = " + str(turn))


# get things rolling
new_game()
frame.start()

