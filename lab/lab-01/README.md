# LAB01: Introduction to VPython

**Course:** SCI-103 Physics I  
**Instructor:** K. Kanjanasit  
**Academic Year:** 1/2025  

---

## Goals
In this lab, you will learn the fundamentals of programming and 3D visualization using **VPython**. By the end of the lab, you should be able to:

- Use the GlowScript IDE to create and run VPython programs.  
- Write basic Python code for arithmetic and vector operations.  
- Implement loops and conditional structures.  
- Create and manipulate 3D geometric objects.  
- Combine 3D graphics with simple animations.  

---

## I. Getting Started

### A. GlowScript IDE
1. Sign in at [GlowScript](https://www.glowscript.org/).  
2. Create or open a folder under **My Programs**.  
3. Create a new program and give it a file name.  

By default, the VPython module is preloaded, so you do not need to type `from vpython import *`. This environment allows you to perform 3D animations easily, while also supporting mathematical functions from Python.

---

### B. Basic Python Programming
Type and execute the following commands in the editor. Python is case-sensitive. The results will appear in the output area. Record and interpret the outputs.

```python
print(6 + 5)    
print(2**3)    
a = 3
b = 5
print(a - b)    
print("Hello World!")  
print("a + b")   
print((a + b) * (a - b))  

c = vector(0,1,0)    
d = vector(1,0,0)    
print(c + d)   
print(dot(c, d))    
print(cross(c, d))  
print(mag(c + d))  
print(pi)   
print(sin(pi/3))   
print(cos(0))   
print(sin(pi))   
print(cos(pi/2))   
print(4.0/3.0)   
print(4/3)   
```

**Question:** What is the distinction between `4` and `4.0`?  

---

### C. Loops
Loops allow repeated execution while a condition is true. Indentation is essential.

```python
i = 1
while i < 11:
    print(i)
    i = i + 1
```

**Task:** Explain the output and your understanding of how the loop executes.  

---

### D. 3D Geometric Objects
Start a new program and enter:

```python
ball = sphere(pos=vec(0,0,0), radius=0.5, color=color.red)
wall1 = box(pos=vec(-10,0,0), length=0.1, height=10, width=5, color=color.blue)
wall2 = box(pos=vec(10,0,0), length=0.1, height=10, width=5, color=color.blue)
```

This produces a 3D display of a red ball between two blue walls. You can rotate or zoom using your mouse.  

Try modifying object attributes, for example:

```python
ball.pos.x = ball.pos.x + 5
```

**Task:** Explain the changes in output and their meaning.  

---

### E. Animation: Combining 3D Objects and Loops
Enhance the program by adding motion:

```python
v = 1.0    # initial velocity
dt = 0.1
while True:
    rate(100)
    ball.pos.x = ball.pos.x + v*dt
```

**Task:** Describe the animation and explain how the ball’s position is updated frame by frame.  
Try changing `x` to `y` to move the ball vertically.  

---

## II. Additional Resources
You are using only a small subset of Python and VPython. For further study:

- [VPython Web Documentation](http://vpython.org/webdoc/visual/index.html)  
- [Python Official Tutorial](https://docs.python.org/3/tutorial/)  
- Mark Lutz, *Learning Python*  
- John Zelle, *Python Programming: An Introduction to Computer Science*  

