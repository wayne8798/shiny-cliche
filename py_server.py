import cv2
import numpy
import zerorpc

class FaceDetector(object):
    def detect(self, img_data):
        fh = open('temp.png', 'wb')
        fh.write((img_data[21:]).decode('base64'))
        fh.close()
        img = cv2.imread('temp.png')
        cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
        rects = cascade.detectMultiScale(img, 1.3, 4, cv2.cv.CV_HAAR_SCALE_IMAGE, (20,20))
        return int(rects[0, 0])

s = zerorpc.Server(FaceDetector())
s.bind('tcp://0.0.0.0:4242')
s.run()
