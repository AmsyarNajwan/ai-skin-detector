from flask import Flask, render_template, request
import os
from model import predict_skin

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


def save_image(file):

    filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
    file.save(filepath)

    return filepath


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    file = request.files["image"]

    filepath = save_image(file)

    skin_type, confidence = predict_skin(filepath)

    return render_template(
    "result.html",
    skin_type=skin_type,
    confidence=round(confidence*100,2),
    image_path=filepath,
    recommendation="Use oil-control cleanser and lightweight moisturizer"
)



if __name__ == "__main__":
    app.run(debug=True)
