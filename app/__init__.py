from .ui import app
def run():
    app.queue(concurrency_count=1).launch(server_name="0.0.0.0", share=False, server_port=8012,)