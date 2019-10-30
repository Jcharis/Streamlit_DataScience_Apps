import streamlit as st
import os

# EDA Pkgs
import pandas as pd 
import numpy as np 

# Data Viz Pkgs
import matplotlib
matplotlib.use('Agg')# To Prevent Errors
import matplotlib.pyplot as plt
import seaborn as sns 

# ML Pkgs
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB,GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.externals import joblib

def main():
	""" ML App with Streamlit for Contraceptive Choice Prediction"""
	st.title("Contraceptive Method Choice Prediction")
	st.subheader("Predicting Contraceptive Choice with ML")

	# Load Our Dataset
	df = pd.read_csv("cmc_dataset.csv")

	if st.checkbox("Show DataSet"):
		number = st.number_input("Number of Rows to View")
		st.dataframe(df.head(number))

	if st.button("Columns Names"):
		st.write(df.columns)

	if st.checkbox("Shape of Dataset"):
		st.write(df.shape)
		data_dim = st.radio("Show Dimension by",("Rows","Columns"))
		if data_dim == 'Rows':
			st.text("Number of  Rows")
			st.write(df.shape[0])
		elif data_dim == 'Columns':
			st.text("Number of Columns")
			st.write(df.shape[1])

	if st.checkbox("Select Columns To Show"):
		all_columns = df.columns.tolist()
		selected_columns = st.multiselect('Select',all_columns)
		new_df = df[selected_columns]
		st.dataframe(new_df)

	if st.button("Data Types"):
		st.write(df.dtypes)

	if st.button("Value Counts"):
		st.text("Value Counts By Target/Class")
		st.write(df.iloc[:,-1].value_counts())

	st.subheader("Data Visualization")
	# Show Correlation Plots
	# Matplotlib Plot
	if st.checkbox("Correlation Plot [Matplotlib]"):
		plt.matshow(df.corr())
		st.pyplot()
	# Seaborn Plot
	if st.checkbox("Correlation Plot with Annotation[Seaborn]"):
		st.write(sns.heatmap(df.corr(),annot=True))
		st.pyplot()

	# Counts Plots
	if st.checkbox("Plot of Value Counts"):
		st.text("Value Counts By Target/Class")

		all_columns_names = df.columns.tolist()
		primary_col = st.selectbox('Select Primary Column To Group By',all_columns_names)
		selected_column_names = st.multiselect('Select Columns',all_columns_names)
		if st.button("Plot"):
			st.text("Generating Plot for: {} and {}".format(primary_col,selected_column_names))
			if selected_column_names:
				vc_plot = df.groupby(primary_col)[selected_column_names].count()		
			else:
				vc_plot = df.iloc[:,-1].value_counts()
			st.write(vc_plot.plot(kind='bar'))
			st.pyplot()

	if st.checkbox("Pie Plot"):
		all_columns_names = df.columns.tolist()
		# st.info("Please Choose Target Column")
		# int_column =  st.selectbox('Select Int Columns For Pie Plot',all_columns_names)
		if st.button("Generate Pie Plot"):
			# cust_values = df[int_column].value_counts()
			# st.write(cust_values.plot.pie(autopct="%1.1f%%"))
			st.write(df.iloc[:,-1].value_counts().plot.pie(autopct="%1.1f%%"))
			st.pyplot()

	# Prediction
	st.subheader("Options For Prediction")
	st.subheader("Attributes To Select from")

	def get_value(val,my_dict):
		for key ,value in my_dict.items():
			if val == key:
				return value

	age = st.slider("Select Age",16,60)
	wife_education = st.number_input("Wife's Education Level(low2High) [1,4]",1,4)
	husband_education = st.number_input("Husband's Education Level(low2High) [1,4]",1,4)
	num_of_children_ever_born = st.number_input("Number of Children")

	wife_reg = {"Non_Religious":0,"Religious":1}
	choice_wife_reg = st.radio("Wife's Religion",tuple(wife_reg.keys()))
	result_wife_reg = get_value(choice_wife_reg,wife_reg)
	# st.text(result_wife_reg)


	wife_working = {"Yes":0,"No":1}
	choice_wife_working = st.radio("Is the Wife Currently Working",tuple(wife_working.keys()))
	result_wife_working = get_value(choice_wife_working,wife_working)
	# st.text(result_wife_working)


	husband_occupation = st.number_input("Husband Occupation(low2High) [1,4]",1,4)
	standard_of_living = st.slider("Standard of Living (low2High) [1,4]",1,4)

	media_exposure = {"Good":0,"Not Good":1}
	choice_media_exposure = st.radio("Media Exposure",tuple(media_exposure.keys()))
	result_media_exposure = get_value(choice_media_exposure,media_exposure)


	# Result and in json format
	results = [age,wife_education,husband_education,num_of_children_ever_born,result_wife_reg,result_wife_working,husband_occupation,standard_of_living,result_media_exposure]
	displayed_results = [age,wife_education,husband_education,num_of_children_ever_born,choice_wife_reg,choice_wife_working,husband_occupation,standard_of_living,choice_media_exposure]
	prettified_result = {"age":age,
	"wife_education":wife_education,
	"husband_education":husband_education,
	"num_of_children_ever_born":num_of_children_ever_born,
	"result_wife_reg":choice_wife_reg,
	"result_wife_working":choice_wife_working,
	"husband_occupation":husband_occupation,
	"standard_of_living":standard_of_living,
	"media_exposure":choice_media_exposure}
	sample_data = np.array(results).reshape(1, -1)
	
	
	if st.checkbox("Your Inputs Summary"):
		st.json(prettified_result)
		st.text("Vectorized as ::{}".format(results))

	st.subheader("Prediction")
	if st.checkbox("Make Prediction"):
		all_ml_dict = {'LR':LogisticRegression(),
		'CART':DecisionTreeClassifier(),
		'RForest':RandomForestClassifier(),
		'NB':GaussianNB(),
		'MultNB':MultinomialNB()}
		# models = []
		# model_choice = st.multiselect('Model Choices',list(all_ml_dict.keys()))
		# for key in all_ml_dict:
		# 	if 'RForest' in key:
		# 		st.write(key)

		# Find the Key From Dictionary
		def get_key(val,my_dict):
			for key ,value in my_dict.items():
				if val == value:
					return key

		# Load Models
		def load_model_n_predict(model_file):
			loaded_model = joblib.load(open(os.path.join(model_file),"rb"))
			return loaded_model

		# Model Selection
		model_choice = st.selectbox('Model Choice',list(all_ml_dict.keys()))
		prediction_label = {"No-use": 1,"Long-term": 2,"Short-term":3}
		if st.button("Predict"):
			if model_choice == 'RForest':
				loaded_model = joblib.load(open("contraceptives_rf_model.pkl","rb"))
				prediction = loaded_model.predict(sample_data)
				final_result = get_key(prediction,prediction_label)
				st.info(final_result)
			elif model_choice == 'LR':
				model_predictor = load_model_n_predict("models/contraceptives_logit_model.pkl")
				prediction = model_predictor.predict(sample_data)
				# st.text(prediction)
			elif model_choice == 'CART':
				model_predictor = load_model_n_predict("models/contraceptives_dcTree_model.pkl")
				prediction = model_predictor.predict(sample_data)
				# st.text(prediction)
			elif model_choice == 'NB':
				model_predictor = load_model_n_predict("models/contraceptives_nv_model.pkl")
				prediction = model_predictor.predict(sample_data)
				# st.text(prediction)
			
			final_result = get_key(prediction,prediction_label)
			st.success(final_result)


					

				# if 'RForest' in key:
				# 	loaded_model = joblib.load(open("contraceptives_rf_model.pkl","rb"))
				# 	prediction = loaded_model.predict(sample_data)
				# 	final_result = get_key(prediction,prediction_label)
				# 	st.info(final_result)
				# elif 'LR' in key:
				# 	model_predictor = load_model_n_predict("models/contraceptives_logit_model.pkl")
				# 	prediction = model_predictor.predict(sample_data)
				# 	st.text(prediction)


				# if prediction == 1:
				# 	st.success("No Use")
				# elif prediction == 2:
				# 	st.warning("Long-term")
				# elif prediction == 3:
				# 	st.info("Short-term")
				# else:
				# 	st.text("Select A Model")
			
			# st.info("Select A Model")

				# final_result = get_key(prediction,prediction_label)
				# st.info(final_result)

				
			

if __name__ == '__main__':
	main()

