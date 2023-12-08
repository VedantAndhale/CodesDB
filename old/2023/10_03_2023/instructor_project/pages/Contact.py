import streamlit as web
from send_email import send_email

web.set_page_config(layout="wide")
web.header("Contact Me")

with web.form(key="email form"):
    user_email = web.text_input("Enter Your Email Address")
    raw_message = web.text_area("Enter Your Message")
    message = f"""\
Subject: New email from {user_email}

From: {user_email}
{raw_message}
    """
    button = web.form_submit_button()
    if button:
        send_email(message)
        web.info("Email sent sucessfully")
