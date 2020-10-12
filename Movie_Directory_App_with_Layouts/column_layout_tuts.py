# core pkg
import streamlit as st 


def main():
	"""Basics on st.beta columns/layout"""
	
	menu = ["Home","Search","About"]

	choice = st.sidebar.selectbox("Menu",menu)

	if choice == 'Home':
		st.subheader("Home")
		st.success("Full Layout")
		# st.text("Sidebar")
		# st.write(dir(st.sidebar))

		# Using st.beta_columns
		col1,col2 = st.beta_columns(2)
		# st.text("Beta Columns")
		# st.write(dir(col1))

		# Method 1
		col1.success("First Column")
		col1.button("Hello")


		col2.success("Second COlumn")
		col2.button("Hello From Col2")

		# Method 2: Context Manager
		with col1:
			search = st.text_area("Enter Text Here")
			if st.button("Submit"):
				st.write(search.upper())


		with col2:
			year = st.number_input('Year',1995,2020)





	elif choice == "Search":
		st.subheader("Search")
		# Different Layout
		c1,c2,c3 = st.beta_columns([3,1,1])

		with c1:
			st.info("From Col 1")

		with c2:
			st.success("From C2 :Less")

		with c3:
			st.warning("From C3 :Less")


	else:
		st.subheader("About")



if __name__ == '__main__':
	main()



