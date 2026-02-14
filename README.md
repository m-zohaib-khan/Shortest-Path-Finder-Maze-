# 🧩 Maze Solver Visualization (BFS Algorithm) — Python

A terminal-based **Maze Solver Visualizer** built using Python’s `curses` library.  
The project demonstrates how the **Breadth-First Search (BFS)** algorithm finds the shortest path inside a maze while visualizing the search process step by step.

This project combines **Data Structures & Algorithms (DSA)** with visualization, making it an excellent learning project for understanding graph traversal.

---

## 🚀 Project Highlights

✨ Maze pathfinding using Breadth-First Search (BFS)  
🧠 Real-time algorithm visualization in terminal  
🎨 Colored maze rendering using `curses`  
📍 Automatic start and end detection  
🧱 Queue-based shortest path search  
📊 Step-by-step animation of exploration

---

## 🧠 How It Works

### 1️⃣ Maze Representation
The maze is stored as a 2D list:

- `#` → Wall (blocked cell)
- `O` → Start position
- `X` → Goal position
- `" "` → Free path

---

### 2️⃣ BFS Algorithm

The program:

1. Finds the starting point (`O`)
2. Uses a **Queue** to explore paths level by level
3. Tracks visited positions
4. Expands neighbors (up, down, left, right)
5. Stops when the goal (`X`) is reached

Because BFS explores level-wise, it always finds the **shortest path**.

---

### 3️⃣ Visualization

Using Python’s `curses` module:

- Maze is displayed in the terminal
- Explored path is highlighted in real-time
- Screen updates after every step for animation

---

## 🖼️ Example Output (Conceptual)

![maze](https://github.com/user-attachments/assets/f1c0ec94-c657-4153-90a1-e139d452f603)
