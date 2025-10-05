import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)
hands = mp.solutions.hands.Hands()
draws = mp.solutions.drawing_utils

while True:
    _, frame = cap.read()

    frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    hands_obj = hands.process(frameRGB)

    if hands_obj.multi_hand_landmarks:
        for hand_landmarks in hands_obj.multi_hand_landmarks:
            draws.draw_landmarks(frame,
                                 hand_landmarks,
                                 mp.solutions.hands.HAND_CONNECTIONS)
            
    cv2.imshow("Wir", frame)
    if cv2.waitKey(1) == ord("q"):
        break

cap.release
cv2.destroyAllWindows()