from redis_setup import redis_conn
import tokens, cache_pool

def init_token_pool(app = None):
    redis_client = redis_conn.redisConnect(app.config['REDISTOGO_URL'])
    pool_service_instance = cache_pool.CachePool(redis_client)
    pool_service_instance.seeding_tokens_to_cache(tokens.getTokens(app.config['POOL_SIZE']))
    return pool_service_instance
