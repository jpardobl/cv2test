import numpy as np
import cv2

#face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

#this is the cascade we just made. Call what you want
gauge_cascade = cv2.CascadeClassifier('cascade_gauge_10stage/cascade.xml')

#cap = cv2.VideoCapture('positivas/542532668_51bd2d31f1.jpg')
cap = cv2.VideoCapture('positivas_seleccionadas/claro.jpg')
if not cap.isOpened():
    raise Exception("No se ha capturado nada")


def detect(img, cascade):
    
    for scale in [float(i)/10 for i in range(11, 15)]:
        for neighbors in range(2,5):
            rects = cascade.detectMultiScale(img, scaleFactor=scale, minNeighbors=neighbors,
                                             minSize=(20, 20), flags=cv2.cv.CV_HAAR_SCALE_IMAGE)
            print 'scale: %s, neighbors: %s, len rects: %d' % (scale, neighbors, len(rects))


while 1:
    ret, img = cap.read()
#    cv2.imshow('img',img)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite('fotogray.png',gray)
#    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    # add this
    # image, reject levels level weights.
    detect(gray, gauge_cascade)
    break
#    gauges = gauge_cascade.detectMultiScale(gray, 20, 20)
    print(gauges)    
    # add this
    for (x,y,w,h) in gauges:
        print(" Encontrado en: " + x + "," + y)
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)

#        roi_gray = gray[y:y+h, x:x+w]
#        roi_color = img[y:y+h, x:x+w]
#        eyes = eye_cascade.detectMultiScale(roi_gray)
#        for (ex,ey,ew,eh) in eyes:
#            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

#    cv2.imshow('img',img)
#    k = cv2.waitKey(30) & 0xff
#    if k == 27:
    break

cap.release()
cv2.destroyAllWindows()
