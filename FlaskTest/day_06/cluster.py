from rediscluster import StrictRedisCluster

startup_nodes = [
    {"host": "127.0.0.1", "port": "7000"},
    {"host": "127.0.0.1", "port": "7001"},
    {"host": "127.0.0.1", "port": "7002"},
]

cluster = StrictRedisCluster(startup_nodes=startup_nodes,decode_responses=True)


cluster.set('name','xiaoming')

print(cluster.get('name'))


