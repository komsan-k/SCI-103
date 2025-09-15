# Lab 11: Visualization of Electric Fields using VPython

## 1. Objectives
- Understand the concept of electric fields due to point charges.  
- Visualize electric field vectors, field lines, and potentials using VPython (GlowScript).  
- Investigate the effects of charge magnitude, polarity, and separation on the electric field.  
- Compare simulation results with theoretical expectations from Coulomb’s law.  

---

## 2. Background Theory
The electric field **E** at a point **r** due to a point charge **q** is given by:

$$
\mathbf{E}(\mathbf{r}) = \frac{1}{4 \pi \varepsilon_0} \, \frac{q}{|\mathbf{r} - \mathbf{r_q}|^3} \, (\mathbf{r} - \mathbf{r_q})
$$
 $$
  |\mathbf{E}| \propto \frac{1}{r^2}
  $$
- **Direction:** away from positive charges, toward negative charges.  
- **Magnitude:** decreases with the square of the distance

 $$
  |\mathbf{E}| \propto \frac{1}{r^2}
  $$
  
- **Superposition principle:** the total field is the vector sum of contributions from all charges.  

**Visualization tools in VPython:**  
- Arrows → represent direction and relative strength of **E**.  
- Curves → represent electric field lines.  
- Colors → represent electric potential values.  

---

## 3. Software & Setup
- GlowScript VPython (3.2+) accessible at [https://glowscript.org](https://glowscript.org)  
- Web browser (Chrome or Firefox recommended)  
- No installation required  

---

## 4. Lab Procedure

### Part A – Electric Field of a Single Charge
```python
# GlowScript 3.2 VPython – Single Charge Field
from vpython import *

scene.title = "Electric Field of a Single Point Charge"
scene.background = color.white

eps0 = 8.854e-12
k = 1/(4*pi*eps0)

q = 1e-9   # +1 nC
rq = vec(0,0,0)
charge = sphere(pos=rq, radius=0.1, color=color.red)

L = 2.0
N = 7
step = (2*L)/(N-1)

for i in range(N):
    for j in range(N):
        for kx in range(N):
            r = vec(-L + i*step, -L + j*step, -L + kx*step)
            if mag(r-rq) < 0.2:
                continue
            R = r - rq
            E = k*q*R/(mag(R)**3)
            arrow(pos=r, axis=norm(E)*0.1, color=color.blue, shaftwidth=0.02)
```

- Observe how arrows radiate outward.  
- Modify `q = -1e-9` to see arrows point inward.  

---

### Part B – Dipole Field
```python
# GlowScript 3.2 VPython – Dipole
scene.title = "Electric Field of a Dipole"
scene.background = color.white

eps0 = 8.854e-12
k = 1/(4*pi*eps0)

d = 0.5
q = 1e-9

rp = vec(-d, 0, 0)
rn = vec(+d, 0, 0)
sphere(pos=rp, radius=0.1, color=color.red)
sphere(pos=rn, radius=0.1, color=color.blue)

L = 2.0
N = 15
step = (2*L)/(N-1)

for i in range(N):
    for j in range(N):
        r = vec(-L + i*step, -L + j*step, 0)
        if mag(r-rp)<0.2 or mag(r-rn)<0.2:
            continue
        Ep = k*q*(r-rp)/(mag(r-rp)**3)
        En = k*(-q)*(r-rn)/(mag(r-rn)**3)
        E = Ep + En
        arrow(pos=r, axis=norm(E)*0.1, color=color.black, shaftwidth=0.02)
```

- Observe the dipole field symmetry.  
- Vary separation `d` and charges to see effects.  

---

### Part C – Field Lines (Stream Tracing)
```python
# GlowScript 3.2 VPython – Field Lines
scene.title = "Electric Field Lines"
scene.background = color.white

eps0 = 8.854e-12
k = 1/(4*pi*eps0)

charges = [
    {'q': +1e-9, 'r': vec(-0.5,0,0)},
    {'q': -1e-9, 'r': vec(+0.5,0,0)}
]

for c in charges:
    sphere(pos=c['r'], radius=0.1, color=color.red if c['q']>0 else color.blue)

def Efield(r):
    E = vec(0,0,0)
    for c in charges:
        R = r - c['r']
        d = mag(R)
        if d < 0.05: continue
        E += k*c['q']*R/d**3
    return E

# Seed points around + charge
seeds = [charges[0]['r']+0.15*vec(cos(theta),sin(theta),0) for theta in arange(0,2*pi,pi/8)]

for s in seeds:
    path = curve(color=color.orange, radius=0.01)
    r = vec(s)
    for step in range(500):
        path.append(r)
        E = Efield(r)
        if mag(E)<1e-6: break
        r = r + norm(E)*0.05
```

---

## 5. Observations
- Record screenshots of single charge, dipole, and field lines.  
- Note differences when changing magnitude/sign of charges.  
- Compare simulation vector directions with theory.  

---

## 6. Lab Questions
1. For a single positive charge, describe how vector length changes with distance. Does it match the \(1/r^2\) law?  
2. What happens to the field lines when you increase the dipole separation?  
3. If both charges are positive, how do the field lines change?  
4. Explain why field lines never cross.  
5. In Part C, what indicates the relative strength of each charge?  

---

## 7. Conclusion
This lab demonstrates how VPython can bring abstract vector field concepts into visual, interactive 3D form. Through charge manipulation, students observe electric field structures and gain intuition about Coulomb’s law, dipole symmetry, and superposition.

