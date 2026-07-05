# import cv2
# import mediapipe as mp
# import pyautogui
# import time

# pyautogui.FAILSAFE = False

# cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# mp_hands = mp.solutions.hands
# hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.75, min_tracking_confidence=0.75)
# drawer = mp.solutions.drawing_utils

# # Settings
# scroll_active = True
# scroll_direction = 1               # 1 = UP Mode, -1 = DOWN Mode
# previous_index_y = None
# scroll_speed = 80
# last_palm_time = 0
# scroll_threshold=0.018

# while True:
#     success, frame = cap.read()
#     if not success: continue

#     frame = cv2.flip(frame, 1)
#     #mirror image to feel real 
    
#     # bgr to rgb conversion 
#     rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
#     results = hands.process(rgb)

#     if results.multi_hand_landmarks:
#         for hand in results.multi_hand_landmarks:
            
#             # ================= OPEN PALM TO SWITCH MODE =================
#             fingers_up = sum(1 for i in [8,12,16,20] if hand.landmark[i].y < hand.landmark[i-2].y)
#             is_open_palm = fingers_up >= 4

#             if is_open_palm and time.time() - last_palm_time > 1.0:
#                 scroll_direction = -scroll_direction
#                 last_palm_time = time.time()
#                 print("Switched to", "UP Mode" if scroll_direction == 1 else "DOWN Mode")

#             # ================= ONE DIRECTION SCROLLING =================
#             index_up = hand.landmark[8].y < hand.landmark[6].y

#             if index_up and previous_index_y is not None:
#                 curr_y = hand.landmark[8].y
#                 delta = previous_index_y - curr_y   # Positive = finger moving up

#                 mode_name = "UP MODE" if scroll_direction == 1 else "DOWN MODE"
#                 cv2.putText(frame, mode_name, (20, 50),
#                            cv2.FONT_HERSHEY_SIMPLEX, 1.1, (0, 255, 0), 3)

#                 # One-directional logic
#                 if scroll_direction == 1:                    # UP Mode
#                     if delta > 0.025:                        # Finger moving UP only
#                         pyautogui.scroll(-scroll_speed)      # Scroll Down (lower content)
#                         print("↓ Scroll Down")

#                 elif scroll_direction == -1:                 # DOWN Mode
#                     if delta < -0.025:                       # Finger moving DOWN only
#                         pyautogui.scroll(scroll_speed)       # Scroll Up (upper content)
#                         print("↑ Scroll Up")

#                 previous_index_y = curr_y
#             else:
#                 previous_index_y = None if not index_up else hand.landmark[8].y

#             drawer.draw_landmarks(frame, hand, mp_hands.HAND_CONNECTIONS)

#     # Status
#     dir_text = "UP" if scroll_direction == 1 else "DOWN"
#     cv2.putText(frame, f"Mode: {dir_text} (Open Palm to Switch)", (20, 450),
#                 cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255,255,255), 2)

#     cv2.imshow("AirScroll Camera", frame)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()

import cv2
import mediapipe as mp
import pyautogui
import time

pyautogui.FAILSAFE = False

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)


# it will detecting 1 hand at max to avoid unstability 
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.75, min_tracking_confidence=0.75)
drawer = mp.solutions.drawing_utils

# Settings
scroll_active = True
scroll_direction = 1
previous_index_y = None
scroll_speed = 90
last_palm_time = 0

while True:
    success, frame = cap.read()
    if not success: continue

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    if results.multi_hand_landmarks:
        for hand in results.multi_hand_landmarks:
            
            # Open Palm to Switch Mode
            fingers_up = sum(1 for i in [8,12,16,20] if hand.landmark[i].y < hand.landmark[i-2].y)
            is_open_palm = fingers_up >= 4

            if is_open_palm and time.time() - last_palm_time > 1.0:
                scroll_direction = -scroll_direction
                last_palm_time = time.time()
                print("Switched to", "UP Mode" if scroll_direction == 1 else "DOWN Mode")

            # Pure Index Finger Tracking
            index_tip_y = hand.landmark[8].y
            
            thumb = hand.landmark[4]
            index = hand.landmark[8]
            
            distance = ((thumb.x - index.x)**2 + (thumb.y-index.y)**2)**0.5
            

            index_raised = index_tip_y < hand.landmark[6].y

            if index_raised:
                mode_name = "UP MODE" if scroll_direction == 1 else "DOWN MODE"
                cv2.putText(frame, mode_name, (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.1, (0, 255, 0), 3)

                if previous_index_y is not None:
                    delta = previous_index_y - index_tip_y

                    if scroll_direction == 1:                    # UP Mode
                        if delta > 0.022:                        # Finger Up
                            pyautogui.scroll(-scroll_speed)
                            print("↓ Scroll Down")

                    elif scroll_direction == -1:                 # DOWN Mode
                        if delta < -0.018:                       # Finger Down (more sensitive)
                            pyautogui.scroll(scroll_speed)
                            print("↑ Scroll Up")

                previous_index_y = index_tip_y
            else:
                previous_index_y = None

            drawer.draw_landmarks(frame, hand, mp_hands.HAND_CONNECTIONS)

    dir_text = "UP" if scroll_direction == 1 else "DOWN"
    cv2.putText(frame, f"Mode: {dir_text} (Open Palm to Switch)", (20, 450),
                cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255,255,255), 2)

    cv2.imshow("AirScroll Camera", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()



# import cv2
# import mediapipe as mp
# import pyautogui
# import time
# import math

# pyautogui.FAILSAFE = False

# cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# mp_hands = mp.solutions.hands
# hands = mp_hands.Hands(
#     max_num_hands=1,
#     min_detection_confidence=0.75,
#     min_tracking_confidence=0.75
# )

# drawer = mp.solutions.drawing_utils

# # ---------------- SETTINGS ----------------
# scroll_direction = 1         # 1 = UP MODE, -1 = DOWN MODE
# scroll_speed = 90

# previous_index_y = None
# last_palm_time = 0

# zoom_mode = False
# previous_pinch_distance = None

# PINCH_START_THRESHOLD = 0.05
# ZOOM_DELTA_THRESHOLD = 0.015

# # ------------------------------------------

# while True:
#     success, frame = cap.read()

#     if not success:
#         continue

#     frame = cv2.flip(frame, 1)

#     rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

#     results = hands.process(rgb)

#     if results.multi_hand_landmarks:

#         for hand in results.multi_hand_landmarks:

#             landmarks = hand.landmark

#             # ---------------- OPEN PALM ----------------
#             fingers_up = sum(
#                 1 for i in [8, 12, 16, 20]
#                 if landmarks[i].y < landmarks[i - 2].y
#             )

#             is_open_palm = fingers_up >= 4

#             # Open palm exits zoom mode
#             if zoom_mode:
#                 if is_open_palm and time.time() - last_palm_time > 1:
#                     zoom_mode = False
#                     previous_pinch_distance = None
#                     last_palm_time = time.time()
#                     print("Exited Zoom Mode")

#             else:
#                 # Open palm toggles scroll direction
#                 if is_open_palm and time.time() - last_palm_time > 1:
#                     scroll_direction *= -1
#                     last_palm_time = time.time()

#                     print(
#                         "Switched to",
#                         "UP MODE" if scroll_direction == 1 else "DOWN MODE"
#                     )

#             # ---------------- PINCH DETECTION ----------------
#             thumb = landmarks[4]
#             index = landmarks[8]

#             pinch_distance = math.hypot(
#                 thumb.x - index.x,
#                 thumb.y - index.y
#             )

#             # Enter zoom mode
#             if not zoom_mode and pinch_distance < PINCH_START_THRESHOLD:
#                 zoom_mode = True
#                 previous_pinch_distance = pinch_distance
#                 print("Entered Zoom Mode")

#             # ---------------- ZOOM MODE ----------------
#             if zoom_mode:

#                 cv2.putText(
#                     frame,
#                     "ZOOM MODE",
#                     (20, 50),
#                     cv2.FONT_HERSHEY_SIMPLEX,
#                     1,
#                     (0, 255, 255),
#                     3
#                 )

#                 if previous_pinch_distance is not None:

#                     zoom_delta = pinch_distance - previous_pinch_distance

#                     # Fingers moving apart
#                     if zoom_delta > ZOOM_DELTA_THRESHOLD:
#                         pyautogui.keyDown("ctrl")
#                         pyautogui.scroll(100)
#                         pyautogui.keyUp("ctrl")

#                         print("Zoom In")

#                     # Fingers moving closer
#                     elif zoom_delta < -ZOOM_DELTA_THRESHOLD:
#                         pyautogui.keyDown("ctrl")
#                         pyautogui.scroll(-100)
#                         pyautogui.keyUp("ctrl")

#                         print("Zoom Out")

#                 previous_pinch_distance = pinch_distance

#             # ---------------- SCROLL MODE ----------------
#             else:

#                 index_tip_y = landmarks[8].y
#                 index_raised = index_tip_y < landmarks[6].y

#                 if index_raised:

#                     mode_name = (
#                         "UP MODE"
#                         if scroll_direction == 1
#                         else "DOWN MODE"
#                     )

#                     cv2.putText(
#                         frame,
#                         mode_name,
#                         (20, 50),
#                         cv2.FONT_HERSHEY_SIMPLEX,
#                         1.1,
#                         (0, 255, 0),
#                         3
#                     )

#                     if previous_index_y is not None:

#                         delta = previous_index_y - index_tip_y

#                         # Finger moving up
#                         if scroll_direction == 1:
#                             if delta > 0.022:
#                                 pyautogui.scroll(-scroll_speed)
#                                 print("Scroll Down")

#                         # Finger moving down
#                         else:
#                             if delta < -0.018:
#                                 pyautogui.scroll(scroll_speed)
#                                 print("Scroll Up")

#                     previous_index_y = index_tip_y

#                 else:
#                     previous_index_y = None

#             drawer.draw_landmarks(
#                 frame,
#                 hand,
#                 mp_hands.HAND_CONNECTIONS
#             )

#     status = (
#         "ZOOM MODE"
#         if zoom_mode
#         else ("UP MODE" if scroll_direction == 1 else "DOWN MODE")
#     )

#     cv2.putText(
#         frame,
#         f"Current: {status}",
#         (20, 450),
#         cv2.FONT_HERSHEY_SIMPLEX,
#         0.75,
#         (255, 255, 255),
#         2
#     )

#     cv2.imshow("AirScroll", frame)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()