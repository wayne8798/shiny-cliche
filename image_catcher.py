import cv2

def diffImg(t0, t1, t2):
    d1 = cv2.absdiff(t2, t1)
    d2 = cv2.absdiff(t1, t0)
    return cv2.bitwise_and(d1, d2)

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
        if key == 27:
            cv2.destroyWindow(winName)
            break
    return im_count

def pick_img(count):
    if count < 10:
        return
    t_minus = cv2.cvtColor(cv2.imread('img/frame1.png'), cv2.COLOR_RGB2GRAY)
    t = cv2.cvtColor(cv2.imread('img/frame2.png'), cv2.COLOR_RGB2GRAY)
    t_plus = cv2.cvtColor(cv2.imread('img/frame3.png'), cv2.COLOR_RGB2GRAY)

    global_index = len(t)
    best_im = None
    im = None

    for iter in range(4, count):
        diff_img = diffImg(t_minus, t, t_plus)
        for i in range(global_index):
            sorted_img = sorted(diff_img[i], reverse=True)
            if sorted_img[19] > 20:
                highest_index = i
                if highest_index < global_index:
                    global_index = highest_index
                    best_im = im
                    print '%d; %d' % (global_index, iter)
                break
        # Read next image
        t_minus = t
        t = t_plus
        im = cv2.imread('img/frame' + str(iter) + '.png')
        t_plus = cv2.cvtColor(im, cv2.COLOR_RGB2GRAY)

    cv2.imwrite('best_photo.png', best_im)

count = capture_img()
pick_img(count)

print 'Goodbye'
