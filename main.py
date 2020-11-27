from Movement import MovementClass
from Audio import Audio

audio = Audio()
movement = MovementClass()

while 1:
    points = movement.getMovement()
    audio.playSine(movement.mouse[0])
    for point in points:
        pass
        # print("x:")
        # print(point.pt[0])
        # print("y:")
        # print(point.pt[1])

    if len(points) > 0:
        pass

    if movement.getIsClosed() == 0:
        break

