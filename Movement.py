import cv2

camera = cv2.VideoCapture(0)
backSub = cv2.createBackgroundSubtractorMOG2(20, 50, 0)

class MovementClass:

    def __init__(self):
        pass


    @staticmethod
    def getMovement():
        ret, frame = camera.read()
        mono = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
        difference = backSub.apply(mono)
        cv2.imshow('bgDiff', difference)

    @staticmethod
    def closed():
        if cv2.waitKey(1) & 0xFF == 27:
            camFrame.release()
            cv2.destroyAllWindows()
            return 0
