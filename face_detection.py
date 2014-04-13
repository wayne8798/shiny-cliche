import cv2

def detect(path):
    img = cv2.imread(path)
    cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
    rects = cascade.detectMultiScale(img, 1.3, 4, cv2.cv.CV_HAAR_SCALE_IMAGE, (20,20))

    if len(rects) == 0:
        return [], img
    rects[:, 2:] += rects[:, :2]
    return rects, img

rects, img = detect("img/frame1.png")
print rects
