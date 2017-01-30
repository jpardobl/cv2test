import numpy as np
import cv2

#face_cascade = cv2.CascadeClassifier('opencv/data/haarcascades/haarcascade_frontalface_default.xml')
#eye_cascade = cv2.CascadeClassifier('opencv/data/haarcascades/haarcascade_eye.xml')
claro_cascade = cv2.CascadeClassifier('data/cascade.xml')

cap = cv2.VideoCapture('positivas_seleccionadas/claro.jpg')
#img = cv2.imread('positivas_seleccionadas/claro.jpg')
ret, img = cap.read()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
claros = claro_cascade.detectMultiScale(gray, 20, 20)
print len(claros)
for (x,y,w,h) in claros:
    print "%s, %s, %s, %s" % (x,y,w,h)
    img = cv2.rectangle(img,(x +5 ,y +5 ),(x+w -5,y+h -5),(255,0,0),2)
    cv2.imwrite("claro2.jpg", img)
    roi_gray = gray[y:y+h, x:x+w]
#    roi_color = img[y:y+h, x:x+w]
#    eyes = eye_cascade.detectMultiScale(roi_gray)
#    for (ex,ey,ew,eh) in eyes:
#        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

cv2.imshow('img',gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
