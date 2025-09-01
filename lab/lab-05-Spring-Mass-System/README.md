# VPython Simulation: 1D Spring-Mass System with Real-Time Graphs

This project demonstrates a 1D spring-mass system using VPython and visualizes position, velocity, and acceleration using scatter plots.

---

## 🎯 Objective

Simulate a spring-mass oscillator and visualize:
- Position vs Time
- Velocity vs Time
- Acceleration vs Time

---

## 🎓 Learning Outcomes

By completing this simulation activity, learners will:

- Understand the behavior of a mass-spring system in one dimension.
- Apply Hooke’s Law to derive acceleration from displacement.
- Implement real-time numerical integration using Python.
- Visualize physical quantities (position, velocity, acceleration) as time-series data.

---
## 📚 Background & Theory

A mass-spring system obeys Hooke’s Law:

$$
F = -k(x - x_{\text{eq}})
$$

where:

- $F$ is the restoring force,  
- $k$ is the spring constant,  
- $x$ is the current position,  
- $x_{\text{eq}}$ is the equilibrium position.

Using Newton’s Second Law $F = ma$, we obtain the acceleration:

$$
a = -\frac{k}{m}(x - x_{\text{eq}})
$$

This simulation numerically solves the second-order differential equation using a discrete time step `dt`. The update equations are:

$$
v_{{t+1}} = v_t + a_t \cdot dt
$$

$$
x_{{t+1}} = x_t + v_{{t+1}} \cdot dt
$$

The simulation visualizes these quantities using real-time graphing.

---

## 💻 Code Overview

```python
from vpython import *
# GlowScript 3.2 VPython

display(width=600, height=600, center=vector(6,0,0))

f1 = gdots(color=color.green, label='position', fast=True)
f2 = gdots(type='scatter', color=color.blue, label='velocity', fast=True)
f3 = gdots(type='scatter', color=color.red, label='acceleration', fast=True)

pivot = vector(0,0,0)
bractket = box(pos=pivot, size=vector(0.1,5,5), color=color.green)
ball = sphere(pos=vector(12,0,0), velocity=vector(0,0,0), radius=1, mass=1.0, color=color.blue)

spring = helix(pos=pivot, axis=ball.pos - pivot, radius=0.4, constant=1, thickness=0.1, coils=20, color=color.red)
eq = vector(9,0,0)  # Equilibrium position

t = 0
dt = 0.05
while t < 20:
    rate(100)
    acc = (spring.constant / ball.mass) * (eq - ball.pos)
    ball.velocity = ball.velocity + acc * dt
    ball.pos = ball.pos + ball.velocity * dt
    spring.axis = ball.pos - spring.pos

    f1.plot(t, ball.pos.x)
    f2.plot(t, ball.velocity.x)
    f3.plot(t, acc.x)

    t = t + dt
```

---

## 🧠 Concepts Illustrated

- **Hooke's Law:** Force proportional to displacement from equilibrium.
- **Numerical Integration:** Velocity-Verlet-like approach.
- **Real-Time Plotting:** Position, velocity, and acceleration are plotted as the simulation runs.

---

## 🛠️ Requirements

- [GlowScript VPython](https://www.glowscript.org/) (for browser-based simulation)
- Alternatively: Install VPython in Python environment via:
  ```bash
  pip install vpython
  ```

---

## 📈 Output

- Interactive 3D animation of a spring-mass system.
- Graphs of:
  - Position (green)
  - Velocity (blue)
  - Acceleration (red)

---

# Submission Checklist: Spring-Mass System Simulation (VPython)

Ensure all components listed below are included in your submission for the Spring-Mass (Simple Harmonic Motion) simulation lab using VPython.

---

## 🔧 Code & Implementation

- ✅ **VPython Script File** (`.py` or `.vpy`) containing:
  - Spring-mass simulation using Euler–Cromer method
  - Animated motion of the mass and spring
  - Real-time plotting using `gcurve` or `gdots`

---

## 📸 Visual Outputs

- ✅ **Screenshots or Video Recording** showing:
  - The animated spring-mass system in motion
  - Graph of Displacement vs Time and Velocity vs Time
  - Energy plot (Kinetic, Potential, and Total Energy vs Time)

---

## 📊 Numerical Verification

- ✅ **Measured Oscillation Period** using the simulation
- ✅ **Analytical Comparison**:
  - Use the formula:  
    $$
    T = 2\pi \sqrt{\frac{m}{k}}
    $$
- ✅ **Energy Conservation Analysis**:
  - Show constancy of total energy over time
  - Optionally compute and report relative error:  
    $$
    \frac{\Delta E}{E} = \frac{E_{\text{final}} - E_{\text{initial}}}{E_{\text{initial}}}
    $$

---

## 📄 Documentation & Explanation

- ✅ **Lab Report or Documentation** (PDF or Markdown):
  - Clear description of simulation objective
  - Explanation of numerical method and implementation
  - Interpretation of results and verification outcomes
  - Labeled graphs and parameter descriptions

---

## 🧪 Optional Extensions (Bonus)

- ⬜ Include simulation with **damping**: $F_d = -bv$
- ⬜ Add a **driving force**: $F = F_0 \cos(\Omega t)$
- ⬜ Plot **acceleration vs time**
- ⬜ Compare with the **explicit Euler method** and discuss stability

---

## 📬 Submission Format

- Compressed folder or zip file:
  - `spring_mass_simulation/`
    - `main.py` or `main.vpy`
    - `screenshots/`
    - `report.md` or `report.pdf`
    - `graphs/`

---

## 🔗 Reference

- VPython documentation: [https://vpython.org](https://vpython.org)
