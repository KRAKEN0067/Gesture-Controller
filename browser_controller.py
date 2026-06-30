import time
import pyautogui as pt


class BrowserController:
    def __init__(self):
        pt.FAILSAFE = False

        self.screen_width, self.screen_height = pt.size()

        self.prev_x, self.prev_y = pt.position()
        pt.PAUSE = 0
        self.dead_zone = 25      # very stable, less sensitive
        self.smoothing = 0.35  # smoother

        self.scroll_prev_y = None
        self.scroll_sensitivity = 700

        self.last_click_time = 0
        self.last_action_time = 0
        self.click_cooldown = 0.5
        self.action_cooldown = 0.8

    def _can_click(self):
        current_time = time.time()
        if current_time - self.last_click_time >= self.click_cooldown:
            self.last_click_time = current_time
            return True
        return False

    def _can_perform_action(self):
        current_time = time.time()
        if current_time - self.last_action_time >= self.action_cooldown:
            self.last_action_time = current_time
            return True
        return False

    def perform_operation(self, gesture, hand_landmarks):


        if gesture == "MOVE_MOUSE":
            index_tip = hand_landmarks.landmark[8]

            min_x = 0.10
            max_x = 0.90
            min_y = 0.15
            max_y = 0.70

            normalized_x = (index_tip.x - min_x) / (max_x - min_x)
            normalized_y = (index_tip.y - min_y) / (max_y - min_y)

            normalized_x = max(0, min(1, normalized_x))
            normalized_y = max(0, min(1, normalized_y))

            target_x = int(normalized_x * self.screen_width)
            target_y = int(normalized_y * self.screen_height)

            dead_zone = 20

            dx = target_x - self.prev_x
            dy = target_y - self.prev_y

            if abs(dx) < dead_zone and abs(dy) < dead_zone:
                return

            curr_x = self.prev_x + dx * self.smoothing
            curr_y = self.prev_y + dy * self.smoothing

            pt.moveTo(curr_x, curr_y)

            self.prev_x = curr_x
            self.prev_y = curr_y

        #LEFT CLICK CONDITION
        elif gesture == "LEFT_CLICK":
            if self._can_click():
                pt.click()

            self.scroll_prev_y = None

        elif gesture == "SCROLL":
            index_tip = hand_landmarks.landmark[8]

            # Use camera-normalized y directly, not screen y
            curr_y = index_tip.y

            # First frame of scroll mode: only set starting point
            if self.scroll_prev_y is None:
                self.scroll_prev_y = curr_y
                return

            dy = curr_y - self.scroll_prev_y

            scroll_dead_zone = 0.025  # ignore tiny finger shaking
            scroll_speed = 150   #
            if abs(dy) > scroll_dead_zone:
                # In pyautogui:
                # positive scroll = up
                # negative scroll = down
                if dy > 0:
                    pt.scroll(-scroll_speed)  # hand moved down -> page scrolls down
                else:
                    pt.scroll(scroll_speed)   # hand moved up -> page scrolls up

                # Reset baseline after each scroll step
                self.scroll_prev_y = curr_y

        elif gesture == "NEW_TAB":
            if self._can_perform_action():
                pt.hotkey("ctrl", "t")

            self.scroll_prev_y = None

        elif gesture == "PREVIOUS_TAB":
            if self._can_perform_action():
                pt.hotkey("ctrl", "shift", "tab")

            self.scroll_prev_y = None

        elif gesture == "NEXT_TAB":
            if self._can_perform_action():
                pt.hotkey("ctrl", "tab")

            self.scroll_prev_y = None

        elif gesture == "REFRESH":
            if self._can_perform_action():
                pt.hotkey("ctrl", "r")

            self.scroll_prev_y = None

        elif gesture == "BACK":
            if self._can_perform_action():
                pt.hotkey("alt", "left")

            self.scroll_prev_y = None

        else:
            self.scroll_prev_y = None



# import pyautogui as pt


# class BrowserController:
#     def __init__(self):
#         pt.FAILSAFE = False
#         self.screen_width, self.screen_height = pt.size()
#         self.prev_x = 0
#         self.prev_y = 0
#         self.smoothing = 5
            
#     def perform_operation(self, gesture, hand_landmarks):

#         if gesture == "MOVE_MOUSE":
#             # screen_width, screen_height = pt.size()

#             index_tip = hand_landmarks.landmark[8]

#             target_x = int(index_tip.x * self.screen_width)
#             target_y = int(index_tip.y * self.screen_height)

#             threshold = 6

#             if abs(target_x - self.prev_x) > threshold or abs(target_y - self.prev_y) > threshold:
#                 curr_x = self.prev_x + (target_x - self.prev_x) / self.smoothing
#                 curr_y = self.prev_y + (target_y - self.prev_y) / self.smoothing

#                 if curr_x is None or curr_y is None:
#                     return
#                 pt.moveTo(curr_x, curr_y)

#                 self.prev_x = curr_x
#                 self.prev_y = curr_y


#         if gesture == "LEFT_CLICK":
        
#             currentMouseX, currentMouseY = pt.position() 

#             # target_x = int(index_tip.x * self.screen_width)
#             # target_y = int(index_tip.y * self.screen_height)

#             pt.click(currentMouseX, currentMouseY)

#         if gesture == "SCROLL":

#             index_tip = hand_landmarks.landmark[8]

#             # curr_x = int(index_tip.x * self.screen_width)
#             curr_y = int(index_tip.y * self.screen_height)
            
#             # if curr_y > self.prev_y :
#             #     pt.scroll(150)
#             # else:
#             #     pt.scroll(-150)

#             pt.scroll(-150)


#             # self.prev_x = curr_x
#             self.prev_y = curr_y


            


    