Now you can automate your desktop applications with this automation script that uses the PyautoGUI module which helps you to perform mouse actions like moving the cursor, left click, etc.

# Automate Mouse Actions
# pip install pyautogui
import pyautogui as pg
# Move Cursor
pg.moveTo(200, 20, duration=1)
# Mouse Click
pg.click(200, 20, duration=1)
# Mouse Double Click
pg.doubleClick(200, 20, duration=1)
# Mouse Right Click
pg.rightClick(200, 20, duration=1)
# Hold Left Mouse Button
pg.mouseDown(200, 20, duration=1)
# Release Left Mouse Button
pg.mouseUp(200, 20, duration=1)
# Drag Mouse
pg.dragTo(200, 20, duration=1)
# Scroll Mouse
pg.scroll(200)
# Get Mouse Position
pg.position()
