#!/bin/sh
# Start up for development and test environment
if [ -z "$@" ]; then
  python3 -m venv /venv
  . /venv/bin/activate
  python3 -m pip install --upgrade pip
  pip install -r requirements.txt
  echo "Ready"
  tail -f /dev/null
else
  exec "$@"
fi
