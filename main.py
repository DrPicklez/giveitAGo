from Movement import MovementClass
from Audio import Audio

audio = Audio()
movement = MovementClass()

while 1:
    points = movement.getMovement()
    for point in points:
        print("x:")
        print(point.pt[0])
        print("y:")
        print(point.pt[1])

    if len(points) > 0:
        audio.playSine(points[0].pt[0])



    if movement.getIsClosed() == 0:
        break

