# Web VPython 3.2
# LAB04: Free Fall with Nonzero Initial Velocity (Part 2)

from vpython import *

# Scene Setup
scene.width = 800
scene.height = 800
scene.range = 16
scene.autoscale = False
scene.center = vector(0, 12, 0)
scene.background = color.white

# Objects
ball = sphere(pos=vector(0, 2, 0), radius=1, color=color.cyan)
ground = box(pos=vector(0, -0.1, 0), size=vector(24, 0.2, 5), color=color.black)

# Physics Parameters
accel = vector(0, -9.8, 0)      # acceleration due to gravity
ball.velocity = vector(0, 15, 0)  # initial upward velocity
dt = 0.005

# Visualization: Velocity Arrow
bv = arrow(pos=ball.pos, axis=ball.velocity * 0.05, color=color.black, shaftwidth=0.3)

# Graphs
display2 = gdisplay(background=color.white, foreground=color.black, width=600, height=400)
poscurve = gcurve(color=color.blue, label="Position (m)")
velcurve = gcurve(color=color.orange, label="Velocity (m/s)")

time = 0.0

# Simulation Loop
while ball.pos.y - ball.radius > ground.pos.y + ground.size.y / 2:
    rate(1 / dt)
    
    # Numerical Integration
    ball.velocity = ball.velocity + accel * dt
    ball.pos = ball.pos + ball.velocity * dt
    
    # Update Visualization
    bv.pos = ball.pos
    bv.axis = ball.velocity * 0.05
    
    # Update Graphs
    time = time + dt
    poscurve.plot(pos=(time, ball.pos.y))
    velcurve.plot(pos=(time, ball.velocity.y))
    
    # Console Output
    print(f"t: {time:.3f}s | y: {ball.pos.y:.2f}m | vy: {ball.velocity.y:.2f}m/s")

print("--- Simulation Complete ---")
print(f"Total time: {time:.3f}s")
