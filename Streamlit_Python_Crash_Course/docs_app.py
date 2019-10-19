import streamlit as st

# Title
st.title("Streamlit Crash Course")
# Header
st.header("Simple Header")
# Subheader
st.subheader("Another sub header")

# Text
st.text("For a simple text")

# Markdown
st.markdown("#### A Markdown ")

# Error text
st.success("Successful")

st.info("This is an info alert ")

st.warning("This is a warning ")

st.error("This shows an error ")

st.exception("NameError('name not defined')")

# Getting Help Info From Python
st.help(range)



# Writing Text/Super Fxn
st.write("Text with write")

st.write("Python Range with write",range(10))

# Images
from PIL import Image 
img = Image.open("example.jpeg")
st.image(img,width=300,caption='Streamlit Images')

# Videos
video_file = open("example.mp4",'rb')
video_bytes = video_file.read()
st.video(video_bytes)

# Audio
# audio_file = open("",'rb')
# audio_bytes = audio_file.read()
# st.audio(audio_bytes,format='audio/mp3')


# Widget
# Checkbox
if st.checkbox("Show/Hide"):
	st.text("Showing or Hiding Widget")

# Radio Button
status = st.radio("What is your status",('Active','Inactive'))
if status == 'Active':
	st.text("Status is Active")
else:
	st.warning("Not Active Yet")

# SelectBox
occupation = st.selectbox("Your Occupation",['Data Scientist','Programmer','Doctor','Businessman'])
st.write("You selected this option",occupation)

# MultiSelect
location = st.multiselect("Where do you stay",("London","New York","Accra","Kiev","Berlin","New Delhi"))
st.write("You selected",len(location),"location")


# Slider
salary = st.slider("What is your salary",1000,10000)

# Buttons
st.button("Simple Button")


# Text Input
name = st.text_input("Enter Name","Type Here...")
if st.button('Submit'):
    result = name.title()
    st.success(result)
else:
    st.write("Press the above button..")

# Text Area
c_text = st.text_area("Enter Text","Type Here...")
if st.button('Analyze'):
    c_result = c_text.title()
    st.success(c_result)
else:
    st.write("Press the above button..")


#  Date Input
import datetime,time
today = st.date_input("Today is",datetime.datetime.now())


# Time Input
t = st.time_input("The time now is",datetime.time())

# SIDE Bar
st.sidebar.header("Side Bar Header")
st.sidebar.text("Hello")


# Display JSON
st.text("Display JSON")
st.json({'name':'hello','age':34})

# Display Raw Code
st.text("Display Raw Code")
st.code("import numpy as np")


st.text("Display Raw Code Alternative Method")
with st.echo():
	# This will also be shown
	import pandas as pd 

	df = pd.DataFrame()


# Progress Bar
# import time
# my_bar = st.progress(0)
# for p  in range(10):
# 	my_bar.progress(p +1)

# Spinner
with st.spinner("Waiting .."):
	time.sleep(5)
st.success("Finished!")

# Placeholder with empty
# age = st.empty()
# age.text("Your Age")
# Replace with image
# age.image(img)


# Cache For Performance
@st.cache
def run_multiple():
	return range(100)
# Display the result of function
st.write(run_multiple())
