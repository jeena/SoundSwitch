SoundSwitch
===========

This script listens to two audio input devices and determins which one is louder
at a given moment and presses programatically one of two defined keys. If for
some time nobody is speaking or everyone at roughly the lame volume then it
presses a third defined key.

With help of this you can for example switch between scenes in
[OBS](https://obsproject.com/) to show the person who is currently speaking.

Installation
------------

There are some python 3 dependencies which need to be installed:

	pip install numpy sounddevice pyautogui


Usage
-----

Run the script by just calling it:

	./soundswitch.py

It will ask you which two devices you want it to listen to, on Linux it could
look something like this:

	➜ jeena@William soundswitch (master✗) ./soundswitch.py 
	   0 HDA Intel PCH: ALC3271 Analog (hw:0,0), ALSA (2 in, 2 out)
	   1 HDA Intel PCH: HDMI 0 (hw:0,3), ALSA (0 in, 2 out)
	   2 HDA Intel PCH: HDMI 1 (hw:0,7), ALSA (0 in, 8 out)
	   3 HDA Intel PCH: HDMI 2 (hw:0,8), ALSA (0 in, 8 out)
	   4 HDA Intel PCH: HDMI 3 (hw:0,9), ALSA (0 in, 8 out)
	   5 HDA Intel PCH: HDMI 4 (hw:0,10), ALSA (0 in, 8 out)
	   6 C922 Pro Stream Webcam: USB Audio (hw:1,0), ALSA (2 in, 0 out)
	   7 H5: USB Audio (hw:2,0), ALSA (0 in, 2 out)
	   8 sysdefault, ALSA (128 in, 128 out)
	   9 front, ALSA (0 in, 2 out)
	  10 surround40, ALSA (0 in, 2 out)
	  11 surround51, ALSA (0 in, 2 out)
	  12 surround71, ALSA (0 in, 2 out)
	  13 hdmi, ALSA (0 in, 2 out)
	  14 samplerate, ALSA (128 in, 128 out)
	  15 speexrate, ALSA (128 in, 128 out)
	  16 pulse, ALSA (32 in, 32 out)
	  17 speex, ALSA (1 in, 1 out)
	  18 upmix, ALSA (8 in, 8 out)
	  19 vdownmix, ALSA (6 in, 6 out)
	  20 VirtualCard0, ALSA (32 in, 32 out)
	  21 dmix, ALSA (0 in, 2 out)
	* 22 default, ALSA (32 in, 32 out)
	Choose microphone 1: 6
	Choose microphone 2: 22

In this case we chose the Webcam as the first device and the default device as
the second device.

Note: The script can only press the buttons when OBS is the window with focus.

License
-------

(c) 2020 Jeena Paradies

SoundSwitch is free software: you can redistribute it and/or modify it under the
terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later version.

FeedTheMonkey is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with
SountSwitch. If not, see http://www.gnu.org/licenses/.
