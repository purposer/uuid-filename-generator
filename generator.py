#!/usr/bin/env python3

import os
import uuid


def rename_files():
    for filename in os.listdir("./img"):
        ext = os.path.splitext(filename)[1]
        if ext == ".txt":
            continue
        id = uuid.uuid5(uuid.NAMESPACE_OID, filename)
        os.rename(f"./img/{filename}", f"./img/{id}{ext}")


rename_files()
