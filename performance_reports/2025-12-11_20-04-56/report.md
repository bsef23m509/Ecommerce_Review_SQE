# Performance Test Report

**Generated:** Thu Dec 11 08:04:57 PM PKT 2025

---

## GET /api/products

Command:
`ab -n 100 -c 10 http://localhost:8000/api/products`

### Results
```
This is ApacheBench, Version 2.3 <$Revision: 1923142 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        uvicorn
Server Hostname:        localhost
Server Port:            8000

Document Path:          /api/products
Document Length:        3025 bytes

Concurrency Level:      10
Time taken for tests:   0.114 seconds
Complete requests:      100
Failed requests:        0
Total transferred:      315200 bytes
HTML transferred:       302500 bytes
Requests per second:    874.25 [#/sec] (mean)
Time per request:       11.438 [ms] (mean)
Time per request:       1.144 [ms] (mean, across all concurrent requests)
Transfer rate:          2691.05 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.1      0       0
Processing:     4   10   3.6      9      23
Waiting:        4   10   3.6      9      22
Total:          4   10   3.6      9      23

Percentage of the requests served within a certain time (ms)
  50%      9
  66%     11
  75%     11
  80%     12
  90%     16
  95%     19
  98%     23
  99%     23
 100%     23 (longest request)
```

---

## GET /api/products/1

Command:
`ab -n 100 -c 10 http://localhost:8000/api/products/1`

### Results
```
This is ApacheBench, Version 2.3 <$Revision: 1923142 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        uvicorn
Server Hostname:        localhost
Server Port:            8000

Document Path:          /api/products/1
Document Length:        2061 bytes

Concurrency Level:      10
Time taken for tests:   0.095 seconds
Complete requests:      100
Failed requests:        0
Total transferred:      218800 bytes
HTML transferred:       206100 bytes
Requests per second:    1056.68 [#/sec] (mean)
Time per request:       9.464 [ms] (mean)
Time per request:       0.946 [ms] (mean, across all concurrent requests)
Transfer rate:          2257.83 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.1      0       0
Processing:     2    9   2.5      9      15
Waiting:        2    9   2.4      9      15
Total:          2    9   2.5      9      15

Percentage of the requests served within a certain time (ms)
  50%      9
  66%     10
  75%     11
  80%     11
  90%     12
  95%     13
  98%     14
  99%     15
 100%     15 (longest request)
```

---

## POST /product/1/reviews

Command:
`ab -n 50 -c 5 -p /tmp/tmp.4oRUpwcU37 -T 'application/x-www-form-urlencoded' http://localhost:8000/product/1/reviews`

### Results
```
This is ApacheBench, Version 2.3 <$Revision: 1923142 $>
Copyright 1996 Adam Twiss, Zeus Technology Ltd, http://www.zeustech.net/
Licensed to The Apache Software Foundation, http://www.apache.org/

Benchmarking localhost (be patient).....done


Server Software:        uvicorn
Server Hostname:        localhost
Server Port:            8000

Document Path:          /product/1/reviews
Document Length:        0 bytes

Concurrency Level:      5
Time taken for tests:   0.086 seconds
Complete requests:      50
Failed requests:        0
Non-2xx responses:      50
Total transferred:      6050 bytes
Total body sent:        10100
HTML transferred:       0 bytes
Requests per second:    580.19 [#/sec] (mean)
Time per request:       8.618 [ms] (mean)
Time per request:       1.724 [ms] (mean, across all concurrent requests)
Transfer rate:          68.56 [Kbytes/sec] received
                        114.45 kb/s sent
                        183.01 kb/s total

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.0      0       0
Processing:     2    8   1.7      9      11
Waiting:        2    8   1.7      8      11
Total:          2    8   1.7      9      11

Percentage of the requests served within a certain time (ms)
  50%      9
  66%      9
  75%     10
  80%     10
  90%     10
  95%     10
  98%     11
  99%     11
 100%     11 (longest request)
```

---


---
**End of Report**
