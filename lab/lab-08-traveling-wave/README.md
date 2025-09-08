# LAB 08: VPython Simulation — Traveling Wave on a String  

## 🎯 Objectives
- To visualize a **traveling sinusoidal wave** on a string using VPython.  
- To understand the mathematical form of a traveling wave:
  \[ y(x,t) = A \sin(kx - \omega t) \]
- To observe how **wave speed, frequency, and wavelength** affect the motion of the string.  
- To develop computational skills by implementing a physics concept in Python.  

---

## 📖 Background Theory

A **traveling wave** on a string can be described as:
\[ y(x,t) = A \sin(kx - \omega t) \]
where:  
- A = amplitude (maximum displacement),  
- k = 2π/λ = wave number,  
- ω = 2πf = angular frequency,  
- λ = wavelength,  
- f = frequency,  
- v = ω/k = wave speed.  

This equation describes a **sinusoidal disturbance** that moves without changing shape along the +x-direction. VPython allows us to **animate the displacement of points on the string** to simulate this wave.  

---

## 🛠 Materials and Software
- Python 3.x  
- VPython library (`vpython`) installed (`pip install vpython`)  
- Jupyter Notebook or any Python IDE  

---

## 🧪 Experimental Procedure

1. **Define Parameters**  
   - Set amplitude A, wavelength λ, frequency f.  
   - Compute angular frequency ω = 2πf and wave number k = 2π/λ.  

2. **Initialize the String**  
   - Represent the string as a set of points along the x-axis using VPython’s `curve` object.  

3. **Update Wave Motion**  
   - For each time step, compute the displacement y(x,t) of each point.  
   - Update the curve to animate the traveling wave.  

4. **Run Simulation**  
   - Observe how the wave propagates with time.  
   - Experiment with different values of amplitude, wavelength, and frequency.  

---

## 💻 VPython Code Example

```python
from vpython import *
import numpy as np

# Scene setup
scene.title = "Traveling Wave on a String"
scene.width = 900
scene.height = 400
scene.background = color.white

# Parameters
A = 1.0              # Amplitude (m)
lam = 4.0            # Wavelength (m)
f = 1.0              # Frequency (Hz)
k = 2*np.pi/lam      # Wave number
omega = 2*np.pi*f    # Angular frequency
v = omega/k          # Wave speed

L = 20               # Length of string (m)
N = 200              # Number of points
dx = L/N             # Spacing
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
        y = A*np.sin(k*x - omega*t)
        string.modify(i, vector(x, y, 0))
```

---

## 📊 Observations
- The wave moves along the **+x-axis** with constant speed.  
- Changing **amplitude** modifies the maximum displacement.  
- Changing **wavelength** modifies how many peaks appear along the string.  
- Changing **frequency** modifies how fast the wave oscillates.  

---

## 📝 Analysis
1. Measure the wave speed from the simulation and compare it with:
   \[ v = \frac{\omega}{k} \]
2. Verify that doubling the frequency doubles the wave speed if wavelength is held constant.  
3. Investigate what happens if both λ and f are changed while keeping v constant.  

---

## ❓ Post-Lab Questions
1. What is the mathematical form of the wave you simulated?  
2. How does the wavelength affect the appearance of the wave?  
3. If frequency is doubled, what happens to the wave speed and wave profile?  
4. How could you modify the simulation to represent a **standing wave**?  
5. In real strings (like a guitar string), what physical factors determine wave speed?  

