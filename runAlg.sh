#!/bin/bash

DPATH='datasets/'
SPATH=${DPATH}$2
#ORDER OF ARGUMENTS: 1. what algorithm 2. what size lists 3. do what? ('p' for print to cmd line, 'r' for record, anything else for neither
for i in $(ls ${SPATH})
do
	python $1 ${SPATH}${i} $3
done

echo 'Running "' $2 '" tests on ' $1 ' algorithm with "' $3 '" argument.'
