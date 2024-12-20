#!/bin/sh

gunicorn -b 0.0.0.0 bot:app --access-logfile '-' --error-logfile '-'
