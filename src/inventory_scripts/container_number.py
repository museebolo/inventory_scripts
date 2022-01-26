# ----------------------------------------------------------------------------------------------------------------------
# container_number.py - Musée Bolo (c) - C. Gaudin
# ----------------------------------------------------------------------------------------------------------------------
# B-0000 -> Box
# P-0000 -> Pallet

import re

def is_valid_container_number(value: str) -> bool:
    return __get_match(value) is not None

def get_kind_and_number(container_number: str) -> (str, int):
    match = __get_match(container_number)
    if match is not None:
        return str(match.group(1)), int(match.group(2))
    else:
        return None, None

def __get_match(value: str) -> re.Match:
    # TODO compile cette regex
    return re.search(r'^([PB]{1})-([0-9]{4})$', value)

def build_container_number(kind: str, num: int) -> str:
    return "{:1s}-{:04d}".format(kind, num)
