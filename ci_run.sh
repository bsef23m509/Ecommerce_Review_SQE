#!/usr/bin/env bash
source .venv/bin/activate

uvicorn app.main:app --port 8000 --host 127.0.0.1 &
APP_PID=$!
sleep 1
PYTHONPATH=$(pwd) pytest -q --html=test_reports/report.html
kill $APP_PID
