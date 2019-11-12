import redis

def redisConnect(redis_url):
    conn_redis = None
    try:
        conn_redis  = redis.from_url(redis_url)
        if conn_redis.ping():
            print('Redis connected %s' % (redis_url))
    except redis.ConnectionError as e:
        print('Redis Error: %s' % e)
    return conn_redis
