# LAB 09: VPython Simulation — Standing Wave on a String  

## 🎯 Objectives
- To simulate a **standing wave** on a string using VPython.  
- To understand the mathematical form of a standing wave:  
  \[ y(x,t) = 2A \sin(kx) \cos(\omega t) \]  
- To observe **nodes** (points of no displacement) and **antinodes** (points of maximum displacement).  
- To explore the relation between wavelength, frequency, and harmonic modes in standing waves.  

---

## 📖 Background Theory

A **standing wave** is formed by the superposition of two identical traveling waves moving in opposite directions:  
\[ y_1(x,t) = A \sin(kx - \omega t), \quad y_2(x,t) = A \sin(kx + \omega t) \]

Adding these gives:  
\[ y(x,t) = y_1 + y_2 = 2A \sin(kx)\cos(\omega t) \]

Where:  
- A = amplitude of each traveling wave,  
- k = 2π/λ = wave number,  
- ω = 2πf = angular frequency,  
- λ = wavelength,  
- f = frequency.  

**Nodes:** occur at sin(kx) = 0 → zero displacement.  
**Antinodes:** occur at sin(kx) = ±1 → maximum displacement.  

In a string of length L fixed at both ends, allowed wavelengths are:  
\[ \lambda_n = \frac{2L}{n}, \quad n = 1,2,3,... \]

---

## 🛠 Materials and Software
- Python 3.x  
- VPython library (`vpython`) installed (`pip install vpython`)  
- Jupyter Notebook or any Python IDE  

---

## 🧪 Experimental Procedure
1. **Set Parameters**: Choose amplitude A, string length L, frequency f, and mode number n.  
2. **Compute Wave Properties**: Calculate wavelength λ = 2L/n, wave number k = 2π/λ, and angular frequency ω = 2πf.  
3. **Model the String**: Use VPython’s `curve` to create discrete points along the x-axis.  
4. **Update with Standing Wave Equation**: For each time step, update displacement y(x,t) = 2A sin(kx)cos(ωt).  
5. **Observe**: Identify nodes and antinodes, and compare with theory.  

---

## 💻 VPython Code Example

```python
from vpython import *  # provides vector, curve, sin, cos, pi, rate, color

scene.title = "Standing Wave on a String (no NumPy)"
scene.background = color.white

# Parameters
A = 1.0      # amplitude of each traveling wave (m)
L = 20.0     # string length (m)
n = 2        # mode number (harmonic)
f = 1.0      # frequency (Hz)

lam = 2*L/n         # wavelength
k = 2*pi/lam        # wave number
omega = 2*pi*f      # angular frequency

N = 200
dx = L/(N-1)
x_vals = [i*dx for i in range(N)]

string = curve(color=color.blue, radius=0.05)
for x in x_vals:
    string.append(vector(x, 0, 0))

t = 0.0
dt = 0.02

while True:
    rate(50)
    t += dt
    for i in range(N):
        x = x_vals[i]
        # y(x,t) = 2A sin(kx) cos(ωt)
        y = 2*A * sin(k*x) * cos(omega*t)
        string.modify(i, vector(x, y, 0))

```

---

## 📊 Observations
- The wave exhibits **fixed ends** at x = 0 and x = L (nodes).  
- **Antinodes** oscillate with maximum amplitude.  
- Increasing **mode number n** increases the number of nodes and antinodes.  
- Frequency determines how fast the string oscillates, while mode number determines its shape.  

---

## 📝 Analysis
1. Verify that the simulated standing wave satisfies:  
   \[ y(x,t) = 2A \sin(kx)\cos(\omega t) \]  
2. Count the number of nodes and compare with n+1 (including both ends).  
3. Verify that wavelength matches λ = 2L/n.  
4. Explore the relationship between f, L, and the mode number n.  

---

## ❓ Post-Lab Questions
1. What is the difference between a traveling wave and a standing wave?  
2. How do nodes and antinodes form in a standing wave?  
3. For n=3, how many nodes and antinodes should you observe?  
4. If the string length doubles, how does the fundamental frequency change?  
5. How can standing waves explain the behavior of musical instruments (e.g., guitar, violin)?  

