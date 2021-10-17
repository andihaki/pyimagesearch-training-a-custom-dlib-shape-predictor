import cv2
import numpy as np
import dlib

webcam = True

cap = cv2.VideoCapture(0)
detector = dlib.get_frontal_face_detector()
# predictor = dlib.shape_predictor("lips_predictor.dat")
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

def empty(a):
  pass

cv2.namedWindow("makeup")
cv2.resizeWindow("makeup",640,240)
cv2.createTrackbar("Blue","makeup",0,255,empty)
cv2.createTrackbar("Green","makeup",0,255,empty)
cv2.createTrackbar("Red","makeup",0,255,empty)

# -- temp
fps_start_time = 0
fps = 0


# used to record the time when we processed last frame
prev_frame_time = 0

# used to record the time at which we processed current frame
new_frame_time = 0
# -- end temp

def createBox(img,points,scale=5,masked=False,cropped=True):
  if masked:
    mask = np.zeros_like(img)
    mask = cv2.fillPoly(mask,[points],(255,255,255))
    img = cv2.bitwise_and(img, mask)

  if cropped:
    bbox = cv2.boundingRect(points)
    x,y,w,h = bbox
    imgCrop = img[y:y+h,x:x+w]
    imgCrop = cv2.resize(imgCrop,(0,0),None,scale,scale)
  
  else:
    return mask

while True:
  if webcam: sucess, img = cap.read();
  else: img = cv2.imread('abc.jpg')
  # swap / flip camera
  img = cv2.flip(img,1)
  img = cv2.resize(img,(0,0),None,1,1)
  imgOriginal = img.copy()
  imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
  faces = detector(imgGray)

  for face in faces:
    x1,y1 = face.left(),face.top()
    x2,y2 = face.right(),face.bottom()
    imgOriginal = cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
    landmarks = predictor(imgGray,face)
    myPoints = []
    # print(landmarks)

    for n in range(68):
    # for n in range(19):
      x = landmarks.part(n).x
      y = landmarks.part(n).y
      myPoints.append([x,y])

    myPoints = np.array(myPoints)
    imgLips = createBox(img,myPoints[48:61],3,masked=True,cropped=False)
    # imgLips = createBox(img,myPoints[0:19],0,masked=True,cropped=False)

    imgColorLips = np.zeros_like(imgLips)
    b = cv2.getTrackbarPos('Blue','makeup')
    g = cv2.getTrackbarPos('Green','makeup')
    r = cv2.getTrackbarPos('Red','makeup')

    imgColorLips[:] = b,g,r
    imgColorLips = cv2.bitwise_and(imgLips,imgColorLips)
    imgColorLips = cv2.GaussianBlur(imgColorLips,(7,7),10)
    # imgOriginalGray = cv2.cvtColor(imgOriginal,cv2.COLOR_BGR2GRAY)
    # imgOriginalGray = cv2.cvtColor(imgOriginalGray,cv2.COLOR_BayerBG2GRAY)
    imgColorLips = cv2.addWeighted(imgOriginal,1,imgColorLips,0.4,0)
    # cv2.imshow('makeup',imgColorLips)

    # showing only masked lips
    # cv2.imshow('Virtual Makeup', imgLips)

    # print(myPoints)
  # showing original video 
  cv2.imshow('Original', imgOriginal)
  cv2.waitKey(1)