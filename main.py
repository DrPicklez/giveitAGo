from Movement import MovementClass

movement = MovementClass()

while 1:
    movement.getMovement()
    if movement.closed() == 0:
        break
