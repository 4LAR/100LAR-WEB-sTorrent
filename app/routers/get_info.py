
from globals import *

async def get_info():
    return {"data": torrent_controller.get_all()}
