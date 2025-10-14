# weather-berlin-mock
A small Python demo app that shows a **mock** weather snapshot for **Berlin**.
This repository is intended for learning/demo purposes (Ausbildung IT) and **does not use any external APIs**.

## Features
- No network required — mock-only.
- Multiple built-in scenarios (sunny, cloudy, rainy, windy).
- Random scenario by default; option to force a scenario via CLI.
- Great for screenshots, demo videos, and classroom tasks.

## Requirements

Python 3.7+

No external libraries required

## How to run
⚙️ How to Run

1 Download or clone the repository
2 Open terminal in project folder
3 Run default random weather snapshot:
python berlin_weather.py
4 Or force a scenario using CLI flags:
python berlin_weather.py --sunny
python berlin_weather.py --cloudy
python berlin_weather.py --rainy
python berlin_weather.py --windy

[Run 1](https://github.com/larabinada752-netizen/weather-berlin-mock/blob/055779f531e66958f3dff192ed85bdf3ae99148a/run_1.png.jpeg?raw=true)



## Example Output

[2025-10-14 14:32:10] Weather snapshot (MOCK)
City: Berlin
Temperature: 19.5°C
Weather: Broken clouds
Wind Speed: 3.0 m/s

##Tips
The weather data is mock only — no live API calls.

You can add new scenarios or adjust values in MOCK_SCENARIOS dictionary.

Useful for testing CLI applications or practicing Python scripting.
