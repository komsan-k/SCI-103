# Lab 13 (fixed): Exploring Electromagnetic Waves Using VPython

Electromagnetic (EM) waves are fundamental to physics and engineering,
spanning applications from radio communications to optics. This lab uses
**VPython** to simulate and visualize EM waves in real-time, making
abstract concepts like field propagation, polarization, interference,
and energy transfer more intuitive.

------------------------------------------------------------------------

## 🎯 Objectives

1.  **Visualize Propagation of Electromagnetic Waves**
    -   Simulate a plane wave propagating in space.\
    -   Observe how the **electric field (E)** and **magnetic field
        (B)** oscillate perpendicularly to each other and to the
        direction of propagation (**k**).
2.  **Explore the Relationship between Wavelength, Frequency, and
    Speed**
    -   Show that wave speed is constant (**c = λf**).\
    -   Demonstrate how changing frequency affects wavelength.
3.  **Simulate Polarization of EM Waves**
    -   Investigate **linear** and **circular** polarization.\
    -   Observe how the electric field orientation changes.
4.  **Investigate Interference of EM Waves**
    -   Simulate **constructive** and **destructive interference** of
        two EM waves.\
    -   Explore phase differences and the principle of superposition.
5.  **Visualize Energy Transfer using the Poynting Vector**
    -   Compute and display the **Poynting vector (S = E × B)**.\
    -   Understand how energy flows in the propagation direction.

------------------------------------------------------------------------

## 📜 Key Concepts

-   Maxwell's equations and EM wave properties\
-   Orthogonality of **E**, **B**, and **k**\
-   Polarization (linear, circular)\
-   Wave interference patterns\
-   Poynting vector and energy transfer

------------------------------------------------------------------------

## 🖥️ Sample Codes

### Objective 1: Propagation of EM Waves

``` python
from vpython import *

E_field = arrow(pos=vector(0, 0, 0), axis=vector(0, 1, 0), color=color.red)
B_field = arrow(pos=vector(0, 0, 0), axis=vector(1, 0, 0), color=color.blue)

t = 0
dt = 0.05
while True:
    rate(100)
    E_field.axis = vector(0, sin(t), 0)  # E oscillates in y
    B_field.axis = vector(sin(t), 0, 0)  # B oscillates in x
    t += dt
```

### Objective 3: Polarization (Linear vs Circular)

``` python
from vpython import *

# Linear polarization
E_field_linear = arrow(pos=vector(0,0,0), axis=vector(0,1,0), color=color.red)

# Circular polarization
E_field_circular = arrow(pos=vector(2,0,0), axis=vector(0,1,0), color=color.green)

t = 0
dt = 0.01
while True:
    rate(100)
    E_field_linear.axis = vector(0, sin(t), 0)
    E_field_circular.axis = vector(cos(t), sin(t), 0)
    t += dt
```

### Objective 5: Poynting Vector

``` python
from vpython import *

E_field = arrow(pos=vector(0,0,0), axis=vector(0,1,0), color=color.red)
B_field = arrow(pos=vector(0,0,0), axis=vector(1,0,0), color=color.blue)
S_vector = arrow(pos=vector(0,0,0), axis=vector(0,0,1), color=color.green)

t = 0
dt = 0.01
while True:
    rate(100)
    E_field.axis = vector(0, sin(t), 0)
    B_field.axis = vector(sin(t), 0, 0)
    S_vector.axis = cross(E_field.axis, B_field.axis)
    t += dt
```

------------------------------------------------------------------------

## 📌 Assignment Task

-   Prepare a **3--5 minute video presentation (YouTube link)**.\
-   Demonstrate the code and explain the results.\
-   Show evidence of critical thinking and understanding of:
    -   Wave propagation\
    -   E, B, and k relationships\
    -   Polarization\
    -   Interference\
    -   Energy transfer

------------------------------------------------------------------------

## ✅ Learning Outcomes

By completing this lab, students will:

-   Gain an intuitive understanding of **EM wave propagation**.\
-   Relate **frequency, wavelength, and wave speed**.\
-   Understand **polarization** in optics and communications.\
-   Observe **wave interference and superposition**.\
-   Visualize **energy transfer using the Poynting vector**.

------------------------------------------------------------------------

## 📚 References

-   Maxwell's Equations (any standard EM textbook)\
-   VPython Documentation: <https://vpython.org>\
-   Electromagnetic Waves tutorials (MIT OCW, Khan Academy)

------------------------------------------------------------------------

