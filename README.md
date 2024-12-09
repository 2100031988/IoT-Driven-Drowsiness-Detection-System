# IoT-Driven Drowsiness Detection System

This Python-based system demonstrates a drowsiness detection implementation for enhanced driver safety. The system simulates various sensor inputs and provides real-time drowsiness monitoring with alerts.

## Features

- Real-time drowsiness detection simulation
- Multi-factor analysis (blink rate, head position, reaction time)
- Configurable alert thresholds
- Detailed logging system
- Alert management with cooldown periods

## Project Structure

```
.
├── main.py                 # Main application entry point
├── modules/
│   ├── config.py          # System configuration
│   ├── drowsiness_detector.py    # Core detection logic
│   ├── alert_system.py    # Alert management
│   └── data_logger.py     # Logging functionality
└── README.md              # Project documentation
```

## How It Works

1. The system continuously monitors driver behavior through simulated sensors
2. Analyzes multiple factors to determine drowsiness level
3. Triggers alerts when drowsiness exceeds configured thresholds
4. Logs all events and measurements for later analysis

## Running the System

To start the drowsiness detection system:

```bash
python main.py
```

Press Ctrl+C to stop the system.

## Configuration

The system's behavior can be customized by modifying the parameters in `config.py`:

- Drowsiness thresholds
- Sampling rates
- Alert cooldown periods
- Alert level boundaries