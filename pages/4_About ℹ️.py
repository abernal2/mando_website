import os
from PIL import Image
import streamlit as st

path = os.path.dirname(os.path.realpath(__file__))
image_path = os.path.join(path, '..', 'files/me.png')
image = Image.open(image_path)

st.write("# Armando Bernal")
st.image(image, width=300)

st.write("## About Me")

st.write(
    """
    I grew up in the Northside of Chicago in the Albany Park neighborhood. Albany Park
    was and still is a rough neighborhood but it truly made me who I am. I went 
    to Roosevelt High School where I met my wife and have a wonderful baby daughter with.
    I strongly believe the AP Calculus course I took really sparked an interest in
    mathematics. Mathematics, oddly enough, did not start clicking until mid-Masters program at
    Stanford University, where I fell in love with mathematical optimization. 
    After having difficulty in acquiring a full-time job after Stanford, I enrolled in the 
    PhD Industrial Engineering program at the University of Michigan Ann-Arbor (thesis can de 
    downloaded from the Education section).
    """
)