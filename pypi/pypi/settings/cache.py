from .base import DEBUG
from .config import CACHE_DIR, CACHE_NUM, CACHE_TIMEOUT
import os

# if DEBUG:
#     CACHES = {
#         'default': {
#             'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
#             'LOCATION': 'unique-snowflake',
#         }
#     }
# else:
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(CACHE_DIR, 'pypi.cache'),
        'TIMEOUT': CACHE_TIMEOUT,  # 过期时间，单位为秒
        'OPTIONS': {
            'MAX_ENTRIES': CACHE_NUM  # 最大缓存数，当缓存的数量超过后删除旧的缓存
        }
    }
}
