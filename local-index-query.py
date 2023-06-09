from llama_index import StorageContext, load_index_from_storage
import gradio as gr

#simple query example instead of chat completion and only uses the local index

# rebuild storage context
storage_context = StorageContext.from_defaults(persist_dir="local-index")
index = load_index_from_storage(storage_context)
query_engine = index.as_query_engine()


def open_ai_prompt(prompt_text):
    return query_engine.query(prompt_text)


demo = gr.Interface(fn=open_ai_prompt, inputs="text", outputs="text",allow_flagging=False)

demo.launch()
