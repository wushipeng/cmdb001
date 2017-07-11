import redis

r = redis.StrictRedis(host="localhost", port=6379)

p = r.pubsub()
# p.subscribe("eeee")
# p.psubscribe("excelFile")
# a = p.get_message()
# print(p.listen())
for p in p.listen():
    print(p)

# print(a)

# pool=redis.ConnectionPool(host='127.0.0.1',port=6379)
# r = redis.StrictRedis(connection_pool=pool)
# p = r.pubsub()
# p.subscribe('excelFile')
#
# print(r.get("channel"))