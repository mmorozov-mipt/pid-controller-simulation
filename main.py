import numpy as np
import matplotlib.pyplot as plt


def simulate_pid(
    T=10.0,
    dt=0.001,
    Kp=3.0,
    Ki=1.0,
    Kd=0.2,
    wn=2.0,
    zeta=0.5,
    K_plant=1.0,
    setpoint=1.0,
):
    """
    Simple PID control simulation for a second-order system.

    Plant model (second order):
        x' = A x + B u
        y = C x

    where x = [position, velocity]
    """
    steps = int(T / dt)

    # State space matrices for a standard second order system
    A = np.array([[0.0, 1.0],
                  [-wn ** 2, -2 * zeta * wn]])
    B = np.array([[0.0],
                  [K_plant]])
    C = np.array([1.0, 0.0])

    x = np.zeros(2)  # initial state
    integral = 0.0
    e_prev = 0.0

    ys = np.zeros(steps)
    us = np.zeros(steps)
    ts = np.linspace(0.0, T, steps)

    for k in range(steps):
        y = float(C @ x)
        e = setpoint - y

        # PID terms
        integral += e * dt
        derivative = (e - e_prev) / dt if k > 0 else 0.0

        # PID controller
        u = Kp * e + Ki * integral + Kd * derivative

        # Simple anti windup: clamp control signal
        u = max(min(u, 10.0), -10.0)

        # System dynamics (Euler integration)
        dx = A @ x + B.flatten() * u
        x = x + dx * dt

        ys[k] = y
        us[k] = u
        e_prev = e

    return ts, ys, us


def main():
    # Simulation parameters
    T = 8.0
    dt = 0.001
    setpoint = 1.0

    # PID gains (can be tweaked)
    Kp = 3.0
    Ki = 1.0
    Kd = 0.2

    ts, ys, us = simulate_pid(
        T=T,
        dt=dt,
        Kp=Kp,
        Ki=Ki,
        Kd=Kd,
        wn=2.0,
        zeta=0.5,
        K_plant=1.0,
        setpoint=setpoint,
    )

    # Simple metrics
    final_value = ys[-1]
    overshoot = (np.max(ys) - setpoint) / setpoint * 100.0
    print(f"Final value: {final_value:.3f}")
    print(f"Overshoot: {overshoot:.1f} percent")

    # Plot response
    plt.figure()
    plt.plot(ts, ys, label="Output y(t)")
    plt.plot(ts, np.ones_like(ts) * setpoint, "--", label="Setpoint")
    plt.xlabel("Time, s")
    plt.ylabel("Output")
    plt.title("PID control of a second-order system")
    plt.grid(True)
    plt.legend()

    # Plot control signal
    plt.figure()
    plt.plot(ts, us, label="Control u(t)")
    plt.xlabel("Time, s")
    plt.ylabel("Control signal")
    plt.title("Control signal")
    plt.grid(True)
    plt.legend()

    plt.show()


if __name__ == "__main__":
    main()
