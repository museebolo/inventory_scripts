#!/usr/bin/python3
# ----------------------------------------------------------------------------------------------------------------------
# gen_inv_num.py - Musée Bolo (c) by C. Gaudin - Generate Inventory Number 
# ----------------------------------------------------------------------------------------------------------------------
import sys
from src.inventory_scripts import inventory_number


def usage():
	print("usage: gen_inv_num.py <start_inv_num> <page_count>")
	sys.exit()


if __name__ == "__main__":
	if len(sys.argv) <= 2:
		usage()

	start_inv_num = sys.argv[1]

	inv_year, inv_num = inventory_number.get_year_and_number(start_inv_num)
	if inv_num is None:
		print("invalid inventory number !")
		sys.exit()

	page_count = int(sys.argv[2])

	for i in range(page_count*84):
		num = inventory_number.build_inventory_number(inv_year, inv_num + i)
		print("{}".format(num))

