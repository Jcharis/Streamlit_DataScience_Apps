# Core Pkgs
import streamlit as st 
import streamlit.components.v1 as stc
import requests 

base_url = "https://jobs.github.com/positions.json?description={}&location={}"

# Fxn to Retrieve Data
def get_data(url):
	resp = requests.get(url)
	return resp.json()


JOB_HTML_TEMPLATE = """
<div style="width:100%;height:100%;margin:1px;padding:5px;position:relative;border-radius:5px;border-bottom-right-radius: 10px;
box-shadow:0 0 1px 1px #eee; background-color: #31333F;
  border-left: 5px solid #6c6c6c;color:white;">
<h4>{}</h4>
<h4>{}</h4>
<h5>{}</h5>
<h6>{}</h6>
</div>
"""

JOB_DES_HTML_TEMPLATE = """
<div style='color:#fff'>
{}
</div>
"""


def main():
	menu = ["Home","About"]
	choice = st.sidebar.selectbox("Menu",menu)

	st.title("DevDeeds -Search Jobs")

	if choice == "Home":
		st.subheader("Home")

		# Nav  Search Form
		with st.form(key='searchform'):
			nav1,nav2,nav3 = st.beta_columns([3,2,1])

			with nav1:
				search_term = st.text_input("Search Job")
			with nav2:
				location = st.text_input("Location")

			with nav3:
				st.text("Search ")
				submit_search = st.form_submit_button(label='Search')

		st.success("You searched for {} in {}".format(search_term,location))

		# Results
		col1, col2 = st.beta_columns([2,1])

		with col1:
			if submit_search:
				# Create Search Query
				search_url = base_url.format(search_term,location)
				# st.write(search_url)
				data = get_data(search_url)

				# Number of Results
				num_of_results = len(data)
				st.subheader("Showing {} jobs".format(num_of_results))
				# st.write(data)
		

				for i in data:
					job_title = i['title']
					job_location = i['location']
					company = i['company']
					company_url = i['company_url']
					job_post_date = i['created_at']
					job_desc = i['description']
					job_howtoapply = i['how_to_apply']
					st.markdown(JOB_HTML_TEMPLATE.format(job_title,company,job_location,job_post_date),
						unsafe_allow_html=True)

					# Description
					with st.beta_expander("Description"):
						stc.html(JOB_DES_HTML_TEMPLATE.format(job_desc),scrolling=True)

					# How to Apply
					with st.beta_expander("How To Apply"):
						# stc.html(job_howtoapply) # For White Theme
						stc.html(JOB_DES_HTML_TEMPLATE.format(job_howtoapply),scrolling=True) # For Dark Theme


		with col2:
			with st.form(key='email_form'):
				st.write("Be the first to get new jobs info")
				email = st.text_input("Email")

				submit_email = st.form_submit_button(label='Subscribe')

				if submit_email:
					st.success("A message was sent to {}".format(email))







	else:
		st.subheader("About")




if __name__ == '__main__':
	main()


