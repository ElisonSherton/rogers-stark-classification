from flask import Flask, request
import flasgger
from flasgger import Swagger
from utils import *
import pickle

with open("model_artifact.pkl", "rb") as f:
    model_artifact = pickle.load(f)
    f.close()

app = Flask(__name__)
Swagger(app)

@app.route("/")
def home():
    return "Welcome to the app for dialogue identification"

@app.route("/predict_dialogue", methods = ["POST"])
def predict_dialogue():
    """This endpoint predicts whether a given dialogue is more likely to be spoken by Cap or Stark
    ---
    parameters:
      - name: text
        in: query
        type: string
        required: true
      
    responses:
        200:
            description: Who is more likely to speak these words, Rogers or Stark
        
    """
    text = request.args.get("text")
    prediction = utils.predict(str(text), model_artifact["probabilites"], model_artifact["log_prior"])

    return f"This dialogue is more likely to have come from {prediction[0]}."

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 8000)