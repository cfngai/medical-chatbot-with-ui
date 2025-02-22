from flask import Flask, render_template, request, jsonify
from transformers import GPT2LMHeadModel, GPT2Tokenizer
from generate import generate_answer
# Initialize the Flask app
app = Flask(__name__)

# Load trained GPT-2 model and tokenizer
tokenizer = GPT2Tokenizer.from_pretrained("./models/trained_modelv1")
model = GPT2LMHeadModel.from_pretrained("./models/trained_modelv1")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    outputs = generate_answer(user_message, tokenizer, model)

    return jsonify({"response": outputs})

if __name__ == "__main__":
    app.run(host= '0.0.0.0', port=80, debug=True)
