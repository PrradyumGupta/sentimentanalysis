from flask import Flask, render_template, request, jsonify
import os
import logging
from dotenv import load_dotenv
from multilingual_sentiment import predict_multilingual_sentiment

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/policy')
def policy():
    return render_template('policy.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/what-about')
def what_about():
    return render_template('what_about.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        data = request.get_json()
        if not data or "text" not in data:
            logger.error('No text provided')
            return jsonify({'error': 'No text provided'}), 400

        text = data["text"].strip()
        if not text:
            logger.error('Empty text provided')
            return jsonify({'error': 'Empty text provided'}), 400

        # Use multilingual sentiment model for prediction
        sentiment, score = predict_multilingual_sentiment(text)
        return jsonify({"sentiment": sentiment, "confidence": score})

    except Exception as e:
        logger.error(str(e))
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, jsonify
import os
import logging
from dotenv import load_dotenv
from multilingual_sentiment import predict_multilingual_sentiment

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# Define a custom error handler
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/policy')
def policy():
    return render_template('policy.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/what-about')
def what_about():
    return render_template('what_about.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        data = request.get_json()
        if not data or "text" not in data:
            logger.error('No text provided')
            return jsonify({'error': 'No text provided'}), 400

        text = data["text"].strip()
        if not text:
            logger.error('Empty text provided')
            return jsonify({'error': 'Empty text provided'}), 400

        # Use multilingual sentiment model for prediction
        sentiment, score = predict_multilingual_sentiment(text)
        return jsonify({"sentiment": sentiment, "confidence": score})

    except Exception as e:
        logger.error(str(e))
        return jsonify({'error': str(e)}), 500

# Run the application
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)