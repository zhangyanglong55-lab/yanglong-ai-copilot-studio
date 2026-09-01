import os
from openai import OpenAI
import streamlit as st

st.set_page_config(page_title="Yanglong AI Copilot Studio", page_icon="⚡", layout="wide")
st.markdown("""<style>.stApp{background:radial-gradient(circle at top left,#13213d 0,#070b14 52%)}[data-testid="stSidebar"]{background:#0b1220}.brand{font-size:2rem;font-weight:800}.sub{color:#8ba3c7}</style><div class="brand">⚡ Yanglong AI Copilot Studio</div><div class="sub">面向 AI 产品、AIGC 商业化与 Agent 设计的智能工作台</div>""", unsafe_allow_html=True)
with st.sidebar:
    st.header("工作台设置")
    model=st.selectbox("模型",["gpt-4o-mini","gpt-4o"])
    st.caption("请配置环境变量 OPENAI_API_KEY")
    st.divider(); st.markdown("**Maintainer**  \nZhang Yanglong  \n[GitHub](https://github.com/zhangyanglong55-lab)")
if "messages" not in st.session_state:
    st.session_state.messages=[{"role":"assistant","content":"你好，我是 Yanglong AI Copilot。今天想一起打磨产品、分析机会，还是设计 Agent？"}]
for message in st.session_state.messages:
    with st.chat_message(message["role"]): st.markdown(message["content"])
if prompt:=st.chat_input("描述你的产品、业务问题或 Agent 想法…"):
    st.session_state.messages.append({"role":"user","content":prompt})
    with st.chat_message("user"): st.markdown(prompt)
    if not os.getenv("OPENAI_API_KEY"):
        answer="请先设置 `OPENAI_API_KEY`，然后重新启动应用。"
    else:
        client=OpenAI(); messages=[{"role":"system","content":"你是 Yanglong AI Copilot，擅长 AI 产品设计、Agent 工作流、AIGC 商业化和医疗 AI。默认用简洁中文回答并给出可执行建议。"}]+st.session_state.messages[1:]
        answer=client.chat.completions.create(model=model,messages=messages).choices[0].message.content
    with st.chat_message("assistant"): st.markdown(answer)
    st.session_state.messages.append({"role":"assistant","content":answer})
