#!/usr/bin/python

import redis

r=redis.Redis(host='localhost',password='redis2017',port=6379,db=0)

r.set('foo','bar')

print (r.get('foo'))