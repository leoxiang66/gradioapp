import gradio as gr
from requests_toolkit.asyncpy import HTTPLoop

    
    
def work():
    loop = HTTPLoop()
    urls = [
        'https://leoxiang6-io-server.onrender.com',
        'https://fmbot.onrender.com',
    ]
    
    for i in urls:
        loop.get(i)
    loop.wait_all_done()
    tmp = "\n".join(urls)
    return f'''
**Done!**
{tmp}
'''

with gr.Blocks() as app:
    btn = gr.Button('Start')
    md =  gr.Markdown()
    btn.click(work, outputs=md)


app.launch()

