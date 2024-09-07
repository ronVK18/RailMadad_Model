import json
from flask import Flask, render_template, request
# import os
import whisper
model=whisper.load_model('base')
app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/audio', methods=['POST'])
def upload_audio():
    if 'ronak' in request.files:
        file = request.files['ronak']
        if file.filename != '':
            result = model.transcribe("harvard.wav",fp16=False )
            return {'text': result["text"]}
    return 'Please send an audio file using POST request'
    


@app.route('/send_json', methods=['POST'])
def send_json_data():
    if request.method == 'POST':
        data = request.get_json()
        return json.dumps({'message': 'Data received:', 'data': data})
    return 'Please send JSON data using POST request'

if __name__ == '__main__':
    app.run(debug=True)