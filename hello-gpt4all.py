import gpt4all

#show available models
#print (gpt4all.GPT4All.list_models())

#download binary from https://gpt4all.io 
gpt = gpt4all.GPT4All(model_name='ggml-vicuna-13b-1.1-q4_2.bin', allow_download=False,
                       model_path='/models/')

messages = [{"role": "user", "content": "What other plants can grow well where grapes thrive? Think step by step"}]
response = gpt.chat_completion(messages=messages, default_prompt_header=True, #this instructs the model to be behave like a chatbot
                               default_prompt_footer=False, verbose=True)

print(response)