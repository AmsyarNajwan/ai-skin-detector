# AI Skin Detector

An AI-powered web application that analyzes uploaded skin images and classifies the skin type as **Dry**, **Oily**, or **Normal** using deep learning.

The system uses a trained image classification model and a Flask web interface to provide an easy way to analyze skin images.

---

## Features

* Upload a skin image for analysis
* AI classification of skin type
* Confidence score for predictions
* Modern dark UI with glass design
* Deep learning model using TensorFlow

---

## Tech Stack

* Python
* TensorFlow
* Flask
* HTML / CSS
* Bootstrap

---

## Project Structure

```
ai-skin-detector
│
├── app.py
├── train_model.py
├── model.py
├── skin_model.h5
│
├── dataset
│   ├── train
│   └── test
│
├── templates
│   ├── index.html
│   └── result.html
│
├── static
│   └── style.css
│
├── uploads
└── README.md
```

---

## Installation

Clone the repository:

```
git clone https://github.com/yourusername/ai-skin-detector.git
```

Navigate to the project folder:

```
cd ai-skin-detector
```

Install dependencies:

```
pip install -r requirements.txt
```

---

## Train the Model

To train the skin classification model:

```
python train_model.py
```

This will generate:

```
skin_model.h5
```

---

## Run the Web App

Start the Flask server:

```
python app.py
```

Open your browser and go to:

```
http://127.0.0.1:5000
```

---

## How It Works

1. User uploads a skin image.
2. The image is sent to the Flask backend.
3. The trained AI model predicts the skin type.
4. The result and confidence score are displayed on the website.

---

## Example Prediction

```
Skin Type: Oily
Confidence: 92%
Recommendation: Use oil-control cleanser and lightweight moisturizer.
```

---

## Future Improvements

* Higher accuracy with transfer learning
* Face and skin region detection
* Real-time camera skin scanning
* Mobile responsive UI

---

## License

This project is for educational and research purposes.
