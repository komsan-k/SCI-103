# Lab 13: Visualization of Electromagnetic (EM) Fields using VPython

## 1. Objectives
- Understand the nature of electromagnetic (EM) fields as time-varying electric and magnetic fields.  
- Visualize the propagation of an EM wave in free space using VPython.  
- Demonstrate the orthogonality of **E**, **B**, and wave propagation direction.  
- Explore the relationships:  

$$
\mathbf{E} \perp \mathbf{B}, \quad \mathbf{E} \perp \mathbf{k}, \quad \mathbf{B} \perp \mathbf{k}
$$  

where \(\mathbf{k}\) is the direction of propagation.  

---

## 2. Background Theory
Maxwell’s equations predict the existence of electromagnetic waves.  
In free space, a plane wave traveling along the \(z\)-axis can be described as:

$$
\mathbf{E}(z,t) = E_0 \cos(kz - \omega t)\,\hat{x}
$$

$$
\mathbf{B}(z,t) = B_0 \cos(kz - \omega t)\,\hat{y}
$$

where:  
- amplitudes is

$$ 
E_0, B_0 
$$

- wave numbe is

$$ 
k = \tfrac{2\pi}{\lambda}\ 
$$  

- angular frequency
  
$$ 
\omega = 2\pi f\
$$ 

- speed of light
  
$$
c = \tfrac{E_0}{B_0} = \lambda f\
$$  

**Key properties:**  
- \(\mathbf{E}, \mathbf{B}, \hat{z}\) are mutually perpendicular.  
- Energy propagates in the direction of the **Poynting vector**:  

$$
\mathbf{S} = \frac{1}{\mu_0} \, (\mathbf{E} \times \mathbf{B})
$$  

---

## 3. Software & Setup
- GlowScript VPython (3.2+) accessible at [https://glowscript.org](https://glowscript.org)  
- Browser: Chrome/Firefox  
- No installation required  

---

## 4. Lab Procedure

### Part A – Visualizing an EM Wave (Animated Arrows)
```python
# GlowScript 3.2 VPython – Electromagnetic Wave Visualization
from vpython import *

scene.title = "Electromagnetic Wave (E and B fields)"
scene.width = 800
scene.height = 500
scene.background = color.white
scene.forward = vec(-1,-0.5,-1.2)

# Constants
c = 3e8
lam = 2.0
f = c/lam
omega = 2*pi*f
k = 2*pi/lam
E0 = 1.0
B0 = E0/c   # from E = cB

# Axes: z is propagation direction
arrow(pos=vec(0,0,0), axis=vec(1,0,0), color=color.red, shaftwidth=0.03)   # x-axis (E)
arrow(pos=vec(0,0,0), axis=vec(0,1,0), color=color.blue, shaftwidth=0.03)  # y-axis (B)
arrow(pos=vec(0,0,0), axis=vec(0,0,1), color=color.green, shaftwidth=0.03) # z-axis (prop)

# Wave sample points along z
N = 25
dz = 0.2
E_arrows = []
B_arrows = []

for i in range(N):
    z = i*dz
    E = arrow(pos=vec(0,0,z), axis=vec(0,0,0), color=color.red, shaftwidth=0.02)
    B = arrow(pos=vec(0,0,z), axis=vec(0,0,0), color=color.blue, shaftwidth=0.02)
    E_arrows.append(E)
    B_arrows.append(B)

t = 0
dt = 0.02

while True:
    rate(30)
    t += dt
    for i in range(N):
        z = i*dz
        phase = k*z - omega*t
        Ex = E0*cos(phase)
        By = B0*cos(phase)
        E_arrows[i].axis = vec(Ex,0,0)
        B_arrows[i].axis = vec(0,By,0)
```

**Observation:**  
- Red arrows = electric field (\(\mathbf{E}\), along x).  
- Blue arrows = magnetic field (\(\mathbf{B}\), along y).  
- Both oscillate perpendicular to each other and to the propagation axis (z).  

---

### Part B – Poynting Vector Visualization
Modify the code to compute and plot the **energy flow direction**:

```python
# GlowScript 3.2 VPython — Part B: Poynting Vector Visualization (Complete)
from vpython import *

scene.title = "EM Wave: Poynting Vector Visualization"
scene.width = 900
scene.height = 520
scene.background = color.white
scene.forward = vec(-1,-0.5,-1.2)

# ------------------------ Wave Parameters ------------------------
c     = 3e8             # speed of light
lam   = 2.0             # wavelength (arbitrary units)
f     = c/lam           # frequency
omega = 2*pi*f          # angular frequency
k     = 2*pi/lam        # wavenumber
E0    = 1.0             # E-field amplitude
B0    = E0/c            # B-field amplitude so that |E| = c|B|
# -----------------------------------------------------------------

# Axes (x: red; y: blue; z: green)
arrow(pos=vec(0,0,0), axis=vec(1,0,0), color=color.red,   shaftwidth=0.03)   # x-axis (E)
arrow(pos=vec(0,0,0), axis=vec(0,1,0), color=color.blue,  shaftwidth=0.03)   # y-axis (B)
arrow(pos=vec(0,0,0), axis=vec(0,0,1), color=color.green, shaftwidth=0.03)   # z-axis (propagation)

# Sample points along +z
N  = 25
dz = 0.2

# Field arrows
E_arrows = []
B_arrows = []
S_arrows = []  # Poynting vector arrows (energy flow)

for i in range(N):
    z = i*dz
    # Start with zero-length axes; we'll update in the loop
    E_arrows.append(arrow(pos=vec(0,0,z), axis=vec(0,0,0), color=color.red,   shaftwidth=0.02))
    B_arrows.append(arrow(pos=vec(0,0,z), axis=vec(0,0,0), color=color.blue,  shaftwidth=0.02))
    S_arrows.append(arrow(pos=vec(0,0,z), axis=vec(0,0,0), color=color.green, shaftwidth=0.02))

label(pos=vec(0, 0, N*dz+0.5), text="Red=E (x̂), Blue=B (ŷ), Green=S (energy flow)", box=False, color=color.black)

t  = 0.0
dt = 0.02

while True:
    rate(30)
    t += dt
    for i in range(N):
        z = i*dz
        phase = k*z - omega*t

        # Plane wave along +z with E || x, B || y (in phase)
        Ex = E0*cos(phase)
        By = B0*cos(phase)

        # Update E and B arrows
        E_arrows[i].axis = vec(Ex, 0, 0)    # E along x
        B_arrows[i].axis = vec(0, By, 0)    # B along y

        # Poynting vector S ∝ E × B (direction only for visualization)
        S_vec = cross(vec(Ex,0,0), vec(0,By,0))  # = (0,0, Ex*By)
        if mag(S_vec) > 1e-12:
            S_arrows[i].axis = norm(S_vec)*0.5   # scale for visibility
        else:
            S_arrows[i].axis = vec(0,0,0)

```

**Observation:** The green arrows (\(\mathbf{S}\)) always point along +z, indicating EM energy flow.  

---


### Part C – Polarization Variations
This section shows how to simulate **linear polarization along y** and **circular polarization** (right-hand and left-hand).

```python
# GlowScript 3.2 VPython — Part C: Polarization Variations
from vpython import *

scene.title = "EM Wave Polarization (Linear-Y / Circular)"
scene.width = 900
scene.height = 520
scene.background = color.white
scene.forward = vec(-1,-0.5,-1.2)

# ------------------------ Parameters ------------------------
c   = 3e8
lam = 2.0
f   = c/lam
omega = 2*pi*f
k     = 2*pi/lam
E0    = 1.0

# Choose polarization: 'linear_y', 'circular_RH', 'circular_LH'
mode = 'linear_y'       # change to 'circular_RH' or 'circular_LH'
# ------------------------------------------------------------

# Axes (x: red; y: blue; z: green)
arrow(pos=vec(0,0,0), axis=vec(1,0,0), color=color.red,   shaftwidth=0.03)   # x
arrow(pos=vec(0,0,0), axis=vec(0,1,0), color=color.blue,  shaftwidth=0.03)   # y
arrow(pos=vec(0,0,0), axis=vec(0,0,1), color=color.green, shaftwidth=0.03)   # z

# Discrete sample arrows along +z
N  = 25
dz = 0.2
E_arrows, B_arrows, S_arrows = [], [], []
for i in range(N):
    z = i*dz
    E_arrows.append(arrow(pos=vec(0,0,z), axis=vec(0,0,0), color=color.red,   shaftwidth=0.02))
    B_arrows.append(arrow(pos=vec(0,0,z), axis=vec(0,0,0), color=color.blue,  shaftwidth=0.02))
    S_arrows.append(arrow(pos=vec(0,0,z), axis=vec(0,0,0), color=color.green, shaftwidth=0.02))

# Helper: enforce B = (k_hat × E)/c
def B_from_E(Ex, Ey):
    # k_hat = ẑ = (0,0,1). k_hat × E = (-Ey, Ex, 0)
    return (-Ey/c, Ex/c, 0.0)

# Polarization modes
def E_components(phase, mode):
    if mode == 'linear_y':
        Ex = 0.0
        Ey = E0*cos(phase)
    elif mode == 'circular_RH':
        Ex = E0*cos(phase)
        Ey = E0*sin(phase)
    elif mode == 'circular_LH':
        Ex = E0*cos(phase)
        Ey = -E0*sin(phase)
    else:
        Ex = E0*cos(phase); Ey = 0.0
    return Ex, Ey

# Label
label(pos=vec(0, 0, N*dz+0.6), text=f"Mode: {mode}\nRed=E, Blue=B, Green=S", box=False, color=color.black)

t  = 0.0
dt = 0.02

while True:
    rate(30)
    t += dt
    for i in range(N):
        z = i*dz
        phase = k*z - omega*t

        Ex, Ey = E_components(phase, mode)
        Bx, By, Bz = B_from_E(Ex, Ey)

        E_arrows[i].axis = vec(Ex, Ey, 0)
        B_arrows[i].axis = vec(Bx, By, Bz)

        S_vec = cross(vec(Ex, Ey, 0), vec(Bx, By, Bz))
        if mag(S_vec) > 1e-12:
            S_arrows[i].axis = norm(S_vec)*0.5
        else:
            S_arrows[i].axis = vec(0,0,0)
```

**Observation:**  
- Linear (y): \(\mathbf{E}\) points along y, \(\mathbf{B}\) along x.  
- Circular RH: \(\mathbf{E}\) tip rotates clockwise (seen along +z).  
- Circular LH: \(\mathbf{E}\) tip rotates counter-clockwise.  
- In all cases, \(\mathbf{S}\) points along +z.  

---.  

---

## 5. Observations
- The electric field and magnetic field are mutually perpendicular.  
- Both are sinusoidal and in phase.  
- The Poynting vector shows constant propagation along the +z direction.  
- Polarization can be visualized by altering the E-field components.  

---

## 6. Lab Questions
1. How are the directions of \(\mathbf{E}, \mathbf{B}, \mathbf{k}\) related?  
2. What is the phase relationship between the electric and magnetic fields?  
3. How does the Poynting vector relate to energy transport?  
4. Simulate circular polarization. How do the tip trajectories of \(\mathbf{E}\) vectors differ from linear polarization?  
5. If the wave propagates in \(-z\) instead of \(+z\), how does the code change?  

---

## 7. Conclusion
This lab demonstrates the geometry of electromagnetic waves: \(\mathbf{E}, \mathbf{B}, \mathbf{k}\) are mutually orthogonal.  
The **Poynting vector** provides a direct way to visualize energy flow. VPython enables students to see, in real time, how Maxwell’s equations predict wave propagation.

