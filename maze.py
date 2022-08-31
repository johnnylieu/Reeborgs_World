def turn_right():
    turn_left()
    turn_left()
    turn_left()
 
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
        turn_right()
        if front_is_clear():
            move()
    if wall_in_front():
        turn_left()
    if front_is_clear():
        move()

#Reeborg's World w/ Johnny Lieu