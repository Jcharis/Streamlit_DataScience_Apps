# Core Pkgs
import streamlit as st 
import pandas as pd 
import numpy as np  

def main():
	menu = ["Home","About"]
	choice = st.sidebar.selectbox("Menu",menu)

	if choice == "Home":
		st.subheader("HomePage")
		st.subheader("Random Gen DataFrame")
		rand_num = st.sidebar.number_input("Random Number",min_value=10,max_value=500,value=10)

		# Create DF
		df = pd.DataFrame(np.random.randint(0,int(rand_num),size=(100,4)),columns=list('ABCD'))
		st.dataframe(df)

		# Download Button
		# Data: binary file
		st.download_button(label='Download CSV',data=df.to_csv(),mime='text/csv')


	else:
		st.subheader("AboutPage")



if __name__ == '__main__':
	main()