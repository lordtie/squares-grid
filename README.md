# 🎨 Squares Grid – Interactive Pixel Drawing App

**Squares Grid** is a web-based interactive drawing board built with **Flask**, **Socket.IO**, and **JavaScript** that lets users paint a grid of squares in real time.  
Each cell in the 16×16 grid can be colored using a color picker, erased with a right-click, or painted across by dragging your mouse. It’s lightweight, responsive, and designed to scale perfectly on both desktop and mobile devices.

---

## 🚀 Features

- 🎨 **Color Picker:** Choose any color to paint squares.
- 🧹 **Right-click Erase:** Instantly clear individual cells.
- 🖱️ **Click & Drag Painting:** Draw freely across the grid.
- ⚡ **Real-Time Updates (Socket.IO):** See instant changes across connected users.
- 📱 **Responsive Design:** Automatically fits browser and mobile screens.
- 💡 **Expandable Design:** Add usernames, multiplayer modes, or save/load features.

---

## 🧰 Tech Stack

| Layer | Technology |
|-------|-------------|
| **Frontend** | HTML, CSS, JavaScript |
| **Backend** | Python (Flask) |
| **Real-Time Engine** | Flask-SocketIO + Eventlet |
| **Hosting** | GitHub + Render |

---

## 🏗️ Future Improvements

- 👤 Add usernames or profile colors  
- 💾 Save and load grid states  
- 🎮 Create multiplayer mini-games (e.g., tic-tac-toe, color wars)  
- 💬 Add a small chat for collaborative drawing  

---

## ⚙️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/lordtie/squares-grid.git
   cd squares-grid
