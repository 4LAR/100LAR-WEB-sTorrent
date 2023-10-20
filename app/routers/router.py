from fastapi import APIRouter
from .get_info import *

router = APIRouter()

router.add_api_route(
    "/get_info",
    get_info,
    methods=['GET'],
    tags=['Torrent'],
    description=""
)
