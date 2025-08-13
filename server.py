from flask import Flask, request, render_template, jsonify
from emotion_detection import emotion_detector  # senin paket yolu

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def emotionDetector():
    if request.method == 'POST':
        text_to_analyze = request.form.get('text')  # formdan gelen veri
        if not text_to_analyze:
            return jsonify({"error": "No text provided"}), 400

        # Emotion Detection fonksiyonunu çağır
        result = emotion_detector(text_to_analyze)

        # Sonucu JSON olarak döndür
        return jsonify(result)

    # GET isteği için index.html dosyasını göster
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
