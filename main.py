from Movement import MovementClass

movement = MovementClass()
movement.__init__()

while 1:
    movement.getMovement()
    if movement.closed() == 0:
        break
