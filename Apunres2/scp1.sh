#!/bin/bash

file=${1}
scp -P 2222 vagrant@127.0.0.1:/home/vagrant/${file}.tar .


