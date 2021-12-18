#!/usr/bin/env python3

import os
import uuid


def rename_files():
    for filename in os.listdir("./folder"):
        ext = os.path.splitext(filename)[1]
        if ext == ".txt":
            continue
        id = uuid.uuid5(uuid.NAMESPACE_OID, filename)
        os.rename(f"./folder/{filename}", f"./folder/{id}{ext}")


rename_files()
