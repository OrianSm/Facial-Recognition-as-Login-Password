import openai
import gradio
import cv2
import face_recognition
from facerec import SimpleFacerec
import sys

def ch():
    with open("key.txt") as f:
        openai.api_key=f.read()

    messages=[{"role":"system","content":"you are a chatbot"}]

    def custombot(your_input):
        messages.append({"role":"user", "content":your_input})
        response=openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
        )
        ChatGpt_reply=response["choices"][0]["message"]["content"]
        messages.append({"role":"assistant","content":ChatGpt_reply})
        return ChatGpt_reply
        demo=gradio.Interface(fn=custombot, inputs="text",outputs="text",title="ChatBot")
        demo.launch(share=True)

#password = sys.argv[1];
#password = password.strip('\'');
path="C:/xampp/htdocs/project/Signuppwd/R1.jpeg";
#path+=password;



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
            ch()
            break

        cv2.imshow("Frame", frame)

        key = cv2.waitKey(1)
        if key==0:
            break

    cap.release()
    cv2.destroyAllWindows()
recognize()
