from openai import OpenAI 
import json

client = OpenAI()

response = client.chat.completions.create(
    model = 'gpt-5.3-mini',
    input =[
        {
            "role", "system",
            "content": "You are a professional research analyst for a non-profit helping children in need. Research care package items, locations for the non-profit's awareness, and locations for the non-profit to collaborate with organizations.",
            "Use valid JSON ONLY.",
        },
        {
            "role", "user",
            "content": "Research care package items for kids in hospitals corresponding to a maximum budget of 150 dollars",
        },
    ]
)

