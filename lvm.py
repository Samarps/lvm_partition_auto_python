# Load required modules
import os
import subprocess as sp


def text(c):
	code = "tput setaf " + c
	os.system(code)

# Code for LVM:

def lvm():
	os.system("clear")
	text("2")
	print("\n\t\t\t\tMenu Program: LVM (Logical Volume Management)\n")
	print("\t\t\t\t````````````````````````````````````````````\n")
	text("7")
	print("\tYou can either type option no. OR can ask in normal human readable English Language :)\n")
	text("3")
	print("1. View all the Block Storage/HD")
	print("2. Create Physical Volume (PV) from a HardDisk")
	print("3. View details of a Physical Volume (PV)")
	print("4. Create Volume Group (VG) from PVs")
	print("5. View details of an existing Volume Group (VG)")
	print("6. Create a Logical Volume (LV) in a VG")
	print("7. View details of Logical Volume (LV)")
	print("8. Extend a Logical Volume (LV)")
	print("9. Extend a Volume Group (VG)")
	print("-> Close/Exit the program\n")
	text("7")

def lvm_1():
	print("")
	os.system("lsblk")

def lvm_2():
	text("6")
	print("\nPV is created from a HardDisk, you can find HD name from the option 1, they are named sdb, sdc, sde, etc\n")
	text("7")
	block = input("Enter HardDisk name: ").lower()
	z = "y"
	while z == "y":
		block = input("\nEnter PV name: ").lower()
		os.system("pvcreate /dev/{}".format(block))
		z = input("Enter 'y' to add more PV, otherwise press ENTER: ").lower()
	lvm()
	text("2")
	print("\nYour Physical Volume (PV) were created Successfully!")
	text("7")

def lvm_3():
	text("6")
	print("\nPV and HardDisk (HD) names are same, you can find HD name from the option 1, they are named sdb, sdc, sde, etc\n")
	text("7")
	block = input("Enter PV name: ").lower()
	lvm()
	text("2")
	os.system("pvdisplay /dev/{}".format(block))
	text("7")

def lvm_4():
	vgname = input("\nName your Volume Group (VG): ")
	text("6")
	print("\nTo create you require one or more Physical Volume (PV)")
	text("7")
	print("You can find PV or HardDisk name from the option 1, they are named generally as sdb, sdc, sde, etc")
	z = "y"
	a = []
	pvs = ""
	while z == "y":
		block = input("\nEnter PV name: ").lower()
		os.system("pvcreate /dev/{}".format(block))
		a.append(block)
		z = input("Enter 'y' to add more PV, otherwise press ENTER: ").lower()
	for i in a:
		pvs = pvs + " /dev/" + i
	os.system("vgcreate {} {}".format(vgname, pvs))
	lvm()
	text("2")
	print("\nYour Volume Group is created!")
	text("7")

def lvm_5():
	vgname = input("\nEnter name of your Volume Group (VG): ")
	lvm()
	text("2")
	os.system("vgdisplay {}".format(vgname))
	text("7")

def lvm_6():
	text("6")
	print("\nYou have to provide name & size of Logical Volume (LV) like 5G, 10G, etc")
	text("7")
	vgname = input("\nEnter name of your Volume Group (VG): ")
	lvname = input("\nEnter LV name: ")
	lvsize = input("Enter LV size: ").upper()
	os.system("lvcreate --size {} --name {} {}".format(lvsize, lvname, vgname))
	os.system("mkfs.ext4 /dev/{}/{}".format(vgname, lvname))
	lvm()
	text("2")
	print("\nYour Logical Volume is Created & Formatted!")
	text("7")

def lvm_7():
	vgname = input("\nEnter name of your Volume Group (VG): ")
	lvname = input("Enter name of you Logical Volume (LV): ")
	lvm()
	text("2")
	os.system("lvdisplay {}/{}".format(vgname, lvname))
	text("7")

def lvm_8():
	vgname = input("\nEnter name of your Volume Group (VG): ")
	lvname = input("Enter name of you Logical Volume (LV): ")
	addsize = input("Enter extend size for LV (like 2G, 4G, etc): ").upper()
	os.system("lvextend --size {} /dev/{}/{}".format(addsize, vgname, lvname))
	lvm()
	text("2")
	print("Your LV size extended by {} Successfully!".format(addsize))
	text("7")

def lvm_9():
	text("6")
	print("\nWe will add new Physical Volume (PV) to an existing Volume Group (VG), OR Extend VG")
	text("3")
	print("\nYou can find PV (or HD) name from the option 1, they are named as sdb, sdc, sde, etc")
	text("7")
	vgname = input("\nEnter name of VG: ")
	pvname = input("Enter PV name (to be added into VG): ").lower()
	os.system("vgextend {} /dev/{}".format(vgname, pvname))
	lvm()
	text("2")
	print("Your VG Extended Successfully!")
	text("7")
