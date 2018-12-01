import tor_requests

pool = tor_requests.SessionPool(5)
print(pool.ips())

for i in range(10):
    s = pool.next()
    print(s, s.ip())
    