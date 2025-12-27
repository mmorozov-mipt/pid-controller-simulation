# pid-controller-simulation

PID controller simulation for a second-order dynamic system using Python, NumPy and Matplotlib.

## Project description

The project demonstrates how a classic PID controller can be used to control
a simple second-order system. The model is implemented in discrete time using
a state space representation and Euler integration.

The script:
- simulates a step response of the closed loop system
- computes the control signal and the output of the plant
- prints simple metrics such as final value and overshoot
- visualizes:
  - system output and setpoint
  - control signal

## Technologies

- Python 3
- NumPy
- Matplotlib
- control theory basics (PID, second order systems)

## How to run

1. Install dependencies:

```bash
pip install numpy matplotlib

2. Run the script:

```bash
python3 main.py
```

After running you will get:
- console output with metrics (final value and overshoot)
- plots showing:
  - system response and setpoint
  - control signal
```


## Example use case

This project can be used as:

- an educational example of PID control
- a simple tool for tuning PID parameters
- demonstration project for interviews related to control systems
- base for modeling dynamic systems in Python

## Disclaimer

This project is intended for educational and research purposes only.
The author is not responsible for any possible misuse of the code.

