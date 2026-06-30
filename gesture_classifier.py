
class GestureClassifier:
    def __init__(self):
        pass

    def predict(self, hand_landmarks, hand_label):

        thumb_tip = hand_landmarks.landmark[4]
        thumb_ip = hand_landmarks.landmark[3]

        index_tip = hand_landmarks.landmark[8]
        index_pip = hand_landmarks.landmark[6]

        middle_tip = hand_landmarks.landmark[12]
        middle_pip = hand_landmarks.landmark[10]

        ring_tip = hand_landmarks.landmark[16]
        ring_pip = hand_landmarks.landmark[14]

        pinky_tip = hand_landmarks.landmark[20]
        pinky_pip = hand_landmarks.landmark[18]

        # -------------------------
        # Finger States
        # -------------------------

        if hand_label == "Right":
            thumb = thumb_tip.x < thumb_ip.x
        else:
            thumb = thumb_tip.x > thumb_ip.x

        index = index_tip.y < index_pip.y
        middle = middle_tip.y < middle_pip.y
        ring = ring_tip.y < ring_pip.y
        pinky = pinky_tip.y < pinky_pip.y

        # -------------------------
        # Variables for palm
        # -------------------------

        thumb_index = abs(thumb_tip.x - index_tip.x)
        index_middle = abs(index_tip.x - middle_tip.x)
        middle_ring = abs(middle_tip.x - ring_tip.x)
        ring_pinky = abs(ring_tip.x - pinky_tip.x)

        # -------------------------
        # Thumb-Index Pinch
        # -------------------------

        pinch = ((thumb_tip.x - index_tip.x) ** 2 +
                (thumb_tip.y - index_tip.y) ** 2) ** 0.5 < 0.05

        # -------------------------
        # Gestures
        # -------------------------

        # ☝️ Move Mouse
        if index and not middle and not ring and not pinky:
            return "MOVE_MOUSE"

        #✌️ Scroll
        elif index and middle and not ring and not pinky:
            return "SCROLL"

        # 👌 Left Click
        elif pinch:
            return "LEFT_CLICK"

        # 🤙 New Tab
        elif thumb and not index and not middle and not ring and pinky:
            return "NEW_TAB"
        

        # # Palm (scroll up and down)
        # elif (thumb and index and middle and ring and pinky and
        #     thumb_index > 0.05 and
        #     index_middle > 0.03 and
        #     middle_ring > 0.03 and
        #     ring_pinky > 0.03):

        #     return "SCROLL"

        # 🤞 Previous Tab
        elif not thumb and index and middle and ring and not pinky:
            return "PREVIOUS_TAB"

        # 🖖 Next Tab
        elif not thumb and index and middle and ring and pinky:
            return "NEXT_TAB"
        
        # 🤞 Previous Tab: Index + Middle + Ring
        elif not thumb and index and middle and ring and not pinky:
            return "PREVIOUS_TAB"

        # 👍 Refresh
        elif thumb and not index and not middle and not ring and not pinky:
            if thumb_tip.y < thumb_ip.y:
                return "REFRESH"
            else:
                return "BACK"

        # # 👎 Back
        # elif thumb and not index and not middle and not ring and not pinky:
        #     if thumb_tip.y > thumb_ip.y:
        #         return "BACK"

        return "UNKNOWN"
        
if __name__ == "__main__":
    pass