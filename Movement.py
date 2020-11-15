import cv2
import numpy

camera = cv2.VideoCapture('/dev/video0')
backSub = cv2.createBackgroundSubtractorMOG2(20, 50, 0)

params = cv2.SimpleBlobDetector_Params()
params.filterByArea = True
params.filterByInertia = False
params.filterByCircularity = False
params.filterByConvexity = False

wid = camera.get(3)     # 3 = width
hig = camera.get(4)
#params.minArea = int(wid / 5) ^ 2
#params.maxArea = int(wid / 2) ^ 2
params.minArea = 200
params.maxArea = 500

detector = cv2.SimpleBlobDetector_create(params)


class MovementClass:

    def __init__(self):
        pass

    @staticmethod
    def getMovement():
        ret, frame = camera.read()
        frame = cv2.flip(frame, 1)
        mono = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
        difference = backSub.apply(mono)
        difference = cv2.bitwise_not(difference)
        difference = cv2.blur(difference, (10, 10))
        keypoints = detector.detect(difference)
        empty = numpy.array(())
        view_blobs = cv2.drawKeypoints(difference, keypoints, empty, (0, 0, 255),
                                       cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
        cv2.imshow('bgDiff', view_blobs)
        return keypoints


    @staticmethod
    def closed():
        if cv2.waitKey(1) & 0xFF == 27:
            camera.release()
            cv2.destroyAllWindows()
            return 0
