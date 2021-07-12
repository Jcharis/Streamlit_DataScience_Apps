# Core Pkgs
import streamlit as st
import streamlit.components.v1 as stc 


# HTML

HTML_BANNER = """
    <div style="background-color:#464e5f;padding:10px;border-radius:10px;font-size:{}px">
    <h1 style="color:white;text-align:center;">Streamlit is Awesome </h1>
    <h1 style="color:white;text-align:center;">Session State is Here!! </h1>
    </div>
    """

def main():
	st.title("Session States")


	menu = ["Home","Custom_Settings","About"]
	choice = st.sidebar.selectbox("Menu",menu)

	# Home
	if choice == "Home":
		st.subheader("Home Page")

		# st.info("Without Session State")
		# counter_without_state = 0
		# st.write("Initial Value",counter_without_state)

		# increment = st.button("Increment Without State")
		# if increment:
		# 	counter_without_state += 1

		# st.write("Counts[without session state]",counter_without_state)

		# Check Session State
		st.write(st.session_state)

		# With Session State
		st.info("With Session State")
		# Define Variable and Initialize State
		if 'counter_one' not in st.session_state:
			# Attrib
			st.session_state.counter_one = 0

			# # Key
			# st.session_state['counter_one'] = 0

		# increment = st.button("Increment By One")


		# # Function
		# if increment:
		# 	st.session_state.counter_one +=1


		# # Results of update
		# st.write("Counts[with session state]",st.session_state.counter_one)


		col1,col2 = st.beta_columns(2)
		with col1:
			increment = st.button("Increment By One")
			# Function
			if increment:
				st.session_state.counter_one +=1

		with col2:
			decrement = st.button("Decrement By One")
			if decrement:
				st.session_state.counter_one -=1

		# # Results of update
		st.write("Counts[with session state]",st.session_state.counter_one)





	elif choice == "Custom_Settings":
		st.subheader("App Custom_Settings")

		# Define and Initialize State
		if 'fontsize' not in st.session_state:
			st.session_state['fontsize'] = 12


		f1,f2 = st.beta_columns(2)

		with f1:
			# Create a button for fxn/cb fxn
			font_increment = st.button('Increase Font')
			if font_increment:
				st.session_state['fontsize'] += 5


		with f2:
			# Create a button for fxn/cb fxn
			font_decrement = st.button('Decrease Font')
			if font_decrement:
				st.session_state['fontsize'] -= 5	


		# Results
		st.write("Current Font Size",st.session_state.fontsize)
		stc.html(HTML_BANNER.format(st.session_state.fontsize))





	else:
		st.subheader("About")
		st.info("Built with Streamlit")
		st.success("Jesus Saves @JCharisTech")
		st.text("By Jesse E.Agbe(JCharis)")



if __name__ == '__main__':
	main()
