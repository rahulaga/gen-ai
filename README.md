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
python hello-openapi.py
```

4. Hello world variation with a UI using Gradio
```
python hello-openapi-gradio.py
```
Open in browser http://127.0.0.1:7860

## A custom chatbot with OpenAI
See [this blog for an overview and details]()

1. Install the `requirements.txt`
2. Index the custom data to create embeddings. I have PDF files in the `local_data` folder that it uses.
```
python build_index.py
```
The output is stored in the folder `local_index`

3. Run the chatbot that will load the embeddings created and interact with it using LangChain
