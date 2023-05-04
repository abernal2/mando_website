import os
import streamlit as st

st.markdown(
    """
    # Ph.D in Industrial and Operations Engineering
    I attended the University of Michigan Ann-Arbor from 2014-2020 where 
    my thesis focused on developing provably optimal revenue-generating 
    policies under stochastic environments. I used tools like
    - Upper confidence bounds (used in multi-armed bandits)
    - Linear Programming
    - Reinforcement Learning

    Additionally, I taught the following courses
    - Introduction to Linear Programming (IOE 310)
    - Linear Programming (IOE 410)
"""
)
path = os.path.dirname(os.path.realpath(__file__))
filepath = os.path.join(path, '..', 'files/ABernal_thesis.pdf')

with open(filepath, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

st.download_button(label="Download Thesis",
                    data=PDFbyte,
                    file_name="ArmandoBernal_Thesis.pdf",
                    mime='application/octet-stream')


st.markdown(
    """
    # Masters in Industrial Engineering
    I attended Stanford University where I focused on mathematical 
    optimization. I took optimization courses from Stephen Boyd, a pioneer in
    convex optimization and took machine learning courses from Andrew Ng. 
    Optimization courses I took are
    - Linear Programming
    - Convex Programming
    - Semi-Definite Programming
    - Conic Programming
"""
)

st.markdown(
    """
    # Bachelors in Mechanical Engineering
    I attended the University of Illinois at Urbana-Champaign from 2006-2010.
    My training was general and introductory but I got a taste of physical
    concepts like thermodynamics, heat-transfer, fluid dynamics, and materials.
"""
)