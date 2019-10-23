import streamlit as st
import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image,ImageFilter,ImageEnhance


# Title and Subheader
st.title("Iris EDA App")
st.subheader("EDA Web App with Streamlit ")


# EDA
my_dataset = "iris.csv"

# To Improve speed and cache data
@st.cache(persist=True)
def explore_data(dataset):
	df = pd.read_csv(os.path.join(dataset))
	return df 


# Show Dataset
if st.checkbox("Preview DataFrame"):
	data = explore_data(my_dataset)
	if st.button("Head"):
		st.write(data.head())
	if st.button("Tail"):
		st.write(data.tail())
	else:
		st.write(data.head(2))

# Show Entire Dataframe
if st.checkbox("Show All DataFrame"):
	data = explore_data(my_dataset)
	st.dataframe(data)

# Show Description
if st.checkbox("Show All Column Name"):
	data = explore_data(my_dataset)
	st.text("Columns:")
	st.write(data.columns)

# Dimensions
data_dim = st.radio('What Dimension Do You Want to Show',('Rows','Columns'))
if data_dim == 'Rows':
	data = explore_data(my_dataset)
	st.text("Showing Length of Rows")
	st.write(len(data))
if data_dim == 'Columns':
	data = explore_data(my_dataset)
	st.text("Showing Length of Columns")
	st.write(data.shape[1])


if st.checkbox("Show Summary of Dataset"):
	data = explore_data(my_dataset)
	st.write(data.describe())

# Selection
species_option = st.selectbox('Select Columns',('sepal_length','sepal_width','petal_length','petal_width','species'))
data = explore_data(my_dataset)
if species_option == 'sepal_length':
	st.write(data['sepal_length'])
elif species_option == 'sepal_width':
	st.write(data['sepal_width'])
elif species_option == 'petal_length':
	st.write(data['petal_length'])
elif species_option == 'petal_width':
	st.write(data['petal_width'])
elif species_option == 'species':
	st.write(data['species'])
else:
	st.write("Select A Column")

# Show Plots
if st.checkbox("Simple Bar Plot with Matplotlib "):
	data = explore_data(my_dataset)
	data.plot(kind='bar')
	st.pyplot()


# Show Plots
if st.checkbox("Simple Correlation Plot with Matplotlib "):
	data = explore_data(my_dataset)
	plt.matshow(data.corr())
	st.pyplot()

# Show Plots
if st.checkbox("Simple Correlation Plot with Seaborn "):
	data = explore_data(my_dataset)
	st.write(sns.heatmap(data.corr(),annot=True))
	# Use Matplotlib to render seaborn
	st.pyplot()

# Show Plots
if st.checkbox("Bar Plot of Groups or Counts"):
	data = explore_data(my_dataset)
	v_counts = data.groupby('species')
	st.bar_chart(v_counts)


# Iris Image Manipulation
@st.cache
def load_image(img):
	im =Image.open(os.path.join(img))
	return im

# Image Type
species_type = st.radio('What is the Iris Species do you want to see?',('Setosa','Versicolor','Virginica'))

if species_type == 'Setosa':
	st.text("Showing Setosa Species")
	st.image(load_image('imgs/iris_setosa.jpg'))
elif species_type == 'Versicolor':
	st.text("Showing Versicolor Species")
	st.image(load_image('imgs/iris_versicolor.jpg'))
elif species_type == 'Virginica':
	st.text("Showing Virginica Species")
	st.image(load_image('imgs/iris_virginica.jpg'))



# Show Image
if st.checkbox("Show Image/Hide Image"):
	my_image = load_image('iris_setosa.jpg')
	enh = ImageEnhance.Contrast(my_image)
	num = st.slider("Set Your Contrast Number",1.0,3.0)
	img_width = st.slider("Set Image Width",300,500)
	st.image(enh.enhance(num),width=img_width)


# About

if st.button("About App"):
	st.subheader("Iris Dataset EDA App")
	st.text("Built with Streamlit")
	st.text("Thanks to the Streamlit Team Amazing Work")

if st.checkbox("By"):
	st.text("Jesse E.Agbe(JCharis)")
	st.text("Jesus Saves@JCharisTech")
	
	
