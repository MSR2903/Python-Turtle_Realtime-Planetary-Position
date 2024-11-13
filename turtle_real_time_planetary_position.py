import datetime
import turtle
import math

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Real-Time Planetary Angles")

# Create a turtle for the Sun
sun = turtle.Turtle()
sun.shape("circle")
sun.color("yellow")
sun.shapesize(stretch_wid=2, stretch_len=2)

# Create a turtle for each planet
planet_turtles = {}
colors = {
    'Mercury': 'gray', 'Venus': 'yellow', 'Earth': 'blue', 'Mars': 'red',
    'Jupiter': 'brown', 'Saturn': 'orange', 'Uranus': 'light blue', 'Neptune': 'dark blue'
}
distances = {
    'Mercury': 50, 'Venus': 75, 'Earth': 100, 'Mars': 150,
    'Jupiter': 200, 'Saturn': 250, 'Uranus': 300, 'Neptune': 350
}

for planet in colors:
    planet_turtle = turtle.Turtle()
    planet_turtle.shape("circle")
    planet_turtle.color(colors[planet])
    planet_turtle.penup()
    planet_turtle.goto(distances[planet], 0)
    planet_turtles[planet] = planet_turtle

def calculate_angle(orbital_period_in_days, start_time, current_time):
    time_difference = (current_time - start_time).total_seconds()
    orbital_period_in_seconds = orbital_period_in_days * 24 * 60 * 60
    angle = (time_difference / orbital_period_in_seconds) * 360
    angle = angle % 360
    return angle

# Orbital periods of the planets in Earth days
orbital_periods = {
    'Mercury': 87.97,
    'Venus': 224.7,
    'Earth': 365.256365,
    'Mars': 686.98,
    'Jupiter': 4332.82,
    'Saturn': 10755.70,
    'Uranus': 30687.15,
    'Neptune': 60190.03
}

# The last time each planet hit 0 degree
start_times = {
    'Mercury': datetime.datetime(2024, 5, 30),
    'Venus': datetime.datetime(2024, 4, 18),
    'Earth': datetime.datetime(2023, 9, 22),
    'Mars': datetime.datetime(2022, 7, 28),
    'Jupiter': datetime.datetime(2022, 8, 16),
    'Saturn': datetime.datetime(1996, 5, 31),
    'Uranus': datetime.datetime(2011, 1, 29),
    'Neptune': datetime.datetime(1861, 8, 18)
}

def display_current_time(current_time):
    time_display = turtle.Turtle()
    time_display.hideturtle()
    time_display.color("white")
    time_display.penup()
    time_display.goto(-450, 330)  # Move to the top left of the screen
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
    time_display.write(f"Time:", align="left", font=("Arial", 14, "normal"))
    time_display.goto(-450, 300)  # Move slightly below the current time label
    time_display.write(formatted_time, align="left", font=("Arial", 14, "normal"))

def display_planet_angles(current_time):
    # Set up displaying text
    angle_display = turtle.Turtle()
    angle_display.hideturtle()
    angle_display.color("white")
    angle_display.penup()
    angle_display.goto(-450, 220)  # Move slightly below the time display
    angle_display.write("Planet Angles:", align="left", font=("Arial", 14, "normal"))

    # Display each planet's current angle
    y_offset = 200
    for planet in orbital_periods:
        angle = calculate_angle(orbital_periods[planet], start_times[planet], current_time)
        angle_display.goto(-450, y_offset)
        angle_display.write(f"{planet}: {angle:.2f}°", align="left", font=("Arial", 12, "normal"))
        y_offset -= 20

# Ask user if they want to input a date
use_input_date = screen.textinput("Input Date", "Do you want to input a date? (y/n)\n'n' will generate current time").lower()

if use_input_date == 'y':
    date_str = screen.textinput("Input Date", "Enter date (YYYY-MM-DD HH:MM:SS): \nPlease follow the provided format!\nProgram will show the current time if the format is incorrect.")
    try:
        current_time = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        current_time = datetime.datetime.now()
else:
    current_time = datetime.datetime.now()

# Call the functions
display_current_time(current_time)
display_planet_angles(current_time)

# Calculate and update the position of each planet turtle
for planet in orbital_periods:
    # Draw orbit path
    planet_turtle = planet_turtles[planet]
    planet_turtle.pendown()
    for degree in range(0, 360, 10):
        radians = math.radians(degree)
        x = distances[planet] * math.cos(radians)
        y = distances[planet] * math.sin(radians)
        planet_turtle.goto(x, y)
    planet_turtle.goto(distances[planet], 0)
    planet_turtle.penup()

    # Move to current position
    angle = calculate_angle(orbital_periods[planet], start_times[planet], current_time)
    radians = math.radians(angle)
    x = distances[planet] * math.cos(radians)
    y = distances[planet] * math.sin(radians)
    planet_turtle.goto(x, y)

screen.mainloop()
