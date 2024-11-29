import cv2
cap= cv2.VideoCapture(0)
resolution=(int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
outop=cv2.VideoWriter("out25.avi",cv2.VideoWriter_fourcc(*'XVID'),25,resolution)
while cap.isOpened():
    ret,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    if ret:
        cv2.imshow("visuals",frame)
        outop.write(frame)
        if cv2.waitKey(1) & 0xFF ==ord("q"):
            break
    else:
       break
cap.release()
outop.release()
cv2.destroyAllWindows()       

