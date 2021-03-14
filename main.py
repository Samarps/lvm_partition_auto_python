import os
import subprocess as sp
import getpass
import lvm
from lvm import *


while True:
	lvm()
	y = input("Tell me what I can do for you: ").lower()
	if (("view" in y) and (("volume" in y) or ("storage" in y) or ("block" in y) or ("harddisk" in y) or ("hd" in y)) or ("1" in y)):
		lvm_1()
	elif (("create") and (("physical" in y) or ("pv" in y)) or ("2" in y)):
		lvm_2()
	elif ((("view" in y) or ("detail" in y)) and (("pv" in y) or ("physical" in y)) or ("3" in y)):
		lvm_3()
	elif (("create" in y) and (("group" in y) or "vg" in y) or ("4" in y)):
		lvm_4()
	elif ((("view" in y) or ("detail" in y)) and (("vg" in y) or ("group" in y)) or ("5" in y)):
		lvm_5()
	elif (("create" in y) and (("logical" in y) or "lv" in y) or ("6" in y)):
		lvm_6()
	elif ((("view" in y) or ("detail" in y)) and (("lv" in y) or ("logical" in y)) or ("7" in y)):
		lvm_7()
	elif (("extend" in y) and (("logical" in y) or ("lv" in y)) or ("8" in y)):
		lvm_8()
	elif (("extend" in y) and (("group" in y) or ("vg" in y)) or ("9" in y)):
		lvm_9()
	elif (("exit" in y) or ("close" in y)):
		text("2")
		print("\nThankyou! Meet you next time :)\n")
		text("7")
		break
	else:
		print("\nI can't understand you! Seems like a wrong input")

	text("6")
	input("\nPress ENTER to Continue...")
	text("7")
	
