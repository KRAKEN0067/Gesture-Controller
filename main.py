import cv2

from camera import Camera
from hand_gesture import HandGesture
from gesture_classifier import GestureClassifier
from browser_controller import BrowserController
from gesture_ui import GestureUI


camera = Camera()
hand = HandGesture()
classifier = GestureClassifier()
control = BrowserController()
ui = GestureUI()


def update_frame():
    frame = camera.get_frame()

    if frame is None:
        camera.release()
        cv2.destroyAllWindows()
        ui.root.destroy()
        return

    frame, hand_landmarks, hand_label = hand.detect(frame)

    gesture = "None"

    if hand_landmarks is not None:
        gesture = classifier.predict(hand_landmarks, hand_label)
        print(gesture)

        if ui.enabled and gesture is not None:
            control.perform_operation(gesture, hand_landmarks)

    ui.set_gesture(gesture)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        camera.release()
        cv2.destroyAllWindows()
        ui.root.destroy()
        return

    ui.root.after(10, update_frame)


def on_close():
    camera.release()
    cv2.destroyAllWindows()
    ui.root.destroy()


ui.root.protocol("WM_DELETE_WINDOW", on_close)

update_frame()
ui.root.mainloop()