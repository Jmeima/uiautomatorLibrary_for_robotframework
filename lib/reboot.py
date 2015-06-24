# -*- coding: utf-8 -*-

from uiautomator import device as d
import time,os,sys
from threading import Thread

SN=sys.argv[1]

TIMEOUT=3000

def Rest():
	if d(text="设置").wait.exists(timeout=TIMEOUT):
		d(text="设置").click()

		if d(scrollable=True).scroll.to(text="备份和重置"):
			d(text="备份和重置").click()

			if d(text="恢复出厂设置").wait.exists(timeout=TIMEOUT):
				d(text="恢复出厂设置").click()

				if d(text="恢复平板电脑出厂设置").wait.exists(timeout=TIMEOUT):
					d(text="恢复平板电脑出厂设置").click()

					if d(text="清除全部内容").wait.exists(timeout=TIMEOUT):
						d(text="清除全部内容").click()

def Start_RPC_Server():
	
	command_line='sh Start_Server.sh > /dev/null'
	f = os.popen(command_line).read()
	print f
	return True

def Check_Device():
	
	command_line='adb devices | grep ' + SN + ' | awk -F " " \'{print $2}\''
	
	f = os.popen(command_line).read()						
	f = f.replace("\n", "")
	
	if f == "device":
		return True
	else:
		return False

def launcher():
	d.screen.on()
	d.press("home")
	d.press("menu")
	print 123

	if d(resourceId='com.nokia.z:id/tos_button').wait.exists(timeout=TIMEOUT):
		d(resourceId='com.nokia.z:id/tos_button').click()

		if d(text='跳过教程').wait.exists(timeout=TIMEOUT):
			d(text='跳过教程').click()

			if d(text='确定').wait.exists(timeout=TIMEOUT):
				d(text='确定').click()


def launcher_Camera():

	if d(resourceId="com.nokia.z:id/secondTopMostLayout").wait.exists(timeout=TIMEOUT):
		d(resourceId="com.nokia.z:id/secondTopMostLayout").swipe.left()

		if d(className="android.widget.RelativeLayout").wait.exists(timeout=TIMEOUT):
			d(className="android.widget.RelativeLayout").swipe.up()

		if d(text="相机",resourceId='com.nokia.z:id/rowTextView').wait.exists(timeout=TIMEOUT):
			d(text="相机",resourceId='com.nokia.z:id/rowTextView').click()
		else:
			print 'can not find Camera'
			command_line='echo "can not find Camera" >> fail.log'
			f = os.popen(command_line).read()

def take_photo():


	if d(resourceId='com.android.camera2:id/shutter_button').wait.exists(timeout=TIMEOUT):
		d(resourceId='com.android.camera2:id/shutter_button').click()

def Check_Camera_Exist():


	command_line='adb logcat -d | grep "back camera found"'
	f = os.popen(command_line).read()

	return True
	# if len(f) != 0:
	# 	return True
	# else:
	# 	return False

def Check_Camera_function_icon_exist():
	if d(text="下一页").wait.exists(timeout=TIMEOUT):
		d(text="下一页").click()

	if d(resourceId="com.android.camera2:id/three_dots").wait.exists(timeout=TIMEOUT):
		d(resourceId="com.android.camera2:id/three_dots").click()

		if d(resourceId="com.android.camera2:id/camera_toggle_button").wait.exists(timeout=TIMEOUT):
			d(resourceId="com.android.camera2:id/camera_toggle_button").click()
		else:
			print 'can not find function icon'
			command_line='echo "can not find function icon" >> fail.log'
			f = os.popen(command_line).read()

	

#heck_Device() 
if __name__ == '__main__':
	thread = Thread(target = Start_RPC_Server())
	thread.start()

	COUNT_NUM = 500
	cnt = 0
	for cnt in range(COUNT_NUM):

		check_value=Check_Camera_Exist()
		if check_value :

			d.screen.on()
			d.press("menu")
			d.press("home")
			Rest()

			#print Check_Device()

			time.sleep(100)
			
			thread2 = Thread(target = Start_RPC_Server())
			thread2.start()
			
			while 1:
				if Check_Device() == True:
					break

			time.sleep(5)

			d.screen.on()
			d.press("menu")
			d.press("home")
			if d(resourceId='com.nokia.z:id/tos_button').wait.exists(timeout=10000000):
				launcher()
				take_photo()
			 	launcher_Camera()
				Check_Camera_function_icon_exist()
				d.press("home")
			print cnt
		else:
			command_line='echo "can not find Camera" >> fail.log'
			f = os.popen(command_line).read()




