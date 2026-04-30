import streamlit as st

st.set_page_config(
    page_title="ChatBot",
    page_icon="😎",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items=None
)

# 大标题
st.title("ChatBot")

# 聊天框
prompt = st.chat_input("Your message")
if prompt:
    st.chat_message("user").write(prompt)
    st.chat_message("assistant").write("正在思考...")
    print("调用大模型，提示词：", prompt)

    # 调用大模型，获取回复

# prompt = st.chat_input(
#     placeholder="输入消息并可上传图片...",
#     accept_file="multiple",  # 允许上传多个文件
#     file_type=["png", "jpg", "jpeg", "gif", "webp"]  # 只接受图片
# )