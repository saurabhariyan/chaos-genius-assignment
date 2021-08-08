## Aim: 
    find most_frequent_500(start_time, end_time) in a stream of data. 
    smallest timedelta : 1 day 
    given the data size, hashmap solution is not feasible. 

    Assumption: Not optimising for aws service (loadbalancers) or by managing servers (hashmap with multiple hosts/partitions)

## Thinking:
    1. not feasible to store the data 
        a. solution should be sublinear space (bloom filters?)
        b. should consider probablistic solution 
    2. Given the data size (~petabytes)
        a. scalablity consideration 
        b. available (single point of failures : both in network and hardware)
    3. count min sketch (?) 
        a. bloom filter with counts

## Confession: 
    Heavily relied on google. limited knowledge on these limitations!
    
## Solution: 
    1. 