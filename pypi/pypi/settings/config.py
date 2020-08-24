from .base import config
import os

MIRROR = config.get('DJANGO', 'MIRROR')
CACHE_DIR = config.get('DJANGO', 'CACHE_DIR')
if not os.path.isdir(CACHE_DIR):
    os.makedirs(CACHE_DIR)
CACHE_NUM = config.get('DJANGO', 'CACHE_NUM', fallback=1000)
CACHE_TIMEOUT = config.get('DJANGO', 'CACHE_TIMEOUT', fallback=3600)
