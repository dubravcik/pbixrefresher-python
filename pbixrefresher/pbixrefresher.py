import time
import os
import sys
import argparse
import psutil
from pywinauto.application import Application
from pywinauto import timings


def type_keys(string, element):
    """Type a string char by char to Element window"""
    for char in string:
        element.type_keys(char)

def main():   
	# Parse arguments from cmd
	parser = argparse.ArgumentParser()
	parser.add_argument("workbook", help = "Path to .pbix file")
	parser.add_argument("--workspace", help = "name of online Power BI service work space to publish in", default = "My workspace")
	parser.add_argument("--refresh-timeout", help = "refresh timeout", default = 30000, type = int)
	parser.add_argument("--no-publish", dest='publish', help="don't publish, just save", default = True, action = 'store_false' )
	parser.add_argument("--init-wait", help = "initial wait time on startup", default = 15, type = int)
	args = parser.parse_args()

	timings.after_clickinput_wait = 1
	WORKBOOK = args.workbook
	WORKSPACE = args.workspace
	INIT_WAIT = args.init_wait
	REFRESH_TIMEOUT = args.refresh_timeout

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
	print("Waiting ",INIT_WAIT,"sec")
	time.sleep(INIT_WAIT)

	# Connect pywinauto
	print("Identifying Power BI window")
	app = Application(backend = 'uia').connect(path = PROCNAME)
	win = app.window(title_re = '.*Power BI Desktop')
	time.sleep(5)
	win.wait("enabled", timeout = 300)
	win.Save.wait("enabled", timeout = 300)
	win.set_focus()
	win.Home.click_input()
	win.Save.wait("enabled", timeout = 300)
	win.wait("enabled", timeout = 300)

	# Refresh
	print("Refreshing")
	win.Refresh.click_input()
	#wait_win_ready(win)
	time.sleep(10)
	print("Waiting for refresh end (timeout in ", REFRESH_TIMEOUT,"sec)")
	win.wait("enabled", timeout = REFRESH_TIMEOUT)

	# Save
	print("Saving")
	type_keys("%1", win)
	#wait_win_ready(win)
	time.sleep(5)
	win.wait("enabled", timeout = REFRESH_TIMEOUT)

	# Publish
	if args.publish:
		print("Publish")
		win.Publish.click_input()
		publish_dialog = win.child_window(auto_id = "KoPublishToGroupDialog")
		publish_dialog.child_window(title = WORKSPACE, found_index=0).click_input()
		publish_dialog.Select.click()
		try:
			win.Replace.wait('visible', timeout = 10)
		except Exception:
			pass
		if win.Replace.exists():
			win.Replace.click_input()
		win["Got it"].wait('visible', timeout = REFRESH_TIMEOUT)
		win["Got it"].click_input()

	#Close
	print("Exiting")
	win.close()

	# Force close
	for proc in psutil.process_iter():
		if proc.name() == PROCNAME:
			proc.kill()

		
if __name__ == '__main__':
	try:
		main()
	except Exception as e:
		print(e)
		sys.exit(1)








