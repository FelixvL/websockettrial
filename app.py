from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
# Zorg voor een geheime sleutel voor sessiebeheer
app.config['SECRET_KEY'] = 'geheime_sleutel'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('bestand.html')

@socketio.on('message')
def handle_message(message):
    print('Ontvangen bericht: ' + message)
    socketio.send('Echo: ' + message)

if __name__ == '__main__':
    socketio.run(app, debug=True)
