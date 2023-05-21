import streamlit as web
import pandas
web.set_page_config(layout="wide")
web.title("The Best Company")
about ="""
        Ante lacus veniam urna delicata eos. 
        Meliore reque velit quam propriae parturient ceteros.
        Convenire quas hinc noluisse suspendisse.
        Tortor vehicula mei dicta ancillae petentium ceteros possit. 
        Maximus iuvaret elitr potenti quis tota aliquet eius.
        Ante lacus veniam urna delicata eos. 
        Meliore reque velit quam propriae parturient ceteros.
        Convenire quas hinc noluisse suspendisse.
        Tortor vehicula mei dicta ancillae petentium ceteros possit. 
        Maximus iuvaret elitr potenti quis tota aliquet eius.
        Ante lacus veniam urna delicata eos. 
        Meliore reque velit quam propriae parturient ceteros.
        Convenire quas hinc noluisse suspendisse.
        Tortor vehicula mei dicta ancillae petentium ceteros possit. 
        Maximus iuvaret elitr potenti quis tota aliquet eius.
        """
web.info(about)
web.header("Our Team")
col1,col2,col3=web.columns(3)

df_data =pandas.read_csv("data.csv")
df_topics =pandas.read_csv("topics.csv")

with col1:
    for index,row in df_data[:4].iterrows():
        web.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        web.write(row['role'])
        web.image('images/'+row['image'])
with col2:
    for index,row in df_data[4:8].iterrows():
        web.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        web.write(row['role'])
        web.image('images/'+row['image'])
with col3:
    for index,row in df_data[8:12].iterrows():
        web.subheader(f"{row['first name'].title()} {row['last name'].title()}")
        web.write(row['role'])
        web.image('images/'+row['image'])
