import cv2

def capture_img():
    cam = cv2.VideoCapture()
    im_count = 1
    while True:
        cv2.imwrite('img/frame' + str(im_count) + '.png',
                    cam.read()[1])
        print im_count
        im_count += 1
        
        key = cv2.waitKey(10)
        if key == 27:
            break

print 'Goodbye'
