#!/bin/bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

function run {
$DIR/../cpp/bin/main/exponential_model_main  $FOLDER $N $H $r $s $p $q $MAX
}

N=100
H=6
p=0.005
q=0.001
r=0.01
s=0.018
MAX=1000


FOLDER=$DIR/../example/
mkdir -p $FOLDER

run
