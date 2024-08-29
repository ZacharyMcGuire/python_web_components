#!/bin/bash
set -e

echo "Running Alembic Upgrade"
alembic upgrade head

echo "Starting FastAPI server"
exec uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
