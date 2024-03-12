import streamlit as st
import rag_backend as demo

st.set_page_config(page_title="Welcome to Core Java AI Assistant")
new_title = '<p>Hey I am Neer! Your AI Assistant , ask me any thing about Core Java.</p>'
st.markdown(new_title,unsafe_allow_html=True)
if 'vector_index' not in st.session_state:
    with st.spinner("Wait Interesting thing is coming up...."):
         st.session_state.vector_index = demo.main()

input_text = st.text_area("Input Text",label_visibility="collapsed")
go_button = st.button("Answer Me!!",type="primary")

if go_button:
     with st.spinner("You know I am a most powerful AI assistant here :-)"):
          response_content = demo.hr_rag_response(index=st.session_state.vector_index,question=input_text)
          st.write(response_content)
                   