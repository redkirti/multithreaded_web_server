#!/bin/bash
echo "Load Throughput RT" >> results.csv
for i in {1..10}
do
    load="$load + 200"
    l=$((load))
    echo $l
    taskset -c 4-7 ./load_gen localhost 8080 $l 0.1 60
done