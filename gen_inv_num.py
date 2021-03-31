#!/usr/bin/python3
#-----------------------------------------------------------------------------------------------------------------------
# gen_inv_num.py - Musée Bolo (c) by C. Gaudin - Generate Inventory Number 
#-----------------------------------------------------------------------------------------------------------------------
import sys
import re
import math

def build_inventory_number(year, num):
	return "{:04d}-{:03d}-{:03d}".format(year, math.floor(num/1000), (num%1000))

def usage():
	print("usage: gen_inv_num.py <start_inv_num> <page_count>")
	sys.exit()

if __name__ == "__main__":
	if len(sys.argv)<=2:
		usage()

	start_inv_num = sys.argv[1]
	m = re.search('^(\d{4})-(\d{3})-(\d{3})$', start_inv_num);
	if m == None:
		print("invalid inventory number !")
		sys.exit()
	inv_year = int(m.group(1))
	inv_num  = int(m.group(2))*1000 + int(m.group(3))
	page_count = int(sys.argv[2])
	
	for i in range(page_count*84):
		num = build_inventory_number(inv_year, inv_num+i)
		print("{}".format(num))

