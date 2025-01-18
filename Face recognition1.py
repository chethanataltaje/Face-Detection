import cv2 as cv

def draw_boundary(img,classifier, scaleFactor,minNeighbours, color, text):
    gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    features=classifier.detectMultiScale(gray, scaleFactor, minNeighbours)
    coords=[]
    for (x,y,w,h) in features:
        cv.rectangle(img, (x,y),(x+w, y+h), color, 2)
        cv.putText(img,text, (x,y-4), cv.FONT_HERSHEY_COMPLEX_SMALL,0.8,color,1,cv.LINE_AA)
        coords.append([x,y,w,h])
    return coords, img

def detect(img,faceCascade, smileCascade):
    color = {"blue":(255,0,0), "Red":(0,0,255), "green":(0,255,0)}

    coords,img=draw_boundary(img, faceCascade, 1.1, 10, color['blue'], "Face")

    for (x, y, w, h) in coords:
        roi_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)[y:y + h, x:x + w]
        smiles = smileCascade.detectMultiScale(roi_gray, scaleFactor=1.8, minNeighbors=20)
        for (sx, sy, sw, sh) in smiles:
            cv.rectangle(img, (x + sx, y + sy), (x + sx + sw, y + sy + sh), color['green'], 2)
            cv.putText(img, "Smile", (x + sx, y + sy - 4), cv.FONT_HERSHEY_COMPLEX_SMALL, 0.8, color['green'], 1, cv.LINE_AA)

    return img
    

faceCascade=cv.CascadeClassifier("haarcascade_frontalface_default.xml")
smileCascade=cv.CascadeClassifier("haarcascade_smile.xml")

video=cv.VideoCapture(0)
if not video.isOpened():
    print("Error: Unable to access the camera.")
    exit()

while True:
    _,img=video.read()
    img=detect(img, faceCascade, smileCascade)
    cv.imshow('Video',img)
    if cv.waitKey(1) & 0xFF==ord('q'):
        break
video.release()
cv.destroyAllWindows()