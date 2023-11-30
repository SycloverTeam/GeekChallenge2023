#!/bin/sh
echo $GZCTF_FLAG>>/app/fl4gfl4gfl4g

export GZCTF_FLAG=not_flag
GZCTF_FLAG=not_flag

python /app/hello/ssti/app.py
