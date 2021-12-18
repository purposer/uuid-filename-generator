#!/usr/bin/env python3

from random import randint
import os


def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)


def rename_files():
    for filename in os.listdir("./img"):
        ext = os.path.splitext(filename)[1]
        os.rename(f"./img/{filename}", f"./img/{random_with_N_digits(8)}{ext}")


rename_files()
