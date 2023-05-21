import smtplib
import ssl


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = 'vedantandhale037@gmail.com'
    password = "Password"
    receiver = "vedantandhale037@gmail.com"
    context = ssl.create_default_context()
#     message = """\
# Subject: Demo Streamlit app
# Vivamus homero prompta dictas neque signiferumque comprehensam vituperata.
# """
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

#
# send_email(message)
# environment variable in linux
# https://www.freecodecamp.org/news/how-to-set-an-environment-variable-in-linux/
# mac and window in course lec no.231
