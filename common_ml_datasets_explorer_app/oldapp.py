import streamlit as st
from PIL import Image
import os,glob
import pandas as pd
import shutil
from zipfile import ZipFile
# import pandas_profiling as pp

# Data Viz Pkgs
import matplotlib
matplotlib.use('Agg')# To Prevent Errors
import matplotlib.pyplot as plt
import seaborn as sns 

# ML Packages
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

def main():
	"""Common ML Data Explorer """
	st.title("Common ML Data Explorer")
	st.subheader("Simple ML App with Streamlit")

	img_list = glob.glob("images/*.png")
	# st.write(img_list)
	# for i in img_list:
	# 	c_image = Image.open(i)
	# 	st.image(i)
	all_image = [Image.open(i) for i in img_list]
	st.image(all_image)
	
	def file_selector(folder_path='./datasets'):
	    filenames = os.listdir(folder_path)
	    selected_filename = st.selectbox('Select a file', filenames)
	    return os.path.join(folder_path, selected_filename)

	filename = file_selector()
	st.write('You selected `%s`' % filename)
	df = pd.read_csv(filename)	

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

	if st.checkbox("Summary"):
		st.write(df.describe())
	
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

	if st.checkbox("BarH Plot"):
		all_columns_names = df.columns.tolist()
		st.info("Please Choose the X and Y Column")
		x_column =  st.selectbox('Select X Columns For Barh Plot',all_columns_names)
		y_column =  st.selectbox('Select Y Columns For Barh Plot',all_columns_names)
		barh_plot = df.plot.barh(x=x_column,y=y_column,figsize=(10,10))
		if st.button("Generate Barh Plot"):
			st.write(barh_plot)
			st.pyplot()

	st.subheader("Customizable Plots")
	all_columns_names = df.columns.tolist()
	type_of_plot = st.selectbox("Select the Type of Plot",["area","bar","line","hist","box","kde"])
	selected_column_names = st.multiselect('Select Columns To Plot',all_columns_names)
	# plot_fig_height = st.number_input("Choose Fig Size For Height",10,50)
	# plot_fig_width = st.number_input("Choose Fig Size For Width",10,50)
	# plot_fig_size =(plot_fig_height,plot_fig_width)
	cust_target = df.iloc[:,-1].name

	if st.button("Generate Plot"):
		st.success("Generating A Customizable Plot of: {} for :: {}".format(type_of_plot,selected_column_names))
		# Plot By Streamlit
		if type_of_plot == 'area':
			cust_data = df[selected_column_names]
			st.area_chart(cust_data)
		elif type_of_plot == 'bar':
			cust_data = df[selected_column_names]
			st.bar_chart(cust_data)
		elif type_of_plot == 'line':
			cust_data = df[selected_column_names]
			st.line_chart(cust_data)
		# Plot By Matplotlib
		# elif type_of_plot == 'pie':
		# 	custom_plot = df[selected_column_names].plot(subplots=True,kind=type_of_plot)
		# 	st.write(custom_plot)
		# 	st.pyplot()
		elif type_of_plot == 'hist':
			custom_plot = df[selected_column_names].plot(kind=type_of_plot,bins=2)
			st.write(custom_plot)
			st.pyplot()
		elif type_of_plot == 'box':
			custom_plot = df[selected_column_names].plot(kind=type_of_plot)
			st.write(custom_plot)
			st.pyplot()
		elif type_of_plot == 'kde':
			custom_plot = df[selected_column_names].plot(kind=type_of_plot)
			st.write(custom_plot)
			st.pyplot()
		else:
			cust_plot = df[selected_column_names].plot(kind=type_of_plot)
			st.write(cust_plot)
			st.pyplot()

	html_temp = """
	<div style="background-color:powderblue;"><p style="color:blue;font-size:60px;"> Hello world colored</p></div>
	"""
# 	html_temp2 = """
# <body style="background-color:red;">
# <p style="color:blue">Hello World Streamlit</p>
# <form>
# <input type="text"/>
# </form>
# </body>
# </html>"""
	st.markdown(html_temp,unsafe_allow_html=True)


	st.subheader("Feature Engineering and ML Aspect")

	if st.checkbox("Show Features"):
		all_features = df.iloc[:,0:-1]
		st.text('Features Names:: {}'.format(all_features.columns[0:-1]))
		st.dataframe(all_features.head(10))

	if st.checkbox("Show Target"):
		all_target = df.iloc[:,-1]
		st.text('Target/Class Name:: {}'.format(all_target.name))
		st.dataframe(all_target.head(10))



	all_ml_dict = {'LR':LogisticRegression(),
	'LDA':LinearDiscriminantAnalysis(),
	'KNN':KNeighborsClassifier(),
	'CART':DecisionTreeClassifier(),
	'NB':GaussianNB(),
	'SVM':SVC()}
	# models = []
	model_choice = st.multiselect('Model Choices',list(all_ml_dict.keys()))
	for key in all_ml_dict:
		if 'LDA' in key:
			st.write(key)


		# results = []
		# names = []
		# allmodels = []
		# scoring = 'accuracy'
		# for name, model in models:
		# 	kfold = model_selection.KFold(n_splits=10, random_state=seed)
		# 	cv_results = model_selection.cross_val_score(model, X, Y, cv=kfold, scoring=scoring)
		# 	results.append(cv_results)
		# 	names.append(name)
		# 	msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
		# 	allmodels.append(msg)
		# 	model_results = results
		# 	model_names = names 



	# Make Downloadable file as zip,since markdown strips to html
	st.markdown("""[google.com](iris.zip)""")

	st.markdown("""[google.com](./iris.zip)""")

	# def make_zip(data):
	# 	output_filename = '{}_archived'.format(data)
	# 	return shutil.make_archive(output_filename,"zip",os.path.join("downloadfiles"))

	def makezipfile(data):
		output_filename = '{}_zipped.zip'.format(data)
		with ZipFile(output_filename,"w") as z:
			z.write(data)
		return output_filename	
				

	if st.button("Download File"):
		DOWNLOAD_TPL = f'[{filename}]({makezipfile(filename)})'
		# st.text(DOWNLOAD_TPL)
		st.text(DOWNLOAD_TPL)
		st.markdown(DOWNLOAD_TPL)









if __name__ == '__main__':
	main()