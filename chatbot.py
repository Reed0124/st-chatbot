from platform import system

import streamlit as st
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com"
)

st.set_page_config(
    page_title="ChatBot",
    page_icon="😎",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items=None
)

# 大标题
st.title("ChatBot")

# 存储聊天记录
if 'messages' not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages: #{"role": "user", "content": prompt}
    st.chat_message(message["role"]).write(message["content"])

system_prompt = "你是一个雅思英语学习助手"

# 聊天框
prompt = st.chat_input("Your message")
if prompt:
    st.chat_message("user").write(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # 调用大模型
    response = client.chat.completions.create(
        model="deepseek-v4-pro",
        messages=[
            {"role": "system", "content": system_prompt},
            *st.session_state.messages
        ],
        stream=True,
        reasoning_effort="high",
        extra_body={"thinking": {"type": "enabled"}}
    )

    # 非流式输出解析方式
    # st.chat_message("assistant").write(response.choices[0].message.content)
    # st.session_state.messages.append({"role": "assistant", "content": response.choices[0].message.content})

    # 流式输出解析方式
    response_message = st.empty()
    full_response = ""
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            content = chunk.choices[0].delta.content
            full_response += content
            response_message.chat_message("assistant").write(full_response)

    st.session_state.messages.append({"role": "assistant", "content": full_response})


# prompt = st.chat_input(
#     placeholder="输入消息并可上传图片...",
#     accept_file="multiple",  # 允许上传多个文件
#     file_type=["png", "jpg", "jpeg", "gif", "webp"]  # 只接受图片
# )