from flask import Flask, jsonify
import logging
import json_log_formatter

formatter = json_log_formatter.JSONFormatter()

json_handler = logging.StreamHandler()
json_handler.setFormatter(formatter)

logger = logging.getLogger()
logger.addHandler(json_handler)
logger.setLevel(logging.INFO)


app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route('/health_check')
def health_check():
    return jsonify({"ping": "pong"})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
