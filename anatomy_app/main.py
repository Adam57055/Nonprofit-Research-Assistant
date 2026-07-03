from openai import OpenAI
import json

client = OpenAI()

SYSTEM_PROMPT = (
    "You are assuming the role of a professional anatomy professor tasked with "
    "assisting the user in retaining lecture material. Use spaced repetition and "
    "other effective learning science techniques to reinforce memory. "
    "Respond ONLY with valid JSON."
)

def get_lecture_response(user_prompt: str) -> dict:
    response = client.chat.completions.create(
        model="gpt-5.3-mini",  # confirm this is a valid/available model on your account
        response_format={"type": "json_object"},
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt},
        ],
    )

    raw_content = response.choices[0].message.content

    try:
        return json.loads(raw_content)
    except json.JSONDecodeError:
        print("Model did not return valid JSON:", raw_content)
        raise

if __name__ == "__main__":
    result = get_lecture_response("Quiz me on the bones of the hand.")
    print(json.dumps(result, indent=2))