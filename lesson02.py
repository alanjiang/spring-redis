#!/usr/bin/python

import redis 

pool = redis.ConnectionPool(host='localhost',password='redis2017',port=6379)

r = redis.Redis(connection_pool=pool)

r.set('name','Alan Jiang')

print(r.get('name'))