def turn_right():
    turn_left()
    turn_left()
    turn_left()
 
def avoid_wall():
        turn_left()
        move()
        turn_right()
        move()
        turn_right()
        move()
        turn_left()
        
while not at_goal():
    if front_is_clear():
        move()
    if wall_in_front():
        avoid_wall()
 

#Reeborg's World Monday Funday w/ Johnny Lieu