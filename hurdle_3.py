def turn_right():
    turn_left()
    turn_left()
    turn_left()

def hurdle(s):
    for i in range(0, s):
        move()
        turn_left()
        move()
        turn_right()
        move()
        turn_right()
        move()
        turn_left()
 
hurdle(6)

#Reeborg's World Sunday Funday w/ Johnny Lieu