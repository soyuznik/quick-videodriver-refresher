import pyautogui


# (win-key) + (ctrl-left) + (shift-left) + (b-key)
try:
    pyautogui.keyDown("winleft")
    pyautogui.keyDown("ctrlleft")
    pyautogui.keyDown("shiftleft")
    pyautogui.keyDown("b")
except:
    pyautogui.keyUp("winleft")
    pyautogui.keyUp("ctrlleft")
    pyautogui.keyUp("shiftleft")
    pyautogui.keyUp("b")
    print("Failed to restart the video driver "
          "and refresh the connection with monitor")
finally:
    pyautogui.keyUp("winleft")
    pyautogui.keyUp("ctrlleft")
    pyautogui.keyUp("shiftleft")
    pyautogui.keyUp("b")
    print("Succesfully restarted the video driver "
          "and refreshed the connection with the monitor.")

