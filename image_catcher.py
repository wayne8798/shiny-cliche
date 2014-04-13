import cv2
import numpy

def capture_img():
    winName = 'Movement Indicator'
    cv2.namedWindow(winName, cv2.CV_WINDOW_AUTOSIZE)
    cam = cv2.VideoCapture(0)
    im_count = 1
    while True:
        im = cam.read()[1]
        cv2.imshow(winName, im)
        cv2.imwrite('img/frame' + str(im_count) + '.png', im)
        im_count += 1
        
        key = cv2.waitKey(10)
        if key == 27 or key == 1048603:
            cv2.destroyWindow(winName)
            break
    return im_count

def detect(path, face_count):
    img = cv2.imread(path)
    cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
    rects = cascade.detectMultiScale(img, 1.3, 4, cv2.cv.CV_HAAR_SCALE_IMAGE, (20,20))

    if len(rects) == 0 or len(rects) > face_count:
        return 1000
    rects[:, 2:] += rects[:, :2]

    ys = rects[:, 1]
    while ys.size < face_count:
        ys = numpy.append(ys, [1000])

    return numpy.mean(ys)

def count_face(count):
    count_stats = []
    for iter in range(1, count):
        img = cv2.imread('img/frame' + str(iter) + '.png')
        cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
        rects = cascade.detectMultiScale(img, 1.3, 4, cv2.cv.CV_HAAR_SCALE_IMAGE, (20,20))
        count_stats.append(len(rects))
    sorted_stats = sorted(count_stats)
    return sorted_stats[-10]

def pick_img(count):
    face_count = count_face(count)
    print '%d faces detected' % face_count
    if count < 10:
        return
    global_index = 1000
    best_im_path = None

    for iter in range(1, count):
        im_path = 'img/frame' + str(iter) + '.png'
        highest_index = detect(im_path, face_count)
        if highest_index < global_index:
            global_index = highest_index
            best_im_path = im_path
            print '%d; %d' % (global_index, iter)

    cv2.imwrite('best_photo.png', cv2.imread(best_im_path))

count = capture_img()
pick_img(count)

print 'Goodbye'
