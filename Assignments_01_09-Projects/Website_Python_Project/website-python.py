import streamlit as st

st.set_page_config(page_title = "my First website", page_icon= "🌎", layout= "centered")
st.title("Welcome to my first Python website.")

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "About", "Contact"])

if page == "Home":
    st.header("Home page")
    st.write("This is a simple Home page built with python and streamlit")
    name = st.text_input("What's your name?")
    if name:
        st.success(f"Hello {name}! Thanks for visiting.")

elif page == "About":
    st.header("About")
    st.write("This website is built entirely using Python and streamlit in under 15 minutes!")

elif page == "Contact":
    st.header("Contact us")
    email = st.text_input("Your email")
    message = st.text_input("Your message.")
    if st.button("submit"):
       st.success("Thank you! We have received your message.")