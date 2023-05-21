import streamlit as web
import pandas as pd
from send_email import send_email

web.set_page_config(layout="wide")
web.header("Contact Me")

with web.form(key="email form"):
    user_name = web.text_input("Enter Your Full Name")
    user_email = web.text_input("Enter Your Email Address")
    df= pd.read_csv("topics.csv")
    select_topic = web.selectbox('Select your topic Of concern',df["topic"])
    raw_message = web.text_area("Enter Your Message")
    message = f"""\
Subject: {user_name} wants to talk about {select_topic}

From: {user_name} ({user_email})
{raw_message}
    """
    button = web.form_submit_button()
    if button:
        send_email(message)
        web.info("Email sent sucessfully")
