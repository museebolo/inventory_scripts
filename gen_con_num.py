#!/usr/bin/python3
# ----------------------------------------------------------------------------------------------------------------------
# gen_con_num.py - Musée Bolo (c) by C. Gaudin - Generate Container Number
# ----------------------------------------------------------------------------------------------------------------------
import sys
from src.inventory_scripts import container_number

def usage():
    print("usage: gen_con_num.py <start_con_num> <page_count>")
    sys.exit()

if __name__ == "__main__":
    if len(sys.argv) <= 2:
        usage()

    start_inv_num = sys.argv[1]

    con_kind, con_num = container_number.get_kind_and_number(start_inv_num)
    if con_num is None:
        print("invalid container number !")
        sys.exit()

    page_count = int(sys.argv[2])

    for i in range(page_count*84):
        num = container_number.build_container_number(con_kind, con_num + i)
        print("{}".format(num))
