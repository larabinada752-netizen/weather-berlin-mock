# weather-berlin-mock
A small Python demo app that shows a **mock** weather snapshot for **Berlin**.
This repository is intended for learning/demo purposes (Ausbildung IT) and **does not use any external APIs**.

## Features
- No network required — mock-only.
- Multiple built-in scenarios (sunny, cloudy, rainy, windy).
- Random scenario by default; option to force a scenario via CLI.
- Great for screenshots, demo videos, and classroom tasks.

## Files
- `weather_berlin_mock.py` — main script (mock-only)
- `README.md` — this file

## Requirements
- Python 3.7+ (no external packages)

## How to run
```bash
python weather_berlin_mock.py        # run with random mock scenario
python weather_berlin_mock.py --rainy  # force rainy scenario
