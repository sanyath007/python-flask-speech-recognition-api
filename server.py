import random
import os
from flask import Flask, request, jsonify
from keyword_spotting_service import keyword_spotting_service

app = Flask(__name__)

@app.route("/predict", methods=["POST"])
def predict():
    # get audio file and save it
    audio_file = request.files["file"]
    file_name = str(random.randint(0, 100000))
    audio_file.save(file_name)

    # invoke keyword spotting service
    kss = keyword_spotting_service()

    # make a prediction
    # predict_keyword = kss


if __name__ == "__main__":
    app.run(debug=True)