import pyautogui
import time
import random

screen_width, screen_height = pyautogui.size()

min_interval = 1
max_interval = 5

min_distance = 100
max_distance = 500

mouse_speed = 300

pyautogui.FAILSAFE = False

while True:
    try:
        interval = random.uniform(min_interval, max_interval)

        dx = random.randint(-max_distance, max_distance)
        dy = random.randint(-max_distance, max_distance)

        new_x = pyautogui.position().x + dx
        new_y = pyautogui.position().y + dy

        new_x = max(0, min(screen_width, new_x))
        new_y = max(0, min(screen_height, new_y))

        pyautogui.moveTo(new_x, new_y, duration=abs(dx) / mouse_speed)

        time.sleep(interval)

    except pyautogui.FailSafeException:
        pyautogui.moveTo(screen_width // 2, screen_height // 2)
        print("Edge reached, re-centering.")

    except Exception as e:
        print(f"Error occurred: {e}")
        break

        