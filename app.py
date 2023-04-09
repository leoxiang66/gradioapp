import gradio as gr
from requests_toolkit.asyncpy import HTTPLoop
import time

    

def work():
    count = 0
    loop = HTTPLoop()
    urls = [
        'https://leoxiang6-io-server.onrender.com',
        'https://fmbot.onrender.com',
        'https://gradioapp.adaptingx.repl.co/',
    ]
    
    while True:
        for i in urls:
            loop.get(i)
            
        count+=1
        print(count)
        time.sleep(600)


with gr.Blocks() as app:
    btn = gr.Button('Start')
    md =  gr.Markdown()
    btn.click(work)


app.launch()

