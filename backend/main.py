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

    text_content = f"{title} {description}"
    sentiment = analyze_sentiment(text_content)

    return jsonify({"sentiment": sentiment, "video_id": video_id})

app.run(debug=True, port=5000)






