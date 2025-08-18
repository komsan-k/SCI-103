# LAB02: Vector Modelling  
**Course:** SCI-103 Physics I  
**Academic Year:** 1/2025  
**Instructor:** K. Kanjanasit  

---

## 🎯 Goals  
In this lab you will learn how to model and manipulate vectors in VPython.  
A vector is a directional quantity that has both a **magnitude** and a **direction**.  

**Mathematical relationship:**  
\`\`\`math
A = |A|  Â
\`\`\`

---

## 📐 Vector Math in VPython  
Vectors can be represented in two ways:
- As graphical **arrow** objects.  
- As numerical **vector(x, y, z)** objects.  

The `vector()` object stores components (x,y,z), while arrows allow visualization. VPython supports vector math directly.

---

## 🏹 Vector Objects  
| Name | Object Type | Color | Shaft Width |
|------|-------------|-------|-------------|
| A    | arrow       | red   | 0.2         |
| B    | arrow       | blue  | 0.2         |

Definitions:  
- `A.mag = 3.0`, `A.dir = (0.7071, 0.7071, 0)`  
- `B.mag = 4.0`, `B.dir = (0.7071, 0.7071, 0)`  

---

## 🧮 Vectors in Component Form  
```python
# Vectors in Component Form
A.axis = A.mag * A.dir
B.axis = B.mag * B.dir
```

---

## 🖨️ Printing Vectors  
```python
# Print Vectors
print("Vector A =", A.axis)
print("Vector B =", B.axis)
print("Ax =", A.axis.x)
print("Bx =", B.axis.x)
```

---

## ➕ Vector Addition  
```python
# Vector C
C = arrow(color=color.green, shaftwidth=0.2)
C.axis = A.axis + B.axis
C.mag = mag(C.axis)
C.dir = C.axis / C.mag
print("Vector C =", C.axis, " | Magnitude =", C.mag, " | Unit =", C.dir)
```

---

## 📏 Aligning Vectors (Head-to-Tail)  
```python
# Aligning Vectors
A.pos = vector(-2, -1, 0)
B.pos = A.pos + A.axis
C.pos = A.pos
```

---

## ⚽ Application: Velocity of a Ball  
```python
if ball.pos.x > wallR.pos.x:
    ball.velocity.x = -ball.velocity.x
```

---

## ✅ Checkpoint Questions  
1. What did you observe in the simulation?  
2. How did the ball move after the collision?  

---

## 📤 Submission  
Please submit your GlowScript link here:  
👉 [GlowScript](https://www.glowscript.org/)  

---

## 📚 References  
- [GlowScript VPython Documentation](https://www.glowscript.org/docs/VPythonDocs/primitives.html)  
- [Visual Introduction](https://www.glowscript.org/docs/VPythonDocs/VisualIntro.html)  

