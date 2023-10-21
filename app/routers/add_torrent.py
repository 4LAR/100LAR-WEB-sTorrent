from fastapi import Depends, UploadFile, File
import shutil
import os

from globals import *
from config import config

async def add_torrent(file: UploadFile):
    if file.filename.split(".")[-1] != "torrent":
        return {"status": False}

    f = file.file
    f.seek(0, os.SEEK_SET)
    with open(config.get("Torrent")['cached_files_path'] + "/" + file.filename, "wb") as buffer:
        shutil.copyfileobj(f, buffer)

    torrent_controller.add(file.filename)

    return {"status": True}
