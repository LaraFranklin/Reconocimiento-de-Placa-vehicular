import numpy as np
import cv2
cap = cv2.VideoCapture(0)
while(True):
    # Capture frame-by-frame
    video_cur_frame = cap.get(cv2.CAP_PROP_POS_FRAMES)
    ret, frame = cap.read()
    #frame = video_capture.read()[1]
    #cv2.imwrite("imagen4.jpg", frame, params=None)
    frame_out = frame.copy()


    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',gray)
    k = cv2.waitKey(1)
    if k  == ord('q'):
        break
    elif k == ord('c'):
        cv2.imwrite('frame%d.jpg' % video_cur_frame, frame_out)

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()