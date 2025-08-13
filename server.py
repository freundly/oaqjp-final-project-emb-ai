"""
server.py: Flask web application for emotion detection using Watson NLP.
Provides endpoints for detecting emotions from text input.
"""

from flask import Flask, request, render_template, jsonify
from emotion_detection import emotion_detector  # veya kendi paket yolunu kullan

app = Flask(__name__)


def get_emotion_result(text):
    """
    Runs emotion detection on the given text.

    Args:
        text (str): Text to analyze.

    Returns:
        dict: Dictionary containing emotion scores and dominant emotion.
              If text is blank or invalid, all values are None.
    """
    if not text.strip():
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
        }
    return emotion_detector(text)


@app.route("/", methods=["GET", "POST"])
def index():
    """
    Root route that renders the main index page.

    Returns:
        Response: Rendered HTML template for the index page.
    """
    return render_template("index.html")


@app.route("/emotionDetector", methods=["GET"])
def detect_emotion():
    """
    Endpoint to detect emotion from GET request parameter 'textToAnalyze'.

    Returns:
        Response: JSON response containing emotion scores and dominant emotion.
                  If input is invalid, returns error message.
    """
    text_to_analyze = request.args.get("textToAnalyze", "")
    result = get_emotion_result(text_to_analyze)
    if result["dominant_emotion"] is None:
        return jsonify({"error": "Invalid text! Please try again!"})
    return jsonify(result)


if __name__ == "__main__":
    # Start the Flask server on all interfaces, port 5000
    app.run(host="0.0.0.0", port=5000, debug=True)
