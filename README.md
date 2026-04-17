# Factorio Manufacturing Dashboard

A Factorio-inspired manufacturing analytics dashboard. Simulates factory production data, stores metrics in SQLite, and visualizes output rates, defect rates, and machine utilization using Plotly Dash.

## Overview

This project simulates a Factorio-style factory producing items across multiple assembly lines. Production metrics are stored in a local SQLite database and visualized through an interactive Plotly Dash dashboard.

## Features

- Simulated factory production data (iron plates, copper cables, green circuits, etc.)
- SQLite database for storing production logs
- Interactive Plotly Dash dashboard with:
  - Production output over time
  - Machine utilization per assembler
  - Defect/efficiency rates
  - Lead time tracking

## Tech Stack

- **Python** — data generation and pipeline
- **SQLite** — local database storage
- **Plotly Dash** — interactive web dashboard

## Project Structure

```
factorio-dashboard/
├── generate_data.py      # Simulates and populates production data
├── dashboard.py          # Plotly Dash app
├── db.py                 # Database setup and queries
├── factory.db            # SQLite database (generated on run)
└── README.md
```

## Getting Started

```bash
pip install plotly dash pandas
python generate_data.py   # Generate simulated data
python dashboard.py       # Launch dashboard at localhost:8050
```

## Motivation

Factorio is essentially an industrial engineering simulator — optimizing production lines, eliminating bottlenecks, and maximizing throughput. This project applies those same concepts using real data tools.
