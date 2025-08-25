# LAB04: Physics Simulation of 1-D Free Fall

## Goals
In this lab, you will simulate **1-D free fall** under gravity using VPython. You will learn how to:
- Represent free fall with numerical integration.
- Compare simulation results to analytic kinematics.
- Visualize velocity and position in real time.
- Extend the simulation to nonzero initial velocity.

---

## Part 1: Free Fall with Initial Velocity = 0

We begin by modeling a ball dropped from rest at a height of **20 m**.

### Scene Setup
```python
from vpython import *

scene.width = 800
scene.height = 800
scene.range = (16,16,16)
scene.autoscale = 0
scene.center = (0,12,0)
scene.background = color.white
```

### Objects
```python
ball = sphere(pos=vector(0,20,0), radius=1, color=color.red)
ground = box(pos=vector(0,-0.1,0), size=vector(24,0.2,5), color=color.green)
```

### Physics Parameters
```python
accel = vector(0,-9.8,0)      # acceleration due to gravity
ball.velocity = vector(0,0,0) # initial velocity
dt = 0.005
```

### Numerical Integration
We use discrete updates:

- v(t+Δt) = v(t) + aΔt  
- x(t+Δt) = x(t) + vΔt

Simulation loop:
```python
while ball.pos.y - ball.radius > ground.pos.y + ground.size.y/2:
    rate(1/dt)
    ball.velocity = ball.velocity + accel*dt
    ball.pos = ball.pos + ball.velocity*dt
```

**Checkpoint 1**
- Does the ball stop when it reaches the ground?  
- Can you see both ball and ground throughout the simulation?  
- Is the motion consistent with expectations (increasing speed under gravity)?  

---

## Visualizing Velocity

We can visualize velocity with an arrow:
```python
bv = arrow(pos=ball.pos, axis=ball.velocity, color=color.yellow)
```

Update inside the loop:
```python
bv.pos = ball.pos
bv.axis = ball.velocity
```

Add quantitative output:
```python
print(ball.velocity.y, ball.pos.y)
```

---

## Plotting Position and Velocity

Add a time variable:
```python
time = 0.0
```

Initialize graph:
```python
display2 = gdisplay(background=color.white, foreground=color.black)
poscurve = gcurve(color=color.blue)
velcurve = gcurve(color=color.orange)
```

Update inside loop:
```python
time = time + dt
poscurve.plot(pos=(time, ball.pos.y))
velcurve.plot(pos=(time, ball.velocity.y))
```

This produces real-time graphs of position and velocity.

---

## Part 2: Free Fall with Nonzero Initial Velocity

Modify initial conditions:
```python
ball.pos = vector(0,2,0)
ball.velocity = vector(0,15,0)  # upward toss
```

**Checkpoint 2**
1. What is the analytic solution for y(t) in this case?  
   y(t) = y0 + v0*t - (1/2) g t^2  
2. Plot the analytic curve and compare it to the simulation.

---

## Submission
- Submit your completed program with link.  
- Include graphs of position and velocity.  
- Answer checkpoint questions with explanations.  

---

## Additional Resources
- [VPython Graphing Documentation](https://www.glowscript.org/docs/VPythonDocs/graph.html)  
- [Newton’s Laws of Motion](https://en.wikipedia.org/wiki/Newton%27s_laws_of_motion)  

