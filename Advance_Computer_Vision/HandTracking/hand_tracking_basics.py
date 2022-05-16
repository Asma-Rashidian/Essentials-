import cv2 
import mediapipe as mp 
import time        #check the frame rate 


cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
"""
    static_image_mode = False >> detrects and keeps tracking 
    max_num_hands = 2 
    min_detections_confidence = 0.5
    min_tracking_confidence = 0.5
"""
hands = mpHands.Hands()        
 
mpDraw = mp.solutions.drawing_utils

previousTime = 0 
currentTime = 0


while True :
    sucess , image = cap.read()
    imageRGB = cv2.cvtColor(image , cv2.COLOR_RGB2BGR)      #the input of hand must be RGB kind
    result = hands.process(imageRGB)
    # print(result.multi_hand_landmarks)

    # loop through hands if exists in result 
    if result.multi_hand_landmarks :
        for handlms in result.multi_hand_landmarks :
            # get information of this hand 
            # so we get the id number and the landmark information 
            # the landmark information gives us x  , y and z  information >> x and y are decimal values so we have to multiply them with x and y to get the pixel
            # they are listed in correct order so we have to check their index number 
            for id , landmark in enumerate(handlms.landmark):
                h,w, c = image.shape
                cx , cy = int(landmark.x * w) , int(landmark.y * h )
                
                # put a circle on landmark number 0 
                # if id == 0 :
                #     cv2.circle(image , (cx,cy) ,15 , (255,0,255) , cv2.FILLED)


            # draw the 21 landmarks for each hand in handlms with  an oject from module function drawhand of mediapipe 
            mpDraw.draw_landmarks(image , handlms , mpHands.HAND_CONNECTIONS)


    currentTime = time.time()
    # frame rate 
    fbs = 1  /(currentTime - previousTime)
    previousTime = currentTime 
    
    cv2.putText(image , str(int(fbs)) ,(5,50) ,cv2.FONT_HERSHEY_SIMPLEX ,1 ,(255,0,255) ,2 )

    cv2.imshow("Hand Tracking" , image)
    if cv2.waitKey(1) & 0xff == ord('q') :
        break 
