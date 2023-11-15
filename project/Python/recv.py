import cv2
from simple_facerec import SimpleFacerec

sft = SimpleFacerec()

sft.load_encoding_images("images/")


cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    #detect faces
    faceloc, face_name = sft.detect_known_faces(frame)
    for face_loc,name in zip(faceloc, face_name):
        y1, x1, y2, x2= face_loc[0], face_loc[1],face_loc[2],face_loc[3]

        cv2.putText(frame,name, (x1,y1 -10), cv2.FONT_HERSHEY_DUPLEX, 1,(0,0,0),1)
        cv2.rectangle(frame,(x1,y1),(x2,y2), (0,0,255),2)

    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key==0:
        break

cap.release()
cv2.destroyAllWindows()