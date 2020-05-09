import streamlit as st




def main():
	"""A Simple Streamlit App For CSS Shape Generation """
	st.title("Simple CSS Shape Generator")

	activity = ['Design','About',]
	choice = st.sidebar.selectbox("Select Activity",activity)

	if choice == 'Design':
		st.subheader("Design")
		bgcolor = st.beta_color_picker("Pick a Background color")
		fontcolor = st.beta_color_picker("Pick a Font Color","#fff")

		html_temp = """
		<div style="background-color:{};padding:10px">
		<h1 style="color:{};text-align:center;">Streamlit Simple CSS Shape Generator </h1>
		</div>
		"""
		st.markdown(html_temp.format(bgcolor,fontcolor),unsafe_allow_html=True)
		st.markdown("<div><p style='color:{}'>Hello Streamlit</p></div>".format(bgcolor),unsafe_allow_html=True)


		st.subheader("Modify Shape")
		bgcolor2 = st.sidebar.beta_color_picker("Pick a Bckground color")
		height = st.sidebar.slider('Height Size',50,200,50)
		width = st.sidebar.slider("Width Size",50,200,50)
		# border = st.slider("Border Radius",10,60,10)
		top_left_border = st.sidebar.number_input('Top Left Border',10,50,10)
		top_right_border = st.sidebar.number_input('Top Right Border',10,50,10)
		bottom_left_border = st.sidebar.number_input('Bottom Left Border',10,50,10)
		bottom_right_border = st.sidebar.number_input('Bottom Right Border',10,50,10)

		border_style = st.sidebar.selectbox("Border Style",["dotted","dashed","solid","double","groove","ridge","inset","outset","none","hidden"])
		border_color = st.sidebar.beta_color_picker("Pick a Border Color","#654FEF")
	

		html_design = """
		<div style="height:{}px;width:{}px;background-color:{};border-radius:{}px {}px {}px {}px;border-style:{};border-color:{}">
		</div>
		"""
		st.markdown(html_design.format(height,width,bgcolor2,top_left_border,top_right_border,bottom_left_border,bottom_right_border,border_style,border_color),unsafe_allow_html=True)

		if st.checkbox("View Results"):
			st.subheader("Result")
			result_of_design = html_design.format(height,width,bgcolor2,top_left_border,top_right_border,bottom_left_border,bottom_right_border,border_style,border_color)			
			st.code(result_of_design)

	if choice =="About":
		st.subheader("About")
		st.info("Jesus Saves @JCharisTech")
		st.text("By Jesse E.Agbe(JCharis)")
		st.success("Built with Streamlit")



if __name__ == '__main__':
	main()