import cv2 
import mediapipe 
import time






class HandDetector :
    
    def __init__(self):
        
        self.mpHands = mediapipe.solutions.hands
        self.hands = self.mpHands.Hands()
        self.mpDraw = mediapipe.solutions.drawing_utils


    def findHands (self , image , draw= True) :
        imageRGB = cv2.cvtColor(image , cv2.COLOR_RGB2BGR)
        self.result = self.hands.process(imageRGB)

        if self.result.multi_hand_landmarks :
            for handlms in self.result.multi_hand_landmarks:
                if draw :
                    self.mpDraw.draw_landmarks(image , handlms , self.mpHands.HAND_CONNECTIONS)

        return image

    def handPosition(self , image , handNo =0 , draw=True):
        handPositionList = []
        if self.result.multi_hand_landmarks:
            hand = self.result.multi_hand_landmarks[handNo]
            for id , landmark in enumerate(hand.landmark):
                h , w, c = image.shape
                cx , cy = int(landmark.x * w) , int(landmark.y * h)
                handPositionList.append([id , cx , cy])
                if draw :
                    cv2.putText(image ,"[{} , {}]".format(cx , cy)  ,(cx +1, cy+1),cv2.FONT_HERSHEY_COMPLEX_SMALL ,1, (0, 0 , 0) ,1)

        return handPositionList



def main():
    
    pereviousTime = 0 
    currentTime = 0 

    cap = cv2.VideoCapture(0)
    handDetect = HandDetector()

    while True :
        success , image = cap.read()
        image = handDetect.findHands(image)
        handPositionList = handDetect.handPosition(image)

        currentTime = time.time()
        fbs = 1/ (currentTime - pereviousTime)
        pereviousTime = currentTime
        cv2.putText(image , str(int(fbs)), (5,25) ,cv2.FONT_HERSHEY_SIMPLEX , 2 , (255,0,255) , 2)

        cv2.imshow("Hand Detector" , image)
        if cv2.waitKey(1) & 0xff == ord("q"):
            break
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()