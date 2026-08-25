Web VPython 3.2
from vpython import *

scene.width  = 800
scene.height = 800
scene.range = 16
scene.autoscale = False
scene.center = vector(0,12,0)
scene.background = color.white

ball = sphere(pos=vector(0,2,0), radius=1, color=color.cyan)
ground = box(pos=vector(0, -0.1, 0), size=vector(24, 0.2, 5), color=color.black)

accel = vector(0,-9.8,0)
ball.velocity = vector(0,15,0)
dt = 0.005

display2 = gdisplay(background=color.white, foreground=color.black)  # Fixed
poscurve = gcurve(color=color.blue, label="position (m)")
velcurve = gcurve(color=color.orange, label="Velocity (m/s)")

time = 0.0
bv = arrow(pos=ball.pos, axis=ball.velocity * 0.005, color=color.black)  # Fixed

while ball.pos.y - ball.radius > ground.pos.y + ground.size.y/2:
    rate(1/dt)
    ball.velocity = ball.velocity + accel * dt
    ball.pos = ball.pos + ball.velocity * dt
    bv.pos = ball.pos
    bv.axis = ball.velocity*0.05
    time = time + dt
    poscurve.plot(pos=(time, ball.pos.y))
    velcurve.plot(pos=(time, ball.velocity.y))
    print(f"y: {ball.pos.y:.2f}, vy: {ball.velocity.y:.2f}")
