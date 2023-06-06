# Generative AI playground

Some experiments in what is new for the moment.

## Text to Image
Generating images, [see this blog first](https://rahulaga.medium.com/from-words-to-pictures-text-to-image-generation-8512b61002fa).


## OpenAI Hello World
1. In your Python 3 virtual environment install dependencies.
```
pip install -r requirements.txt
```

2. Get an OpenAI API key. Simple way for testing is to set env variable.
```
export OPENAI_API_KEY='sk...'
``` 

3. Run the hello-world and it should give you some stock recommendations
```
This one uses openai library directly
python hello-openai.py 

This is via LangChain - used next
python hello-openapi.py
```

4. Hello world variation with a UI using Gradio
```
python hello-openapi-gradio.py
```
Open in browser http://127.0.0.1:7860

## A custom chatbot with OpenAI
See [this blog for an overview and details](https://rahulaga.medium.com/creating-a-custom-chatbot-with-openai-2e08b1e98133)

1. Install the `requirements.txt`
2. Index the custom data to create embeddings using LlamaIndex. I have PDF files in the `local-data` folder that it uses.
```
python build_index.py
```
The output is stored in the folder `local-index`

3. Run the chatbot that will load the embeddings created and interact with it using LangChain
```
python local-index-chat.py
```
Open in browser http://127.0.0.1:7860

## Local LLM with GPT4All
Locally on CPU only (no GPU) it is possible to run some models thanks to GPT4All. It works but relatively slow on my machine. There is no support to generate embeddings as of now.
1. Install the `requirements.txt`
2. Get a model from gpt4all.io or hugging faces. Modify `hello-gpt4all.py` to point to the correct path you downloaded the model.

```
python hello-gpt4all.py
```
