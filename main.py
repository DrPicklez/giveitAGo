import cv2

camFrame = cv2.VideoCapture(0)
while(True):
    # Capture frame-by-frame
    ret, frame = camFrame.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2BGRA)

    # Display the resulting frame
    cv2.imshow('frame', gray)
    oldFrame = camFrame

    if cv2.waitKey(1) & 0xFF == 27:
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()