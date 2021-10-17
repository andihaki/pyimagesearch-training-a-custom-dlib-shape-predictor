import cv2
import numpy as np
import dlib

webcam = True

cap = cv2.VideoCapture(0)
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("lips_predictor.dat")
# predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

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

  # # ------------- show fps
  # import time
  # # Find OpenCV version
  # (major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')

  # # With webcam get(CV_CAP_PROP_FPS) does not work.
  # # Let's see for ourselves.

  # if int(major_ver)  < 3 :
  #     fps = cap.get(cv2.cv.CV_CAP_PROP_FPS)
  #     print("Frames per second using video.get(cv2.cv.CV_CAP_PROP_FPS): {0}".format(fps))
  # else :
  #     fps = cap.get(cv2.CAP_PROP_FPS)
  #     print("Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(fps))

  # # Number of frames to capture
  # num_frames = 120;

  # print("Capturing {0} frames".format(num_frames))

  # # Start time
  # start = time.time()

  # # Grab a few frames
  # for i in range(0, num_frames) :
  #     ret, frame = cap.read()

  # # End time
  # end = time.time()

  # # Time elapsed
  # seconds = end - start
  # print ("Time taken : {0} seconds".format(seconds))

  # # Calculate frames per second
  # fps  = num_frames / seconds
  # print("Estimated frames per second : {0}".format(fps))
  # # ------------- end show fps

  # # -- show fps
  # import time
  # # Capture frame-by-frame
  # # # used to record the time when we processed last frame
  # # prev_frame_time = 0
  
  # # # used to record the time at which we processed current frame
  # # new_frame_time = 0
  # ret, frame = cap.read()

  # # if video finished or no Video Input
  # if not ret:
  #     break

  # # Our operations on the frame come here
  # gray = frame

  # # resizing the frame size according to our need
  # gray = cv2.resize(gray, (500, 300))

  # # font which we will be using to display FPS
  # font = cv2.FONT_HERSHEY_SIMPLEX
  # # time when we finish processing for this frame
  # new_frame_time = time.time()

  # # Calculating the fps

  # # fps will be number of frame processed in given time frame
  # # since their will be most of time error of 0.001 second
  # # we will be subtracting it to get more accurate result
  # # fps = 1/(new_frame_time-prev_frame_time)
  # fps = 10/(new_frame_time-prev_frame_time)
  # prev_frame_time = new_frame_time

  # # # converting the fps into integer
  # fps = int(fps)
  
  # # converting the fps to string so that we can display it on frame
  # # by using putText function
  # fps = str(fps)

  # # putting the FPS count on the frame
  # cv2.putText(gray, fps, (7, 170), font, 3, (100, 255, 0), 3, cv2.LINE_AA)

  # # displaying the frame with fps
  # cv2.imshow('frame', gray)
  # # -- end show fps

  # import time
  # fps_end_time = time.time()
  # time_diff = fps_end_time - fps_start_time
  # fps = 1/(time_diff)
  # fps_start_time = fps_end_time
  # fps_text = "FPS: {:.2f}".format(fps)
  # cv2.putText(img, fps_text, (5,130), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,255), 1)
  # cv2.imshow('frame', img)

  for face in faces:
    x1,y1 = face.left(),face.top()
    x2,y2 = face.right(),face.bottom()
    # imgOriginal = cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
    landmarks = predictor(imgGray,face)
    myPoints = []
    # print(landmarks)

    # for n in range(68):
    for n in range(19):
      x = landmarks.part(n).x
      y = landmarks.part(n).y
      myPoints.append([x,y])

    myPoints = np.array(myPoints)
    # imgLips = createBox(img,myPoints[48:61],3,masked=True,cropped=False)
    imgLips = createBox(img,myPoints[0:19],0,masked=True,cropped=False)

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
    cv2.imshow('makeup',imgColorLips)

    # showing only masked lips
    # cv2.imshow('Virtual Makeup', imgLips)

    # print(myPoints)
  # showing original video 
  # cv2.imshow('Original', imgOriginal)
  cv2.waitKey(1)