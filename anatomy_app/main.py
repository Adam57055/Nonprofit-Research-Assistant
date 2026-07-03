from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI
from dotenv import load_dotenv
import json

load_dotenv()  # reads .env for API key

app = Flask(__name__)
CORS(app)  # frontend is connected to backend

client = OpenAI()

SYSTEM_PROMPT = (
    "You are assuming the role of a professional anatomy professor tasked with "
    "assisting the user in retaining lecture material. Use spaced repetition and "
    "other effective learning science techniques to reinforce memory. "
    "Respond ONLY with valid JSON."
)

@app.route("/api/lecture", methods=["POST"])
def get_lecture_response():
    user_prompt = request.json.get("prompt", "")

    response = client.chat.completions.create(
        model="gpt-5.3-mini",
        response_format={"type": "json_object"},
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt},
        ],
    )

    raw_content = response.choices[0].message.content

    try:
        result = json.loads(raw_content)
        return jsonify(result)
    except json.JSONDecodeError:
        print("Model did not return valid JSON:", raw_content)
        return jsonify({"error": "Model returned invalid JSON"}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)