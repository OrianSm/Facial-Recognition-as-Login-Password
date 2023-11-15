import cv2
import face_recognition
from simple_facerec import SimpleFacerec

image= cv2.imread("kohli.jpg")
rgb_img=cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
img_encoding= face_recognition.face_encodings(rgb_img)[0]


img= cv2.imread("js.jpeg")
im2=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_encoding2=face_recognition.face_encodings(im2)[0]

result=face_recognition.compare_faces([img_encoding], img_encoding2)
print("Result:",result)
cv2.waitKey(0)
