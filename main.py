from Movement import MovementClass\

movement = MovementClass()


while 1:
    points = movement.getMovement()
    for point in points:
        print("x:")
        print(point.pt[0])
        print("y:")
        print(point.pt[1])

    if movement.closed() == 0:
        break
