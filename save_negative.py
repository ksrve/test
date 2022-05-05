import numpy as np
import time
import cv2

PATH_TO_VIDEOSOURCE = "../datasource/test.mp4"

cap = cv2.VideoCapture(PATH_TO_VIDEOSOURCE)

# период сохранения изображений
duration = 2*60

start_time = time.time()
count = 0

while( int(time.time() - start_time) < duration):
    ret, frame = cap.read()

    if ret==True:
        cv2.imshow('frame',frame)
        cv2.imwrite("../data/negative/frame%d.jpg" % count, frame)
        count += 1
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()
