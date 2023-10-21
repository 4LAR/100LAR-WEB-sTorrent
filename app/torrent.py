import libtorrent as lt
import time
import sys
import os
import threading

from globals import *
from config import config

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

    def add(file):
        ...

    def remove(self, id):
        ...

    def get(self, id):
        ...

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

        # self.download_thread = threading.Thread(target=self.thread_func)
        # self.download_thread.start()
        # self.s = None

    # def thread_func(self):
    #     while (not self.h.is_seed()):
    #         self.s = self.h.status()
    #         time.sleep(1)

    def get_status(self):
        if not self.h.is_seed():
            s = self.h.status()
            return {
                "name": self.h.name(),
                "progress": s.progress * 100,
                "download": s.download_rate,
                "up": s.upload_rate,
                "state": s.state
            }

        else:
            return {}

    def pause(self):
        ...

    def delete(self):
        ...
