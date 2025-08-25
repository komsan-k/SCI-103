# LAB03: Physics Simulation of a Bouncing Ball

## Goals
In this lab, you will explore how **Newton’s Second Law** governs motion using VPython simulations.  
You will begin by modeling a perfectly elastic ball in free fall (no air resistance) and then extend the simulation to include more realistic effects.  

---

## Preliminaries
We will simulate the vertical motion of a ball. The theoretical background is Newton’s Second Law:

![equation](https://latex.codecogs.com/png.latex?\frac{dp_y}{dt}=(F_{\text{net}})_y)

For constant mass *m*, momentum simplifies to *p = mv*:

![equation](https://latex.codecogs.com/png.latex?\frac{dv_y}{dt}=\frac{1}{m}(F_{\text{net}})_y)

For small time steps Δt:

![equation](https://latex.codecogs.com/png.latex?\Delta%20v_y\approx\frac{1}{m}(F_{\text{net}})_y\Delta%20t)

so that

![equation](https://latex.codecogs.com/png.latex?v_{2y}\approx%20v_{1y}+\frac{1}{m}(F_{\text{net}})_y\Delta%20t)

In free fall without air resistance:

![equation](https://latex.codecogs.com/png.latex?(F_{\text{net}})_y=-mg\quad\Rightarrow\quad%20v_{2y}\approx%20v_{1y}-g\Delta%20t)

Position update:

![equation](https://latex.codecogs.com/png.latex?y_2\approx%20y_1+v_y\Delta%20t)

---


## Example Calculation
Ball dropped from rest at **y = 4.0 m**, using \(\Delta t = 0.1s\):

| t (s) | y(t) (m) | v_y(t) (m/s) | F_net/m (m/s²) |
|-------|----------|---------------|----------------|
| 0.0   | 4.0      | 0.0           | -9.8           |
| 0.1   | ...      | ...           | -9.8           |
| 0.2   | ...      | ...           | -9.8           |
| 0.3   | ...      | ...           | -9.8           |

**Checkpoint #1:** Discuss your results and compare them with expected values.  

---

## Programming in VPython

### 1. Free Fall (No Bounce, No Drag)
```python
from vpython import *

floor = box(pos=vector(0,0,0), size=vector(6,0.2,6), color=color.blue)
ball = sphere(pos=vector(0,4,0), radius=0.5, color=color.red, make_trail=True)

ball.velocity = vector(0,-0.1,0)
g = 9.8
dt = 0.01

while ball.pos.y > 0.5:
    rate(100)
    ball.velocity.y = ball.velocity.y - g*dt
    ball.pos = ball.pos + ball.velocity*dt
```

---

### 2. Bouncing Ball (Perfectly Elastic)
```python
from vpython import *

floor = box(pos=vector(0,0,0), size=vector(6,0.2,6), color=color.blue)
ball = sphere(pos=vector(0,4,0), radius=0.5, color=color.red, make_trail=True)

ball.velocity = vector(0,-0.1,0)
g = 9.8
dt = 0.01

while True:
    rate(100)
    ball.velocity.y = ball.velocity.y - g*dt
    ball.pos = ball.pos + ball.velocity*dt
    
    if ball.pos.y <= ball.radius:
        ball.velocity.y = -ball.velocity.y
```

---

### 3. Bouncing with Air Resistance (Drag Force)
```python
from vpython import *

floor = box(pos=vector(0,0,0), size=vector(6,0.2,6), color=color.blue)
ball = sphere(pos=vector(0,4,0), radius=0.5, color=color.red, make_trail=True)

ball.velocity = vector(0,-0.1,0)
g = 9.8
rho = 1.225   # air density (kg/m^3)
Cd = 0.47     # drag coefficient for a sphere
A = pi*ball.radius**2
m = 0.05      # mass of the ball (kg)
dt = 0.01

while True:
    rate(100)
    Fg = vector(0,-m*g,0)
    v = mag(ball.velocity)
    Fd = -0.5 * Cd * rho * A * v**2 * norm(ball.velocity)
    Fnet = Fg + Fd
    a = Fnet/m
    
    ball.velocity = ball.velocity + a*dt
    ball.pos = ball.pos + ball.velocity*dt
    
    if ball.pos.y <= ball.radius:
        ball.velocity.y = -0.9*ball.velocity.y
```

---

## Checkpoints
- **Checkpoint #1:** Verify the free-fall calculations and compare with manual values.  
- **Checkpoint #2:** Test bouncing. Does the ball bounce indefinitely (elastic) or lose energy (inelastic)?  
- **Extension:** Analyze how drag force affects bounce height and damping.  

---

## Submission
- Submit your program with a working link.  
- Include discussion of checkpoints and observations.  

---

## Additional References
- [VPython Bouncing Ball Example](https://vpython.org/contents/bounce_example.html)  
- [Newton’s Laws of Motion](https://en.wikipedia.org/wiki/Newton%27s_laws_of_motion)  
- [Drag (Physics)](https://en.wikipedia.org/wiki/Drag_(physics))  
- [Drag Coefficient](https://en.wikipedia.org/wiki/Drag_coefficient)  
- [Density of Air](https://en.wikipedia.org/wiki/Density_of_air)  

