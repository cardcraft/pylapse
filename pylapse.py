from PIL import Image  # Will need to make sure PIL is installed
import mss
import time
import os

import signal
import sys
import shutil

def exit_func(signal, frame):
	print("exiting")
	os.system("ffmpeg -r " + fps + " -pattern_type glob -i " + foldername + '"/' + '*.png"' + " -vcodec libx264" + foldername + ".mp4")
	print("command ran " + "ffmpeg -r " + fps + " -pattern_type glob -i " + foldername + "/" + '*.png' + " -vcodec libx264" + foldername + ".mp4")
	if remove == "y":
		shutil.rmtree(foldername)
	sys.exit()

signal.signal(signal.SIGINT, exit_func)


starttime = time.time()
i = 0
monnum = input("what monitor (num): ")
delay = input("seconds beetween captures (num) [10]: ")
delay = int(delay)
monnum = int(monnum)
foldername = input("folder name (str) [in current dir]: ")
fps = input("framerate of video (num): ")
remove = input("remove " + foldername + " after done? (y/n)")

os.mkdir(foldername)

while True:
	print("taking image" + str(i))
	with mss.mss() as mss_instance:
		monitor = mss_instance.monitors[monnum]
		screenshot = mss_instance.grab(monitor)
		img = Image.frombytes("RGB", screenshot.size, screenshot.bgra, "raw", "BGRX")  # Convert to PIL.Image
		img.save( foldername + '/' + 'output' + str(i) + '.png', 'PNG')
		i += 1
		time.sleep(delay - ((time.time() - starttime) % delay))

