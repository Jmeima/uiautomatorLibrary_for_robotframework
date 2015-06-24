__version__ = '0.1'
# !/usr/bin/python
# -*- coding: utf-8 -*-

import sys,time
import os,commands,shlex
from robot.libraries.BuiltIn import BuiltIn
from uiautomator import device as d

def flag(fg,msg):
	""" Pass/fail statement"""
	if fg==False:
		BuiltIn().run_keyword_if(fg==False,"Fail",'[Error Message] Cannot find "'+ msg + '"')
	elif fg==True:
		print '[Message] "'+ msg + '"'

###########gestures##############
#click
def click_txt(txt):
	"""Click on the given Text.

	Click on the center of the specific ui object.

	Example:
	| click txt | Settings |
	"""
	if d(text=txt).exists:
		d(text=txt).click()
		flag(True,txt)
	else:
		flag(False,txt)

def click_txt_rscId(txt,rscId):
	"""Click on the given Text and Resource Id.

	Click on the center of the specific ui object.

	Example:
	| click txt rscId | Settings | com.nokia.z:id/rowTextView |
	"""
	if d(text=txt,resourceId=rscId).exists:
		d(text=txt,resourceId=rscId).click()
		flag(True,txt)
	else:
		flag(False,txt)

def click_rscId(rscId):
	"""Click on the given Resource Id.

	Click on the center of the specific ui object.

	Example:
	| click rscId | com.nokia.z:id/rowTextView |
	"""
	if d(resourceId=rscId).exists:
		d(resourceId=rscId).click()
		flag(True,rscId)
	else:
		flag(False,rscId)

def click_txt_class(txt,className):
	"""Click on the given Text & ClassName.

	Click on the center of the specific ui object.

	Example:
	| click txt class|Settings |
	"""
	if d(text=txt,className=className).exists:
		d(text=txt,className=className).click()
		flag(True,txt)
	else:
		flag(False,txt)

def click_by_index_rscId(index,rscId):
	"""click on the given Resource Id and index.

	 click on the center of the specific ui object by index

	Example:
	| click by index rscId | 1 | com.nokia.z:id/rowTextView |
	"""

	if d(resourceId=rscId)[int(index)].exists:
		d(resourceId=rscId)[int(index)].click()
		flag(True,rscId)
	else:
		flag(False,rscId)

def long_click_txt(txt):
	"""Long click on the given Text.

	 Long click on the center of the specific ui object

	Example:
	| long click txt| skylight5G| android.widget.TextView |
	"""

	if d(text=txt).exists:
		d(text=txt).long_click()
		flag(True,txt)
	else:
		flag(False,txt)

def long_click_txt_rscId(txt,rscId):
	"""Long click on the given Text & Resource Id.

	 Long click on the center of the specific ui object

	Example:
	| long click txt rscId| OK | com.nokia.z:id/rowTextView  |
	"""

	if d(text=txt,resourceId=rscId).exists:
		d(text=txt,resourceId=rscId).long_click()
		flag(True,txt)
	else:
		flag(False,txt)

def long_click_rscId(rscId):
	"""Long click on the given Resource Id.

	 Long click on the center of the specific ui object

	Example:
	| long click rscId| com.nokia.z:id/rowTextView  |
	"""

	if d(resourceId=rscId).exists:
		d(resourceId=rscId).long_click()
		flag(True,rscId)
	else:
		flag(False,rscId)

def long_click_by_index_rscId(index,rscId):
	"""Long click on the given Resource Id and index.

	 Long click on the center of the specific ui object by index

	Example:
	| long click by index rscId | 1 | com.nokia.z:id/rowTextView |
	"""

	if d(resourceId=rscId)[int(index)].exists:
		d(resourceId=rscId)[int(index)].long_click()
		flag(True,rscId)
	else:
		flag(False,rscId)

#scroll
# # scroll backward vertically
def scroll_vert_forward():
	""" scroll forward vertically"""
	d(scrollable=True).scroll.vert.forward()

def scroll_vert_backward():
	""" scroll backward vertically"""
	d(scrollable=True).scroll.vert.backward()

def scroll_vert_toBeginning():
	"""scroll to Beginning vertically"""
	d(scrollable=True).scroll.toBeginning()


def scroll_vert_toEnd():
	"""scroll to end vertically"""
	d(scrollable=True).scroll.toEnd()

def scroll_horiz_forward():
	""" scroll forward horizentally"""
	d(scrollable=True).scroll.horiz.forward()

def scroll_horiz_backward():
	""" scroll backward horizentally"""
	d(scrollable=True).scroll.horiz.backward()

def scroll_horiz_toBeginning():
	"""scroll to beginning horizentally"""
	d(scrollable=True).scroll.horiz.toBeginning()

def scroll_horiz_toEnd():
	"""scroll to end horizentally"""
	d(scrollable=True).scroll.horiz.toEnd()

# scroll forward vertically until specific ui object appears
def  scroll_to_txt(txt):
	"""scroll forward vertically until specific ui object appears"""
	d(scrollable=True).scroll.to(text=txt)
	# if d(text=scroll_to_text).exists:
	# 	print "the text" + scroll_to_text + " exists"

#swipe
def swipe_left_rscId(rscId,timeout=50):
	"""Swipe left on the given Resource Id or the given timeout expires.

	Example:
	| swipe left rscId| com.nokia.z:id/secondTopMostLayout | 15000 | 
	"""
	if d(resourceId=rscId).wait.exists(timeout=timeout):
		d(resourceId=rscId).swipe.left()


def swipe_right_rscId(rscId,timeout=50):
	"""Swipe right on the given Resource Id or the given timeout expires.

	Example:
	| swipe right rscId| com.nokia.z:id/secondTopMostLayout | 15000 |
	"""
	if d(resourceId=rscId).wait.exists(timeout=timeout):
		d(resourceId=rscId).swipe.right()

def swipe_up_className(className,timeout=50):
	"""Swipe up on the given Resource Id or the given timeout expires.

	Example:
	| swipe up rscId| com.nokia.z:id/secondTopMostLayout | 15000 |
	"""
	if d(className=className).wait.exists(timeout=timeout):
		d(className=className).swipe.up()

def swipe_down_rscId(rscId,timeout=50):
	"""Swipe down on the given Resource Id or the given timeout expires.

	Example:
	| swipe down rscId| com.nokia.z:id/secondTopMostLayout | 15000 |
	"""
	if d(resourceId=rscId).wait.exists(timeout=timeout):
		d(resourceId=rscId).swipe.down()

#drag
def drag_txt1_to_txt2(txt1,txt2):
	"""Drag the ui object to another ui object (center).

	Example:
	| drag txt1 to txt2| txt1 | txt2 | #drag txt1 to txt2 | 
	"""
	d(text=txt1).drag.to(text=txt2, steps=50)

def drag_txt_to_xy(txt,x,y,steps=100):
	"""Drag the ui object to point (x, y).

	Example:
	| drag txt1 to xy| Music | 250 | 300 | 
	"""
	d(text=txt).drag.to(x, y, steps)

############Partial Behavior##################
def swipe_to_applist():
	"""[Z Launcher] Go to app list from Home screen by swiping left. """
	swipe_left_rscId("com.nokia.z:id/secondTopMostLayout")
	# swipe_up_className("android.widget.RelativeLayout")

#long click options
def longClick_AppInfo(txt):
	"""[Z Launcher] Long click app icon for App Info"""
	long_click_txt_rscId(txt,"com.nokia.z:id/rowTextView")
	click_txt_rscId("App Info","com.nokia.z:id/edit_actions")

def longClick_Hide(txt):
	"""[Z Launcher] Long click app icon for Hide"""
	long_click_txt_rscId(txt,"com.nokia.z:id/rowTextView")
	click_txt_rscId("Hide","com.nokia.z:id/edit_ranking")

def longClick_Uninstall_OK(txt):
	"""[Z Launcher] Long click app icon for Uninstall"""
	long_click_txt_rscId(txt,"com.nokia.z:id/rowTextView")
	click_txt_rscId("Uninstall","com.nokia.z:id/edit_actions")
	click_txt_rscId("OK","android:id/button1")
	
def longClick_Uninstall_Cancel(txt):
	"""[Z Launcher] Long click app icon for canceal uninstall"""
	long_click_txt_rscId(txt,"com.nokia.z:id/rowTextView")
	click_txt_rscId("Uninstall","com.nokia.z:id/edit_actions")
	click_txt_rscId("Cancel","android:id/button2")

# def click_Settings():
# 	if d(text='Settings',resourceId="com.nokia.z:id/rowTextView").exists:
# 		d(text='Settings',resourceId="com.nokia.z:id/rowTextView").click()

