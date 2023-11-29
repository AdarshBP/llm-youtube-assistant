import streamlit as st
import langchain_helper as lch
import textwrap

st.title("AI YouTube Assistant")

with st.sidebar:
    with st.form(key='form'):
        youtube_url = st.text_area(
            label="Please paste YouTube video URL?",
            max_chars=50
            )
        query = st.text_area(
            label="What do you want to know about the video?",
            max_chars=50,
            key="query"
            )
        
        submit_button = st.form_submit_button(label='Submit')

if query and youtube_url and submit_button:
    db = lch.create_db_from_youtube_video_url(youtube_url)
    response, docs = lch.get_response_from_query(db, query)
    st.subheader("Answer:")
    st.text(textwrap.fill(response, width=85))
        