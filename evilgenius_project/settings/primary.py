from local_settings import GONDOR_REDIS_HOST, GONDOR_REDIS_PORT, GONDOR_REDIS_PASSWORD

CACHES = {
    "default": {
        "BACKEND": "redis_cache.RedisCache",
        "LOCATION": "%s:%s" % (GONDOR_REDIS_HOST, GONDOR_REDIS_PORT),
        "OPTIONS": {
            "DB": 1,
            "PASSWORD": GONDOR_REDIS_PASSWORD,
        },
    },
}