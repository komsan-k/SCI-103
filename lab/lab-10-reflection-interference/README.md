# LAB 10: VPython Simulation — Reflection and Interference of Waves  

## 🎯 Objectives
- To simulate **wave reflection** at a fixed boundary using VPython.  
- To visualize **interference** patterns produced by the superposition of incident and reflected waves.  
- To observe the formation of **nodes** and **antinodes** due to constructive and destructive interference.  
- To strengthen understanding of the principle of superposition in wave physics.  

---

## 📖 Background Theory

When a wave traveling along a string reaches a fixed boundary, it reflects with an **inverted phase**. The reflected wave combines with the incident wave, leading to **interference**.  

Incident wave:  
\[ y_i(x,t) = A \sin(kx - \omega t) \]  

Reflected wave:  
\[ y_r(x,t) = -A \sin(kx + \omega t) \]  

By superposition:  
\[ y(x,t) = y_i + y_r = A \sin(kx - \omega t) - A \sin(kx + \omega t) \]  

This simplifies to a **standing wave equation**:  
\[ y(x,t) = 2A \sin(kx) \cos(\omega t) \]  

Key points:  
- **Nodes:** points where destructive interference occurs (y=0).  
- **Antinodes:** points where constructive interference occurs (y=±2A).  
- Interference patterns depend on wavelength, frequency, and boundary conditions.  

---

## 🛠 Materials and Software
- Python 3.x  
- VPython library (`vpython`) installed (`pip install vpython`)  
- Jupyter Notebook or Python IDE  

---

## 🧪 Experimental Procedure
1. **Define Parameters:** Choose amplitude A, frequency f, string length L, and number of points.  
2. **Create Incident Wave:** Implement y_i(x,t) = A sin(kx - ωt).  
3. **Create Reflected Wave:** Implement y_r(x,t) = -A sin(kx + ωt).  
4. **Superpose Waves:** Add y_i and y_r to generate interference pattern.  
5. **Visualize in VPython:** Plot the resultant wave along the string.  
6. **Observe:** Identify nodes and antinodes and compare with theory.  

---

## 💻 VPython Code Example

```python
from vpython import *
import numpy as np

# Scene setup
scene.title = "Reflection and Interference of Waves"
scene.width = 900
scene.height = 400
scene.background = color.white

# Parameters
A = 1.0        # Amplitude (m)
L = 20.0       # Length of string (m)
f = 1.0        # Frequency (Hz)
lam = 10.0     # Wavelength (m)

k = 2*np.pi/lam       # Wave number
omega = 2*np.pi*f     # Angular frequency

N = 200               # Number of points
x_vals = np.linspace(0, L, N)

# Create string
string = curve(color=color.blue, radius=0.05)
for x in x_vals:
    string.append(vector(x, 0, 0))

t = 0
dt = 0.02

# Animation loop
while True:
    rate(50)
    t += dt
    for i, x in enumerate(x_vals):
        y_incident = A*np.sin(k*x - omega*t)
        y_reflected = -A*np.sin(k*x + omega*t)
        y = y_incident + y_reflected
        string.modify(i, vector(x, y, 0))
```

---

## 📊 Observations
- At the fixed end, the displacement is always zero (node).  
- Waves superpose to create **standing wave patterns**.  
- **Nodes** occur at fixed positions where waves cancel.  
- **Antinodes** oscillate with maximum amplitude due to constructive interference.  
- Changing wavelength or frequency alters the interference pattern.  

---

## 📝 Analysis
1. Verify that the simulation satisfies:  
   \[ y(x,t) = 2A \sin(kx) \cos(\omega t) \]  
2. Locate nodes in the simulation and compare with:  
   \[ x = n \frac{\lambda}{2}, \quad n=0,1,2,... \]  
3. Locate antinodes and compare with:  
   \[ x = \frac{\lambda}{4}, \frac{3\lambda}{4}, \frac{5\lambda}{4}, ... \]  
4. Measure wave speed and check consistency with:  
   \[ v = \frac{\omega}{k} \]  

---

## ❓ Post-Lab Questions
1. What happens to the phase of a wave when it reflects from a fixed boundary?  
2. How do constructive and destructive interference differ?  
3. If the boundary were free (not fixed), how would the reflected wave change?  
4. How many nodes and antinodes would be present if L = 20 m and λ = 10 m?  
5. How does interference explain resonance in musical instruments?  

