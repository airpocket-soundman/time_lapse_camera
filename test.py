import cv2

WIDTH  = 1600   #320/640/800/1024/1280/1600/2048
HEIGHT = 1200   #240/480/600/ 768/ 960/1200/1536

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)
cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)


while True:
    ret, frame = cap.read()
    cv2.imshow('image', frame)
    key = cv2.waitKey(1)
    if key != -1:
        break

cap.release()
cv2.destroyAllWindows()