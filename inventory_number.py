# ----------------------------------------------------------------------------------------------------------------------
# gen_inv_num.py - Musée Bolo (c) by C. Gaudin
# ----------------------------------------------------------------------------------------------------------------------
import re
import datetime
import math


def is_valid_inventory_number(value: str) -> bool:
    return __get_match(value) is not None


def is_valid_inv_number_and_year(value: str) -> bool:
    inventory_pattern = __get_match(value)
    if inventory_pattern is None:
        return False
    year = int(inventory_pattern.group(1))
    return datetime.date.today().year >= year >= 2020


def get_year_and_number(inventory_number: str) -> (int, int):
    match = __get_match(inventory_number)
    if match is not None:
        return int(match.group(1)), int(match.group(3)) + int(match.group(2)) * 1000
    else:
        return None, None


def __get_match(value: str) -> re.Match:
    # TODO compile cette regex
    inventory_pattern = re.search(r'^([2-9][0-9]{3})-([0-9]{3})-([0-9]{3})$', value)
    return inventory_pattern


def build_inventory_number(year: int, num: int) -> str:
    return "{:04d}-{:03d}-{:03d}".format(year, math.floor(num / 1000), (num % 1000))
