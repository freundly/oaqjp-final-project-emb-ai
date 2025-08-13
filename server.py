from flask import Flask, request, render_template, jsonify
from emotion_detection import emotion_detector  # veya paketini doğru import et

app = Flask(__name__)

# Root route
@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")

# Formdan gelen veriyi işle
@app.route("/emotionDetector", methods=["GET"])
def detect_emotion():
    text_to_analyze = request.args.get("textToAnalyze", "")

    # emotion_detector fonksiyonu artık boş veya hatalı girişleri yönetiyor
    result = emotion_detector(text_to_analyze)

    # dominant_emotion None ise kullanıcıya mesaj göster
    if result.get("dominant_emotion") is None:
        return jsonify({"error": "Invalid text! Please try again!"})

    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
