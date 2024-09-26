import streamlit as st

st.title("Ai Web Scraper ")
url = st.text_input("Enter a Website URL")

if st.button("Scrpate Site"):
    st.write("Scraping the site data ")