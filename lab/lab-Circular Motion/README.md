# LAB 04: Uniform Circular Motion with VPython

---

This manuscript presents a simulation of uniform circular motion (UCM) using VPython. A point mass attached to a virtual string moves with constant speed along a circular path. The simulation visualizes the trajectory in 3D and optionally plots radial acceleration.

---

## 🎯 Learning Outcomes

- Model and visualize uniform circular motion using VPython.
- Understand the relationship between velocity, radius, and centripetal acceleration.
- Animate a particle's motion constrained to a circular path.
- Use vector operations to compute dynamic quantities in motion.

---

## 📚 Background & Theory

Uniform Circular Motion is motion in a circle at constant speed. The object experiences **centripetal acceleration** directed toward the center of the circle:

### Centripetal Acceleration

$$
a_c = \frac{v^2}{r}
$$

### Angular Velocity

Let \( \omega\) be the angular velocity (rad/s):

$$
v = r\omega
$$

The position vector of the object in the \( xy \)-plane is given by:

$$
\vec{r}(t) = r\cos(\omega t)\hat{i} + r\sin(\omega t)\hat{j}
$$

The velocity is tangent to the circular path:

$$
\vec{v}(t) = -r\omega\sin(\omega t)\hat{i} + r\omega\cos(\omega t)\hat{j}
$$

---

## 💻 VPython Implementation

```python
from vpython import *

# ---------- Scene Setup ----------
scene.width = 800
scene.height = 600
scene.background = color.white
scene.title = "Uniform Circular Motion"

# ---------- Constants ----------
radius = 5.0         # Radius of the circular path (m)
omega = 2.0          # Angular velocity (rad/s)
dt = 0.01            # Time step
t = 0                # Time

# ---------- Objects ----------
center = vector(0, 0, 0)
track = ring(pos=center, axis=vector(0,0,1), radius=radius, thickness=0.05, color=color.gray(0.7))
mass = sphere(pos=vector(radius, 0, 0), radius=1.0, color=color.red, make_trail=True)
velocity_arrow = arrow(pos=mass.pos, axis=vector(0,0,0), color=color.blue, shaftwidth=0.2)
acceleration_arrow = arrow(pos=mass.pos, axis=vector(0,0,0), color=color.green, shaftwidth=0.2)

# ---------- Simulation Loop ----------
while t < 20:
    rate(100)

    # Update position
    x = radius * cos(omega * t)
    y = radius * sin(omega * t)
    mass.pos = vector(x, y, 0)

    # Update velocity and acceleration vectors
    velocity = vector(-radius * omega * sin(omega * t), radius * omega * cos(omega * t), 0)
    acceleration = -omega**2 * mass.pos

    velocity_arrow.pos = mass.pos
    velocity_arrow.axis = velocity * 0.5  # scaled for visibility
    acceleration_arrow.pos = mass.pos
    acceleration_arrow.axis = acceleration * 0.5  # scaled

    t += dt
```

---

## 🔍 Observations

- The object maintains constant speed, but its velocity vector changes direction.
- Acceleration vector always points inward (toward center).
- Velocity is perpendicular to the position vector at all times.

---

## ✅ Verification Tasks

1. Verify that the object remains on the circular path with radius \( r \).
2. Confirm that the magnitude of acceleration is \( a = v^2 / r \).
3. Plot angular position vs time (optional extension).
4. Derive and confirm parametric equations of motion.

---

## 🧪 Extensions

- Add trail of acceleration vector’s tip.
- Plot angular displacement vs time using `gcurve`.
- Add a rotating reference frame and show the object is stationary in it.
- Change to **non-uniform** circular motion by gradually increasing ω.
- Show torque and angular momentum for advanced analysis.

---

## 📥 Submission Checklist

- ✅ VPython script file (.py or .vpy)
- ✅ Screenshots of simulation and vector arrows
- ✅ Notes on theoretical verification (velocity, acceleration)
- ✅ Graphs of angular displacement or acceleration over time

---

## 🔗 References

- VPython Docs: [https://vpython.org](https://vpython.org)

