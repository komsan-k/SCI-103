# 🚚 Truck Motion Simulation with VPython

## 📖 Problem Statement  

A truck is moving along a straight road. It starts from rest and accelerates uniformly at **2.00 m/s²** until it reaches a speed of **20.0 m/s**. After reaching this speed, the truck continues to travel at a constant velocity of **20.0 m/s** for **20.0 s**. Finally, the brakes are applied, and the truck decelerates uniformly to rest in **5.00 s**.  

### Tasks  
1. **Determine the total time of motion of the truck.**  
2. **Calculate the total displacement of the truck during the motion.**  
3. **Find the average velocity of the truck for the entire journey.**  
4. **Using VPython, simulate the motion of the truck with a simple animation, showing the phases of acceleration, constant speed, and deceleration.**  

---

## 🧮 Analytical Results  

- Time to accelerate:  
  \[
  t_\text{accel} = \frac{v}{a} = \frac{20}{2} = 10 \,\text{s}
  \]

- Total time of motion:  
  \[
  T = t_\text{accel} + t_\text{cruise} + t_\text{brake} = 10 + 20 + 5 = 35 \,\text{s}
  \]

- Displacements:  
  - Acceleration phase:  
    \[
    s_1 = \tfrac{1}{2} a t^2 = 0.5 \cdot 2 \cdot 10^2 = 100 \,\text{m}
    \]  
  - Constant velocity:  
    \[
    s_2 = v \cdot t = 20 \cdot 20 = 400 \,\text{m}
    \]  
  - Braking phase:  
    \[
    s_3 = \tfrac{1}{2}(v+0)\cdot t = 0.5 \cdot 20 \cdot 5 = 50 \,\text{m}
    \]  

- Total displacement:  
  \[
  S = s_1 + s_2 + s_3 = 100 + 400 + 50 = 550 \,\text{m}
  \]

- Average velocity:  
  \[
  v_\text{avg} = \frac{S}{T} = \frac{550}{35} \approx 15.7 \,\text{m/s}
  \]

---

## 💻 VPython Minimal Animation Code  

```python
# GlowScript VPython 3.2
from vpython import *

# --- Parameters ---
a1 = 2.0
vmax = 20.0
t_cruise = 20.0
t_brake = 5.0

t_accel = vmax / a1
T = t_accel + t_cruise + t_brake
a3 = -vmax / t_brake

# --- Scene ---
road = box(pos=vec(0,-0.1,0), size=vec(120,0.05,4), color=color.gray(0.7))
truck = box(pos=vec(-55,0,0), size=vec(2,1,1), color=color.orange)

# --- Simulation ---
t, x, v = 0, 0, 0
dt = 0.01

while t < T:
    rate(100)
    if t < t_accel:
        a = a1
    elif t < t_accel + t_cruise:
        a = 0
    else:
        a = a3
    v = v + a*dt
    x = x + v*dt
    truck.pos = vec(-55 + x/5, 0, 0)
    t += dt
```

---

## ✅ Expected Results  
- **Total time of motion**: 35.0 s  
- **Total displacement**: 550.0 m  
- **Average velocity**: 15.7 m/s  

---

