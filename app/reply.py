

def reply(user_message, history):
    '''
    example:
    chatbot = gr.Chatbot()
    msg = gr.Textbox()
    msg.submit(reply, [msg, chatbot], [msg, chatbot])

    :param user_message:
    :param history:
    :return:
    '''
    return "", history + [[user_message, 'Please modify this to enable your conversation.']]