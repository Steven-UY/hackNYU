from flask import Flask, request, jsonify
from sentimental_analysis import analyze_sentiment

app = Flask(__name__)

@app.route('/video', methods=['POST'])
def video() -> str:
    """
    we get the video data and insert it into the database

    """
    data = request.get_json()
    title = data['title']
    description = data['description']
    video_id = data['video_id']






