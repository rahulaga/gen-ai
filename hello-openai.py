import os
import openai

openai.api_key  = os.environ['OPENAI_API_KEY']

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
    )
    print(response)
    return response.choices[0].message["content"]

print(get_completion("What would be good stocks to buy for a hypothetical high risk portfolio"))