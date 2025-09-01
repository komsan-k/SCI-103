# Simple Harmonic Motion (SHM) with Plotting Graphs using VPython

*A Guided Manuscript for Physics & Programming Labs*

---

## 🧠 Abstract

This manuscript develops a simulation of one-dimensional simple harmonic motion (SHM) using VPython. A mass-spring system is modeled numerically via the Euler–Cromer method. Displacement, velocity, and energy are plotted versus time, and results are compared with analytic solutions.

---

## 🎯 Learning Outcomes

- Derive the equation of motion for SHM: `m * d²x/dt² + kx = 0`.
- Implement Euler–Cromer numerical integration in VPython.
- Plot displacement and velocity against time using `gcurve`.
- Verify conservation of total mechanical energy in ideal SHM.

---

## 📚 Background & Theory

For a mass `m` attached to a spring with constant `k`, the displacement `x(t)` satisfies:

```
m * d²x/dt² + kx = 0, where ω = sqrt(k/m)
```

The analytical solution:

```
x(t) = A * cos(ωt) + B * sin(ωt)
```

The velocity is:

```
v(t) = dx/dt
```

### ⚙️ Euler–Cromer Scheme

```
v[n+1] = v[n] + a[n] * Δt
x[n+1] = x[n] + v[n+1] * Δt
```

where acceleration `a[n] = - (k/m) * x[n]`.

---

## 💻 VPython Implementation

### Code: SHM with Graphs

```python
from vpython import *

# ---------- Scene ----------
scene.width = 900
scene.height = 500
scene.background = color.white
ceiling = box(pos=vector(0,0,0), size=vector(0.2,0.01,0.2), color=color.gray(0.8))
mass = box(pos=vector(0,-1,0), size=vector(0.2,0.2,0.2), color=color.red)
spring = helix(pos=ceiling.pos, axis=mass.pos-ceiling.pos, radius=0.05, coils=15)

# ---------- Parameters ----------
m = 0.5  # kg
k = 20.0  # N/m
omega = (k/m)**0.5
x0 = -0.3  # initial displacement (m)
v0 = 0.0  # initial velocity
dt = 0.001

# State variables
x = x0
v = v0
t = 0.0

# ---------- Graphs ----------
g1 = graph(title="SHM: Displacement & Velocity vs Time",
           xtitle="t (s)", ytitle="x, v", background=color.white, foreground=color.black)
xc = gcurve(color=color.blue, label="x(t)")
vc = gcurve(color=color.red, label="v(t)")

g2 = graph(title="SHM: Energy vs Time",
           xtitle="t (s)", ytitle="Energy (J)", background=color.white, foreground=color.black)
KEc = gcurve(color=color.orange, label="Kinetic")
PEc = gcurve(color=color.green, label="Potential")
TEc = gcurve(color=color.black, label="Total")

# ---------- Time evolution ----------
while t < 10:
    rate(1000)
    # Acceleration from Hooke's law
    a = -(k/m)*x
    # Euler-Cromer updates
    v = v + a*dt
    x = x + v*dt
    t = t + dt

    # Update visuals
    mass.pos.y = -1 + x
    spring.axis = mass.pos - ceiling.pos

    # Energies
    KE = 0.5*m*v**2
    PE = 0.5*k*x**2
    TE = KE + PE

    # Plot
    xc.plot(t, x)
    vc.plot(t, v)
    KEc.plot(t, KE)
    PEc.plot(t, PE)
    TEc.plot(t, TE)
```

---

## 🔍 Observations

- `x(t)` oscillates sinusoidally; `v(t)` is π/2 out of phase.
- Kinetic and potential energy oscillate out of phase, but total energy `E = KE + PE` remains constant.
- Euler–Cromer is stable for oscillatory motion; explicit Euler would diverge.

---

## ✅ Verification Tasks

1. Check the simulated oscillation period against the analytic prediction `T = 2π / ω`.
2. Plot `x(t)` versus the analytic `x(t) = x₀ * cos(ωt)` for `v₀ = 0`.
3. Quantify energy conservation error by computing `ΔE / E` over the run.

---

## 🧪 Extensions

- Add damping: `F_d = -b * v`, observe amplitude decay and exponential envelope.
- Add driving force: `F = F₀ * cos(Ωt)`; observe resonance near `Ω = ω`.
- Vary `Δt` to study numerical stability and convergence.

---

## 📥 Submission Checklist

- ✅ VPython script and screenshots of graphs.
- ✅ Measured period and comparison to analytic formula.
- ✅ Notes on energy conservation and errors observed.

---

## 🔗 References

- VPython documentation: [https://vpython.org/](https://vpython.org/)
- Introductory mechanics textbooks on oscillations.
