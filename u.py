import requests
import random
import os 
import sys
import time
#asayya edit Kay bas Nawe Xawanakay dabne 
#create by : LOST
#Xom encrypt nakrdua WA nazanm Nazanm Enc Kam hhhhh
def fb():
	lost="""

\033[91m.##........#######...######..########
\033[91m.##.......##.....##.##....##....##...
\033[91m.##.......##.....##.##..........##...
\033[33m.##.......##.....##..######.....##...
\033[92m.##.......##.....##.......##....##...
\033[92m.##.......##.....##.##....##....##...
\033[92m.########..#######...######.....##...
\033[94m
-------------------------------------------------------------------------------
Auther : LOST

Github : https://github.com/LoSt-SoFtware

YT        : LOST KURDISH
-------------------------------------------------------------------------------
	\033[97m
	"""
	os.system("clear")
	print(lost)
	filer=open("user.txt","r").readlines()
	for x in filer:
		u=x.strip()
		re = requests.get('https://www.facebook.com/{}'.format(u)).status_code
		if re==200:
			print("")
			print(u+" >= \033[1;31mHAYA \033[1;37m ")
		else:
			print("")
			print(u+" >= \033[1;32mNYA \033[1;37m")
		time.sleep(3)
	

##############


def insta():
	os.system("clear")
	
	lost="""
\033[91m.##........#######...######..########
\033[91m.##.......##.....##.##....##....##...
\033[91m.##.......##.....##.##..........##...
\033[33m.##.......##.....##..######.....##...
\033[92m.##.......##.....##.......##....##...
\033[92m.##.......##.....##.##....##....##...
\033[92m.########..#######...######.....##...
\033[94m
-------------------------------------------------------------------------------
Auther : LOST

Github : https://github.com/LoSt-SoFtware

YT        : LOST KURDISH
-------------------------------------------------------------------------------
	\033[97m
	"""
	
	print(lost)
	namee=open("user.txt","r").readlines()
	for x in namee:
		time.sleep(1)
		u=x.strip()
		re =requests.get('https://www.instagram.com/{}/'.format(u)).status_code
		if re==200:
			print("")
			print(u+ " >= \033[1;31mHAYA\033[1;37m")
		else:
			print("")
			print(u+ " >= \033[1;32mNYA\033[1;37m")

	
def user_maker():
	os.system("clear")
	lost="""
\033[91m.##........#######...######..########
\033[91m.##.......##.....##.##....##....##...
\033[91m.##.......##.....##.##..........##...
\033[33m.##.......##.....##..######.....##...
\033[92m.##.......##.....##.......##....##...
\033[92m.##.......##.....##.##....##....##...
\033[92m.########..#######...######.....##...
\033[94m
-------------------------------------------------------------------------------
Auther : LOST

Github : https://github.com/LoSt-SoFtware

YT        : LOST KURDISH
-------------------------------------------------------------------------------
	\033[97m
	"""
	print(lost)
	filer=open("user.txt","w")
	print("==================")
	print("")
	user=int(input("Chand Pet be :"))
	for x in range(300):
		text="qwertyuioplkjhgfdsazxcvbnm1234567i90-_."
		word=''.join(random.choice(text) for x in range(user))
		filer.write(word+"\n")
		
		print(word)
	time.sleep(3)
	print("")
	print("----------")
	print("")
	print("ALL USER SAVED IN FILE USER.TXT")
	time.sleep(3)




def minu():
	os.system("clear")
	print("------")
	print("\033[97m-----------")
	print(" Aro     =========")
	
	print("------")
	print("Aro -----------")
	print(" LOST          =========")
	print("")
	print("")
	print("")
	print("============lost_software===============")
	print("")
	
	print(" < 1 > henane username ")
	print("")
	print("-------")
	print("< 2 > fa7s krdne username instagram")
	print("")
	print("-------")
	print(" < 3 > fa7d krdne username facbook")
	print("")
	print('`````````````')
	print("")
	print("")
	lost=int(input(" Choice : "))
	if lost==1:
		os.system("clear")
		user_maker()
		minu()
	if lost==2:
		os.system("clear")
		insta()
		minu()
	if lost==3:
		os.system("clear")
		fb()
		minu()
	
	
minu()