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
# Add Poynting vector arrows (green)
S_arrows = []
for i in range(N):
    z = i*dz
    S = arrow(pos=vec(0,0,z), axis=vec(0,0,0), color=color.green, shaftwidth=0.02)
    S_arrows.append(S)

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
        # Poynting vector S = E x B / mu0
        S_vec = cross(vec(Ex,0,0), vec(0,By,0))
        S_arrows[i].axis = norm(S_vec)*0.5
```

**Observation:** The green arrows (\(\mathbf{S}\)) always point along +z, indicating EM energy flow.  

---

### Part C – Polarization Variations
1. Change the electric field direction to \(E_y = E_0 \cos(\text{phase})\) and magnetic to \(B_x\).  
2. Combine \(E_x\) and \(E_y\) components with phase shift to create **circular polarization**.  

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

