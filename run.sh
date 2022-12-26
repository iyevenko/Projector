#!/bin/sh
conda activate discord
rm content/*
python bot.py > /dev/null
cd frontend
npm run dev
echo script running
