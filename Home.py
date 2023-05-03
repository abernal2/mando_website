import streamlit as st
from PIL import Image
import os

st.set_page_config(
    page_icon="👋",
)

path = os.path.dirname(os.path.realpath(__file__))
image_path = os.path.join(path, 'files/me.png')
image = Image.open(image_path)


st.markdown('## Machine Learning and Mathematical Optimization Specialist!')
st.image(image, width=300, caption='Armando Bernal')

st.markdown(
    """
    Hiring Data Scientist/Optimization Engineers staff can be expensive for 
    small and medium sized companies. On top of that, powerful commercial 
    software to build and deploy said ML/optimization models adds to these costs. If you 
    want to leverage data science and optimization models but the costs are 
    prohibitive, then reach out to me to discuss how I can bring these models 
    into your business-decision arsenal at about one-third the annual costs.

    My name is Armando Bernal and I have worked for various companies, big and 
    small, startups and fortune 500 companies in the analytical division 
    informing their business-decision making process.

    ### Want to learn more?
    Please reach out to me to discuss your business analytical needs and costs
    to bring these models to production.
"""
)

filepath = os.path.join(path, 'files/Resume.pdf')

with open(filepath, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

st.download_button(label="Download CV",
                    data=PDFbyte,
                    file_name="ArmandoBernal_Resume.pdf",
                    mime='application/octet-stream')