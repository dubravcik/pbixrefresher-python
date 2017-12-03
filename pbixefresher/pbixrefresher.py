import time
import os
import argparse
import psutil
from pywinauto.application import Application, win32defines
from pywinauto import timings
from pywinauto.win32functions import SetForegroundWindow, ShowWindow



def type_keys(string, element):
    """Type a string char by char to Element window"""
    for char in string:
        element.type_keys(char, set_foreground=False)

     
# Parse arguments from cmd
parser = argparse.ArgumentParser()
parser.add_argument("workbook", help = "Path to .pbix file")
parser.add_argument("--workspace", default = "My workspace")
args = parser.parse_args()

timings.after_clickinput_wait = 1
WORKBOOK = args.workbook
WORKSPACE = args.workspace

# Kill running PBI
PROCNAME = "PBIDesktop.exe"
for proc in psutil.process_iter():
    # check whether the process name matches
    if proc.name() == PROCNAME:
        proc.kill()
time.sleep(3)

# Start PBI and open the workbook
print("Starting Power BI")
os.system('start "" "' + WORKBOOK + '"')
time.sleep(15)

# Connect pywinauto
print("Identifying Power BI window")
app = Application(backend = 'uia').connect(path = PROCNAME)
win = app.window(title_re = '.*Power BI Desktop')
time.sleep(2)
win.wait("enabled", timeout = 300)

#win.maximize()
win.set_focus()
win.Ribbon.click_input()
win.wait("enabled", timeout = 300)

# Refresh
print("Refreshing")
type_keys("%y01y14", win)
#wait_win_ready(win)
time.sleep(2)
win.wait("enabled", timeout = 300)

# Save
print("Saving")
type_keys("%1", win)
#wait_win_ready(win)
time.sleep(2)
win.wait("enabled", timeout = 300)

# Publish
print("Publish")
type_keys("%y01y27", win)
publish_dialog = win.child_window(auto_id = "KoPublishToGroupDialog")
publish_dialog.child_window(title = WORKSPACE).click_input()
publish_dialog.Select.click()
try:
    win.Replace.wait('visible', timeout = 10)
except Exception:
    pass
if win.Replace.exists():
    win.Replace.click_input()
win["Got it"].wait('visible', timeout = 3000)
win["Got it"].click_input()

#Close
print("Exiting")
win.close()

# Force close
for proc in psutil.process_iter():
    if proc.name() == PROCNAME:
        proc.kill()








