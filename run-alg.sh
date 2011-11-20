#!/bin/bash

#ORDER OF ARGUMENTS: 1. what algorithm 2. what size lists 3. do what? ('p' for print to cmd line, 'r' for record, anything else for neither
for i in $(ls $2)
do
	for j in {1..2}
	do
		python $1 $i $3
	done	
done

echo 'Running "' $2 '" tests on ' $1 ' algorithm with "' $3 '" argument.'
