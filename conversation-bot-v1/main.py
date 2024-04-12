import streamlit as sl
from langchain.llms import OpenAI


#Generate Page Content

sl.set_page_config(page_title="Demo")
sl.title('Chat-model')
sl.write("Simple implementation of langchain's openAI llm ")

##Generate response

def get_text():
    input=sl.text_input("You: ", key="input")
    return input


def load_answer(question):
    llm=OpenAI(temperature=0.7,max_tokens=512,openai_api_key="Api Key")
    answer=llm(question)
    return answer

user_input=get_text()
response=load_answer(user_input)

submit=sl.button("Generate")
if submit:
    sl.subheader("Answer: ")
    sl.write(response)

