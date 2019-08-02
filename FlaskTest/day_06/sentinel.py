from redis.sentinel import Sentinel

redis_sentinel = [
    ("127.0.0.1", "26380"),
    ("127.0.0.1", "26381"),
    ("127.0.0.1", "26382"),
]

sentinel_name = 'mymaster'

sentinel_obj = Sentinel(redis_sentinel, decode_responses=True)

master_client = sentinel_obj.master_for(service_name=sentinel_name)

slave_client = sentinel_obj.slave_for(service_name=sentinel_name)

master_client.set('name','xiaoming')


name = slave_client.get('name')

print(name)


