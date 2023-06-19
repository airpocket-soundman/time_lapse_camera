import signal
import time
import cv2


WIDTH  = 1280   #320/640/800/1024/1280/1600/2048
HEIGHT =  960   #240/480/600/ 768/ 960/1200/1536

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)


def scheduler(arg1, args2):
    print("schedule")
    print(time.time())
    print(arg1)
    ret, frame = capture.read()
    if ret:
        cv2.imshow("camara", frame)
    else:
        print("not ret")


print("signal")
signal.signal(signal.SIGALRM, scheduler)
signal.setitimer(signal.ITIMER_REAL, 1, 1)

capture.release()
cv2.destroyAllWindows()

#time.sleep(1000)


