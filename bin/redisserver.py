import redis
r = redis.StrictRedis(host="localhost", port=6379)

p = r.pubsub()
p.psubscribe("zheshidiyigechannel")
# a= p.get_message()
#
# print(a)
r.publish("sub","sdfsfa")
#
# pool=redis.ConnectionPool(host='127.0.0.1',port=6379)
# r = redis.StrictRedis(connection_pool=pool)
#
# r.publish('spub', "sdfsdf")
# r.set("channel","12312")