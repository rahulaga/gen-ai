import os
import openai

openai.api_key  = os.environ['OPENAI_API_KEY']

#chat completion example, multiple messages maybe sent
messages = [{"role": "user", "content": "What would be good stocks to buy for a hypothetical high risk portfolio"}]
response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                        messages=messages, temperature=0)
print(response)