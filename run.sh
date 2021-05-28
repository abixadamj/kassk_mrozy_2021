#!/bin/bash
set -e
APP=kassk_mrozy_2021
DIR=/srv/${APP}
LOG=/tmp/${APP}.log
LISTEN_IP=0.0.0.0

cd $DIR
. ./venv/bin/activate
pkill -9 uvicorn
nohup uvicorn main:app --reload --host ${LISTEN_IP} --port 5000 > $LOG &
