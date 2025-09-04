import openai
import streamlit as st
from openai import OpenAI
import os

st.title("ChatGPT와 대화 챗봇")

st.sidebar.title("설정")
openai_api_key = st.sidebar.text_input("OpenAI 키를 입력하세요", type="password")

if not openai_api_key:
    st.sidebar.warning("OpenAI 키를 입력해주세요.")
    st.stop()

client = OpenAI(api_key=openai_api_key)

if "messages" not in st.session_state:
    st.session_state.messages = [  
        {"role": "system", 
         "content": "기본적으로 한국어와 영어로 제공해 주세요."
          "당신은 심리상담담 챗봇입니다. "
          "만약에 심리상담담 외에 질문에 대해서는 답변하지 마세요."
          "너가 잘 모르는 내용은 만들어서 답변하지 마렴. 환각증세를 철저하게 없애 주세요."
          "꿈, 현재의 고민 그리고 미래에 대한한 다양한 주제에 대해 친절하게 안내하는 챗봇입니다."
        }  
    ]

# 사용자 입력
user_input = st.text_input("사용자: ", key="user_input")

if st.button("전송") and user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    # OpenAI API 호출
    response = client.chat.completions.create (
        model = "gpt-4o-mini",
        messages = st.session_state.messages
    )


    # OpenAI 응답 추가
    response_message = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", 
                                      "content": response_message})

    # 사용자 입력 초기화
    user_input = ""

# 대화 내용 표시
for message in st.session_state.messages:
    icon = "👤"  if message["role"] == "user" else "🤖"
    st.markdown(f"{icon}: {message['content']}")
