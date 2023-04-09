import gradio as gr
from .reply import reply
from .prompts import get_core_functions
core_fns = get_core_functions()

gr_L1 = lambda: gr.Row().style()
gr_L2 = lambda scale: gr.Column(scale=scale)

LAYOUT = "TOP-DOWN"
with gr.Blocks(title="Chatbot X - Your Intro",
               analytics_enabled=False,
               ) as app:
    gr.HTML(f"<h1 align=\"center\">Chatbot App</h1>")
    with gr_L1():
        with gr_L2(scale=2):
            chatbot = gr.Chatbot()
            chatbot.style(height=800)
            history = gr.State([])
        with gr_L2(scale=1):
            with gr.Accordion("输入区", open=True) as area_input_primary:
                with gr.Row():
                    txt = gr.Textbox(show_label=False, placeholder="Input question here.").style(container=False)
                with gr.Row():
                    submitBtn = gr.Button("提交", variant="primary")
                with gr.Row():
                    resetBtn = gr.Button("重置", variant="secondary"); resetBtn.style(size="sm")
                    stopBtn = gr.Button("停止", variant="secondary"); stopBtn.style(size="sm")
                with gr.Row():
                    gr.Markdown(f"Tip: 按Enter提交, 按Shift+Enter换行。当前模型: ?")
            with gr.Accordion("基础功能区", open=True) as area_basic_fn:
                with gr.Row():
                    pass
                    for k in core_fns:
                        variant = core_fns[k]["Color"] if "Color" in core_fns[k] else "secondary"
                        core_fns[k]["Button"] = gr.Button(k, variant=variant)

    # bind callbacks and cancellation
    inputs = [txt, chatbot]
    outputs = [txt, chatbot]
    tmp = dict(fn=reply, inputs=inputs, outputs=outputs)
    binds = [
        submitBtn.click(**tmp),
        txt.submit(**tmp),
        resetBtn.click(lambda: ('', []), None, outputs=outputs)
    ]
    # todo
    # for k in core_fns:
        # click_handle = core_fns[k]["Button"].click(fn=...,input=...,output=...)
        # cancel_handles.append(click_handle)

    stopBtn.click(fn=None, inputs=None, outputs=None, cancels=binds)


