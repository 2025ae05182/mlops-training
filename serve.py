from flask import Flask, request, jsonify
import joblib

#initialize Flask App
app = Flask(__name__)

#load the trained model
model = joblib.load("iris_model.pkl")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Expect JSON input with "features"
        data = request.json.get("features")
        if not data:
            return jsonify({"error": "No features provided"}, 400)
        
        # make prediction
        prediction = model.predict([data])
        return jsonify({"prediction": int(prediction[0])})
    except Exception as e:
        return jsonify({"error": int(str(e))}, 500)

@app.route("/", methods=["GET"])
def home():
    return "Flask model server is running. Use /predict to POST features."

if __name__ == "__main__":
    # Run on all interfaces, port 5000
    app.run(host="127.0.0.1", port=5000, debug=False)