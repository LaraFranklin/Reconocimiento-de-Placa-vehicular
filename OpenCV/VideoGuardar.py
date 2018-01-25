import threading
import cv2
def getFrame():
    global frame
    while True:
        frame = video_capture.read()[1]

def face_analyse():
    while True:
        pass
#do some of the opeartion you want

def realtime():
    while True:
        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            video_capture.release()
            cv2.destroyAllWindows()
            break

if __name__ == "__main__":
    video_capture = cv2.VideoCapture(0)
    frame = video_capture.read()[1]
    cv2.imwrite("imagen2.jpg",frame,params=None)
    gfthread = threading.Thread(target=getFrame, args='')
    gfthread.daemon = True
    gfthread.start()
    rtthread = threading.Thread(target=realtime, args='')
    rtthread.daemon = True
    rtthread.start()
    fathread = threading.Thread(target=face_analyse, args='')
    fathread.daemon = True
    fathread.start()

    while True: #keep main thread running while the other two threads are non-daemon
        pass