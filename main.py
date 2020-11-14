import cv2
camFrame = cv2.VideoCapture(0)
backSub = cv2.createBackgroundSubtractorMOG2(20, 50, 0)
while 1:

    # Capture frame-by-frame
    ret, frame = camFrame.read()
    # Our operations on the frame come here
    mono = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)

    difference = backSub.apply(mono)

    cv2.imshow('frame', difference)
    oldFrame = camFrame

    # 27 = ESC
    if cv2.waitKey(1) & 0xFF == 27:
        break

# When everything done, release the capture
camFrame.release()
cv2.destroyAllWindows()