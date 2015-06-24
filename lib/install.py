#!/usr/bin/env python 
# -*- coding: utf-8 -*-
import sys
import os,commands,shlex
from subprocess import call
import time 

#def install(apk_dir_path='/home/jeremy/K_project/test_toos/install_dir'): 
#def install(apk_dir_path='/home/jueimei/au'): 
def install(apk_dir_path):

	device_list=[]

	#check usb plugin & can push or install
	command_line='adb devices'
	f = os.popen(command_line)
	f = f.read()

	Contain_str='Android Debug Bridge version'
	Contain_str2='devices attached'

	# setting error
	if Contain_str in f:
		print 'please check you devices setting'

	#devices list
	elif Contain_str2 in f:
		f=f.split('\n')
		i=1
		for i in range(2):
			f.pop()
		f.pop(0)

	#device number >2
	count_num=1
	if len(f)>1:
		print 'you devices count more two , please select number to do something...'
		for i in f:
			print "devices num:(%s)\t%s"%(count_num,i[:i.find('\t')])			
			count_num=count_num+1
			device_list.append(i[:i.find('\t')])
		x = raw_input(">>> Input devices number: ")
		if x==str(1):
			print 1
			command_line='export ANDROID_SERIAL=\''+device_list[0]+'\''
			f = os.popen(command_line)
		
		if x==str(2):
			print 2
			command_line='export ANDROID_SERIAL=\''+device_list[1]+'\''
			print command_line
			f = os.popen(command_line)

			command_line='export $ANDROID_SERIAL'
			f = os.popen(command_line).read()
			print f

	
	print 'install:'
	#push
	# command_line='pwd'
	# f = os.popen(command_line).read()
	# print f
	#command_line_apk='ls '+f[:f.find('\n')]+'/install_dir |grep apk'
	command_line_apk='ls '+apk_dir_path+' |grep apk'
	
	
	f = os.popen(command_line_apk).read()
	print f
	f_list=f.split('\n')
	f_list.pop()

	while(len(f_list)>0):
		command_line='adb install '+apk_dir_path+'/'+f_list.pop()
		f = os.popen(command_line).read()
		print f


#install(apk_dir_path)
# install('/home/jueimei/au/apk')


#if __name__ == "__main__": 
#	install(sys.argv[1])

