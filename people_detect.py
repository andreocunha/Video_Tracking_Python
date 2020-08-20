import cv2

cap = cv2.VideoCapture("walking.avi")
font = cv2.FONT_HERSHEY_SCRIPT_COMPLEX
harcascade = cv2.CascadeClassifier("haarcascade_fullbody.xml")

while True:
    ret, frames = cap.read()
    gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)

    full_body = harcascade.detectMultiScale(gray,1.3,2)

    for(x, y, w, h) in full_body:
        cv2.rectangle(frames, (x, y), (x+w, y+h), (0, 255, 255), 2)

        cv2.putText(frames, str('person'), (x, y+h), font, 1, 255)

        cv2.imshow("Screen", frames)

        if cv2.waitKey(33) == 27:
            break

cv2.destroyAllWindows()