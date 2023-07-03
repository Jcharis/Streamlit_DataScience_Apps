import chainlit as cl 
from textblob import TextBlob
from gpt4all import GPT4All

gpt = GPT4All(model_name="ggml-gpt4all-j-v1.2-jazzy.bin",model_path="/home/jcharis/.local/share/nomic.ai/GPT4All/")



# continuously on a loop
@cl.on_message
def main(message:str):
    # Your logic will be here
    result = message.title()

    if "sentiment" in message:
        file = None
        while file == None:
            file = cl.ask_for_file(title="Please upload a text file to analyse",accept=["text/plain"])

        # Decode bytes to text
        text = file.content.decode("utf-8")
        blob = TextBlob(text)


        # send a response back to the user 
        cl.send_message(content=f"Sure, here is your analysis:{text},\n your result is {blob.sentiment}")

    else:
        # LLM 
        result = gpt.chat_completion([{"role":"assistant","content":message}])
        response = result["choices"][0]["message"]["content"]
        # send a response back to the user 
        cl.send_message(content=f"Sure, :{response}")



@cl.on_chat_start
def start():
    content = "Hello I am JCharis AI"
    cl.send_message(content=content)