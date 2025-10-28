import json
from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")  # Allow local testing

GRID_FILE = 'grid_colors.json'

# Load saved colors or start empty
try:
    with open(GRID_FILE, 'r') as f:
        grid_colors = json.load(f)
except FileNotFoundError:
    grid_colors = {}

@app.route('/')
def index():
    return render_template('index.html', grid_colors=grid_colors)

@socketio.on('update_color')
def handle_update_color(data):
    square_id = data['square_id']
    color = data['color']
    grid_colors[square_id] = color

    # Save to file
    with open(GRID_FILE, 'w') as f:
        json.dump(grid_colors, f)

    # Broadcast to all clients
    emit('color_update', {'square_id': square_id, 'color': color}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', debug=True)
