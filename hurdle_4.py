def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def avoid_wall():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    while front_is_clear():
        move()
    turn_left()
    while front_is_clear() and not at_goal():
        move()
 
while not at_goal():
    avoid_wall()

#Reeborg's World Monday Funday w/ Johnny Lieu