import os
from flask import Flask, render_template, request, jsonify
import openai

# Load API key from environment variable (safe method)
openai.api_key = os.environ.get("OPENAI_API_KEY")

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_message}]
        )
        reply = response.choices[0].message.content
        return jsonify({"reply": reply})
    except Exception as e:
        return jsonify({"reply": "Hi my love ❤️💕 I love you sooo much 😘💗. "
                                 "Sorry for my annoying nature sometimes… please don't be angry na meri jaan 🥺💞. "
                                 "I am all yours, my love — my whole heart and life is for you 💖. "
                                 "Love you my dear kuchu puchu 😘💗💗💗"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
