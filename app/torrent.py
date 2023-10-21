import libtorrent as lt
import time
import sys
import os
import shutil

from globals import *
from config import config

if len(config.get("Torrent")['outgoing_interfaces']) > 0:
    ses = lt.session({
        'outgoing_interfaces': config.get("Torrent")['outgoing_interfaces']
    })

else:
    ses = lt.session()
    
ses.listen_on(6881, 6891)

state_str = [
    'queued',
    'checking',
    'downloading metadata',
    'downloading',
    'finished',
    'seeding',
    'allocating',
    'checking fastresume'
]

class Torrent_Controller:
    def __init__(self):
        self.torrents = []

        for file in [file_name for file_name in os.listdir(config.get("Torrent")['cached_files_path']) if file_name.split(".")[-1] == "torrent"]:
            self.torrents.append(Download(config.get("Torrent")['cached_files_path'] + "/" + file))

    def add(self, file):
        torrent_file = config.get("Torrent")['cached_files_path'] + "/" + file
        for el in self.torrents:
            if torrent_file == el.file_name:
                return

        self.torrents.append(Download(torrent_file))

    def remove(self, id):
        os.remove(self.torrents[id].file_name)
        # shutil.rmtree(self.torrents[id].h.name())
        self.torrents.pop(id)

    def get(self, id):
        return self.torrents[id].get_status()

    def get_all(self):
        result = []
        for i, item in enumerate(self.torrents):
            result.append({
                "id": i,
                **item.get_status()
            })

        return result

class Download:
    def __init__(self, file):
        self.file_name = file
        self.info = lt.torrent_info(file)
        self.h = ses.add_torrent({'ti': self.info, 'save_path': config.get("Torrent")['save_path']})

    def get_status(self):
        if not self.h.is_seed():
            s = self.h.status()
            return {
                "name": self.h.name(),
                "progress": round(s.progress * 100, 1),
                "download": s.download_rate,
                "up": s.upload_rate,
                "state": s.state,
                "total_size": s.total_wanted
            }

        else:
            return {}

    def pause(self):
        ...

    def delete(self):
        ...
