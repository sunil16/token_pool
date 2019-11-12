from util import common
import json

class CachePool(object):
    """Cache Class for handling pool of tokens ."""

    def __init__(self, redis_conn = None):
        self.available_tokens_cache = 'available_tokens'
        self.unavailable_tokens = 'unavailable_tokens'
        self.redis_conn = redis_conn
        self.waiting_token = None

    def seeding_tokens_to_cache(self, tokens = None): # seeding prefetched tokens into cache
        for token in tokens:
            self.set_token(self.available_tokens_cache, token)
        self.redis_conn.ltrim(self.available_tokens_cache,0,50) # fixed size cache (50 items)

    def get_available_token(self): # getting available token from cache
        token = self.get_token(self.available_tokens_cache)
        if self.is_token_available(token):
           self.update_token_stats(token)
           return token['token']
        return None

    def update_token_stats(self, token): #updating token stats
        token['counter'] = token['counter'] + 1
        token['isAvailable'] = False
        token['last_inactive_date_time'] = str(common.get_today_datetime())
        self.set_token(self.unavailable_tokens, token)

    def is_token_expired(self):
        if self.size_of_unavailable_tokens() and self.waiting_token == None:
            self.waiting_token = self.get_token(self.unavailable_tokens)
        if self.waiting_token and (int(common.diff_with_today_times_secounds(self.waiting_token['last_inactive_date_time'])) >= 5 ):
            self.waiting_token['last_active_date_time'] = str(common.get_today_datetime())
            self.waiting_token['isAvailable'] = True
            self.set_token(self.available_tokens_cache, self.waiting_token)
            self.waiting_token = None

    def set_token(self,cache_name = None, token = None):
        self.redis_conn.lpush(cache_name, common.to_string(token))

    def get_token(self, cache_name = None):
        return common.to_dict(self.redis_conn.rpop(cache_name))

    def size_of_unavailable_tokens(self):
        return True if len(self.redis_conn.lrange(self.unavailable_tokens, 0, 0)) else False

    def get_all_tokens(self, cache_name = None):
        return self.redis_conn.lrange(cache_name,0,-1)

    def is_token_available(self, token = None):
        return token if token['isAvailable'] else None

    def get_stats(self):
        token_stats = {}
        token_stats['available_tokens'] =  common.to_dict_colletion(self.get_all_tokens(self.available_tokens_cache))
        token_stats['unavailable_tokens'] = common.to_dict_colletion(self.get_all_tokens(self.unavailable_tokens))
        return token_stats

if __name__ == '__main__':
    print("Cache Pooling Handler Class, pass argument redis_conn to create instance")
