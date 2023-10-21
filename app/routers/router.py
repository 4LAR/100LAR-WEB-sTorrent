from fastapi import APIRouter
from .get_info import *
from .add_torrent import *
from .remove_torrent import *

router = APIRouter()

router.add_api_route(
    "/get_info",
    get_info,
    methods=['GET'],
    tags=['Torrent'],
    description=""
)

router.add_api_route(
    "/add_torrent",
    add_torrent,
    methods=['POST'],
    tags=['Torrent'],
    description=""
)

router.add_api_route(
    "/remove_torrent",
    remove_torrent,
    methods=['POST'],
    tags=['Torrent'],
    description=""
)
