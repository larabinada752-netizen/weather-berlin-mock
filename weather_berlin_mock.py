import argparse
import random
from datetime import datetime

CITY = "Berlin"

MOCK_SCENARIOS = {
    "sunny": {
        "temp": 25.0,
        "description": "clear sky",
        "wind": 2.1
    },
    "cloudy": {
        "temp": 19.5,
        "description": "broken clouds",
        "wind": 3.0
    },
    "rainy": {
        "temp": 16.2,
        "description": "light rain",
        "wind": 4.5
    },
    "windy": {
        "temp": 14.8,
        "description": "windy",
        "wind": 9.2
    }
}

def format_output(city: str, temp: float, desc: str, wind: float):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    output = (
        f"\n[{now}] Weather snapshot (MOCK)\n"
        f"City: {city}\n"
        f"Temperature: {temp:.1f}°C\n"
        f"Weather: {desc.capitalize()}\n"
        f"Wind Speed: {wind:.1f} m/s\n"
    )
    return output

def main(force: str | None = None):
    if force:
        scenario = force
        if scenario not in MOCK_SCENARIOS:
            print(f"Unknown scenario '{scenario}'. Available: {', '.join(MOCK_SCENARIOS)}")
            return
    else:
        scenario = random.choice(list(MOCK_SCENARIOS.keys()))

    data = MOCK_SCENARIOS[scenario]
    print(format_output(CITY, data["temp"], data["description"], data["wind"]))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Berlin Weather App (mock only)")
    parser.add_argument("--sunny", action="store_true", help="Force sunny scenario")
    parser.add_argument("--cloudy", action="store_true", help="Force cloudy scenario")
    parser.add_argument("--rainy", action="store_true", help="Force rainy scenario")
    parser.add_argument("--windy", action="store_true", help="Force windy scenario")
    args = parser.parse_args()

    forced = None
    if args.sunny: forced = "sunny"
    if args.cloudy: forced = "cloudy"
    if args.rainy: forced = "rainy"
    if args.windy: forced = "windy"

    main(force=forced)
