import cv2

global camFrame
camFrame = cv2.VideoCapture()
global backSub
backSub = cv2.createBackgroundSubtractorMOG2(20, 50, 0)


def end():
    camFrame.release()
    cv2.destroyAllWindows()


def getMovement():
    # Capture frame-by-frame
    ret, frame = camFrame.read()
    mono = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
    difference = backSub.apply(mono)
    cv2.imshow('frame', difference)


if cv2.waitKey(1) & 0xFF == 27:
    end()
