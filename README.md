# AI Traffic Simulator

A multi-vehicle traffic junction simulator built with Python and Pygame. Vehicles spawn from all four directions and navigate a crossroad controlled by an adaptive AI signal controller that adjusts phase timing based on real-time queue lengths and wait times.

---

## Features

- Cars, buses, and trucks spawn randomly from North, South, East, and West
- Adaptive AI controller monitors queue sizes and average wait times per lane
- Signal phases switch dynamically to reduce congestion
- Four numbered traffic lights each assigned to their own lane (E, W, S, S)
- Live HUD showing FPS, signal phase, queue counts, vehicles passed, and average wait time
- Zebra crossings, stop lines, lane markings, and direction arrows

---

## Tech Stack

- Python 3.8+
- Pygame

---

## Project Structure

- main.py — Game loop, event handling, rendering pipeline
- controller.py — Adaptive signal phase logic
- vehicle.py — Vehicle movement, signal compliance, collision spacing
- traffic_light.py — Light rendering with numbered ID and lane labels
- spawner.py — Random vehicle generation with spacing checks
- road.py — Road, lane markings, zebra crossings, stop lines
- junction.py — Junction box decoration and direction arrows
- hud.py — On-screen stats panel
- settings.py — All constants: screen size, speeds, colors, dimensions

---

## Getting Started

Install dependencies:

    pip install pygame

Run the simulator:

    python main.py

---

## How the AI Controller Works

The AdaptiveController scores each direction using queue size and average wait time:

    score = queue * 2 + average_wait * 0.3

It holds a green phase for a minimum of 5 seconds and a maximum of 12 seconds. If the opposing direction scores more than 2 points higher after the minimum time, it switches early. Yellow phases last 2 seconds between transitions.

---

## Author

Built with Python and Pygame by Shri6.
