from flask import Flask, request, render_template, jsonify
from emotion_detection import emotion_detector  # veya paketini doğru import et

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    """Render the main page with the text input form."""
    return render_template("index.html")

@app.route("/emotionDetector", methods=["GET"])
def detect_emotion():
    """Process the text input and return the detected emotion as JSON.
    
    Returns an error message if text is empty or invalid.
    """
    text_to_analyze = request.args.get("textToAnalyze", "")

    # emotion_detector fonksiyonu boş veya hatalı girişleri yönetiyor
    result = emotion_detector(text_to_analyze)

    if result.get("dominant_emotion") is None:
        return jsonify({"error": "Invalid text! Please try again!"})

    return jsonify(result)

if __name__ == "__main__":
    """Start the Flask server on all interfaces, port 5000."""
    app.run(host="0.0.0.0", port=5000, debug=True)
