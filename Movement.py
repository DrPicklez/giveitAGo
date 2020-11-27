import cv2
import numpy
import threading

# self.params.minArea = int(wid / 5) ^ 2
# self.params.maxArea = int(wid / 2) ^ 2

# params.minArea = int(wid / 5) ^ 2
# params.maxArea = int(wid / 2) ^ 2


class MovementClass:

    def __init__(self):
        self.camera = cv2.VideoCapture('/dev/video0')
        self.backSub = cv2.createBackgroundSubtractorMOG2(20, 50, 0)
        params = self.setParams(cv2.SimpleBlobDetector_Params())
        self.detector = cv2.SimpleBlobDetector_create(params)
        pass

    def setParams(self, param):
        param.filterByArea = True
        param.filterByInertia = False
        param.filterByCircularity = False
        param.filterByConvexity = False
        param.minArea = 200
        param.maxArea = 500
        return param

    def getMovement(self):
        ret, frame = self.camera.read()
        frame = cv2.flip(frame, 1)
        mono = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)
        difference = self.backSub.apply(mono)
        difference = cv2.bitwise_not(difference)
        difference = cv2.blur(difference, (10, 10))
        keypoints = self.detector.detect(difference)
        empty = numpy.array(())
        view_blobs = cv2.drawKeypoints(difference, keypoints, empty, (0, 0, 255),
                                       cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
        cv2.imshow('bgDiff', view_blobs)
        return keypoints

    def getMouse(self, event, x, y, flags, param):

        return mouse

    def getWidth(self):
        return self.camera.get(3)

    def getHeight(self):
        return self.camera.get(4)

    def getIsClosed(self):
        if cv2.waitKey(1) & 0xFF == 27:
            self.camera.release()
            cv2.destroyAllWindows()
            return 0                #Kill Loop
