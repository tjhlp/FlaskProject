from redis import StrictRedis

redis_cli = StrictRedis(host='127.0.0.1', port=6381, decode_responses=True)
pl = redis_cli.pipeline()
pl.set('a', 200)
pl.set('b', 100)
pl.get('a')
pl.get('b')
ret = pl.execute()
print(ret)