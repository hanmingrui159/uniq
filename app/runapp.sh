#!/bin/sh
export LC_ALL=C.UTF-8
export LANG=C.UTF-8
python3 -m uvicorn uniqueid_server:app --reload --host 0.0.0.0 --port 8105
