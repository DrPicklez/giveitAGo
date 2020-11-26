from Movement import MovementClass
from Audio import Audio

audio = Audio()
movement = MovementClass()

while 1:
    #audio.updateSoundStream()
    points = movement.getMovement()
    for point in points:
        print("x:")
        print(point.pt[0])
        print("y:")
        print(point.pt[1])

    if movement.getIsClosed() == 0:
        break

