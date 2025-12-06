#!/usr/bin/env bash
# Simple helper to run the app in background and then tests (Linux/Mac)
uvicorn app.main:app --port 8000 --host 127.0.0.1 &
APP_PID=$!
sleep 1
PYTHONPATH=$(pwd) pytest -q
kill $APP_PID
