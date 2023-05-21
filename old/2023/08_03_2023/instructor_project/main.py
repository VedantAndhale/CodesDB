import streamlit as web
import pandas
web.set_page_config(layout="wide")
col1,col2=web.columns(2)
with col1:
    web.image("images/photo.png")

with col2:
    web.title("Ardit Sulce")
    content = """
    Senectus faucibus integer volumus aliquid. 
    Potenti nunc dicant simul parturient dicant solet duo litora error. 
    Eos mea augue quaestio menandri dolor sodales debet libero. 
    Euismod massa finibus mediocrem mel oporteat nobis dicam dictum sagittis. 
    Civibus graeci vocibus eleifend augue dolores.
    """
    web.info(content)

content2="""Below you can find some of the apps I have built in Python.
          Feel free to contact me !"""

web.write(content2)

col3,empty_col,col4=web.columns([1.5,0.5,1.5])

df = pandas.read_csv("data.csv",sep=";")
with col3:
    for index,row in df[:10].iterrows():
        web.header(row["title"])
        web.write(row["description"])
        web.image("images/" + row["image"])
        web.write(f"[SourceCode]({row['url']})")


with col4:
    for index,row in df[10:].iterrows():
        web.header(row["title"])
        web.write(row["description"])
        web.image("images/" + row["image"])
        web.write(f"[SourceCode]({row['url']})")

