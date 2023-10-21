
from globals import *

async def remove_torrent(id: int):
    torrent_controller.remove(id)

    return {"status": True}
