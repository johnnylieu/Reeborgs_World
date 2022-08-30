def turn_right():
    turn_left()
    turn_left()
    turn_left()
 
while not at_goal():
    if front_is_clear():
        move()
    if right_is_clear():
        turn_right()
        move()
        turn_right()
        if front_is_clear():
            move()
    if not front_is_clear():
        turn_left()
    while front_is_clear() and wall_on_right():
        move()

#Reeborg's World w/ Johnny Lieu