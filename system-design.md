## most_frequent_500(start_time, end_time) in a stream of data.

## Constraint
    - smallest timedelta : 1 day
    - 3 dimensions in each subpopulation.
    - 10 different type of dimensions.
    - each dimension can take 10^5 values.
    - hashmap solution is not feasible.

## Assumption:
    Not looking for answers focusing on aws service (kafka, loadbalancers) or by managing servers (hashmap with multiple hosts/partitions)

## Thinking:
    1. not feasible to store the data
        a. solution should be sublinear space (bloom filters?)
        b. should consider probablistic solution
    2. Given the data size (~petabytes)
        a. scalablity consideration
        b. available (single point of failures : both in network and hardware)
## Confession:
    Heavily relied on google. limited knowledge on these limitations!

## Solution:
    1. count-min-sketch(buckets, hash_functions):
        a. buckets = number of dimensions = 10
        b. hash_functions = 2 (minimum)
        c. 2d array[bucket][hash_fuction] with all values initialized to 0
        d. support methods inc(x) and count(x)
        e. inc(x)
                for i in buckets:
                    CMS[i][hash_fucntion[i]] +=1
        f. count(x) returns the number of times inc(x) has been called.
        g. count(x) can be implemented in a different 2d array with index matching.
        h. collisions in hash values can overestimate the count.
        i. we can increase the bucket size to 10^6 (1MB) to reduces this error.
    . scalablity: computations mentioned above can parallelize easliy