import streamlit as st 
# ML Pkg
# from sklearn.externals import joblib
import joblib
import time
from PIL import Image

# load Vectorizer For Gender Prediction
gender_vectorizer = open("models/gender_vectorizer.pkl","rb")
gender_cv = joblib.load(gender_vectorizer)

# load Model For Gender Prediction
gender_nv_model = open("models/naivebayesgendermodel.pkl","rb")
gender_clf = joblib.load(gender_nv_model)


# Prediction
def predict_gender(data):
	vect = gender_cv.transform(data).toarray()
	result = gender_clf.predict(vect)
	return result

# Load CSS File
def load_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

def load_icon(icon_name):
    st.markdown('<i class="material-icons">{}</i>'.format(icon_name), unsafe_allow_html=True)

# Images
def load_images(file_name):
	img = Image.open(file_name)
	return st.image(img,width=300)


def main():
	"""Gender Classifier App
	Using Machine Learning and Streamlit

	"""

	st.title("Gender Classifier")
	html_temp = """
	<div style="background-color:tomato;padding:10px">
	<h2 style="color:white;text-align:center;">Streamlit ML App </h2>
	</div>

	"""
	st.markdown(html_temp,unsafe_allow_html=True)
	load_css('icon.css')
	load_icon('people')

	name = st.text_input("Enter Name","Type Here")
	if st.button("Predict"):
		result = predict_gender([name])
		if result[0] == 0:
			prediction = 'Female'
			c_img = 'female.png'
		else:
			result[0] == 1
			prediction = 'Male'
			c_img = 'male.png'

		st.success('Name: {} was classified as {}'.format(name.title(),prediction))
		load_images(c_img)


	if st.button("About"):

		st.text("Jesus Saves @JCharisTech")
		st.text("By Jesse E.Agbe(JCharis)")
		st.text("Built with Streamlit")



if __name__ == '__main__':
	main()