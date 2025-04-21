from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'

# Create a SocketIO instance
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(msg):
    print(f"Message: {msg}")
    send(msg, broadcast=True)

if __name__ == '__main__':
    # Run the app (allow_unsafe_werkzeug is only for development on Render etc.)
    socketio.run(app, debug=True, allow_unsafe_werkzeug=True)
