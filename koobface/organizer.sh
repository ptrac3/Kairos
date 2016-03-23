#! /bin/bash

file_list=$(ls ./dat/*.dat | gshuf > file_list.txt)
number=$(cat file_list.txt |wc -l)
training=`expr $number \* 70 / 100`
echo $training
traininglist=$(cat file_list.txt | head -n "$training" > training.txt)
test=$((number-training))
echo $test
testlist=$(cat file_list.txt | tail -n "$test" > test.txt)

for file in $(cat training.txt)
do echo "training" $file; cp "$file" ./training/
done 

for file in $(cat test.txt)
do echo "test"  $file; cp "$file" ./test/
done 

