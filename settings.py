from decouple import config

MONGODB_HOST = config('MONGODB_PRIVATE_SRV')
MONGODB_DB_NAME = config('MONGODB_DB_NAME')
