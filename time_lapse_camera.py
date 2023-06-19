import signal
import time
import cv2
import os


image_size_list = [[320,240],[640,480],[800,600],[1024,768],[1280,960],[1600,1200],[2048,1536]]
display_image_size = [640,480]
image_size = 5
temp_folder_path = "temp/"
file_number = 0

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, image_size_list[5][0])
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, image_size_list[5][1])
capture.set(cv2.CAP_PROP_BUFFERSIZE, 1)


def create_folder_if_not_exists(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

def get_next_file_number():
    global file_number
    file_number += 1
    return file_number

def save_image(image, file_name):
    cv2.imwrite(file_name, image)
    print(file_name)

def scheduler(arg1, args2):
    print(time.time())
    ret, frame = capture.read()
    display_image = cv2.resize(frame, (display_image_size[0], display_image_size[1]))
    cv2.imshow('image', display_image)
    file_name = temp_folder_path + str(file_number).zfill(6) + ".jpg"
    save_image(frame, file_name)
    get_next_file_number()
    key = cv2.waitKey(1)

def main_func():
    create_folder_if_not_exists(temp_folder_path)

    signal.signal(signal.SIGALRM, scheduler)
    signal.setitimer(signal.ITIMER_REAL, 1, 1)

    while True:
        time.sleep(1000)

if __name__ == '__main__':
	result = main_func()