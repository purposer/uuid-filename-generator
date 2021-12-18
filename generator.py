#!/usr/bin/env python3

import os
import uuid


def rename_files():
    for filename in os.listdir("./folder"):
        ext = os.path.splitext(filename)[1]
        if ext == ".txt":
            continue
        os.rename(f"./folder/{filename}", f"./folder/{uuid.uuid4()}{ext}")


rename_files()
