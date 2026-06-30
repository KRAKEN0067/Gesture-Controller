import cv2


class Camera:

    def __init__(self):
        self.cam = cv2.VideoCapture(0)

        self.cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
        self.cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    def get_frame(self):
        ret, frame = self.cam.read()

        if not ret:
            return None

        frame = cv2.flip(frame, 1)

        return frame

    def release(self):
        self.cam.release()