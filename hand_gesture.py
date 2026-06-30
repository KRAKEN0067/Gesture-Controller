import cv2
import mediapipe as mp


class HandGesture:

    def __init__(self):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=2,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5
        )

        self.mp_drawing = mp.solutions.drawing_utils

    def detect(self, frame):
        # Convert BGR to RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Improve performance
        rgb_frame.flags.writeable = False
        results = self.hands.process(rgb_frame)
        rgb_frame.flags.writeable = True

        hand_landmarks = None
        hand_label = None
        # Draw landmarks if hands are detected
        if results.multi_hand_landmarks:
            for hand_landmarks , handedness in zip(results.multi_hand_landmarks, results.multi_handedness):

                hand_label = handedness.classification[0].label
                print(hand_label)   # Left or Right

                self.mp_drawing.draw_landmarks(
                    frame,
                    hand_landmarks,
                    self.mp_hands.HAND_CONNECTIONS
                )

                wrist = hand_landmarks.landmark[0]

                thumb_MCP = hand_landmarks.landmark[1]
                thumb_PIP = hand_landmarks.landmark[2]
                thumb_DIP = hand_landmarks.landmark[3]
                thumb_tip = hand_landmarks.landmark[4]

                index_MCP = hand_landmarks.landmark[5]
                index_PIP = hand_landmarks.landmark[6]
                index_DIP = hand_landmarks.landmark[7]
                index_tip = hand_landmarks.landmark[8]

                middle_MCP = hand_landmarks.landmark[9]
                middle_PIP = hand_landmarks.landmark[10]
                middleDIP = hand_landmarks.landmark[11]
                middle_tip = hand_landmarks.landmark[12]

                ring_MCP = hand_landmarks.landmark[13]
                ring_PIP = hand_landmarks.landmark[14]
                ring_DIP = hand_landmarks.landmark[15]
                ring_tip = hand_landmarks.landmark[16]

                pinky_MCP = hand_landmarks.landmark[17]
                pinky_PIP = hand_landmarks.landmark[18]
                pinky_DIP = hand_landmarks.landmark[19]
                pinky_tip = hand_landmarks.landmark[20]

                # print("Wrist =", wrist.x)
                
                # print("thumb Finger Tip")
                # print("x =", thumb_tip.x)
                # print("y =", thumb_tip.y)
                # print("z =", thumb_tip.z)

                # print("Index Finger Tip")
                # print("x =", index_tip.x)
                # print("y =", index_tip.y)
                # print("z =", index_tip.z)

                # print("middle Finger Tip")
                # print("x =", middle_tip.x)
                # print("y =", middle_tip.y)
                # print("z =", middle_tip.z)

                # print("ring Finger Tip")
                # print("x =", ring_tip.x)
                # print("y =", ring_tip.y)
                # print("z =", ring_tip.z)

                # print("pinky Finger Tip")
                # print("x =", pinky_tip.x)
                # print("y =", pinky_tip.y)
                # print("z =", pinky_tip.z)

        return frame, hand_landmarks, hand_label
    
    def close(self):
        self.hands.close()