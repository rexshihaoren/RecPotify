import json
from app import celery
from app import redis

@celery.task()
def dump_tracks(tracks):
    redis.setnx('tracks', 0)
    redis.expire('tracks',120)
    redis.append('tracks', pickle.dumps(tracks))


