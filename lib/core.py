# !/usr/bin/python
# -*- coding: utf-8 -*-

import sys,time
import os,commands,shlex
from robot.libraries.BuiltIn import BuiltIn
from uiautomator import device as d

# TIMEOUT=15
#server 
def install_server():
	"""Install python uiautomator server from given jar_path.

	Example:
	| install_server | /home/sqa/jar|
	"""
	cwd = os.getcwd()
	jar_path = os.path.abspath(os.path.join(cwd, os.pardir))+'/jar'
	command_line='adb push ' + jar_path + '/bundle.jar /data/local/tmp|adb push ' + jar_path + '/uiautomator-stub.jar /data/local/tmp'
	f = os.popen(command_line)
	f = f.read() 
	print f

def start_server():
	"""Start uiautomator server"""
	#command_line='adb shell uiautomator runtest bundle.jar uiautomator-stub.jar -c com.github.uiautomatorstub.Stub &'
	command_line='adb shell uiautomator runtest bundle.jar uiautomator-stub.jar -c com.github.uiautomatorstub.Stub > /dev/null &'
	f = os.popen(command_line)
	f = f.read() 
	print f

#launch&exit
def launch_app(pkg,act):
	"""Launch App"""
	command_line='adb shell am start -n ' + pkg + '/' + act
	f = os.popen(command_line)
	f = f.read() 
	print f

def exit_app(pkg):
	"""Exit App"""
	command_line='adb shell am force-stop ' + pkg
	f = os.popen(command_line)
	f = f.read() 
	print f

# others
def flag(fg,msg):
	""" Pass/fail statement"""
	if fg==False:
		# BuiltIn().run_keyword_if(fg==False,"Fatal Error",'[Error Message] Cannot find "'+ msg + '"')
		BuiltIn().run_keyword_if(fg==False,"Fail",'[Error Message] Cannot find "'+ msg + '"')
	elif fg==True:
		print '[Message] "'+ msg + '"'

def screenshot(shot):
	"""Screenshot will be taken and saved as the given file name 

	Example:
	| screenshot | screenshot1.png|
	"""
	cwd = os.getcwd()
	print cwd
	newpath = os.path.abspath(os.path.join(cwd, os.pardir))+'/screenshots/'
	print newpath
	if not os.path.exists(newpath): 
		os.makedirs(newpath)
	shot_path =  newpath+shot
	d.screenshot(shot_path)

#system behavior

def home_screen():
	""" Press Home key"""
	d.press.menu()

def screen_on():
	""" Turn on screen"""
	d.screen.on()

def sleep_mode():
	"""Sleep the device"""
	d.sleep()

def vol_up():
	"""Turn up volume"""
	d.volume_up()

def vol_down():
	"""Turn down volume"""
	d.volume_down()

def vol_mute():
	"""Turn volumn into mute"""
	d.volume_mute()

#system btn
def press_back():
	"""Press Back"""
	d.press.back()

def press_home():
	"""Press Home"""
	d.press.home()

def press_recent():
	"""Press Recent"""
	d.press.recent()

#notification
def open_notification():
	"""Open notification"""
	d.open.notification()

def quick_settings():
	"""Open quick settings"""
	d.open.notification()
	d.open.quick_settings()

def shortcut_settings():
	quick_settings
	d.click(resourceId="com.android.systemui:id/settings_button")
#wait
def wait_until_txt(txt,TIMEOUT=15):
	"""Wait until the ui object appears or the given timeout expires.

	Example:
	| wait until txt | Settings | 15000 | 
	"""
	TIMEOUT=int(TIMEOUT)
	if d(text=txt).wait.exists(timeout=TIMEOUT):
		flag(True,txt)
	else:
		flag(False,txt)

def wait_until_txt_gone(txt,TIMEOUT=15):
	"""Wait until the ui object gone or the given timeout expires.

	Example:
	| wait until txt gone | Settings | 15000 | 
	"""
	TIMEOUT=int(TIMEOUT)
	d(text=txt).wait.gone(timeout=TIMEOUT)

def wait_until_window_idle():
	"""Wait for current window to idle"""
	d.wait.idle()

def wait_until_window_update():
	"""Wait until window update event occurs"""
	d.wait.update()

def wait_until_contain_txt(txt,TIMEOUT=15):
	"""Wait until page contain Text or the given timeout expires."""
	TIMEOUT=int(TIMEOUT)
	if d(textContains=txt).wait.exists(timeout=TIMEOUT):
		flag(True,txt)
	else:
		flag(False,txt)

def wait_until_contain_txt_rscid(txt,rscId,TIMEOUT=15):
	"""Wait until page contain Text or the given timeout expires."""
	TIMEOUT=int(TIMEOUT)
	if d(textContains=txt,resourceId=rscId).wait.exists(timeout=TIMEOUT):
		flag(True,txt)
	else:
		flag(False,txt)

def wait_until_contain_rscid(rscId,TIMEOUT=15):
	"""Wait until page contain RscId or the given timeout expires."""
	TIMEOUT=int(TIMEOUT)
	if d(resourceId=rscId).wait.exists(timeout=TIMEOUT):
		flag(True,rscId)
	else:
		flag(False,rscId)

def wait_until_right_contain_txt_className(txt,className,TIMEOUT=15):
	"""Wait until page contain the className's object that in the right side of txt or the given timeout expires."""
	TIMEOUT=int(TIMEOUT)
	if d(text=txt).right(className=className).wait.exists(timeout=TIMEOUT):
		flag(True,txt)
	else:
		flag(False,txt)

#rotation

def rotate_left():
	"""Rotate left"""
	d.orientation = "l" # "left"
	rotate_info()

def rotate_right():
	"""Rotate right"""
	d.orientation = "r" # "right"
	rotate_info()

# def rotate_upsidedown():
# 	d.orientation = "upsidedown" # "upsidedown"
# 	rotate_info()

def rotate_auto():
	"""Set to Auto-rotate"""
	d.orientation = "n" # "natural"
	rotate_info()

def rotate_freeze():
	"""Set to freeze rotation"""
	d.freeze_rotation()
	rotate_info()

def rotate_unfreeze():
	"""Set to un-freeze rotation"""
	d.freeze_rotation(False)

def rotate_info():
	"""Display rotation information"""
	print 'Rotation info: ' + (d.orientation)

def reset():
	pass

def reboot():
	command_line='adb reboot'
	f = os.popen(command_line)
	f = f.read() 
	print f


def launch():
	pass

#input 
def input_txt(rscId,txt):	
	"""Set Text of editable field. 

	Example:
	| input txt | com.android.settings:id/password | 88888888 | #Type in passwords "88888888" at the given id field |
	"""
	if d(resourceId=rscId).exists:
		d(resourceId=rscId).set_text(txt)

def get_txt_by_rscId(rscId):
	"""Get Text of editable field. 

	Example:
	| input | com.android.settings:id/password | #get text by the given id field |
	"""
	if d(resourceId=rscId).exists:
		return d(resourceId=rscId).text

def get_txt_by_index_rscId(index,rscId):
	"""Get Text of editable field. 

	Example:
	| input | com.android.settings:id/password | #get text by the given id field |
	"""
	if d(resourceId=rscId)[int(index)].exists:
		return d(resourceId=rscId)[int(index)].text

def power():
	"""Press Power"""
	d.press.power();

def cwd():
	cwd = os.getcwd()
	print "===current working path==="+cwd
	return cwd

def get_lang():
	command_line='adb shell getprop persist.sys.language'
	f = os.popen(command_line)
	f = f.read() 
	return f

def get_locale():
	command_line='adb shell getprop persist.sys.country'
	f = os.popen(command_line)
	f = f.read() 
	return f

def i18n_detector():
	cwd = os.getcwd()
	print cwd
	current_i18n_dir = os.path.abspath(os.path.join(cwd, os.pardir))+'/lib/i18n/'
	lan=get_lang().rstrip()+"_"+get_locale()
	lang=lan.rstrip()
	if lang == "zh_TW":
		BuiltIn().import_variables(current_i18n_dir+"tw.py")
		print "System language info: "+lang
	elif lang == "zh_CN":
		BuiltIn().import_variables(current_i18n_dir+"cn.py")
		print "System language info: "+lang
	elif lang == "zh_HK":
		BuiltIn().import_variables(current_i18n_dir+"hk.py")
		print "System language info: "+lang
	elif lang == "en_US":
		BuiltIn().import_variables(current_i18n_dir+"en.py")
		print "System language info: "+lang
	elif lang == "zh_UK":
		BuiltIn().import_variables(current_i18n_dir+"uk.py")
		print "System language info: "+lang

