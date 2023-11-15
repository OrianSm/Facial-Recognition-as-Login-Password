import cv2
import face_recognition
from facerec import SimpleFacerec
import sys

password = sys.argv[1]
password = password.strip('\'')
path="C:/xampp/htdocs/project/Signuppwd/"
path+=password

sft = SimpleFacerec()
image= cv2.imread(path)  #Path Should go here
rgb_img=cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
img_encoding= face_recognition.face_encodings(rgb_img)[0]
sft.load_encoded_image(img_encoding)

def recognize():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
    #detect faces
        matched_face= sft.detect_known_faces(frame)
        if matched_face==True:
            print("Face Matched")
            break

        cv2.imshow("Frame", frame)

        key = cv2.waitKey(1)
        if key==0:
            break

    cap.release()
    cv2.destroyAllWindows()
recognize()
