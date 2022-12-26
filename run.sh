#!/bin/sh
rm content/*
python bot.py > /dev/null
npm run dev  --prefix frontend
echo script running
