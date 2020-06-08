import streamlit as st
import pandas as pd 

from db_fxns import *


def main():
	"""Securing Login Apps"""

	st.title("Securing Login Apps Against SQL Injection")


	menu = ["Home","Login","SignUp"]
	choice = st.sidebar.selectbox('Menu',menu)

	if choice == "Home":
		st.subheader("Securing Apps")

	elif choice == "Login":
		st.subheader("Login Into App")
		username = st.sidebar.text_input("Username")
		password = st.sidebar.text_input("Password",type='password')
		if st.sidebar.checkbox("Login"):
			create_usertable()
			result = login_user(username,password)
			# result = login_user_unsafe(username,password)
			# if password == "12345":
			if result:
				st.success("Logged In as {}".format(username))

				task = st.selectbox("Task",["Add Posts","Analytics","Manage"])

				if task == "Add Posts":
					st.subheader("Add Posts")

				elif task == "Analytics":
					st.subheader("Analytics")

				elif task == "Manage":
					st.subheader("Manage Blog")
					users_result = view_all_users()
					clean_db = pd.DataFrame(users_result,columns=["Username","Password"])
					st.dataframe(clean_db)
			else:
				st.warning("Incorrect Username/Password")
	

	elif choice =="SignUp":
		st.subheader("Create An Account")
		new_username = st.text_input("User name")
		new_password = st.text_input("Password",type='password')
		confirm_password = st.text_input('Confirm Password',type='password')

		if new_password == confirm_password:
			st.success("Valid Password Confirmed")
		else:
			st.warning("Password not the same")

		if st.button("Sign Up"):
			create_usertable()
			add_userdata(new_username,new_password)
			st.success("Successfully Created an Account")





if __name__ == '__main__':
	main()