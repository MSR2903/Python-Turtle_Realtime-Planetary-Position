# Real-Time Planetary Position Visualization

This Python script uses the `turtle` graphics library to create a visual representation of the real-time positions and angles of planets in the solar system. It calculates the orbital angles based on each planet's unique orbital period and displays them around a central "Sun" object.

## Features

- **Real-Time Planetary Angles**: Calculates the angle of each planet based on orbital periods.
- **Input Custom Date and Time**: Option to input a specific date and time or default to the current time.
- **Dynamic Visualization**: Each planet moves along its orbit path relative to the Sun.

## Requirements

- Python 3.x
- `turtle` (standard Python library)
- `datetime` and `math` libraries (standard Python libraries)

## How It Works

1. **Initialize Screen and Objects**: Sets up the `turtle` screen with a black background and a central yellow "Sun."
2. **Calculate Planetary Angles**: Calculates the angle for each planet based on orbital periods, using a starting point of 0 degrees.
3. **Display Date and Time**: Option to display the current date and time or a custom date.
4. **Orbit Drawing**: Each planet moves along a pre-determined circular orbit based on its distance from the Sun.
5. **Planet Display**: Displays the angle for each planet in degrees.

## Planetary Data

| Planet   | Orbital Period (Earth days) | Distance from Sun (pixels) |
|----------|-----------------------------|-----------------------------|
| Mercury  | 87.97                       | 50                          |
| Venus    | 224.7                       | 75                          |
| Earth    | 365.256365                  | 100                         |
| Mars     | 686.98                      | 150                         |
| Jupiter  | 4332.82                     | 200                         |
| Saturn   | 10755.7                     | 250                         |
| Uranus   | 30687.15                    | 300                         |
| Neptune  | 60190.03                    | 350                         |

## Usage

1. Run the script: `python turtle_real_time_planetary_position.py`
2. Choose whether to input a custom date and time or use the current time.
3. Watch the planets move to their respective positions and angles around the Sun.

## Notes

- The script calculates planetary angles assuming ideal circular orbits.
- Planetary colors are approximations and are customizable in the script.
