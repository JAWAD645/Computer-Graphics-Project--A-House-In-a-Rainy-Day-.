

# Rainy House 🌧🏠

A **Python OpenGL** computer graphics project that depicts a cozy house under a rainstorm. The scene includes interactive features such as toggling between day and night modes and moving the rain direction. Built with **PyOpenGL**, this project is a great demonstration of 2D drawing and animation techniques.



## 📌 Overview

The *Rainy House* renders a detailed 2D house with:

* **Walls, roof, windows, and door** drawn using OpenGL primitives.
* **Raindrops** falling from above, animated frame by frame.
* Ability to **switch between day and night backgrounds**.
* Control over **rain direction** using the keyboard.

This project demonstrates:

* Use of **OpenGL line and triangle primitives**.
* Real-time rain particle generation and motion.
* Interactive keyboard controls for scene manipulation.



## 🛠 Features & Functionality

### 🏠 House Rendering

* **Walls:** Green outline with rectangular structure.
* **Roof:** Red triangle roof.
* **Windows:** Symmetrical left and right windows.
* **Door:** Yellow-colored door at the center.

### 🌧 Rain Animation

* Raindrops generated at random horizontal positions.
* Falling motion simulated by decreasing vertical positions.
* Continuous regeneration of raindrops for a dynamic effect.

### ☀🌙 Day/Night Mode

* **Day Mode:** White background.
* **Night Mode:** Black background.

### 🎮 Controls

| Action               | Key             |
| -------------------- | --------------- |
| Switch to Day Mode   | `d`             |
| Switch to Night Mode | `n`             |
| Move Rain Right      | **Right Arrow** |
| Move Rain Left       | **Left Arrow**  |



## 📐 Technical Details

* **Language:** Python 3
* **Libraries:** PyOpenGL, random
* **Window Size:** 750×750 pixels
* **Projection:** Perspective (`gluPerspective`)
* **Rain Physics:** Simple linear falling motion, no collision detection.



## 🖼 Image Previews


View(In day):

<img src="assets/ring.jpg" alt="Ring Generator Preview" width="400">

View(In night):

<img src="assets/ring.jpg" alt="Ring Generator Preview" width="400">

Play the demo:

<img src="assets/ring.jpg" alt="Ring Generator Preview" width="400">


## 📥 Installation & Running

### 1️⃣ Install Python

Ensure **Python 3.8+** is installed.
[Download Python](https://www.python.org/downloads/)

### 2️⃣ Install Required Libraries

```bash
pip install PyOpenGL PyOpenGL_accelerate
```

### 3️⃣ Download the Project

```bash
git clone https://github.com/<your-username>/rainy-house.git
cd rainy-house
```

### 4️⃣ Run the Program

```bash
python "Rainy House.py"
```



## 🔮 Future Improvements

* Add sound effects for rain.
* Animate clouds or lightning strikes.
* Make the rain intensity adjustable.



## 👨‍💻 Author

**Jaawad Tashick**
*Computer Science Graduate *

