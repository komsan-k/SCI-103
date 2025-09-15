# Lab 12: Visualization of Magnetic Fields using VPython

## 1. Objectives
- Understand the concept of magnetic fields due to current-carrying conductors and dipoles.  
- Visualize magnetic field vectors and field lines using VPython (GlowScript).  
- Study the effect of current direction and magnitude on the magnetic field.  
- Compare VPython visualizations with theoretical expectations from the **Biot–Savart law**.  

---

## 2. Background Theory
The **Biot–Savart law** gives the magnetic field **B** at point **r** due to a current element \(I d\mathbf{l}\):

$$
\mathbf{B}(\mathbf{r}) = \frac{\mu_0}{4 \pi} \int \frac{I \, d\mathbf{l} \times (\mathbf{r} - \mathbf{r'})}{|\mathbf{r} - \mathbf{r'}|^3}
$$

**Special cases:**

1. **Straight Long Wire:**

$$
B = \frac{\mu_0 I}{2 \pi r}
$$

Directed tangentially (right-hand rule).  

2. **Magnetic Dipole (Bar Magnet approximation):**

$$
\mathbf{B}(\mathbf{r}) = \frac{\mu_0}{4 \pi} \cdot \frac{3(\mathbf{m} \cdot \hat{r}) \hat{r} - \mathbf{m}}{|\mathbf{r}|^3}
$$

where \(\mathbf{m}\) is the magnetic dipole moment.  

---

## 3. Software & Setup
- GlowScript VPython (3.2+) accessible at [https://glowscript.org](https://glowscript.org)  
- A modern browser  
- No installation required  

---

## 4. Lab Procedure

### Part A – Magnetic Field of a Straight Current-Carrying Wire  
**Goal:** Show circular magnetic field vectors around a vertical wire.  

```python
# GlowScript 3.2 VPython – Magnetic Field of a Straight Wire
from vpython import *

scene.title = "Magnetic Field around a Straight Wire"
scene.background = color.white
scene.forward = vec(-1,-1,-1)

mu0 = 4*pi*1e-7
I = 5.0    # Current in Amps

# Represent the wire
wire = cylinder(pos=vec(0,-2,0), axis=vec(0,4,0), radius=0.05, color=color.gray(0.5))

# Lattice points around the wire
L = 2.0
N = 12
step = (2*L)/(N-1)

for i in range(N):
    for j in range(N):
        x = -L + i*step
        z = -L + j*step
        r = vec(x,0,z)
        if mag(r) < 0.2: 
            continue
        # Magnetic field magnitude (circular, tangential direction)
        r_mag = sqrt(x**2 + z**2)
        Bmag = mu0*I/(2*pi*r_mag)
        # Direction (phi-hat)
        phi_dir = norm(vec(-z,0,x))   # tangent to circle (right-hand rule)
        arrow(pos=r, axis=phi_dir*0.2, color=color.blue, shaftwidth=0.03)
```

**Observe:** Arrows form circles around the wire. Reversing `I` flips direction.  

---

### Part B – Magnetic Dipole (Bar Magnet Approximation)  
**Goal:** Show field lines similar to a bar magnet using the dipole equation.  

```python
# GlowScript 3.2 VPython – Magnetic Dipole
from vpython import *

scene.title = "Magnetic Field of a Dipole"
scene.background = color.white

mu0 = 4*pi*1e-7
m = vec(0,1,0)  # Dipole moment along y-axis

# Represent the dipole (bar magnet)
north = sphere(pos=vec(0,0.3,0), radius=0.1, color=color.red)
south = sphere(pos=vec(0,-0.3,0), radius=0.1, color=color.blue)
cylinder(pos=vec(0,-0.3,0), axis=vec(0,0.6,0), radius=0.05, color=color.gray(0.7))

def Bfield(r):
    R = r
    rmag = mag(R)
    if rmag < 0.2: return vec(0,0,0)
    return (mu0/(4*pi)) * ( (3*dot(m,R)*R/(rmag**5)) - (m/(rmag**3)) )

L = 2.0
N = 12
step = (2*L)/(N-1)

for i in range(N):
    for j in range(N):
        for k in range(N):
            r = vec(-L+i*step, -L+j*step, -L+k*step)
            if mag(r) < 0.3: 
                continue
            B = Bfield(r)
            if mag(B) == 0: 
                continue
            arrow(pos=r, axis=norm(B)*0.2, color=color.green, shaftwidth=0.03)
```

**Observe:** The field resembles a bar magnet, exiting the north pole (red) and entering the south pole (blue).  

---

### Part C – Magnetic Field Lines (Stream Tracing for Dipole)  

```python
# GlowScript 3.2 VPython – Dipole Field Lines
from vpython import *

scene.title = "Magnetic Dipole Field Lines"
scene.background = color.white

mu0 = 4*pi*1e-7
m = vec(0,1,0)

north = sphere(pos=vec(0,0.3,0), radius=0.1, color=color.red)
south = sphere(pos=vec(0,-0.3,0), radius=0.1, color=color.blue)

def Bfield(r):
    rmag = mag(r)
    if rmag < 0.2: return vec(0,0,0)
    return (mu0/(4*pi)) * ( (3*dot(m,r)*r/(rmag**5)) - (m/(rmag**3)) )

# Seed points around north pole
seeds = [vec(0.15*cos(theta),0.3,0.15*sin(theta)) for theta in arange(0,2*pi,pi/8)]

for s in seeds:
    path = curve(color=color.orange, radius=0.01)
    r = vec(s)
    for step in range(800):
        path.append(r)
        B = Bfield(r)
        if mag(B)<1e-6: break
        r = r + norm(B)*0.05
        if mag(r) > 3: break
```

**Observe:** Field lines emerge from north (red) and curve around into south (blue).  

---

## 5. Observations
- Record screenshots of the straight wire, dipole vectors, and field lines.  
- Note how reversing current changes field orientation.  
- Compare dipole simulation to textbook diagrams.  

---

## 6. Lab Questions
1. For the straight wire, how does the magnetic field magnitude depend on distance?  
2. What happens to the dipole field strength when the dipole moment vector **m** is doubled?  
3. Compare the magnetic field lines of a dipole to those of an electric dipole. What similarities and differences do you observe?  
4. How does the right-hand rule explain the vector directions in Part A?  
5. In the dipole visualization, what happens if you rotate the dipole moment to lie along the x-axis?  

---

## 7. Conclusion
This lab demonstrates how VPython simulations make the invisible magnetic field patterns visible in 3D. Students can directly connect the Biot–Savart law and dipole theory to vector field diagrams and field lines, reinforcing both qualitative intuition and quantitative understanding.

