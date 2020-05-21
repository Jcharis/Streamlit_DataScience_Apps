import streamlit as st
import pandas as pd

# # NLP pkgs
# import spacy
# from spacy import displacy
# nlp = spacy.load('en')

# Database Functions
from db_fxns import *

from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')


# Avatar Image using a url
avatar1 ="https://www.w3schools.com/howto/img_avatar1.png"
avatar2 ="https://www.w3schools.com/howto/img_avatar2.png"

# Reading Time
def readingTime(mytext):
	total_words = len([ token for token in mytext.split(" ")])
	estimatedTime = total_words/200.0
	return estimatedTime

def analyze_text(text):
	return nlp(text)

# Layout Templates
title_temp ="""
	<div style="background-color:#464e5f;padding:10px;border-radius:10px;margin:10px;">
	<h4 style="color:white;text-align:center;">{}</h1>
	<img src="https://www.w3schools.com/howto/img_avatar.png" alt="Avatar" style="vertical-align: middle;float:left;width: 50px;height: 50px;border-radius: 50%;" >
	<h6>Author:{}</h6>
	<br/>
	<br/>	
	<p style="text-align:justify">{}</p>
	</div>
	"""
article_temp ="""
	<div style="background-color:#464e5f;padding:10px;border-radius:5px;margin:10px;">
	<h4 style="color:white;text-align:center;">{}</h1>
	<h6>Author:{}</h6> 
	<h6>Post Date: {}</h6>
	<img src="https://www.w3schools.com/howto/img_avatar.png" alt="Avatar" style="vertical-align: middle;width: 50px;height: 50px;border-radius: 50%;" >
	<br/>
	<br/>
	<p style="text-align:justify">{}</p>
	</div>
	"""
head_message_temp ="""
	<div style="background-color:#464e5f;padding:10px;border-radius:5px;margin:10px;">
	<h4 style="color:white;text-align:center;">{}</h1>
	<img src="https://www.w3schools.com/howto/img_avatar.png" alt="Avatar" style="vertical-align: middle;float:left;width: 50px;height: 50px;border-radius: 50%;">
	<h6>Author:{}</h6> 		
	<h6>Post Date: {}</h6>		
	</div>
	"""
full_message_temp ="""
	<div style="background-color:silver;overflow-x: auto; padding:10px;border-radius:5px;margin:10px;">
		<p style="text-align:justify;color:black;padding:10px">{}</p>
	</div>
	"""

HTML_WRAPPER = """<div style="overflow-x: auto; border: 1px solid #e6e9ef; border-radius: 0.25rem; padding: 1rem">{}</div>"""

def main():
	"""A Simple CRUD Blog App"""
	html_temp = """
		<div style="background-color:{};padding:10px;border-radius:10px">
		<h1 style="color:{};text-align:center;">Simple Blog </h1>
		</div>
		"""
	st.markdown(html_temp.format('royalblue','white'),unsafe_allow_html=True)
		

	menu = ["Home","View Post","Add Post","Search","Manage Blog"]
	choice = st.sidebar.selectbox("Menu",menu)

	if choice == "Home":
		st.subheader("Home")		
		result = view_all_notes()
		for i in result:
			# short_article = str(i[2])[0:int(len(i[2])/2)]
			short_article = str(i[2])[0:50]
			st.write(title_temp.format(i[1],i[0],short_article),unsafe_allow_html=True)

		# st.write(result)
	elif choice == "View Post":
		st.subheader("View Post")

		all_titles = [i[0] for i in view_all_titles()]
		postlist = st.sidebar.selectbox("Posts",all_titles)
		post_result = get_blog_by_title(postlist)
		for i in post_result:
			st.text("Reading Time:{} minutes".format(readingTime(str(i[2]))))
			st.markdown(head_message_temp.format(i[1],i[0],i[3]),unsafe_allow_html=True)
			st.markdown(full_message_temp.format(i[2]),unsafe_allow_html=True)

			# if st.button("Analyze"):
	
			# 	docx = analyze_text(i[2])
			# 	html = displacy.render(docx,style="ent")
			# 	html = html.replace("\n\n","\n")
			# 	st.write(HTML_WRAPPER.format(html),unsafe_allow_html=True)

			


	elif choice == "Add Post":
		st.subheader("Add Your Article")
		create_table()
		blog_title = st.text_input('Enter Post Title')
		blog_author = st.text_input("Enter Author Name",max_chars=50)
		blog_article = st.text_area("Enter Your Message",height=200)
		blog_post_date = st.date_input("Post Date")
		if st.button("Add"):
			add_data(blog_author,blog_title,blog_article,blog_post_date)
			st.success("Post::'{}' Saved".format(blog_title))


	elif choice == "Search":
		st.subheader("Search Articles")
		search_term = st.text_input("Enter Term")
		search_choice = st.radio("Field to Search",("title","author"))
		if st.button('Search'):
			if search_choice == "title":
				article_result = get_blog_by_title(search_term)
			elif search_choice =="author":
				article_result = get_blog_by_author(search_term)
			
			# Preview Articles
			for i in article_result:
				st.text("Reading Time:{} minutes".format(readingTime(str(i[2]))))
				# st.write(article_temp.format(i[1],i[0],i[3],i[2]),unsafe_allow_html=True)
				st.write(head_message_temp.format(i[1],i[0],i[3]),unsafe_allow_html=True)
				st.write(full_message_temp.format(i[2]),unsafe_allow_html=True)
			

	elif choice == "Manage Blog":
		st.subheader("Manage Blog")
		result = view_all_notes()
		clean_db = pd.DataFrame(result,columns=["Author","Title","Article","Date","Index"])
		st.dataframe(clean_db)
		unique_list = [i[0] for i in view_all_titles()]
		delete_by_title =  st.selectbox("Select Title",unique_list)
		if st.button("Delete"):
			delete_data(delete_by_title)
			st.warning("Deleted: '{}'".format(delete_by_title))

		if st.checkbox("Metrics"):
			new_df = clean_db
			new_df['Length'] = new_df['Article'].str.len() 


			st.dataframe(new_df)
			# st.dataframe(new_df['Author'].value_counts())
			st.subheader("Author Stats")
			new_df['Author'].value_counts().plot(kind='bar')
			st.pyplot()

			new_df['Author'].value_counts().plot.pie(autopct="%1.1f%%")
			st.pyplot()

		if st.checkbox("WordCloud"):
			# text = clean_db['Article'].iloc[0]
			st.subheader("Word Cloud")
			text = ', '.join(clean_db['Article'])
			# Create and generate a word cloud image:
			wordcloud = WordCloud().generate(text)

			# Display the generated image:
			plt.imshow(wordcloud, interpolation='bilinear')
			plt.axis("off")
			st.pyplot()

		if st.checkbox("BarH Plot"):
				st.subheader("Length of Articles")
				new_df = clean_db
				new_df['Length'] = new_df['Article'].str.len() 
				barh_plot = new_df.plot.barh(x='Author',y='Length',figsize=(10,10))
				st.write(barh_plot)
				st.pyplot()



if __name__ == '__main__':
	main()
