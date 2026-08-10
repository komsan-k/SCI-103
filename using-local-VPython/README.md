# Running VPython on a Local Computer

Yes. **VPython works very well on a local computer** and is generally more reliable than Google Colab.

## Option 1: Jupyter Notebook (Recommended)

### 1. Install Python

Download and install Python from:

- https://www.python.org/downloads/

> **Note:** During installation, check **"Add Python to PATH."**

### 2. Install VPython and Jupyter

Open **Command Prompt** (Windows) or **Terminal** (macOS/Linux):

```bash
pip install vpython notebook
```

### 3. Launch Jupyter Notebook

```bash
jupyter notebook
```

A browser window will open automatically.

### 4. Run Your First VPython Program

```python
from vpython import *

scene.title = "SCI-103 Physics I"

ball = sphere(
    pos=vector(0,0,0),
    radius=0.5,
    color=color.red
)

arrow(axis=vector(2,0,0), color=color.green)
```

A 3D scene will appear directly inside the notebook.

---

## Option 2: Visual Studio Code (VS Code)

Install VPython:

```bash
pip install vpython
```

Example:

```python
from vpython import *

box(color=color.blue)
sphere(pos=vector(1,0,0), color=color.red)

while True:
    rate(60)
```

A browser window will open automatically to display the 3D animation.

---

## Option 3: Spyder

Install VPython:

```bash
pip install vpython
```

Run the same VPython code. The visualization will open in your web browser.

---

# Example: Projectile Motion

```python
from vpython import *

ball = sphere(
    pos=vector(0,0,0),
    radius=0.1,
    color=color.red,
    make_trail=True
)

ball.velocity = vector(5,8,0)

g = vector(0,-9.81,0)
dt = 0.01

while ball.pos.y >= 0:
    rate(100)
    ball.velocity += g * dt
    ball.pos += ball.velocity * dt
```

This example simulates projectile motion and displays its trajectory in 3D.

---

# Comparison

| Environment | Difficulty | Performance | Recommendation |
|--------------|------------|-------------|----------------|
| **Jupyter Notebook** | Easy | ⭐⭐⭐⭐⭐ | ⭐ Best Overall |
| **VS Code** | Easy | ⭐⭐⭐⭐⭐ | Excellent |
| **Spyder** | Easy | ⭐⭐⭐⭐☆ | Good |
| **Google Colab** | Medium | ⭐⭐☆☆☆ | Limited VPython support |
| **GlowScript VPython** | Very Easy | ⭐⭐⭐⭐⭐ | Best for teaching without installation |


