import streamlit as st 

def main():
	"""Deploying Streamlit App with Docker"""

	st.title("Streamlit App")
	st.header("Deploying Streamlit with Docker on GCP")

	st.title("Updated Version")


	activities = ["EDA","Plots"]

	choices = st.sidebar.selectbox('Select Activities',activities)

	if choices == 'EDA':
		st.subheader("EDA")

	elif choices == 'Plots':
		st.subheader("Visualization")




if __name__ == '__main__':
	main()