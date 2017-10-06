""" Webcam implementation of HOG-based Meow detector """
import dlib
import cv2
import PIL
import numpy as np

meowtector = dlib.simple_object_detector('meow.svm')

video_capture = cv2.VideoCapture(0)

w = int(video_capture.get(3))
h = int(video_capture.get(4))

# disable if there's no need to save the video output
out = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 10, (w, h))

while(video_capture.isOpened()):
    ret, frame = video_capture.read()
    rects = meowtector(frame)

    if ret == True:
        for k, d in enumerate(rects):
            cv2.rectangle(frame, (d.left(), d.top()), (d.right(), d.bottom()), (0, 0, 255), 2)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, 'Meow detected!', (d.left()-10, d.top()-20), font, 1.0, (0, 0, 255), 2)

        out.write(frame)
        cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

video_capture.release()
out.release()
cv2.destroyAllWindows()
