import streamlit as st
import random
def generate():
    st.write(random.randint(0, 10))


st.button("Click me", on_click=generate())