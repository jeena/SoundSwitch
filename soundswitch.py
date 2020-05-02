#!/usr/bin/env python3

"""
Just a PoC to be able to listen to different audio input devices
and press keyboard buttons depending on which one is louder.
"""

import time as t
import numpy as np
import sounddevice as sd
import threading
import sys
import pyautogui

# Settings

# Which hot keys should it press?
# First: default if nobody is speaking or both are speaking
# Second: first device is louder
# Third: second device is louder
scene_keys = ['1', '2', '3']

# At which loudness should we switch to a microphone?
# Choose something between 1 and 50 
min_v=10

# What difference between laudness needs to be to choose
# the specific microphone?
# Choose something between 1 and 50
dif_v=10

# How long to stay on microphone after it's quiet?
# In seconds
timeout_speaking=3

#
# Global variables, don't change
#
mic1_v=0
mic1_t=t.time()
mic2_v=0
mic2_t=t.time()
last_key=scene_keys[1]

def show_scene():
	global last_key
	key=last_key
	now = t.time()
	if (mic1_v - mic2_v) > dif_v and mic1_v > min_v:
		key=scene_keys[1]
	elif (mic2_v - mic1_v) > dif_v and mic2_v > min_v:
		key=scene_keys[2]
	else:
		now = t.time()
		if ( (now - mic1_t) > timeout_speaking and (now - mic2_t) > timeout_speaking ):
			key=scene_keys[0]
	if last_key != key:
		last_key = key
		pyautogui.press(key)
	# print("mic1:", mic1_v, int(now - mic1_t), "mic2:",mic2_v, int(now - mic2_t), key)
	threading.Timer(1, show_scene).start()

def audio_callback_mic1(indata, frames, time, status):
	global mic1_v
	global mic1_t
	mic1_v=int(np.linalg.norm(indata) * 10)
	if mic1_v > min_v:
		mic1_t = t.time()

def audio_callback_mic2(indata, frames, time, status):
	global mic2_v
	global mic2_t
	mic2_v=int(np.linalg.norm(indata) * 10)
	if mic2_v > min_v:
		mic2_t = t.time()

def start(callback, device=None):
	stream = sd.InputStream(callback=callback, device=device)
	stream.start()

if __name__ == "__main__":
	print(sd.query_devices())
	print("Choose microphone 1:", end=" ", flush=True)
	mic1 = int(sys.stdin.readline())
	print("Choose microphone 2:", end=" ", flush=True)
	try:
		mic2 = int(sys.stdin.readline())
	except ValueError:
		mic2 = None
	t1 = threading.Thread(target=start, args=(audio_callback_mic1, mic1,))
	t2 = threading.Thread(target=start, args=(audio_callback_mic2, mic2,))
	t1.start()
	t2.start()
	show_scene()
